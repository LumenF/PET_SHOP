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
