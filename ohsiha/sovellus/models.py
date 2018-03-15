from django.db import models

# Create your models here.


class video(models.Model):
    def __str__(self):
        return self.nimi
    nimi = models.CharField(max_length=200)
    pituus = models.CharField(max_length=200)
    katselukerrat = models.IntegerField()
    kanava = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    julkaistu = models.DateTimeField()
