from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name='categories'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('cart/menu-items/', views.CartView.as_view(), name='cart'),
    path('orders/', views.OrderView.as_view(), name='orders'),
    path('groups/manager/users/', views.ManagerUsersView.as_view(), name='manager-users'),
    path('groups/delivery-crew/users/', views.DeliveryCrewUsersView.as_view(), name='delivery-crew-users'),
    path('groups/manager/users/<int:pk>/', views.ManagerUserDetailView.as_view(), name='manager-user-detail'),
    path('groups/delivery-crew/users/<int:pk>/', views.DeliveryCrewUserDetailView.as_view(), name='delivery-crew-user-detail'),
]
