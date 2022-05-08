from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.RegisterUser.as_view(), name='signup_page'),
    path('logout/', views.logout_user, name='logout'),
]
