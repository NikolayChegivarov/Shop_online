from typing import Type

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django_rest_passwordreset.signals import reset_password_token_created

from my_app.models import ConfirmEmailToken, CustomUser

new_user_registered = Signal()

new_order = Signal()


@receiver(reset_password_token_created)  # отправляется после генерации токена сброса пароля, но до его отправки польз.
def password_reset_token_created(sender, instance, reset_password_token, **kwargs):
    """
    Отправляем письмо с токеном для сброса пароля
    Когда токен создан, пользователю необходимо отправить электронное письмо.
    :param sender: View Class который послал сигнал
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param kwargs:
    :return:
    """
    # отправить e-mail пользователю

    msg = EmailMultiAlternatives(
        # title:
        f"Password Reset Token for {reset_password_token.user}",
        # message:
        reset_password_token.key,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email]
    )
    msg.send()


@receiver(post_save, sender=CustomUser)
def new_user_registered_signal(sender: Type[CustomUser], instance: CustomUser, created: bool, **kwargs):
    """
     Отправляем письмо с подтверждением почты.
    """
    if created and not instance.is_active:
        # # отправить e-mail пользователю
        token, _ = ConfirmEmailToken.objects.get_or_create(user_id=instance.pk)

        msg = EmailMultiAlternatives(
            # title:
            f"Password Reset Token for {instance.email}",
            # message:
            token.key,
            # from:
            settings.EMAIL_HOST_USER,
            # to:
            [instance.email]
        )
        msg.send()


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
    