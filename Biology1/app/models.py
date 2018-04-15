"""
Definition of models.
"""

from django.db import models

from datetime import datetime
from django.contrib import admin        #добавили использование админ. модуля
from django.core.urlresolvers import reverse

# Модель данных Блога
class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
    #user = models.ForeignKey(User, editable = False)


    def get_absolute_url(self):
        return reverse("blogpost", kwargs = {"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Posts"
        ordering = ["-posted"]
        verbose_name = "статья блога"
        verbose_name_plural = "статьи блога"

admin.site.register(Blog)
