from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Nazvanie_kategorii')
    is_active = models.BooleanField(default=True, null=True, blank=True, verbose_name='Активность категории')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория рекламы'
        verbose_name_plural = 'Категории реклам'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('ad:promotion_list_by_category', args=[self.slug])


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE,
                                 verbose_name='Категория рекламы')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название подкатегории')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Nazvanie_podkategorii')
    is_active = models.BooleanField(default=True, null=True, blank=True, verbose_name='Активность категории')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подкатегория рекламы'
        verbose_name_plural = 'Подкатегории реклам'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('ad:promotion_list_by_subcategory', args=[self.slug])


class Promotion(models.Model):
    category = models.ManyToManyField(Category, related_name='promotions', blank=True,
                                 verbose_name='Категория рекламы')
    subcategory = models.ForeignKey(SubCategory, related_name='promotions', on_delete=models.CASCADE,
                                    verbose_name='Податегория рекламы')
    # subcategory_2 = models.ManyToManyField(Category, blank=True, null=True, verbose_name='Категория рекламы_2')
    name = models.CharField(blank=True, null=True, default=None, max_length=200, verbose_name='Название рекламодателя')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Nazvanie_reklamodatelya')
    country = models.CharField(blank=True, null=True, default='Россия', max_length=200, verbose_name='Страна')
    region = models.CharField(blank=True, null=True, default='Курская область', max_length=200, verbose_name='Регион')
    town = models.CharField(blank=True, null=True, default='Курск', max_length=200, verbose_name='Город')
    address = models.TextField(max_length=512, blank=True, verbose_name='Адрес')
    site = models.URLField(max_length=1024, blank=True, default=None, null=None, verbose_name='Сайт')
    phone = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name='Номер тел.')
    email = models.EmailField(max_length=128, blank=True, null=True, default=None, verbose_name='Емейл')
    photo = models.ImageField(upload_to='promotions_photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    logotype = models.ImageField(upload_to='promotions_logotypes/%Y/%m/%d', blank=True, verbose_name='Логотип')
    description = models.TextField(max_length=2048, blank=True, verbose_name='Описание деятельности')
    is_active = models.BooleanField(default=False, verbose_name='Активность рекламы')
    paid = models.BooleanField(default=False, verbose_name='Оплачен показ рекламы?')
    schedule_start = models.TimeField(blank=True, null=True, verbose_name='Начало рабочего дня (Пон - Пт)')
    schedule_end = models.TimeField(blank=True, null=True, verbose_name='Конец рабочего дня (Пон - Пт)')
    weekend_start = models.TimeField(blank=True, null=True, verbose_name='Начало рабочего дня (Суббота)')
    weekend_end = models.TimeField(blank=True, null=True, verbose_name='Конец рабочего дня (Суббота)')
    weekend2_start = models.TimeField(blank=True, null=True, verbose_name='Начало рабочего дня (Воскресенье)')
    weekend2_end = models.TimeField(blank=True, null=True, verbose_name='Конец рабочего дня (Воскресенье)')
    dinner_time_start = models.TimeField(blank=True, null=True, verbose_name='Обеденный перерыв (начало)')
    dinner_time_end = models.TimeField(blank=True, null=True, verbose_name='Обеденный перерыв (конец)')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    @property
    def Категории(self):
        return "\n".join([p.name for p in self.category.all()])

    class Meta:
        ordering = ('-created', 'name')
        index_together = (('id', 'slug'),)
        verbose_name = 'Рекламирование'
        verbose_name_plural = 'Рекламирование'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('ad:promotion_detail', args=[self.id, self.slug])


class PromotionDetails(models.Model):
    promotion = models.ForeignKey(Promotion, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Место под рекламу (детали)')
    is_main = models.BooleanField(default=False, blank=True, null=True, verbose_name='Главный офис')
    is_not_main = models.BooleanField(default=True, blank=True, null=True, verbose_name='Дополнительный офис')
    is_active = models.BooleanField(default=True, blank=True, null=True, verbose_name='Активный?')
    schedule_start = models.TimeField(blank=True, null=True, verbose_name='Начало рабочего дня (Пон - Пт)')
    schedule_end = models.TimeField(blank=True, null=True, verbose_name='Конец рабочего дня (Пон - Пт)')
    weekend_start = models.TimeField(blank=True, null=True, verbose_name='Начало рабочего дня (Суббота)')
    weekend_end = models.TimeField(blank=True, null=True, verbose_name='Конец рабочего дня (Суббота)')
    weekend2_start = models.TimeField(blank=True, null=True, verbose_name='Начало рабочего дня (Воскресенье)')
    weekend2_end = models.TimeField(blank=True, null=True, verbose_name='Конец рабочего дня (Воскресенье)')
    dinner_time_start = models.TimeField(blank=True, null=True, verbose_name='Обеденный перерыв (начало)')
    dinner_time_end = models.TimeField(blank=True, null=True, verbose_name='Обеденный перерыв (конец)')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Подробная информация к рекламодателям'
        verbose_name_plural = 'Подробная информация к рекламодателям'
