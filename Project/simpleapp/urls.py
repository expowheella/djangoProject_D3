# импортируем библиотеку для работы с путями urls
from django.urls import path
# импортируем наше представление
from .views import ProductList, ProductDetail

urlpatterns = [
    # путь ко всем товарам (пустой)
    path('',
         # вызываем метод as_view для того, чтобы представить класс ProductList в виде view
         ProductList.as_view()),
    # передача private key продукта (id продукта)
    path('<int:pk>', ProductDetail.as_view())
]
