from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from my_app.views import *

app_name = 'backend'
urlpatterns = [
    path('user/register', RegisterAccount.as_view(), name='user-register'),  # Для регистрации пользователя.
    path('user/confirm-email/<str:token_key>/', ConfirmEmail.as_view(), name='confirm-email'),  # Подтверждения E-mail.
    path('user/login', LoginAccount.as_view(), name='user-login'),  # Для авторизации пользователей.
    path('partner/state', PartnerState.as_view(), name='partner-state'),  # Класс для управления состоянием партнера.

    # Для удаления аккаунта пользователя.
    path('user/delete/<int:user_id>/', DeleteAccount.as_view(), name='user-delete'),  # Удаление аккаунта.

    # Встроенные views.
    # Посылает токен сброса пароля на электронный адрес пользователя.
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    # Проверяет действительность токена и, если все в порядке, обновляет пароль пользователя в системе.
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),

    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),  # Для обновления прайса от поставщика.
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),  # Класс для получения заказов поставщиками.

    path('user/details', AccountDetails.as_view(), name='user-details'),  # Для управления данными.
    path('user/contact', ContactView.as_view(), name='user-contact'),  # Для управления контактной информацией.

    path('categories', CategoryView.as_view(), name='categories'),  # Класс для просмотра категорий.
    path('shops', ShopView.as_view(), name='shops'),  # Для просмотра списка магазинов.
    path('products', ProductInfoView.as_view(), name='product_search'),  # Класс для поиска товаров.
    path('basket', BasketView.as_view(), name='basket'),  # Для управления корзиной покупок пользователя.
    path('order', OrderView.as_view(), name='order'),  # Для получения и размещения заказов пользователями.
]
