from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField("Ваше имя:", max_length=100)
    task = models.TextField("Ваше сообщение:")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'Форум'