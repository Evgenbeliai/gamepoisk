from django.db import models
from django.utils.text import slugify
class Game(models.Model):
    title = models.CharField(max_length=255,verbose_name='Название игр')
    image = models.ImageField(upload_to='games_image', default='', verbose_name='Изображение игры')
    slug = models.SlugField(max_length=200,unique=True, blank=True, verbose_name='URL-метка' )
    description = models.TextField(max_length=255)
    release_data = models.DateField()
    razrab = models.CharField(max_length=255, verbose_name='Главный разработчик')
    reiting = models.IntegerField()
    company = models.CharField(max_length=255, verbose_name='Компания')
    seria = models.CharField(max_length=255,verbose_name='Серия игр')
    ves = models.IntegerField(verbose_name='Вес игры')
    genre = models.CharField(max_length=255,verbose_name='Жанр игры')
    video = models.FileField(blank=True, upload_to='video/', verbose_name='ссылка на видео')
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Game, self).save(*args,**kwargs)
    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
class Screenshot(models.Model):
    image = models.ImageField(upload_to='screenshot')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    def __str__(self):
        return f'Screenshot for {self.image}'
    class Meta:
        verbose_name = 'Скриншот'
        verbose_name_plural = 'Скриншоты'
# Create your models here.
