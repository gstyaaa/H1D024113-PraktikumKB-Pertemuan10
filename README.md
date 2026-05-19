# Algoritma Genetika - Knapsack Problem (Pertemuan 10)

Repositori ini berisi implementasi sederhana **Algoritma Genetika (Genetic Algorithm)** untuk menyelesaikan **Knapsack Problem**. Program ini ditulis dalam bahasa Python dan dirancang untuk mencari kombinasi barang yang memberikan keuntungan maksimal tanpa melebihi kapasitas beban tertentu.

## Deskripsi Masalah

Terdapat sejumlah barang yang masing-masing memiliki nilai keuntungan (profit) dan ukuran (berat/volume). Tujuannya adalah memilih kombinasi barang yang akan dimasukkan ke dalam wadah (knapsack) dengan batasan kapasitas maksimal agar total keuntungan yang didapat adalah yang tertinggi.

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

Dalam script `algen.py`, parameter yang digunakan adalah:
- **Jumlah Populasi:** 20 individu per generasi.
- **Jumlah Generasi:** 50 iterasi.
- **Representasi Genetik:** Biner (0 = tidak diambil, 1 = diambil).

## Struktur Kode

1.  **`fitness(kromosom)`**: Menghitung total keuntungan. Jika total ukuran melebihi kapasitas, nilai fitness menjadi 0.
2.  **`inisialisasi_populasi()`**: Membuat populasi awal secara acak.
3.  **`selection(populasi, fitnesses)`**: Memilih induk menggunakan metode *Roulette Wheel Selection*.
4.  **`crossover(parent1, parent2)`**: Melakukan persilangan satu titik (*single-point crossover*) untuk menghasilkan keturunan.
5.  **`mutation(kromosom)`**: Melakukan mutasi gen (bit-flip) secara acak untuk menjaga variasi genetik.

## Cara Menjalankan

### Prasyarat
- Pastikan Anda sudah menginstal Python (versi 3.x direkomendasikan).

### Langkah-langkah
1.  Buka terminal atau command prompt.
2.  Arahkan ke direktori proyek ini.
3.  Jalankan perintah berikut:
    ```bash
    python algen.py
    ```

## Contoh Output
Setelah dijalankan, program akan menampilkan:
- Kromosom terbaik (kombinasi biner).
- Keuntungan maksimum yang diperoleh.
- Daftar barang yang terpilih beserta detail keuntungan dan ukurannya.
- Total ukuran dari barang-barang yang terpilih.

---
*Dibuat untuk keperluan praktikum Kecerdasan Buatan (KB) - Pertemuan 10.*
