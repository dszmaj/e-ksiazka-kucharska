# Generated by Django 2.0.7 on 2018-07-23 13:42

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
                ('name', models.CharField(max_length=150, null=True, verbose_name='Nazwa dania')),
                ('kcal', models.PositiveIntegerField(null=True, verbose_name='Ilość kalorii w 100g')),
                ('protein', models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Zawartość białka w 100g')),
                ('carbohydrate', models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Zawartość węglowodanów 100g')),
                ('sugar', models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Zawartość cukru w 100g')),
                ('fat', models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Zawartość tłuszczu w 100g')),
                ('fibre', models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Zawartość błonnika w 100g')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/', verbose_name='Zdjęcie produktu')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(null=True, verbose_name='Treść')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='products.ProductCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductComment'),
        ),
    ]