from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from result import views as result_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', result_views.home, name='home'),
    path('compare-ingredients/', result_views.compare_ingredients, name='compare_ingredients'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 



