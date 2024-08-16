from typing import Type

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

from my_app.models import ConfirmEmailToken, CustomUser
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from urllib.parse import quote

new_user_registered = Signal()  # Уведомляет о создании нового пользователя.
new_order = Signal()  # Уведомляет о создании нового заказа.


@receiver(post_save, sender=CustomUser)
def create_confirm_email_token_and_send_email(sender, instance, created, **kwargs):
    """
    Для авторизации пользователя.

    :param sender: Класс представления (View), который послал сигнал. В данном случае, CustomUser.
    :param instance: Экземпляр класса CustomUser.
    :param created: Булево значение, указывающее, был ли объект только что создан (True).
    :param kwargs: Дополнительные аргументы, которые могут быть переданы вместе с сигналом.
    """

    if created:
        # Генерируем и сохраняем токен подтверждения.
        token = ConfirmEmailToken.objects.create(user=instance)
        email = instance.email

        print(f'{token} сгенерирован.')
        print('')

        # Создаём ссылку подтверждения.
        # confirmation_link = f"http://127.0.0.1:8000/api/v1/user/confirm-email/{quote(token.key)}"
        confirmation_link = f"http://127.0.0.1:8000/api/v1/user/confirm-email/?token={quote(token.key)}&email={quote(email)}"

        # Отправляем электронное письмо со ссылкой для подтверждения.
        subject = 'Пожалуйста, подтвердите свой адрес электронной почты'
        message = f'Чтобы подтвердить свой адрес электронной почты, перейдите по этой ссылке: {confirmation_link}'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email])
        print('Письмо пользователю отправлено.')
        print('')


@receiver(new_order)
def new_order_signal(user_id, **kwargs):
    """
    Отправляем письмо при изменении статуса заказа.
    """
    # send an e-mail to the user
    user = CustomUser.objects.get(id=user_id)

    msg = EmailMultiAlternatives(
        # title:
        f"Обновление статуса заказа",
        # message:
        'Заказ сформирован',
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user.email]
    )
    msg.send()
    