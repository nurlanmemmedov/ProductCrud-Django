# Generated by Django 3.0.2 on 2020-02-03 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_translate',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
