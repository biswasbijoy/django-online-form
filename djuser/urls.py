from django.urls import path
from djuser.views import views
from djuser.views.views import PasswordsChangeView

app_name = 'djuser'
urlpatterns = [
    path('signup', views.signUp, name='signup'),
    path('login', views.logIn, name='login'),
    path('logout', views.logOut, name='logout'),
    path('edit-profile', views.EditProfilePageView.as_view(), name='edit_profile'),
    path('<int:pk>/password/', PasswordsChangeView.as_view(), name='password'),
    path('', views.home_auth, name='home'),
]