from django import forms
from .models import Produk, Kategori, Status


class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']
        widgets = {
            'nama_produk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama produk',
                'required': True
            }),
            'harga': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan harga',
                'min': '0',
                'step': '0.01',
                'required': True
            }),
            'kategori': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
        }
        labels = {
            'nama_produk': 'Nama Produk',
            'harga': 'Harga',
            'kategori': 'Kategori',
            'status': 'Status',
        }

    def clean_nama_produk(self):
        """Validasi: Nama produk harus diisi"""
        nama = self.cleaned_data.get('nama_produk')
        if not nama or nama.strip() == '':
            raise forms.ValidationError("Nama produk harus diisi dan tidak boleh kosong")
        return nama.strip()

    def clean_harga(self):
        """Validasi: Harga harus berupa angka positif"""
        harga = self.cleaned_data.get('harga')
        if harga is None:
            raise forms.ValidationError("Harga harus diisi")
        if harga < 0:
            raise forms.ValidationError("Harga harus berupa angka positif")
        return harga
