# Generated by Django 5.0.6 on 2024-06-23 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='article-default-image.png', upload_to='images/'),
        ),
    ]
