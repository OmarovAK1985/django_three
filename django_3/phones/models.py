from django.db import models
from django.urls import reverse


class Phones(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()


    class Meta:
        ordering = ('-release_date',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('phones:detail', args=[self.id, self.slug])
