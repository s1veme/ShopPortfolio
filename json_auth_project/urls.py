from django.contrib import admin
from django.urls import path, include
from authentication.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls', namespace='authentication')),
    path('api/shop/', include('shop.urls'))
]
