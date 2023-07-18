# Generated by Django 4.1.3 on 2023-07-17 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('profile_image_url', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=300)),
                ('seller', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('details', models.CharField(max_length=300)),
                ('date_placed', models.DateField()),
                ('payment_type', models.CharField(max_length=50)),
                ('open', models.BooleanField(default=True)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_order', to='bangazonapi.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to='bangazonapi.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product_image_url', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('product_info', models.CharField(max_length=500)),
                ('created_on', models.DateField()),
                ('category', models.CharField(max_length=50)),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_product', to='bangazonapi.seller')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='bangazonapi.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='bangazonapi.product')),
            ],
        ),
    ]
