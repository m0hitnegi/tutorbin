from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload$', views.uploadimage, name='upload'),
    url(r'^saveimage$', views.saveimage, name='saveimage'),
    url(r'^showimage', views.showimage, name='showimage'),
    url(r'^tag', views.searchbytag, name='searchbytag'),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
