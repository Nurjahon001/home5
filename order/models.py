from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


    class Meta:
        db_table='products_table'


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField(default=timezone.now)
    valid_to = models.DateTimeField()


    def __str__(self):
        return f"{self.product.name} - {self.percentage}% chegirma"


    class Meta:
        db_table='discounts_table'


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    ordered_at = models.DateTimeField(default=timezone.now)
    products = models.ManyToManyField(Product, through='OrderItem')

    def __str__(self):
        return f"Buyurtma qiluvchi- {self.customer_name} ; Sana- {self.ordered_at}"


    class Meta:
        db_table='orders_table'

    def calculate_order_price(self):
        total_price = 0
        for order_item in self.orderitem_set.all():
            product_price = order_item.product.price
            if order_item.product.discount_set.filter(valid_from__lte=timezone.now(),
                                                      valid_to__gte=timezone.now()).exists():
                discount_percentage = order_item.product.discount_set.get(valid_from__lte=timezone.now(),
                                                                          valid_to__gte=timezone.now()).percentage
                discounted_price = product_price * (1 - discount_percentage / 100)
                total_price += discounted_price * order_item.quantity
            else:
                total_price += product_price * order_item.quantity
        return total_price


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Mahsulot nomi: {self.product.name}; Miqdori:{self.quantity} ; Buyurtma: {self.order}"
