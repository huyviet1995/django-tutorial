# Generated by Django 5.0 on 2023-12-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(blank=True, default='https://cdn-icons-png.flaticon.com/512/1147/1147805.png', max_length=5000, null=True),
        ),
    ]