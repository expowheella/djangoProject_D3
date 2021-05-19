from django.contrib import admin

# импортируем наши модели
from .models import Category, Product
# и зарегистрируем их
admin.site.register(Product)
admin.site.register(Category)
