from django.urls import path
from portalmahasiswa import views

urlpatterns = [
    path('', views.portal, name="portal"),
    path('mahasiswa/detail/<int:pk>', views.MahasiswaDetailView.as_view(), name="mahasiswa_detail"),
    path('mahasiswa/update/<int:pk>', views.MahasiswaUpdateView.as_view(), name="mahasiswa_update"),
    path('mahasiswa/delete/<int:pk>', views.MahasiswaDeleteView.as_view(), name="mahasiswa_delete"),
    path('mahasiswa/create/', views.MahasiswaCreateView.as_view(), name="mahasiswa_create"),
]