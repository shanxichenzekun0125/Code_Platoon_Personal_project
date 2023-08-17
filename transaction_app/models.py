from django.db import models
from django.utils import timezone
from category_app.models import Category
# Create your models here.
class Transaction(models.Model):
    money_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    time = models.DateTimeField(default=timezone.now, null=False)
    location = models.CharField(max_length=100, default="Hamptonroad area")
    note = models.TextField(default="Would you like to put some notes for this transaction")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    
    def __str__(self):
        return f"A transaction of ${self.money_amount} for {self.category} was recorded"