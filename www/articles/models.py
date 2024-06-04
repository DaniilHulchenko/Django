from django.db import models
from django.urls import reverse
# Create your models here.

class Articles(models.Model):
    objects: None = None
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Preview', max_length=200)
    description = models.TextField('Description', blank= True)
    # photoID = models.IntegerField('PictureID', unique=True)
    photo = models.ImageField('Picture', upload_to='articles_photos/%Y/%m/%d/', null=True )
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100,null=True,unique=True, db_index=True, verbose_name='slug')
    cat = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('art-detail', kwargs={'pk': self.pk} )

    def get_absolute_url_slug(self):
        return reverse('art-detail', kwargs={'art_slug': self.slug} )

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-date_create']

class Category(models.Model):

    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True,verbose_name='slug')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_cat', kwargs={'cat_slug': self.slug} )


    # class Meta:
    #     verbose_name = 'Category'
    #     verbose_name_plural = 'Categorys'
    #


