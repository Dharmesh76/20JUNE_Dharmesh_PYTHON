from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('',views.index),
   path('siteadmin/',views.siteadmin),
   path('manager/',views.sitemanager),
   path('adddata/',views.adddata),
   path('viewdata/',views.viewdata),
   path('deletedata/<int:id>/',views.deletedata),
   path('deleteview/',views.deleteview,name='deleteview'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)