# Generated by Django 5.0.6 on 2024-07-07 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0013_alter_article_date_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 7, 7, 15, 3, 52, 788146, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 7, 7, 15, 3, 52, 788146, tzinfo=datetime.timezone.utc)),
        ),
    ]
