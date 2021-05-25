from datetime import datetime

from django.shortcuts import render

# импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView

# импортируем модель Product из models.py
from .models import Product, Category


# создадим модель объектов, которые будем выводить
class ProductList(ListView):
    # здесь укажем модель, объекты которой мы будем выводить
    # т.е. модель товаров
    model = Product

    # указываем имя html-шаблона с инструкциями о том,
    # как именно пользователю должны вывестись объекты
    template_name = 'products.html'

    # имя списка в html, в котором лежат все объекты
    # к нему можно обратиться через html-шаблон
    context_object_name = 'products'

    # порядок вывода продуктов - в обратном порядке по их id
    queryset = Product.objects.order_by('-id')

    # добавим ещё одну переменную в ProductList, которая будет
    # отображать текущее время.
    # Для этого создадим метод get_context_data,
    # которая принимает на вход все объекты из products

    # однако, чтобы эта переменная попадала в шаблон views,
    # её нужно переопределить
    def get_context_data(self, **kwargs):
        # поэтому здесь products распаковывается
        context = super().get_context_data(**kwargs)
        # к распакованному products добавляем переменную time_now
        # которая равна текущему значению времени
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context


# пишем класс, который наследуется от дженерика DetailView
# чтобы отображалась информация конкретно об одном товаре
class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
