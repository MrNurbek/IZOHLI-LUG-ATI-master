from django.db import models

# Create your models here.


class Word(models.Model):
    name = models.CharField(max_length=50, verbose_name="So'z", db_index=True)
    description = models.TextField(max_length=500, verbose_name="So'z izohi")
    slug = models.SlugField(max_length=200, verbose_name="slug")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "So'z"
        verbose_name_plural = "So'zlar"
