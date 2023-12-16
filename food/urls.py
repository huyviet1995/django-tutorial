from . import views
from django.urls import path

app_name = 'food'
 
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('<int:item_id>', views.detail, name='detail'),
    path('/item', views.item, name='item'),
    path('', views.index, name='index'),
    # Add item
    path('add', views.create_item, name="create_item"),

    # Update item
    path('update/<int:item_id>', views.update_item, name="update_item"),

    # delete
    path('delete/<int:item_id>', views.delete_item, name="delete_item"),
]