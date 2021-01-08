from django.db import models
from django.contrib.auth.models import User

# Create your models here.
dürümler=[
    (True,'Onaylandı'),
    (False,'Onay Aşamasında')
]
kapaklar = [
    ('ALM','Aliminyum'),
    ('STL','Çelik')
]

voltajlar = [
    (12,12),
    (24,24)
]

ödeme_araçları = [
    ('Kredi','Kredi kartı'),
    ('Nakit','Nakit ödeme')
]


class Bayi(models.Model):
    adı = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    şehir = models.CharField(max_length=20)
    telefon = models.CharField(max_length=11)
    adres = models.TextField()
    ülke = models.CharField(max_length=20)
    aktif = models.BooleanField(default=False)


class Müşteri(models.Model):
    adı = models.CharField(max_length=20)
    soyadı = models.CharField(max_length=20)
    adres = models.TextField()
    telefon = models.CharField(max_length=11)



class Hammadde(models.Model):
    adı = models.CharField(max_length=20)
    depodaki_miktar = models.IntegerField(default=0)
    tedarik_süresi = models.IntegerField(default=1)
    kritik_seviye = models.IntegerField(default=0)


class Ürün(models.Model):
    adı = models.CharField(max_length=20)
    kapak = models.CharField(max_length=3, choices=kapaklar, default='ALM')
    genişlik = models.IntegerField()
    yükseklik = models.IntegerField()
    kapasite = models.IntegerField()
    voltaj = models.IntegerField(choices=voltajlar)
    ağırlık = models.IntegerField()
    bakım_aralığı = models.IntegerField()
    fiyat = models.FloatField()
    depodaki_miktar= models.IntegerField(default=0)
    # Depodaki miktar ürün üretmek için eklendi


class Reçete(models.Model):
    ürün = models.ForeignKey(Ürün,on_delete=models.DO_NOTHING)
    hammadde = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING)
    miktar = models.IntegerField(default=0)


class Sipariş(models.Model):
    bayi = models.ForeignKey(Bayi, on_delete=models.DO_NOTHING)
    sipariş_tarihi = models.DateField(auto_now_add=True,editable=False,blank=True)
    teslim_tarihi = models.DateField(null=True, editable=True,blank=True)
    tutar = models.FloatField(null=True,blank=True)

    onaylandı= models.BooleanField(null=True, choices=dürümler)

    def __str__(self):
        return str(self.pk)


class Sipariş_Ürün(models.Model):
    sipariş = models.ForeignKey(Sipariş, on_delete=models.CASCADE)
    ürün =  models.ForeignKey(Ürün, on_delete=models.CASCADE)
    adet = models.IntegerField(default=1)

class Ödeme(models.Model):
    sipariş = models.ForeignKey(Sipariş, on_delete=models.DO_NOTHING)
    tutar = models.FloatField()
    tarih = models.DateField(auto_now_add=True,editable=False,blank=True)
    ödeme_aracı = models.CharField(max_length=5,choices=ödeme_araçları)

class Bakım(models.Model):
    müşteri = models.ForeignKey(Müşteri, on_delete=models.DO_NOTHING)
    ürün = models.ForeignKey(Ürün, on_delete=models.DO_NOTHING)
    bakım_tarihi = models.DateField(auto_now_add=True, editable=False, blank=True)
    #TODO gelecek bakım tarihi otomatik olarak ürün bakım aralığı hesaplanıp üzerine eklenecek
    tutar = models.FloatField()


class Katolog(models.Model):
    ürün = models.ForeignKey(Ürün, on_delete=models.CASCADE)
    bayi = models.ForeignKey(Bayi, on_delete=models.CASCADE)
    satış_fiyatı = models.FloatField()

class Satış(models.Model):
    bayi = models.ForeignKey(Bayi, on_delete=models.DO_NOTHING)
    müşteri = models.ForeignKey(Müşteri, on_delete=models.DO_NOTHING)
    ürün = models.ForeignKey(Ürün, on_delete=models.DO_NOTHING)
    tarih = models.DateField(auto_now_add=True,editable=False,blank=True)
    satış_fiyatı = models.FloatField()
    alış_fiyatı = models.FloatField()
    ödeme_aracı = models.CharField(max_length=5,choices=ödeme_araçları)


#TODO Ürünler sayfası bağlanacak

#TODO bayi onaylandı tuşu çalıştırılac
#TODO bayiler listelenecek

#TODO bayi kayıt sayfası oluşturulacak kayıt işlemi gerçekleştirilecek giriş yapan bayi
# bayi arayüzüne yönlendirilecek

#TODO Fabrikanın arayüzündeki fonksiyonlar çalışır hale getirilecek
    #TODO Sipariş
    #TODO Ürün ekleme
    #TODO Bayi
    #TODO Ödeme
    #TODO Reçete

#TODO Bayi arayüzündeki fonksiyonlar çalışır hale getirilecek