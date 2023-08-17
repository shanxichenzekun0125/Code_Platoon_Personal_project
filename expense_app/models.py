from django.db import models

# Create your models here.
class Expense(models.Model):
    category = models.CharField(max_length=100, null=False)
    money_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    time = models.DateTimeField(auto_now_add=True, null=False)
    location = models.CharField(max_length=100)
    note = models.TextField()