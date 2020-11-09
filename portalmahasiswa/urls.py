from django.urls import path
from portalmahasiswa import views


urlpatterns = [
    path('', views.portal, name="portal"),
]