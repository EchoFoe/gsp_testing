# Generated by Django 3.0.3 on 2020-04-09 15:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Подкатегория')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='Nazvanie_kategorii')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активность категории')),
                ('created', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи')),
                ('updated', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия записи')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='job.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория -> Подкатегория',
                'verbose_name_plural': 'Категории -> Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Имя заказчика')),
                ('last_name', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Фамилия заказчика')),
                ('middle_name', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Отчество заказчика')),
                ('phone', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Номер тел.')),
                ('email', models.EmailField(blank=True, default=None, max_length=128, null=True, verbose_name='Емейл')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Наименование работ')),
                ('slug', models.SlugField(max_length=200, verbose_name='Слаг')),
                ('image', models.ImageField(blank=True, upload_to='offers/%Y/%m/%d', verbose_name='Фото')),
                ('description', models.TextField(blank=True, max_length=512, verbose_name='Описание работ')),
                ('price', models.DecimalField(blank=True, decimal_places=0, default=None, max_digits=10, null=True, verbose_name='Цена работы')),
                ('start_time', models.DateField(blank=True, default=None, null=True, verbose_name='Дата начала работ')),
                ('end_time', models.DateField(blank=True, default=None, null=True, verbose_name='Дата окончания работ')),
                ('available', models.BooleanField(default=False, verbose_name='Актуальность заказа')),
                ('created', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи')),
                ('updated', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата ред-ия записи')),
                ('category', mptt.fields.TreeManyToManyField(blank=True, related_name='offers', to='job.Category', verbose_name='Категория работ')),
            ],
            options={
                'verbose_name': 'Предложение о работе',
                'verbose_name_plural': 'Предложения о работе',
                'ordering': ('-created', 'name'),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
