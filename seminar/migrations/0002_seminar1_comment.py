# Generated by Django 3.0.7 on 2020-07-04 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar1',
            name='comment',
            field=models.TextField(default='good'),
        ),
    ]
