from django.db import models
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Подкатегория')
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True, verbose_name='Nazvanie_kategorii')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Категория')
    is_active = models.BooleanField(default=True, verbose_name='Активность категории')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = 'Тест мптт'
        verbose_name_plural = 'Тест мптт'

    class Meta:
        verbose_name = 'Категория -> Подкатегория'
        verbose_name_plural = 'Категории -> Подкатегории'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('reclame:promotion_list_by_category', args=[self.slug])


class Promotion(models.Model):
    category = TreeManyToManyField(Category, blank=True, symmetrical=False, related_name='promotions', verbose_name='Категория')
    # category = TreeForeignKey(Genre, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='promotions', verbose_name='Категория')
    name = models.CharField(blank=True, null=True, default=None, max_length=200, verbose_name='Название рекламодателя')
    slug = models.SlugField(null=True, blank=True, max_length=200, db_index=True,
                            verbose_name='Nazvanie_reklamodatelya')
    country = models.CharField(blank=True, null=True, default='Россия', max_length=200, verbose_name='Страна')
    region = models.CharField(blank=True, null=True, default='Курская область', max_length=200, verbose_name='Регион')
    town = models.CharField(blank=True, null=True, default='Курск', max_length=200, verbose_name='Город')
    site = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Сайт')
    email = models.EmailField(max_length=128, blank=True, null=True, default=None, verbose_name='Емейл')
    photo = models.ImageField(upload_to='promotions_test_photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    logotype = models.ImageField(upload_to='promotions_test_logotypes/%Y/%m/%d', blank=True, verbose_name='Логотип')
    description = models.TextField(max_length=512, blank=True, verbose_name='Описание деятельности')
    is_active = models.BooleanField(default=False, verbose_name='Активность рекламы')
    paid = models.BooleanField(default=False, verbose_name='Оплачен показ рекламы?')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        ordering = ('-created', 'name')
        index_together = (('id', 'slug'),)
        verbose_name = 'Место под рекламу'
        verbose_name_plural = 'Места под рекламу'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('reclame:promotion_detail', args=[self.id, self.slug])


class PromotionDetails(models.Model):
    promotion = models.ForeignKey(Promotion, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                  verbose_name='Место под рекламу (детали)')
    is_main = models.BooleanField(default=False, blank=True, null=True, verbose_name='Гл. офис?')
    is_not_main = models.BooleanField(default=True, blank=True, null=True, verbose_name='Доп. офис')
    is_active = models.BooleanField(default=True, blank=True, null=True, verbose_name='Активный?')
    address = models.CharField(max_length=1024, blank=True, verbose_name='Адрес')
    phone = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name='Номер тел.')
    schedule_start = models.TimeField(blank=True, null=True, verbose_name='Н. раб. дня (Пон - Пт)')
    schedule_end = models.TimeField(blank=True, null=True, verbose_name='К. раб. дня (Пон - Пт)')
    weekend_start = models.TimeField(blank=True, null=True, verbose_name='Н. раб. дня (Суббота)')
    weekend_end = models.TimeField(blank=True, null=True, verbose_name='К. раб. дня (Суббота)')
    weekend2_start = models.TimeField(blank=True, null=True, verbose_name='Н. раб. дня (Воскресенье)')
    weekend2_end = models.TimeField(blank=True, null=True, verbose_name='К. раб. дня (Воскресенье)')
    dinner_time_start = models.TimeField(blank=True, null=True, verbose_name='Обед. пер-в (н.)')
    dinner_time_end = models.TimeField(blank=True, null=True, verbose_name='Обед. пер-в (к.)')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Подробная информация к рекламодателю'
        verbose_name_plural = 'Подробная информация к рекламодателям'
