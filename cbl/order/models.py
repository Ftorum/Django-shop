from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.forms import ModelForm

# Create your models here.


class ShopCart(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Покупатель', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(
        Product, verbose_name='Продукт', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(verbose_name='Количество',)

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return (self.product.price)

    @property
    def amount(self):
        return (self.quantity * self.product.price)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = "Корзины"


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(
        User, verbose_name='Покупатель', on_delete=models.SET_NULL, null=True)
    code = models.CharField(verbose_name='Код', max_length=5, editable=False)
    first_name = models.CharField(verbose_name='Имя', max_length=10)
    last_name = models.CharField(verbose_name='Фамилия', max_length=10)
    phone = models.CharField(verbose_name='Телефон', blank=True, max_length=20)
    tab_number = models.CharField(
        verbose_name='Табельный номер', blank=True, max_length=150)
    total = models.FloatField(verbose_name='Итого',)
    status = models.CharField(verbose_name='Статус',
                              max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(verbose_name='Дата и время заказа',auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = "Заказы"
        ordering =['create_at']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'tab_number', 'phone']


class OrderProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    order = models.ForeignKey(
        Order, verbose_name='Заказ', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, verbose_name='Покупатель', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name='Продукт', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количество',)
    price = models.FloatField(verbose_name='Цена',)
    amount = models.FloatField(verbose_name='Итоговая стоимость корзины')
    status = models.CharField(verbose_name='Статус',
                              max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = "Продукты в корзине"
