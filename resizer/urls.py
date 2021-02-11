from django.urls import path

from . import views


urlpatterns = [
    path('', views.PicturesView.as_view(), name='picture_list'),
    path('add/', views.PictureCreate.as_view(), name='picture_create'),
    path('<int:pk>/', views.PictureDetail.as_view(), name='picture_detail'),
]
