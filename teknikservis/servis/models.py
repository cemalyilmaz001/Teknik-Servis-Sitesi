from django.db import models

# Create your models here.
class Ayarlar(models.Model):
    usernameqv   = models.CharField(max_length=50)
    şrkt_name    = models.CharField(max_length=50)
    şrkt_tel     = models.CharField(max_length=50)
    şrkt_email   = models.CharField(max_length=50)


class Data(models.Model):
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50)
    tc_kimlik_no = models.CharField(max_length=11)
    telefon      = models.CharField(max_length=11)
    email        = models.CharField(max_length=50)
    cihaz        = models.CharField(max_length=50)
    marka        = models.CharField(max_length=50)
    model        = models.CharField(max_length=50)
    arıza        = models.CharField(max_length=50)
    açıklama     = models.CharField(max_length=50)
    geliş_tarihi = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    son_degisiklik_tarihi = models.DateTimeField(null=True, blank=True, auto_now_add=True)
