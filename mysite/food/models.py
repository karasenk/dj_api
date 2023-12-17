from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        help_text='название категории')


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        help_text='название продукта')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        help_text='категория'
    )
    price = models.IntegerField(
        help_text='цена',
        default=50
    )
