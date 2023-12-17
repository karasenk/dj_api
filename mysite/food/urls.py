from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('post/', views.postData),
    path('update/<int:pk>', views.UpdateProduct.as_view())
    ]
