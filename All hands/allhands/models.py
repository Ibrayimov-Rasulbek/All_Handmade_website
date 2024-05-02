from django.db import models

# Create your models here.
class Mahsulot(models.Model):
    mahsulot_nomi = models.CharField(max_length=100)
    mahsulot_izohi = models.CharField(max_length=200)
    rasm = models.ImageField(blank=True)
    mahsulot_narxi = models.IntegerField(blank=True, null=True)
    
    def __repr__(self):
        return self.mahsulot_nomi