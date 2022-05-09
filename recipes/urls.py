
#from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

app_name = "recipes"

urlpatterns = [
    path('home', views.home, name='home'),
    path('recipes/category/<int:category_id>/', views.category, name='category'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
