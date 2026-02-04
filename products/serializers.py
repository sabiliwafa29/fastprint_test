from rest_framework import serializers
from .models import Kategori, Status, Produk


class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id_kategori', 'nama_kategori']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id_status', 'nama_status']


class ProdukSerializer(serializers.ModelSerializer):
    kategori_nama = serializers.CharField(source='kategori.nama_kategori', read_only=True)
    status_nama = serializers.CharField(source='status.nama_status', read_only=True)

    class Meta:
        model = Produk
        fields = [
            'id_produk',
            'nama_produk',
            'harga',
            'kategori',
            'kategori_nama',
            'status',
            'status_nama'
        ]

    def validate_nama_produk(self, value):
        """Validasi: Nama produk harus diisi"""
        if not value or value.strip() == '':
            raise serializers.ValidationError("Nama produk harus diisi dan tidak boleh kosong")
        return value.strip()

    def validate_harga(self, value):
        """Validasi: Harga harus berupa angka positif"""
        if value is None:
            raise serializers.ValidationError("Harga harus diisi")
        if value < 0:
            raise serializers.ValidationError("Harga harus berupa angka positif")
        return value
