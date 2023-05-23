# Generated by Django 4.1.5 on 2023-03-13 05:57

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='tittle',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='poston',
            field=models.DateField(default=datetime.date(2023, 3, 13)),
        ),
    ]
