from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('hello/', views.HelloView.as_view(), name='hello'),
    # path('hello/', views.hello_view, name='hello'),
    path('product/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_details, name='product_details'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]