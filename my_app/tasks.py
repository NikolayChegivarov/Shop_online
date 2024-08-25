from celery import shared_task

from django.core.mail import send_mail
from .models import PasswordResetToken

@shared_task
def send_reset_password_email(token_id):
    try:
        token = PasswordResetToken.objects.get(id=token_id)
        subject = "Восстановление пароля"
        message = f"Для восстановления пароля перейдите по ссылке: {token.reset_url}"
        send_mail(subject, message, 'noreply@example.com', [token.email])
    except PasswordResetToken.DoesNotExist:
        print("Токен не найден")


@shared_task
def reset_password_confirm(user_id, token):
    user = User.objects.get(pk=user_id)

    # Здесь должна быть логика подтверждения пароля
    # Например:
    if token == user.get_password_reset_token():
        # Обновление пароля пользователя
        user.set_password('новый_пароль')
        user.save()
