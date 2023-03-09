from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
]


admin.site.site_header = 'Заявки'
admin.site.site_title = 'Заявки'
admin.site.index_title = ''