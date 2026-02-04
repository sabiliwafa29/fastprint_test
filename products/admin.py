from django.contrib import admin
from .models import Kategori, Status, Produk


@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ['id_kategori', 'nama_kategori']
    search_fields = ['nama_kategori']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id_status', 'nama_status']
    search_fields = ['nama_status']


@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ['id_produk', 'nama_produk', 'harga', 'kategori', 'status']
    list_filter = ['status', 'kategori']
    search_fields = ['nama_produk']
    list_per_page = 25
