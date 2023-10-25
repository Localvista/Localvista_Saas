from django.urls import path
from .views import (
    AccountLoginView,
    AccountLogoutView,
    UserAccountUpdateView,
    BusinessAccountUpdateView,
    UserDetailsView,  # Include UserDetailsView
)

urlpatterns = [
    path('update/user/', UserAccountUpdateView.as_view(), name='user-account-update'),
    path('update/business/', BusinessAccountUpdateView.as_view(), name='business-account-update'),
    path('login/', AccountLoginView.as_view(), name='account-login'),
    path('logout/', AccountLogoutView.as_view(), name='account-logout'),
    path('user/details/', UserDetailsView.as_view(), name='user-details'),  # Include UserDetailsView
]
