from django.db import models
from django.utils import timezone


class EmailType(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Тип эл. адреса')
    is_active = models.BooleanField(default=True, null=True, blank=True, verbose_name='Активность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Тип е-мейла'
        verbose_name_plural = 'Типы е-мейлов'


class EmailSendingFact (models.Model):
    type = models.ForeignKey(EmailType, null=True, blank=True, default=True, on_delete=models.CASCADE, verbose_name='Тип эл. адреса')
    offer = models.ForeignKey('job.Offer', blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Работа')
    email = models.EmailField(max_length=128, blank=True, null=True, default=None, verbose_name='Емейл')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return self.type.name

    class Meta:
        verbose_name = 'Отправленный е-мейл'
        verbose_name_plural = 'Отправленные е-мейлы'
