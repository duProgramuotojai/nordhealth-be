# Generated by Django 4.0.2 on 2022-02-09 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_productsmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geeksmodel',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='geeksmodel',
            name='shopping_cart',
            field=models.ManyToManyField(blank=True, to='api.ProductsModel'),
        ),
    ]
