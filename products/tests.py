from django.test import TestCase, Client
from django.urls import reverse
from .models import Kategori, Status, Produk
from decimal import Decimal


class KategoriModelTest(TestCase):
    def setUp(self):
        self.kategori = Kategori.objects.create(nama_kategori="Test Kategori")

    def test_kategori_creation(self):
        self.assertEqual(self.kategori.nama_kategori, "Test Kategori")
        self.assertEqual(str(self.kategori), "Test Kategori")


class StatusModelTest(TestCase):
    def setUp(self):
        self.status = Status.objects.create(nama_status="bisa dijual")

    def test_status_creation(self):
        self.assertEqual(self.status.nama_status, "bisa dijual")
        self.assertEqual(str(self.status), "bisa dijual")


class ProdukModelTest(TestCase):
    def setUp(self):
        self.kategori = Kategori.objects.create(nama_kategori="Test Kategori")
        self.status = Status.objects.create(nama_status="bisa dijual")
        self.produk = Produk.objects.create(
            nama_produk="Test Produk",
            harga=Decimal("10000.00"),
            kategori=self.kategori,
            status=self.status
        )

    def test_produk_creation(self):
        self.assertEqual(self.produk.nama_produk, "Test Produk")
        self.assertEqual(self.produk.harga, Decimal("10000.00"))
        self.assertEqual(self.produk.kategori, self.kategori)
        self.assertEqual(self.produk.status, self.status)


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.kategori = Kategori.objects.create(nama_kategori="Test Kategori")
        self.status_bisa = Status.objects.create(nama_status="bisa dijual")
        self.status_tidak = Status.objects.create(nama_status="tidak bisa dijual")
        
        self.produk1 = Produk.objects.create(
            nama_produk="Produk 1",
            harga=Decimal("10000.00"),
            kategori=self.kategori,
            status=self.status_bisa
        )
        
        self.produk2 = Produk.objects.create(
            nama_produk="Produk 2",
            harga=Decimal("20000.00"),
            kategori=self.kategori,
            status=self.status_tidak
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Produk 1")
        self.assertContains(response, "Produk 2")

    def test_produk_bisa_dijual_view(self):
        response = self.client.get(reverse('produk_bisa_dijual'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Produk 1")
        self.assertNotContains(response, "Produk 2")

    def test_tambah_produk_view_get(self):
        response = self.client.get(reverse('tambah_produk'))
        self.assertEqual(response.status_code, 200)

    def test_tambah_produk_view_post(self):
        data = {
            'nama_produk': 'Produk Baru',
            'harga': '15000',
            'kategori': self.kategori.id_kategori,
            'status': self.status_bisa.id_status,
        }
        response = self.client.post(reverse('tambah_produk'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Produk.objects.filter(nama_produk='Produk Baru').exists())
