from django import forms
from portalmahasiswa import models

class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = models.Mahasiswa
        fields = ('__all__')
        
    nama_mahasiswa = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    nomor_siswa = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    alamat = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
        