# Generated by Django 4.2.4 on 2023-08-18 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0001_initial'),
        ('transaction_app', '0002_alter_transaction_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(default='Grocery', on_delete=django.db.models.deletion.CASCADE, related_name='category', to='category_app.category'),
        ),
    ]