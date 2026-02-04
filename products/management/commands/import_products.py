import requests
import hashlib
from django.core.management.base import BaseCommand
from django.conf import settings
from products.models import Kategori, Status, Produk


class Command(BaseCommand):
    help = 'Import produk dari API Fastprint'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Memulai import data dari API...'))

        # Get credentials from settings
        api_url = settings.API_URL
        username = settings.API_USERNAME
        password_plain = settings.API_PASSWORD_PLAIN

        # Hash password dengan MD5
        password_md5 = hashlib.md5(password_plain.encode()).hexdigest()
        self.stdout.write(f'MD5 Hash: {password_md5}')

        # Prepare request
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        data = {
            'username': username,
            'password': password_md5
        }

        try:
            # Request ke API
            self.stdout.write('Menghubungi API...')
            response = requests.post(api_url, headers=headers, data=data)
            
            if response.status_code != 200:
                self.stdout.write(
                    self.style.ERROR(f'Error: Status code {response.status_code}')
                )
                return

            json_data = response.json()
            
            if json_data.get('error') != 0:
                self.stdout.write(
                    self.style.ERROR(f'API Error: {json_data}')
                )
                return

            products_data = json_data.get('data', [])
            
            self.stdout.write(
                self.style.SUCCESS(f'Berhasil mendapat {len(products_data)} produk dari API')
            )

            # Process data
            kategori_count = 0
            status_count = 0
            produk_count = 0

            for item in products_data:
                # Create or get Kategori
                kategori, created = Kategori.objects.get_or_create(
                    nama_kategori=item['kategori']
                )
                if created:
                    kategori_count += 1

                # Create or get Status
                status, created = Status.objects.get_or_create(
                    nama_status=item['status']
                )
                if created:
                    status_count += 1

                # Create or update Produk
                produk, created = Produk.objects.update_or_create(
                    id_produk=int(item['id_produk']),
                    defaults={
                        'nama_produk': item['nama_produk'],
                        'harga': float(item['harga']),
                        'kategori': kategori,
                        'status': status,
                    }
                )
                if created:
                    produk_count += 1

            self.stdout.write(
                self.style.SUCCESS(
                    f'\nBerhasil import data:\n'
                    f'- Kategori baru: {kategori_count}\n'
                    f'- Status baru: {status_count}\n'
                    f'- Produk baru: {produk_count}\n'
                    f'- Total produk di database: {Produk.objects.count()}'
                )
            )

        except requests.exceptions.RequestException as e:
            self.stdout.write(
                self.style.ERROR(f'Error saat request ke API: {str(e)}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {str(e)}')
            )
