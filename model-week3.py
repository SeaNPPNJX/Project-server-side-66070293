from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    address = models.JSONField(null=True)

    def __str__(self):
        return ...
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    create_date = models.DateTimeField('date created')
    expired_in = models.IntegerField(default=60)

    def __str__(self):
        return ...
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return ...

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date ordered')
    remark = models.TextField(null=True)

    def __str__(self):
        return ...
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return ...

class ProductCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return ...
    
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    remaining_amout = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField("shop.ProductCategory")
    
    def __str__(self):
        return ...

class Payment(models.Model):
    order = models.OneToOneField(Order)
    payment_date = models.DateTimeField('date payment')
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return ...
    
class PaymentItem(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    order_item = models.OneToOneField(OrderItem)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return ...

class PaymentMethod(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    method = models.TextChoices(['QR','CREDIT'])
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return ...
    
