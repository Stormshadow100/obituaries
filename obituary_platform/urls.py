from django.contrib import admin
from django.urls import path
from obituaries import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.submit_obituary, name='submit_obituary'),
    path('obituaries/', views.view_obituaries, name='view_obituaries'),
]
