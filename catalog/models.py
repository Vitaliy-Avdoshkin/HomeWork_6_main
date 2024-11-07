from django.db import models

class Product(models.Model):
    name = models.CharField(max_lenght=100, verbose_name='Наименование', help_text='Введите наименование продукта')
    description = models.CharField(max_lenght=100, verbose_name='Описание', help_text='Введите описание продукта')
    photo = models.ImageField(upload_to='catalog/photo', blank=True, null=True, verbose_name='Фото', help_text='Загрузите фото продукта')
    category = models.CharField(max_lenght=100, verbose_name='Категория', help_text='Пожалуйста, укажите категорию продукта')
    purchase_price = models.IntegerField()
    created_at = models.DateField(blank=True, null=True, verbose_name='Дата создания', help_text='Укажите дату создания')
    updated_at = models.DateField(blank=True, null=True, verbose_name='Дата последнего изменения', help_text='Укажите дату последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'purchase_price', 'created_at']

    def __str__(self):
        return self.name
