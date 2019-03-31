from django.db import models

class Subscribers(models.Model):
        email = models.EmailField(unique=True)
        first_name = models.CharField(max_length=200, blank=True,)
        last_name = models.CharField(max_length=200, blank=True,)

        def __str__(self):
          return "Агент %s %s" % (self.first_name, self.email)
        
        class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Риелтора'
            verbose_name_plural = 'Риелторы'

class apartment(models.Model):
    title = models.CharField(max_length=200, blank=True, help_text="введите название обьекта")
    text = models.CharField(max_length=200, blank=True, help_text="Адрес обьекта")
    price = models.FloatField(default=0.0, help_text="цена обьекта")

    def __str__(self):
        return "%s %s %s" % (self.title, self.price, self.text)

    class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Квартиру'
            verbose_name_plural = 'Квартиры'
    

class rental(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
    )

    text = models.CharField(
        max_length=200,
        blank=True,
    )
    class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Арену квартиры'
            verbose_name_plural = 'Аренда квартиры'