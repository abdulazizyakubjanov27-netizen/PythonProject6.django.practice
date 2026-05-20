
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    POSTER = 'poster'
    MODERATOR = 'moderator'


class User(AbstractUser):
    role = models.CharField(max_length=200, choices=UserRole.choices, default=UserRole.POSTER)
    phone_number = models.CharField(max_length=11, blank=True)
    email = models.EmailField(max_length=200, unique=True)

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = "users"


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.status}"
