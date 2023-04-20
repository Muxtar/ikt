from django.urls import path
from accounts.views import * #login, logout, register
from django.contrib.auth import views as auth_views
from accounts.views import MyPasswordResetView

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name = 'register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name = 'profile'),

    path('password_reset/', MyPasswordResetView.as_view(), name='forget_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

