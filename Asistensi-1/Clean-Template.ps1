# Clean-Template.ps1
# Jalankan dari folder ...\asistensi-kuis-pbp\Asistensi-1
#   powershell -ExecutionPolicy Bypass -File .\Clean-Template.ps1
# Fungsi: timpa 6 file soal dengan versi template (sisa TODO), cek sisa jawaban, buat TODO-INDEX.md.
$ErrorActionPreference = 'Stop'
if (-not (Test-Path .\soal1\main\models.py)) { throw 'Salah folder. cd ke ...\Asistensi-1 dulu.' }
$utf8 = New-Object System.Text.UTF8Encoding($false)
$root = (Get-Location).Path

function Write-Tpl([string]$rel, [string]$text) {
    $p = Join-Path $root $rel
    $t = ($text -replace "`r`n", "`n").TrimEnd() + "`n"
    [System.IO.File]::WriteAllText($p, $t, $utf8)
    Write-Host ("cleaned  " + $rel)
}
Write-Tpl 'soal1\main\models.py' @'
from django.db import models


class Book(models.Model):
    """Lengkapi model ini sesuai kontrak pada readme.txt."""

    # TODO 1: definisikan field title, author, dan stock.

    def __str__(self):
        # TODO 2: kembalikan judul buku.
        pass

    @property
    def is_available(self):
        # TODO 3: buku tersedia hanya jika stock lebih besar dari nol.
        pass

    @property
    def is_low_stock(self):
        # BONUS: True hanya jika stok berada pada rentang 1 sampai 3.
        pass
'@
Write-Tpl 'soal2\main\views.py' @'
from django.shortcuts import render

from main.models import Book


def book_list(request):
    # TODO 2: ambil seluruh Book dan kirimkan ke template dengan key "books".
    pass
'@
Write-Tpl 'soal2\main\urls.py' @'
from django.urls import path

from main.views import book_list

app_name = "main"

urlpatterns = [
    # TODO 3: petakan path "books/" ke book_list dengan nama "book_list".
]
'@
Write-Tpl 'soal2\quiz_mvt\urls.py' @'
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # TODO 1: teruskan seluruh URL proyek ke main.urls.
]
'@
Write-Tpl 'soal2\templates\main\book_list.html' @'
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Katalog Pojok Baca</title>
</head>
<body>
    <h1>Katalog Pojok Baca</h1>

    <!-- TODO 4:
         - Ulangi setiap objek dalam books.
         - Tampilkan title dan author.
         - Tampilkan "Tersedia" jika is_available bernilai True.
         - Tampilkan "Stok habis" jika is_available bernilai False.
         - Jika books kosong, tampilkan persis: Belum ada buku.
    -->
</body>
</html>
'@
Write-Tpl 'soal3\main\tests.py' @'
from django.test import TestCase
from django.urls import reverse
from unittest import skip

from main.models import Book


class BookCatalogTest(TestCase):
    def setUp(self):
        # TODO 1: buat satu buku berjudul "Django Dasar", penulis "Alya", stok 2,
        # lalu simpan objeknya pada self.book.
        pass

    def test_book_availability(self):
        # TODO 2: pastikan buku pada setUp tersedia.
        pass

    def test_book_list_uses_correct_template(self):
        # TODO 3: request named route main:book_list, lalu periksa status 200
        # dan template main/book_list.html.
        pass

    def test_book_data_appears_on_page(self):
        # TODO 4: pastikan judul, penulis, dan teks "Tersedia" muncul di response.
        pass

    def test_empty_book_list(self):
        # TODO 5: hapus semua Book, request halaman katalog, lalu pastikan teks
        # "Belum ada buku." muncul dan "Django Dasar" tidak muncul.
        pass

    @skip("BONUS: hapus decorator ini setelah mengerjakan test.")
    def test_stock_change_updates_availability(self):
        # BONUS: hapus decorator @skip, ubah stock self.book menjadi 0, simpan,
        # lalu pastikan is_available False dan halaman menampilkan "Stok habis".
        pass
'@

# ---- cek sisa jawaban di 6 file (harus kosong)
$files = @('soal1\main\models.py','soal2\main\views.py','soal2\main\urls.py','soal2\quiz_mvt\urls.py','soal2\templates\main\book_list.html','soal3\main\tests.py')
$leak = Select-String -Path $files -Pattern 'CharField|PositiveIntegerField|objects\.all|objects\.create|path\("books|include\("main|assertContains|assertTemplateUsed|assertTrue|\{% for|return self\.' 
Write-Host ''
if ($leak) { Write-Host 'SISA JAWABAN:' -ForegroundColor Red; $leak | ForEach-Object { '{0}:{1}: {2}' -f $_.Path, $_.LineNumber, $_.Line.Trim() } }
else { Write-Host 'LEAK CHECK: bersih, tidak ada sisa jawaban.' -ForegroundColor Green }

# ---- TODO-INDEX.md (AI baca ini, lalu fetch HANYA file yang dibutuhkan)
$hits = Select-String -Path (git ls-files '*.py','*.html','*.js') -Pattern 'TODO|BONUS'
$lines = @('# TODO-INDEX (auto-generated, jangan edit tangan)', '# format: path:line: teks. Regenerate: jalankan Clean-Template.ps1 atau perintah di StudyPlan 0B.', '')
foreach ($m in $hits) {
    $rel = (Resolve-Path -LiteralPath $m.Path -Relative).Substring(2).Replace('\','/')
    $lines += ('{0}:{1}: {2}' -f $rel, $m.LineNumber, $m.Line.Trim())
}
[System.IO.File]::WriteAllLines((Join-Path $root 'TODO-INDEX.md'), [string[]]$lines, $utf8)
Write-Host ''
Write-Host 'TODO-INDEX.md:'
$lines | ForEach-Object { $_ }
Write-Host ''
Write-Host ('Total TODO/BONUS: ' + @($hits).Count)
