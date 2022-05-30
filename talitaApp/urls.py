from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = "talitaApp"

urlpatterns = [
    # path('', views.dashboard, name='dashboard'),
    path('',views.dashboard, name='dashboard'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('register', views.register, name='register'),

    #reset
    # change password urls
    path('password_change/',
    auth_views.PasswordChangeView.as_view(success_url='password_reset/done/'),
    name='password_change'),

    path('password_change/done/',
    auth_views.PasswordChangeDoneView.as_view(),
    name='password_change_done'),
        # reset password urls
    path('password_reset/',
        auth_views.PasswordResetView.as_view(
            success_url=reverse_lazy('talitaApp:password_reset_done'),
            email_template_name = 'registration/password_reset_email.html'),
        name='password_reset'),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('talitaApp:password_reset_complete'),),
        name='password_reset_confirm'),
    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),

        #dashboard
    #edit
    path('edit/<int:pk>/', views.edit, name='edit'),
    #add
    path('add/', views.add, name='add'),
    #delete Card
    path('delete/<int:pk>/', views.delete, name='deleteImg'),

    #pdf
    path('pdf/', views.pdf, name='pdf')
    
    
    
]