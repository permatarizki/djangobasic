from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    nama_mahasiswa = models.CharField(max_length=80)
    nomor_siswa = models.CharField(max_length=20)
    alamat = models.TextField()

    def __str__(self):
        return self.nama_mahasiswa
