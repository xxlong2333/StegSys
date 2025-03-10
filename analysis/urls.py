from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('upload/', views.upload_image, name='upload_image'),
    path('analyze/<int:analysis_id>/', views.analyze_image, name='analyze_image'),
    path('history/', views.get_analysis_history, name='analysis_history'),
] 