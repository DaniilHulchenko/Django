from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Articles,Category

# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug','cat','get_article_photo', 'date_create', 'date_update' )
    list_display_links = ('id', 'title')
    # list_display_links = ('id', 'title', 'photo')
    search_fields = ('title', 'id')
    prepopulated_fields = {"slug": ("title",)}
    ordering = ['id'] # or ('id',)
    fields =['title','anons','description','photo','get_article_photo','slug','date_create','date_update']
    readonly_fields = ['get_article_photo','date_create','date_update']
    save_on_top = True

    def get_article_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=80>")

admin.site.register(Articles,ArticlesAdmin)


class CategoryAdmin(admin.ModelAdmin):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['cat'].empty_label = "No one"

    list_display = ('id', 'name',  'slug')
    list_display_links = ('name', 'id')
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}
    ordering = ['id']



admin.site.register(Category,CategoryAdmin)