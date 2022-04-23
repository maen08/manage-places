from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main_app.views import PlaceView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<slug:slug>', PlaceView.as_view(
        {
            'delete':'destroy',
            'get':'list'
        }
    )),
    path('api/', PlaceView.as_view(
        {
            'get':'list',
            'post':'create'
        }
    ))
]





if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)