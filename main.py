from engine.funtions import header, length, proses_input_user, proses_data_berita
from engine.tf_idf import calculate_frequency, calculate_document_frequency, calculate_idf, calculate_tfidf
from engine.bm25 import avgdl, idf_bm25, scoreBM25, tf_bm25
from database.berita import test, berita
from engine.preprocessing import case_folding


while True:
    header()
    query = proses_input_user()
    data = proses_data_berita()

    # bm25
    df = calculate_document_frequency(query, data)
    for i in range(length(berita)):
        print(scoreBM25(query, data[i], df))

    print('Apakah ada yang mau ditanyakan lagi?')
    print("ketik 'Keluar' untuk berhenti")
    kondisi = input()
    if case_folding(kondisi) == 'keluar':
        break









# hasil = calculate_tfidf(tf, idf)
# for kata in hasil:
#     print(f"\nKata: {kata}")

#     if hasil[kata]:
#         for dokumen in hasil[kata]:
#             print(f"  {dokumen}: {hasil[kata][dokumen]}")
#     else:
#         print("  Tidak ditemukan")
