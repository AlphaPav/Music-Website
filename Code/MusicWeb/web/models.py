from django.db import models

# Create your models here.
class Song(models.Model):
    SongID= models.CharField('SongID', max_length=40)
    Domain = models.CharField('Domain',max_length=40)
    AlbumName= models.CharField('AlbumName',max_length=40)
    SingerName=models.CharField('SingerName', max_length=40)
    SongName= models.CharField('SongName', max_length=40)
    SongPath = models.CharField('SongPath', max_length=100)
    AlbumImgPath=models.CharField('AlbumImgPath',max_length=100)
    Lyrics = models.TextField('Lyrics', max_length=2000)

class Img(models.Model):

    png_url= models.ImageField(upload_to='PngImg')
    png_filename= models.CharField('png_filename',max_length=40,default="")



