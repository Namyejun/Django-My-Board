# Generated by Django 4.1.7 on 2023-04-06 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='작성시간'),
        ),
    ]
