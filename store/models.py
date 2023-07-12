from django.db import models
import datetime
import os
# Create your models here.

def get_file_path(request,filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')

    filename = "%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/',filename)

class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False,help_text="0=default, 1=Trending")
    meta_title = models.CharField(max_length=150,null=False,blank=False)
    meta_keywords = models.CharField(max_length=150,null=False,blank=False)
    meta_descriptions = models.CharField(max_length=150,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/images/slider.jpg"

    
class Kategori(models.Model):
    #kategori_ID =models.AutoField(primary_key=True)
    kategori_isim = models.CharField(max_length=150,null=False,blank=False)
    slug = models.CharField(max_length=150,null=True,blank=True)  
    kategori_aciklama = models.TextField(max_length=500,null=False,blank=False)  
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    
    def __str__(self):
        return self.kategori_isim   
        #@property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url 

class Alt_Kategori(models.Model):
    #alt_kategori_ID= models.AutoField(primary_key=True)
    slug = models.CharField(max_length=150,null=True,blank=True)  
    Kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)  
    altkategori_isim =  models.CharField(max_length=150,null=False,blank=False)
        
    def __str__(self):
        return self.altkategori_isim  
    
class Urun(models.Model):
    urunID = models.AutoField(primary_key=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE) 
    alt_Kategori = models.ForeignKey(Alt_Kategori, on_delete=models.CASCADE) 
    slug = models.CharField(max_length=150,null=True,blank=True)      
    urun_isim = models.CharField(max_length=150,null=False,blank=False)  
    renk = models.CharField(max_length=150,null=False,blank=False)
    stok = models.IntegerField(null=False, blank=False)
    satis_fiyati = models.FloatField(null=False,blank=False)
    indirimli_satis_fiyati = models.FloatField(null=False,blank=False)
    stokda = models.BooleanField(default=False,help_text="0=default, 1=yok")
    trendUrun = models.BooleanField(default=False,help_text="0=default, 1=Trending")
    gorsel = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    MEMBERSHIP_CHOICES = [
        ("S","Small"),
        ("M","Medium"),
        ("L","Large"),
        ("XL","X Large"),        
    ]
    beden = models.CharField(max_length=2,choices = MEMBERSHIP_CHOICES,default="S")
    def __str__(self):
        return self.urun_isim
    def get_photo_url(self):
        if self.gorsel and hasattr(self.gorsel, 'url'):
            return self.gorsel.url     
    
class Musteri(models.Model):
    kullanıcıIsim = models.CharField(max_length=150,null=False,blank=False)  
    kullanıcıSoyisim = models.CharField(max_length=150,null=False,blank=False) 
    ePosta = models.CharField(max_length=150,null=False,blank=False) 
    sifre =  models.CharField(max_length=150,null=False,blank=False)
    telNo =  models.CharField(max_length=150,null=False,blank=False)
    kullanıcıProfilFoto = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    kullanıcıPuan = models.PositiveSmallIntegerField(default=0,null=True, blank=True)
    kayıtTarihi = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.kullanıcıIsim
    
class Adres(models.Model):
    kullanıcıID = models.ForeignKey(Musteri, on_delete=models.CASCADE)  
    sehir =  models.CharField(max_length=150,null=False,blank=False)  
    sokak = models.CharField(max_length=150,null=False,blank=False) 
    cadde = models.CharField(max_length=150,null=False,blank=False)
    bina = models.CharField(max_length=150,null=False,blank=False)
    def __str__(self):
        return self.sehir
    
class Kart(models.Model):
    kartNo = models.PositiveBigIntegerField(null=False,blank=False,primary_key=True)
    kartIsim = models.CharField(max_length=150,null=False,blank=False)
    kullanıcıID = models.ForeignKey(Musteri, on_delete=models.CASCADE)  
    bankName = models.CharField(max_length=150,null=False,blank=False)
    CVC = models.CharField(max_length=3,null=False,blank=False)
    def __str__(self):
        return self.kartIsim

class Siparis(models.Model):
    siparisID = models.BigAutoField(primary_key=True)
    siparisIsim = models.CharField(max_length=150,null=False,blank=False)
    kullanıcıID = models.ForeignKey(Musteri, on_delete=models.CASCADE)  
    UrunID = models.ForeignKey(Urun, on_delete=models.CASCADE)  
    siparisTarihi = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.siparisIsim

class Iade(models.Model):
    iadeID = models.BigAutoField(primary_key=True)
    kullanıcıID = models.ForeignKey(Musteri, on_delete=models.CASCADE)  
    UrunID = models.ForeignKey(Urun, on_delete=models.CASCADE)  
    iadeTarihi = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.iadeID            
            
class Sube(models.Model):
    subeID = models.BigAutoField(primary_key=True)
    subeIsim = models.CharField(max_length=150,null=False,blank=False) 
    sehir =  models.CharField(max_length=150,null=False,blank=False)  
    sokak = models.CharField(max_length=150,null=False,blank=False) 
    postaKodu = models.CharField(max_length=6,null=False,blank=False)   
    def __str__(self):
        return self.subeIsim
    
class Sepet(models.Model):
    kullanıcıID = models.ForeignKey(Musteri, on_delete=models.CASCADE)  
    UrunID = models.ForeignKey(Urun, on_delete=models.CASCADE)
    def __str__(self):
        return self.kullanıcıID      

class Degerlendirme(models.Model):
    kullanıcıID = models.ForeignKey(Musteri, on_delete=models.CASCADE)  
    UrunID = models.ForeignKey(Urun, on_delete=models.CASCADE)
    urunYorum = models.TextField(max_length=500,null=True,blank=True)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    def __str__(self):
        return self.urunYorum   
    
    
class Product(models.Model):
    category = models.ForeignKey(Kategori, on_delete=models.CASCADE)  
    alt_category = models.ForeignKey(Alt_Kategori, on_delete=models.CASCADE)    
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    product_image= models.ImageField(upload_to=get_file_path, null=True, blank=True)
    descriptions = models.CharField(max_length=250,null=False,blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    descriptions =models.TextField(max_length=500,null=False,blank=False)
    original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False,help_text="0=default, 1=Trending")
    tag = models.CharField(max_length=150,null=False,blank=False)
    meta_title = models.CharField(max_length=150,null=False,blank=False)
    meta_keywords = models.CharField(max_length=150,null=False,blank=False)
    meta_descriptions = models.CharField(max_length=150,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name