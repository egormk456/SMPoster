from data.commands import getter, setter
import datetime

clients = await getter.all_clients()

for client in clients:
    # Получение времени окончания подписки
    end_date = client.subscribe
    
    # Вычисление количества дней до окончания подписки
    days_left = (end_date - datetime.datetime.now()).days
    
    # Отправка уведомления за день и за 3 дня до окончания подписки
    if days_left == 1:
        await send_notification(client.user_id, "Ваша подписка заканчивается завтра!")
    elif days_left == 3:
        await send_notification(client.user_id, "Ваша подписка заканчивается через 3 дня!")




