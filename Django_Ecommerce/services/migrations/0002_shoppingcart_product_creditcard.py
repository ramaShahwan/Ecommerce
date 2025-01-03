# Generated by Django 4.2.17 on 2024-12-31 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customer', verbose_name='Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Description')),
                ('ram', models.CharField(blank=True, max_length=50, null=True, verbose_name='RAM')),
                ('processor', models.CharField(blank=True, max_length=255, null=True, verbose_name='Processor')),
                ('screen_size', models.CharField(blank=True, max_length=50, null=True, verbose_name='Screen Size')),
                ('price', models.FloatField(verbose_name='Price')),
                ('storage', models.CharField(blank=True, max_length=50, null=True, verbose_name='Storage')),
                ('battery_life', models.CharField(blank=True, max_length=50, null=True, verbose_name='Battery Life')),
                ('quantity_available', models.IntegerField(verbose_name='Quantity Available')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Product Image')),
                ('warranty_period', models.CharField(blank=True, max_length=50, null=True, verbose_name='Warranty Period')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='Weight')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release Date')),
                ('id_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.brand', verbose_name='Brand')),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.category', verbose_name='Category')),
                ('id_discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.discount', verbose_name='Discount')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=19, verbose_name='Card Number')),
                ('cardholder_name', models.CharField(max_length=255, verbose_name='Cardholder Name')),
                ('expiration_date', models.DateField(verbose_name='Expiration Date')),
                ('cvv', models.CharField(max_length=4, verbose_name='CVV')),
                ('billing_address', models.CharField(max_length=255, verbose_name='Billing Address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customer', verbose_name='Customer')),
            ],
        ),
    ]