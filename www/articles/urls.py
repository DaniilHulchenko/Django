from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

# /articles/

urlpatterns = [
    path('create_articles', views.create, name='create_art'),
    path('page/<int:pk>', views.articles_pages, name='articles_pages'),

    # path('details/<int:pk>', views.Articles_Details.as_view(), name='art-detail'),
    path('details/<slug:art_slug>', views.Articles_Details.as_view(), name='art-detail'),

    # path('category/<int:pk>', views.show_category, name='show_cat' ),
    # path('category/<slug:cat_slug>', views.show_category, name='show_cat' ),
    path('category/<slug:cat_slug>', cache_page(60)(views.Show_Category_Art.as_view()), name='show_cat'),

    path('qwerty', views.layout),
]

