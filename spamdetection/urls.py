from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detect', views.detect, name='detect'),
    path('predict', views.predict, name='predict'),
    path('demo', views.demo, name='demo')
]
