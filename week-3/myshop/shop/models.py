from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    address = models.JSONField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    create_date = models.DateTimeField('date created')
    expired_in = models.IntegerField(default=60)

    def __str__(self):
        return f"Cart #{self.id} ของ {self.customer}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date ordered')
    remark = models.TextField(null=True)

    def __str__(self):
        return f"Order #{self.id} ของ {self.customer}"

class ProductCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField("shop.ProductCategory")

    def __str__(self):
        return self.name

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.amount} x {self.product.name} ใน {self.cart}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.amount} x {self.product.name} ใน {self.order}"

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField('date payment')
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Payment #{self.id} สำหรับ {self.order}"

class PaymentItem(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    order_item = models.OneToOneField(OrderItem, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"PaymentItem #{self.id} สำหรับ {self.order_item}"

class PaymentMethod(models.Model):
    class MethodType(models.TextChoices):
        QR = 'QR'
        CREDIT = 'CREDIT'

    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    method = models.CharField(
        max_length=10,
        choices=MethodType.choices,
        default=MethodType.QR,
        null=False,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.method} - {self.price} บาท (Payment #{self.payment.id})"