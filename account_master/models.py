from django.db import models
from django.utils import timezone
from django.conf import settings


class Master(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    slug = models.SlugField(blank=True, null=True, max_length=200, unique=True, verbose_name='User')
    middle_name = models.CharField(blank=True, null=True, default=None, max_length=200,
                                   verbose_name='Отчество мастера')
    phone = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Номер тел. мастера')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='masters/%Y/%m/%d/', blank=True, verbose_name='Фотография мастера')
    description = models.TextField(max_length=512, blank=True, verbose_name='Описание мастера')
    available = models.BooleanField(default=False, verbose_name='Актуальность мастера')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)
