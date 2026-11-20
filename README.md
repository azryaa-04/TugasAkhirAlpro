# TheSee — Mini Search Engine

**TheSee** merupakan program Mini Search Engine berbasis Command Line Interface (CLI) yang dikembangkan menggunakan Python. Program ini dirancang untuk mencari berita bertema Indonesian disaster newa berdasarkan relevansi kata kunci yang dimasukkan pengguna.

TheSee menerapkan pengolahan teks dan perhitungan matematis secara manual sebagai bagian dari implementasi algoritma pencarian informasi.

## Fitur

- **Text Preprocessing** — Mengolah teks berita dan query pengguna agar dapat digunakan dalam proses pencarian.
- **Term Frequency (TF)** — Menghitung frekuensi kemunculan kata dalam teks.
- **Document Frequency (DF)** — Menghitung jumlah dokumen yang mengandung suatu kata.
- **Inverse Document Frequency (IDF)** — Menghitung tingkat kepentingan kata dalam keseluruhan koleksi dokumen.
- **TF-IDF** — Memberikan bobot pada kata berdasarkan frekuensi dan tingkat kepentingannya.
- **Cosine Similarity** — Mengukur tingkat kemiripan antara query pengguna dan dokumen.
- **Search Result Ranking** — Mengurutkan hasil pencarian berdasarkan skor relevansi.

## Teknologi yang Digunakan

| Teknologi | Keterangan |
|---|---|
| Python | Bahasa pemrograman utama |
| CLI | Antarmuka program berbasis terminal |


## Konfigurasi dan Persyaratan

Sebelum menjalankan TheSee, pastikan perangkat telah memenuhi persyaratan berikut:

- Python 3.x
- Git (opsional, jika melakukan cloning repository)
- Terminal atau Command Prompt
- Visual Studio Code (opsional, untuk pengembangan)

## Instalasi

### 1. Clone repository

```bash
git clone https://github.com/azryaa-04/TugasAkhirAlpro.git
```

### 2. Masuk ke direktori proyek

```bash
cd TugasAkhirAlpro
```

### 3. Pastikan Python telah terinstal

```bash
python --version
```

Jika perintah tersebut tidak tersedia, coba:

```bash
py --version
```

## Cara Menjalankan Program

Jalankan program melalui terminal dari direktori utama proyek.

```bash
python main.py
```

Jika menggunakan Windows dan perintah `python` tidak tersedia, gunakan:

```bash
py main.py
```

Setelah program dijalankan, ikuti instruksi yang ditampilkan pada terminal dan masukkan kata kunci pencarian yang ingin dicari.

## Struktur Proyek

```text
TugasAkhirAlpro/
│
├── database/
│   └── berita.py
│
├── engine/
│   │── funtions.py
│   ├── preprocessing.py
│   ├── cosine.py
│   ├── bm25.py
│
├── main.py
└── README.md
```

> Struktur di atas merupakan gambaran sederhana. Sesuaikan dengan struktur direktori terbaru proyek.

## Alur Pencarian

1. Pengguna memasukkan kata kunci pencarian.
2. Query pengguna diproses melalui tahap text preprocessing.
3. Program menghitung bobot kata menggunakan TF dan IDF.
4. Program menghitung tingkat kemiripan query terhadap dokumen.
5. Hasil pencarian disajikan berdasarkan skor relevansi.

## Tujuan Proyek

Proyek ini dikembangkan sebagai implementasi pembelajaran algoritma dan pemrograman, khususnya dalam memahami pengolahan teks, struktur data, algoritma pencarian, dan penerapan perhitungan matematis dalam Information Retrieval.

## Developer

- **Ubay**
- **Lyra**

---

*TheSee — Finding Information Through Algorithm.*
