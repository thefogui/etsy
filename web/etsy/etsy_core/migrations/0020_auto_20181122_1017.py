# Generated by Django 2.1.3 on 2018-11-22 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etsy_core', '0019_auto_20181117_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOnCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('items', models.ManyToManyField(through='etsy_core.ProductOnCart', to='etsy_core.Product')),
            ],
        ),
        migrations.AddField(
            model_name='productoncart',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etsy_core.ShoppingCart'),
        ),
        migrations.AddField(
            model_name='productoncart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etsy_core.Product'),
        ),
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='etsy_core.ShoppingCart'),
        ),
    ]
