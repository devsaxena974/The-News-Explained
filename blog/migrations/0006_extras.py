# Generated by Django 3.1.7 on 2021-03-10 15:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210309_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
