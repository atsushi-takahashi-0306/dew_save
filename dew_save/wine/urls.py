from django.urls import path
from .import views
from .views import My_wine
from .views import Add_wine
from .views import All_wine
from .views import Detail_wine
from .views import Delete_wine
from .views import Update_wine
from django.conf import settings
from django.conf.urls.static import static


app_name = 'wine'

urlpatterns = [
    path('', views.home, name='home'),
    path('my_wine/', My_wine.as_view(), name='my'),
    path('add_post/', Add_wine.as_view(), name='add'),
    path('new_posts/', All_wine.as_view(), name='all'),
    path('detail_wine/<int:pk>/', Detail_wine.as_view(), name='detail'),
    path('delete_wine/<int:pk>/', Delete_wine.as_view(), name='delete'),
    path('update_wine/<int:pk>/', Update_wine.as_view(), name='update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)