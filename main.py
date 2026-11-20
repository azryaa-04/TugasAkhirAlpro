from engine.cosine import df_cosine, idf_cosine, score_cosine
from engine.funtions import  bubble_sort, header, length, proses_input_user, proses_data_berita, result_bm25
from engine.bm25 import df_bm25, scoreBM25
from database.berita import berita
from engine.preprocessing import case_folding



while True:
    # tampilan awal
    header()

    # inputan user
    query = proses_input_user()
    print()

    # proses data berita
    data = proses_data_berita()

# =================================================================================

    # cosine similarity
    
    print("\n" + "="*40)
    print("       HASIL SKORING COSINE SIMILARITY")
    print("="*40)

    # proses mencari relevansi berita
    df = df_cosine()
    idf = idf_cosine(df)
    hasil_cosine = []
    for i in range(length(berita)):
        hasil_cosine += [score_cosine(query, data[i], idf)]

    # mengurutkan hasil
    rangking = bubble_sort(hasil_cosine)
    
    # menampilkan hasil
    result_bm25(rangking)

# =================================================================================

    # bm25
    print("\n" + "="*40)
    print("          HASIL SKORING BM25")
    print("="*40)

    # proses mencari relevansi berita
    df = df_bm25(query, data)
    lst = []
    for i in range(length(berita)):
        lst += [scoreBM25(query, data[i], df)]
    
    # mengurutkan hasil
    rangking = bubble_sort(lst)

    # menampilkan hasil
    result_bm25(rangking)

# =================================================================================

    # kondisi lanjut or no
    print('Apakah ada yang mau ditanyakan lagi?')
    print("Lanjut cari lagi kah bang? (y/n)")
    kondisi = input()
    if case_folding(kondisi) == 'n':
        break