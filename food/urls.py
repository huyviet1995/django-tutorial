from . import views
from django.urls import path

app_name = 'food'
 
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('<int:item_id>', views.detail, name='detail'),
    path('/item', views.item, name='item'),
    path('', views.index, name='index'),
]