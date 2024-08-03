from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
   

class Company(models.Model):
    user = models.OneToOneField(User, related_name='company', on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, related_name='customer_profile', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Customer {self.user.username}"


class Seller(models.Model):
    user = models.OneToOneField(User, related_name='seller_profile', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name='sellers', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Seller {self.user.username}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, related_name='products', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ], default='Pending')

    def __str__(self):
        return f"Order {self.id} by {self.customer.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"


class Address(models.Model):
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.street}, {self.city}"


class Review(models.Model):
    customer = models.ForeignKey(Customer, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.customer.user.username} for {self.product.name}"


class Cart(models.Model):
    customer = models.OneToOneField(Customer, related_name='cart', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for {self.customer.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in cart"


class Wishlist(models.Model):
    customer = models.OneToOneField(Customer, related_name='wishlist', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Wishlist for {self.customer.user.username}"


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='wishlist_items', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} in wishlist"


class Payment(models.Model):
    order = models.OneToOneField(Order, related_name='payment', on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.payment_id} for order {self.order.id}"


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Coupon {self.code} for {self.discount}% off"


class ShippingMethod(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_delivery_days = models.PositiveIntegerField()

    def __str__(self):
        return self.name
