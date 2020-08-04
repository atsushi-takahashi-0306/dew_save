from django.urls import path
from .import views
from .views import Add_wine
from .views import All_wine
# imege file用↓
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

path('', views.home, name='home'),
path('add_wine/', Add_wine.as_view(), name='add'),
path('all_wine/', All_wine.as_view(), name='all'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)