from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('base/', views.base_view, name="base"),
    path('', views.home_view, name="home"),
]
