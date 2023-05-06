from django.db import models
import os
from ckeditor.fields import RichTextField
import uuid
from PIL import Image
from django.utils.timezone import now

# Create your models here.


class GalleryNews(models.Model):
    Name=models.CharField(max_length=70,verbose_name="Название галереи", unique=True,error_messages={'unique':"Галерея с таким названием уже существует!"})

    class Meta:
        db_table="galleryNews"
        ordering = ['-id']
    def __str__(self) -> str:
        return self.Name   
    
    
# Функция для кодировки название файла
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename_start = filename.replace(filename,'_f')
    filename = "%s__%s.%s" % (uuid.uuid4(),filename_start, ext)
    return os.path.join(instance.path_url, filename)
    

class PhotosNews(models.Model):
    URL=models.ImageField(verbose_name="Путь картинки", 
                         upload_to = get_file_path)
    Caption=models.CharField(max_length=200,verbose_name="Название картинки")
    Gallery=models.ForeignKey(GalleryNews,on_delete=models.RESTRICT,verbose_name="Галерея")
    
    path_url = "static/img/"
  
        
    def __str__(self) -> str:
        return self.Caption 
    
    def save(self, *args, **kwargs):
        super(PhotosNews, self).save(*args, **kwargs)
        image = Image.open(self.URL.path)
        if image.width > 800 or image.height > 400:
            output_size = (600, 400)
            image.thumbnail(output_size)
            image.save(self.URL.path)
       
            
    class Meta:
        ordering = ['-id']

# Новости

class News(models.Model):
    Title=models.CharField(max_length=100,verbose_name="Заголовок новости", unique=True,error_messages={'unique':"Новость с таким названием уже существует!"})
    Short_Description = models.CharField(max_length=200,verbose_name="Краткое описание")
    Description=RichTextField(verbose_name="Описание")
    Date_added=models.DateTimeField(verbose_name="Дата публикации", default=now)
    Gallery=models.ForeignKey(GalleryNews,on_delete=models.RESTRICT,verbose_name="Галерея")
    
    class Meta:
        ordering = ['-id']
    def __str__(self) -> str:
        return self.Title
    
# Языки
class Status(models.TextChoices):
    first = "Убитая дорога", "Убитая дорога"
    second = "Локальный дефект", "Локальный дефект"
    third = "Локальный дефект исправлен", "Локальный дефект исправлен"
    fourth = "Дорога отремонтирована", "Дорога отремонтирована"
    fivth = "Нарушения на дороге", "Нарушения на дороге"
    
class Ratind(models.Model):
    Title=models.CharField(max_length=100,verbose_name="Заголовок новости", unique=True,error_messages={'unique':"Новость с таким названием уже существует!"})
    Short_Description = models.CharField(max_length=200,verbose_name="Краткое описание")
    Description=RichTextField(verbose_name="Описание")
    Date_added=models.DateTimeField(verbose_name="Дата публикации", default=now)
    Status = models.CharField(
                               max_length = 78, 
                               choices = Status.choices,
                               default = Status.first,
                               verbose_name = "Статус"
                             )
    Gallery=models.ForeignKey(GalleryNews,on_delete=models.RESTRICT,verbose_name="Галерея")

    class Meta:
        ordering = ['-id']
    def __str__(self) -> str:
        return self.Title