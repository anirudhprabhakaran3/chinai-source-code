# Generated by Django 2.2.7 on 2020-03-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200322_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(default='https://picsum.photos/700.webp?blur', max_length=300),
        ),
    ]
