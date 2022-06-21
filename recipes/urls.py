from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "recipes"

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/category/<int:category_id>/', views.category, name='category'), # noqa
    path('recipes/<int:id>/', views.recipe, name='recipe'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('/img/favicon.ico'))) # noqa
]
