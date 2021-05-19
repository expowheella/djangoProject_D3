from django.core.validators import MinValueValidator
from django.db import models


# Создаем модель товара
class Product(models.Model):
    # названия товаров
    name = models.CharField(
        max_length=50,
        # чтобы названия товаров не повторялись
        unique=True,
    )
    # описание товара
    description = models.TextField()
    # количество товара
    quantity = models.IntegerField(
        # проверка значения, чтобы оно было >= 0
        validators=[MinValueValidator(0)],
    )

    # связь «один ко многим» с моделью Category
    category = models.ForeignKey(
        # указываем с какой моделью должна быть связь
        to='Category',
        # при удалении категории, удалятся связанные с ней продукты
        on_delete=models.CASCADE,
        # все продукты из категории будут доступны через поле products
        related_name='products',
    )

    # стоимость товара
    price = models.FloatField(
        # проверка, чтобы стоимость была больше равно 0.0 рублей
        validators=[MinValueValidator(0.0)],
    )

    # формат вывода наименования товара и его описания (первые 20 знаков)
    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


# Создаем модель категории товаров
class Category(models.Model):
    # название категории
    name = models.CharField(
        max_length=100,
        # уникальная категория
        unique=True,
    )

    # формат вывода названия категории
    def __str__(self):
        return f'{self.name.title()}'
