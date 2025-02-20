# Generated by Django 4.2.17 on 2025-01-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_product_dvd_product_color_product_fingerprint_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['name'], 'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.AddField(
            model_name='address',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Description'),
        ),
    ]
