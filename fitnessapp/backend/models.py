from django.db import models
from django.core.validators import MinValueValidator

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return self.name

from django.contrib.auth.models import User

class Subscriber(models.Model):
    membership_types = [
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    goal = models.CharField(max_length=50, blank=True, null=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    membership_type = models.CharField(max_length=20, choices=membership_types)
    start_date = models.DateField()
    end_date = models.DateField()
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # in kilograms
    height = models.DecimalField(max_digits=5, decimal_places=2)  # in centimeters
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))

    def __str__(self):
        return self.name

class Recommendation(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    recommendation_type = models.CharField(max_length=50)
    recommendation_text = models.TextField()

    def __str__(self):
        return f"Recommendation for {self.subscriber.name} ({self.recommendation_type})"


class AttendanceRecord(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    attended = models.BooleanField(default=False)

class RevenueRecord(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"Revenue on {self.date}"
