from django.db import models


class OrderModel(models.Model):
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    name = models.CharField(
        verbose_name='Имя',
        max_length=255,
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=255,
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=255,
    )

    def __str__(self):
        return self.name


class ContactModel(models.Model):
    class Meta:
        verbose_name = 'Инфо'
        verbose_name_plural = 'Инфо'

    name = models.CharField(
        verbose_name='Имя',
        max_length=255,
    )
    value = models.CharField(
        verbose_name='Значение',
        max_length=255,
    )