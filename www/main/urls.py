from django.urls import path, include
from . import views
from django.conf import settings

# admin/
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('feedback', views.feedback, name='feedback'),
    path('location', views.location, name='location'),
    path('registration',views.Register.as_view(), name='reg'),
    # path('registration',views.registration, name='reg'),
    path('logout', views.logout_view, name='logout'),
    path('account/<int:pk>', views.Account.as_view(),name='account'),
    path('accounts/<int:pk>/edit', views.Edit_Account.as_view(), name='edit_account'),

]


if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ]+ urlpatterns