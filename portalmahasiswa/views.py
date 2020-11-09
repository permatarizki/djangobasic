from django.shortcuts import render
from portalmahasiswa import models
from portalmahasiswa.forms import MahasiswaForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def portal(request):
    semua_mahasiswa = models.Mahasiswa.objects.all()
    # print(semua_mahasiswa)
    def post(self, request):
        print(request.POST.get('keyword', ''))

    
    return render(request, 'index.html', {
        'semua_mahasiswa': semua_mahasiswa,
    })

class MahasiswaDetailView(DetailView):
    model = models.Mahasiswa
    template_name = "detail_mahasiswa.html"

class MahasiswaCreateView(CreateView):
    model = models.Mahasiswa
    template_name = "create_mahasiswa.html"
    form_class = MahasiswaForm
    success_url = reverse_lazy('portal')

class MahasiswaUpdateView(UpdateView):
    model = models.Mahasiswa
    template_name = "update_mahasiswa.html"
    form_class = MahasiswaForm
    success_url = reverse_lazy('portal')

class MahasiswaDeleteView(DeleteView):
    model = models.Mahasiswa
    template_name = "delete_confirm_mahasiswa.html"
    success_url = reverse_lazy('portal')