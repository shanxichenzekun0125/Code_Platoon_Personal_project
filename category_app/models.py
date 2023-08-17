from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)

    def __str__(self):
        return f"Category: <{self.name}> has been created. "
