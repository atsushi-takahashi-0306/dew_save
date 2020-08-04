from django.urls import path
from .import views
from .views import Add_wine
from .views import All_wine
from .views import Detail_wine
from .views import Delete_wine
# imege file用↓
from django.conf import settings
from django.conf.urls.static import static



app_name = 'wine'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_wine/', Add_wine.as_view(), name='add'),
    path('all_wine/', All_wine.as_view(), name='all'),
    path('detail_wine/<int:pk>/', Detail_wine.as_view(), name='detail'),
    path('delete_wine/<int:pk>/', Delete_wine.as_view(), name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)