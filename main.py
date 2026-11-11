import os
from engine.funtions import all_berita, length
from engine.preprocessing import case_folding, terlarang, stopwords, tokenisasi
from engine.tf_idf import calculate_frequency, calculate_document_frequency, calculate_idf, calculate_tfidf
from database.berita import berita

def header():
    os.system("cls")
    print(f"{'Search Engine Techseek':^40}")
    print(f"{'-'*40:^40}")

def preprocessing(query):
    huruf_kecil = case_folding(query)
    karakter_terlarang = terlarang(huruf_kecil)
    kata_stopword = stopwords(karakter_terlarang)
    token = tokenisasi(kata_stopword)

    return token

def proses_input_user():
    search = input("Ask Google Buatan Kami😁😁 \n")
    return preprocessing(search)


    


header()
query = proses_input_user()
print(calculate_frequency(query))


for i in range(length(berita)):
    data = preprocessing(berita[i]['judul'])
    print(calculate_frequency(data))
