from django.db import models


class AutoBrand(models.Model):
    brand = models.CharField(
        verbose_name='Марка автомобиля',
        max_length=32,
        default=None
    )

    def __str__(self):
        return "%s" % self.brand

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'


class AutoModel(models.Model):
    model = models.CharField(
        verbose_name='Модель автомобиля',
        max_length=32,
        default=None
    )

    def __str__(self):
        return "%s" % self.model

    class Meta:
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модели автомобилей'


class Auto(models.Model):
    brand = models.ForeignKey(
        AutoBrand,
        verbose_name='Марка',
        null=True,
        default=None
    )
    model = models.ForeignKey(
        AutoModel,
        verbose_name='Модель',
        null=True,
        default=None
    )
    category = models.PositiveIntegerField(
        verbose_name='Категория',
        max_length=1,
        null=True,
        default=None
    )
    year = models.PositiveIntegerField(
        verbose_name='Год выпуска',
        null=True,
        default=None
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        null=True,
        default=0
    )
    owner = models.CharField(
        verbose_name='Собственик',
        max_length=32,
        null=True,
        default=None
    )

    def _get_category(self):
        if self.year < 1990:
            return 0
        elif self.year >= 1990 and self.year < 2000:
            return 1
        elif self.year >= 2000 and self.year < 2010:
            return 2
        else:
            return 3

    def save(self, *args, **kwargs):
        if self.year:
            self.category = self._get_category()
        super(Auto, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


