from django.db import models

# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('processing', 'Processing'),
#         ('delivered', 'Delivered'),
#         ('cancelled', 'Cancelled'),
#     ]
#
#     customer_name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=20)
#     address = models.TextField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     is_paid = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.customer_name} - {self.status}"
#

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')