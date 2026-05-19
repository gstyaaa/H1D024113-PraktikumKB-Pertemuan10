# Algoritma Genetika - Knapsack Problem (Pertemuan 10)

Repositori ini berisi implementasi **Algoritma Genetika (Genetic Algorithm)** untuk menyelesaikan **Knapsack Problem**. Program ini ditulis dalam bahasa Python untuk mencari kombinasi barang dengan keuntungan maksimal tanpa melebihi kapasitas beban yang ditentukan.

## Deskripsi Masalah

Terdapat sejumlah barang yang masing-masing memiliki nilai keuntungan (profit) dan ukuran (berat/volume). Tujuannya adalah memilih kombinasi barang yang memberikan total keuntungan tertinggi dengan batasan kapasitas maksimal gudang.

### Data Barang
| Nama Barang | Keuntungan | Ukuran |
| :--- | :---: | :---: |
| Barang1 | 10 | 5 |
| Barang2 | 40 | 4 |
| Barang3 | 30 | 6 |
| Barang4 | 50 | 3 |
| Barang5 | 35 | 7 |

**Kapasitas Maksimal:** 15

## Parameter Algoritma Genetika

- **Jumlah Populasi:** 20 individu.
- **Jumlah Generasi:** 50 iterasi.
- **Probabilitas Crossover:** 0.8.
- **Probabilitas Mutasi:** 0.1.
- **Representasi Genetik:** Biner (1 = diambil, 0 = tidak diambil).

## Struktur Kode

1.  **`hitung_fitness(kromosom)`**: Menghitung total keuntungan. Jika total ukuran melebihi kapasitas gudang, nilai fitness menjadi 0.
2.  **`inisialisasi_populasi()`**: Menghasilkan populasi awal kromosom biner secara acak.
3.  **`tournament_selection()`**: Memilih individu terbaik dari sub-grup acak sebagai induk.
4.  **`one_point_crossover()`**: Melakukan persilangan satu titik antara dua induk untuk menghasilkan keturunan.
5.  **`inversion_mutation()`**: Melakukan mutasi dengan membalik urutan segmen gen dalam kromosom.

## Cara Menjalankan

### Prasyarat
- Python 3.x

### Langkah-langkah
1.  Buka terminal/command prompt.
2.  Arahkan ke direktori proyek.
3.  Jalankan perintah:
    ```bash
    python algen.py
    ```

## Contoh Output
Program akan menampilkan:
- Kromosom terbaik yang ditemukan.
- Keuntungan maksimum.
- Daftar barang yang terpilih.
- Total ukuran beban yang masuk ke gudang.

---
*Dibuat untuk keperluan praktikum Kecerdasan Buatan (KB) - Pertemuan 10.*
