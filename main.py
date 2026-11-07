from preprocessing import case_folding
from engine.tf_idf import calculate_frequency, calculate_document_frequency, calculate_idf, calculate_tfidf
from database.berita import berita

# Meminta user apa yang akan dicari
cari = input("Ask Google Buatan Kita😁: ")

# mengubah inputan user menjadi huruf kecil
query = case_folding(cari)

# mengubah teks berita menjadi huruf kecil
for i in range(50):
    print(f"Judul ke-{i + 1}: {case_folding(berita[i]["judul"])}")
    print(f"Isi ke-{i + 1}: {case_folding(berita[i]["isi"])}")
    print()


