from django.urls import path
from .views import MenuItemView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('menu/items', MenuItemView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>', SingleMenuItemView.as_view(), name='single-menu-item'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]