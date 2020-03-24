# Generated by Django 3.0.3 on 2020-02-19 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygsp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='end_time',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата окончания работ'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='start_time',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата начала работ'),
        ),
    ]
