# Generated by Django 3.0.3 on 2020-03-03 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='User')),
                ('last_name', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Фамилия мастера')),
                ('middle_name', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Отчество мастера')),
                ('phone', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Номер тел. мастера')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('photo', models.ImageField(blank=True, upload_to='masters/%Y/%m/%d/', verbose_name='Фотография мастера')),
                ('description', models.TextField(blank=True, max_length=512, verbose_name='Описание мастера')),
                ('available', models.BooleanField(default=False, verbose_name='Актуальность мастера')),
                ('created', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи')),
                ('updated', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия записи')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
                'ordering': ('-created', 'last_name'),
            },
        ),
    ]
