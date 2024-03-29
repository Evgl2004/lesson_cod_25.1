from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


class Mileage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, **NULLABLE, verbose_name='машина', related_name='mileage')
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, **NULLABLE, verbose_name='мотоцикл', related_name='mileage')

    mileage = models.PositiveIntegerField(verbose_name='пробег')
    year = models.SmallIntegerField(verbose_name='год регистрации')

    def __str__(self):
        if self.car:
            return f'{self.car} - {self.year}'
        else:
            return f'{self.moto} - {self.year}'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробег'

        ordering = ('-year', )
