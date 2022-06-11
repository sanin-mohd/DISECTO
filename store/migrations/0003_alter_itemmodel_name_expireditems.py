# Generated by Django 4.0 on 2022-06-11 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_itemmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='ExpiredItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.itemmodel')),
            ],
        ),
    ]