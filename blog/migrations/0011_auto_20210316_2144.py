# Generated by Django 3.1.7 on 2021-03-17 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210316_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extras',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]