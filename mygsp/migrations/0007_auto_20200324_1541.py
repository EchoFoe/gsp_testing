# Generated by Django 3.0.3 on 2020-03-24 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mygsp', '0006_auto_20200224_1245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offer',
            options={'ordering': ('-created', 'name'), 'verbose_name': 'Предложение о работе', 'verbose_name_plural': 'Предложения о работе'},
        ),
    ]
