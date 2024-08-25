from celery import shared_task

from django.core.mail import send_mail
from django_rest_passwordreset.models import ResetPasswordToken

@shared_task
def send_reset_password_email(token_id):
    try:
        token = ResetPasswordToken.objects.get(id=token_id)
        subject = "Восстановление пароля"
        message = f"Для восстановления пароля перейдите по ссылке: {token.reset_url}"
        send_mail(subject, message, 'noreply@example.com', [token.email])
    except ResetPasswordToken.DoesNotExist:
        print("Токен не найден")


@shared_task

