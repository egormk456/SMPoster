import json
import asyncio
import subprocess
import tempfile
import time
import requests

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from data.commands import getter

POST_CONTENT_TYPES = [
    'photo',
    'video'
]
HANDLE_TYPES = POST_CONTENT_TYPES + ['text']


async def queue_manager():
    dp = Dispatcher.get_current()
    bot = dp.bot
    while True:
        await asyncio.sleep(10)
        queue = dp.queue

        if queue:
            print('totally queue:', queue)
            first_key = next(iter(queue))
            first_queue_item = queue.get(first_key)
            if first_queue_item[-1].get('media_group') and first_queue_item[-1]['save_time'] + 5 > time.time():
                continue

            message_items = queue.pop(first_key)
            if message_items[0].get('media_group'):
                message_items = [message_item.get('item') for message_item in message_items]

            asyncio.create_task(send_proc(bot, message_items))


async def send_proc(bot, message_items):
    attachments = []
    text = None
    entities = None
    reply_markup = None
    bind = None
    owner = None
    vk_group_id = None
    try:

        for message_item in message_items:
            chat_id = message_item['chat_id']
            if not (bind or owner):
                bind = await getter.client_select_bind_with_tg_channel_id(str(chat_id))
                if not bind:
                    raise ValueError('bind not found')

                owner = await getter.client_select(bind.owner_id)

            if 'caption' in message_item and message_item['caption'] is not None:
                text = message_item['caption']
            elif 'text' in message_item and message_item['text'] is not None:
                text = message_item['text']
            if 'entities' in message_item and message_item['entities'] is not None:
                entities = message_item['entities']
            elif 'caption_entities' in message_item and message_item['caption_entities'] is not None:
                entities = message_item['caption_entities']
            if 'reply_markup' in message_item and message_item['reply_markup'] is not None:
                reply_markup = message_item['reply_markup']

            if 'photo' in message_item:
                attachments.append(await get_photo_attachment(bot, message_item['photo']['file_id'], owner.vk_token))

            if 'video' in message_item:
                attachments.append(await get_video_attachment(bot, message_item['video']['file_id'], owner.vk_token))

        text = parse_entities(text, entities)
        text = parse_buttons(text, reply_markup)

        for vk_group_id in bind.vk_groups_ids:
            requests.get(
                url='https://api.vk.com/method/wall.post',
                params={
                    'access_token': owner.vk_token,
                    'owner_id': -int(vk_group_id),
                    'message': text,
                    'from_group': 1,
                    'attachments': ','.join(attachments) if attachments != [] else None,
                    'v': "5.131"
                }
            )
            print(f'send OK to {vk_group_id}')

    except Exception as ex:
        print(f'send ERROR [{ex.args}] vk [{vk_group_id}]')


async def get_photo_attachment(bot, file_id, vk_token):
    file_url = await get_file_url(bot, file_id)
    upload_url = get_upload_url('https://api.vk.com/method/photos.getWallUploadServer', vk_token)
    temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    temp_file.write(file_url.getvalue())
    curl_command = f'curl -F "photo=@{temp_file.name}" "{upload_url}"'
    process = subprocess.Popen(curl_command, shell=True, stdout=subprocess.PIPE, )
    output, _ = process.communicate()
    temp_file.close()

    output_data = json.loads(output)

    save_result = requests.get(
        url='https://api.vk.com/method/photos.saveWallPhoto',
        params={
            'access_token': vk_token,
            'v': '5.131',
            'photo': output_data['photo'],
            'server': output_data['server'],
            'hash': output_data['hash']
        }
    )
    if save_result.status_code == 200:
        save_result = save_result.json()['response']
        return f'photo{save_result[0]["owner_id"]}_{save_result[0]["id"]}'


async def get_video_attachment(bot, file_id, vk_token):
    file_url = await get_file_url(bot, file_id)
    upload_url = get_upload_url('https://api.vk.com/method/video.save', vk_token)

    temp_file = tempfile.NamedTemporaryFile(suffix='.mp4', delete=False)
    temp_file.write(file_url.getvalue())

    curl_command = f'curl -F "video=@{temp_file.name}" "{upload_url}"'
    process = subprocess.Popen(curl_command, shell=True, stdout=subprocess.PIPE, )
    output, _ = process.communicate()

    temp_file.close()

    save_result = json.loads(output)
    return f'video{save_result["owner_id"]}_{save_result["video_id"]}'


def get_upload_url(url, vk_token):
    return requests.get(
        url=url,
        params={
            'access_token': vk_token,
            'v': '5.131'
        }
    ).json()['response']['upload_url']


def parse_message_media(key: str, collected_message: dict) -> dict[str: str | float]:
    parsed_message_media = {}
    match key:
        case 'photo':
            parsed_message_media = {
                "file_id": collected_message[key][-1]['file_id']
            }
        case 'video':
            parsed_message_media = {
                "file_id": collected_message[key]['file_id']
            }
    return parsed_message_media


async def parse_message(message: types.Message, is_media_group: bool = False) -> dict:
    collected_message = json.loads(str(message))
    message_items = ['text', 'caption', 'entities', 'caption_entities', 'reply_markup']
    message_media = POST_CONTENT_TYPES
    parsed_message = {}
    for key, value in collected_message.items():
        if key in message_items:
            parsed_message[key] = value
        elif not is_media_group and key in message_media:
            parsed_message[key] = parse_message_media(key, collected_message)
        elif is_media_group and key in message_media:
            parsed_message[key] = parse_message_media(key, collected_message)
    parsed_message['chat_id'] = message.chat.id
    return parsed_message


async def merge_dict(state: FSMContext):
    data = await state.get_data()
    keys_for_merge = [key for key in data.keys() if str(key).startswith('collected_post:')]
    values_for_merge = [data.pop(key) for key in sorted(keys_for_merge)]
    data['collected_post'] = values_for_merge
    await state.set_data(data)


async def collect_post(message: types.Message):
    if message.media_group_id:
        return {'media_group': message.media_group_id, 'item': await parse_message(message, is_media_group=True)}
    else:
        return await parse_message(message)


async def process_queue(item, results, message_id):
    media_group_id = item.get('media_group')
    if media_group_id is None:
        results[message_id].append(item)
    else:
        item['save_time'] = time.time()
        results[media_group_id].append(item)


async def get_file_url(bot, file_id):
    file_info = await bot.get_file(file_id)
    return await bot.download_file(file_info.file_path)


def parse_entities(text: str, entities: list[dict]):
    if not entities:
        return text

    link_entities = []
    complete_text = ''

    l = 0
    for entity in entities:
        if entity.get('type') == 'text_link':
            link_entities.append({"offset": entity["offset"], "length": entity["length"], "url": entity["url"]})
            offset = entity['offset']
            length = entity['length']
            url = entity['url']
            complete_text += text[l: offset]
            complete_text += f'{text[offset:offset+length - 1].strip()} -> {url} '
            l = offset + length - 1
    complete_text += text[l:]
    return complete_text


def parse_buttons(text: str, buttons_dict: dict):
    if not buttons_dict:
        return text

    text += '\n'
    buttons_rows = buttons_dict['inline_keyboard']
    for btn_row in buttons_rows:
        for button in btn_row:
            if button.get('url'):
                text += f'\n{button["text"]} -> {button["url"]}'
    return text
