# Generated by Django 3.1.7 on 2021-03-16 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210313_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extras',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]