from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bisa-dijual/', views.produk_bisa_dijual, name='produk_bisa_dijual'),
    path('tambah/', views.tambah_produk, name='tambah_produk'),
    path('edit/<int:id_produk>/', views.edit_produk, name='edit_produk'),
    path('hapus/<int:id_produk>/', views.hapus_produk, name='hapus_produk'),
]
