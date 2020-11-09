from django.shortcuts import render
from portalmahasiswa import models

# Create your views here.

def portal(request):
    semua_mahasiswa = models.Mahasiswa.objects.all()
    # print(semua_mahasiswa)

    return render(request, 'index.html', {
        'semua_mahasiswa': semua_mahasiswa,
    })