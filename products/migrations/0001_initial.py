# Generated by Django 2.0.7 on 2018-07-28 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Product name')),
                ('kcal', models.PositiveIntegerField(null=True, verbose_name='Calories per 100g')),
                ('protein', models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Protein per 100g')),
                ('carbohydrate', models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Carbohydrate per 100g')),
                ('sugar', models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Sugar per 100g')),
                ('fat', models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Fat per 100g')),
                ('fibre', models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Fibre per 100g')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/', verbose_name='Photo')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(null=True, verbose_name='Content')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='products.ProductCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='comment',
            field=models.ManyToManyField(related_name='products', to='products.ProductComment'),
        ),
    ]
