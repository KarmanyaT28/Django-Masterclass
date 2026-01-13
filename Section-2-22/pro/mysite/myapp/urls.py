from django.urls import path
from . import views


app_name = 'myapp'

urlpatterns = [
    path('',views.IndexClassView.as_view(),name='index'),
    # path('item/',views.item,name='item'),
    path('<int:pk>/',views.DetailClassView.as_view(), name='detail'),
    path('add/',views.ItemCreateView.as_view(), name='create-item'), 
    path('update/<int:pk>/',views.ItemUpdateView.as_view(), name='update-item'),
    path('delete/<int:pk>/',views.ItemDeleteView.as_view(), name='delete-item'),
]
