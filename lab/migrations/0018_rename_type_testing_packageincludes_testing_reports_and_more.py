# Generated by Django 4.1.5 on 2023-04-14 04:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0017_alter_blog_poston_alter_testing_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testing',
            old_name='Type',
            new_name='packageincludes',
        ),
        migrations.AddField(
            model_name='testing',
            name='Reports',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='poston',
            field=models.DateField(default=datetime.date(2023, 4, 14)),
        ),
    ]
