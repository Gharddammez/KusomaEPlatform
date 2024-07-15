# Generated by Django 5.0.4 on 2024-05-30 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_test_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='test',
        ),
        migrations.AddField(
            model_name='answer',
            name='lesson',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.lesson'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.CharField(default='', max_length=100),
        ),
    ]