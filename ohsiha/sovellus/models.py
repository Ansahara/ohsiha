from django.db import models

# Create your models here.


class autot(models.Model):
    def __str__(self):
        return self.malli
    malli = models.CharField(max_length=200)
    kayttovoima = models.CharField(max_length=200)
    vaihteisto = models.CharField(max_length=200)
    hinta = models.IntegerField()
    tunniste = models.IntegerField()
    moottori = models.IntegerField()
    vuosimalli = models.IntegerField()
    mittarilukema = models.IntegerField()
