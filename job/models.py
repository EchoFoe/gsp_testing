from django.db import models
from django.utils import timezone
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    name = models.CharField(max_length=200, db_index=True, unique=True, verbose_name='Подкатегория')
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True, verbose_name='Nazvanie_kategorii')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Категория')
    is_active = models.BooleanField(default=True, verbose_name='Активность категории')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = 'Категория -> Подкатегория'
        verbose_name_plural = 'Категории -> Подкатегории'

    class Meta:
        verbose_name = 'Категория -> Подкатегория'
        verbose_name_plural = 'Категории -> Подкатегории'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('job:offer_list_by_category', args=[self.slug])


class Offer(models.Model):
    category = TreeManyToManyField(Category, related_name='offers', blank=True, verbose_name='Категория работ')
    first_name = models.CharField(blank=True, null=True, default=None, max_length=200, verbose_name='Имя заказчика')
    last_name = models.CharField(blank=True, null=True, default=None, max_length=200, verbose_name='Фамилия заказчика')
    middle_name = models.CharField(blank=True, null=True, default=None, max_length=200, verbose_name='Отчество заказчика')
    phone = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Номер тел.')
    email = models.EmailField(max_length=128, blank=True, null=True, default=None, verbose_name='Емейл')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование работ')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Слаг')
    image = models.ImageField(upload_to='offers/%Y/%m/%d', blank=True, verbose_name='Фото')
    description = models.TextField(max_length=512, blank=True, verbose_name='Описание работ')
    price = models.DecimalField(blank=True, null=True, default=None, max_digits=10, decimal_places=0,
                                verbose_name='Цена работы')
    start_time = models.DateField(null=True, blank=True, default=None, verbose_name='Дата начала работ')
    end_time = models.DateField(null=True, blank=True, default=None, verbose_name='Дата окончания работ')
    available = models.BooleanField(default=False, verbose_name='Актуальность заказа')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    @property
    def Категории(self):
        return "\n".join([p.name for p in self.category.all()])

    class Meta:
        ordering = ('-created', 'name')
        index_together = (('id', 'slug'),)
        verbose_name = 'Предложение о работе'
        verbose_name_plural = 'Предложения о работе'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('job:offer_detail', args=[self.id, self.slug])
