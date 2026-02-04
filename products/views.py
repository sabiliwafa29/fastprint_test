from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produk, Kategori, Status
from .forms import ProdukForm
from .serializers import ProdukSerializer


def index(request):
    """Halaman utama - Tampilkan semua produk"""
    products = Produk.objects.select_related('kategori', 'status').all()
    context = {
        'title': 'Semua Produk',
        'products': products,
        'show_all': True
    }
    return render(request, 'products/index.html', context)


def produk_bisa_dijual(request):
    """Halaman produk yang bisa dijual"""
    products = Produk.objects.select_related('kategori', 'status').filter(
        status__nama_status='bisa dijual'
    )
    context = {
        'title': 'Produk Bisa Dijual',
        'products': products,
        'show_all': False
    }
    return render(request, 'products/index.html', context)


def tambah_produk(request):
    """Tambah produk baru"""
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            # Validasi tambahan menggunakan serializer
            serializer = ProdukSerializer(data={
                'nama_produk': form.cleaned_data['nama_produk'],
                'harga': form.cleaned_data['harga'],
                'kategori': form.cleaned_data['kategori'].id_kategori,
                'status': form.cleaned_data['status'].id_status,
            })
            
            if serializer.is_valid():
                form.save()
                messages.success(request, 'Produk berhasil ditambahkan!')
                return redirect('index')
            else:
                for field, errors in serializer.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = ProdukForm()
    
    context = {
        'title': 'Tambah Produk',
        'form': form,
        'action': 'Tambah'
    }
    return render(request, 'products/form.html', context)


def edit_produk(request, id_produk):
    """Edit produk"""
    produk = get_object_or_404(Produk, id_produk=id_produk)
    
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            # Validasi tambahan menggunakan serializer
            serializer = ProdukSerializer(data={
                'nama_produk': form.cleaned_data['nama_produk'],
                'harga': form.cleaned_data['harga'],
                'kategori': form.cleaned_data['kategori'].id_kategori,
                'status': form.cleaned_data['status'].id_status,
            })
            
            if serializer.is_valid():
                form.save()
                messages.success(request, 'Produk berhasil diupdate!')
                return redirect('index')
            else:
                for field, errors in serializer.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = ProdukForm(instance=produk)
    
    context = {
        'title': 'Edit Produk',
        'form': form,
        'action': 'Edit',
        'produk': produk
    }
    return render(request, 'products/form.html', context)


def hapus_produk(request, id_produk):
    """Hapus produk"""
    produk = get_object_or_404(Produk, id_produk=id_produk)
    
    if request.method == 'POST':
        nama_produk = produk.nama_produk
        produk.delete()
        messages.success(request, f'Produk "{nama_produk}" berhasil dihapus!')
        return redirect('index')
    
    # Jika bukan POST, redirect ke index
    return redirect('index')
