from django import forms
from portalmahasiswa import models

class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = models.Mahasiswa
        fields = ('__all__')