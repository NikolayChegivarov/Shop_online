from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CustomUserManager


class CustomUserManagerTests(TestCase):
    def setUp(self):
        """Для инициализации переменных и объектов, которые будут использоваться во всех тестовых методах класса."""
        self.user_manager = CustomUserManager.objects.get_user_manager()
        self.email = '[email protected]'
        self.password = 'testpassword'

    def test_create_user(self):
        """Гарантирует, что метод create_user работает корректно
        и создает объекты правильного типа с правильными атрибутами."""
        user = self.user_manager.create_user(email=self.email, password=self.password)
        self.assertIsInstance(user, CustomUserManager)
        self.assertEqual(user.email, self.email)

    def test_create_superuser(self):
        """Гарантирует что метод create_superuser корректно обрабатывает
        создание пользователей с повышенными правами доступа."""
        superuser = self.user_manager.create_superuser(email=self.email, password=self.password)
        self.assertIsInstance(superuser, CustomUserManager)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_get_by_natural_key(self):
        """Гарантирует, что метод поиска работает корректно и может надежно
        идентифицировать пользователей по их естественному ключу."""
        user = self.user_manager.create_user(email=self.email, password=self.password)
        retrieved_user = self.user_manager.get_by_natural_key(email=user.email)
        self.assertEqual(retrieved_user, user)

    def test_value_error_on_empty_email(self):
        """Проверяет обработку ошибок при попытке создать пользователя с пустым email."""
        with self.assertRaises(ValueError):
            self.user_manager.create_user(email='', password=self.password)
