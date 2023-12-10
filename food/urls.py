from . import views
from django.urls import path
 
urlpatterns = [
    path('', views.index, name='index'),
    # path('admin/', admin.site.urls),
    path('/<int:item_id>', views.detail, name='detail'),
    path('/item', views.item, name='item'),
]