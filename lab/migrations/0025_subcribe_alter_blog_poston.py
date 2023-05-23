# Generated by Django 4.1.5 on 2023-05-16 05:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0024_alter_appointment_gender_alter_blog_poston_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('emailid', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'Subcribe',
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='poston',
            field=models.DateField(default=datetime.date(2023, 5, 16)),
        ),
    ]
