from django.shortcuts import render

# импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView

# импортируем модель Product из models.py
from .models import Product, Category


# Create your views here.
# создадим модель объектов, которые будем выводить
class ProductList(ListView):
    # здесь укажем модель, объекты которой мы будем выводить
    # т.е. модель товаров
    model = Product

    # указываем имя шаблона, в котором будет лежать html-файл
    # с инструкциями о том, как именно пользователю должны вывестись объекты
    template_name = 'products.html'

    # имя списка в html, в котором лежат все объекты
    # к нему можно обратиться через html-шаблон
    context_object_name = 'products'

    # порядок вывода продуктов - в обратном порядке по их id
    queryset = Product.objects.order_by('-id')

# пишем класс, который наследуется от дженерика DetailView
# чтобы отображалась информация конкретно об одном товаре
class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'