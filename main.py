import os
from engine.funtions import all_berita, length
from preprocessing import case_folding, terlarang
from engine.tf_idf import calculate_frequency, calculate_document_frequency, calculate_idf, calculate_tfidf
from database.berita import berita

def header():
    os.system("cls")
    print(f"{'Search Engine Techseek':^40}")
    print(f"{'-'*40:^40}")

def preprocessing(query):
    huruf_kecil = case_folding(query)
    karakter_terlarang = terlarang(huruf_kecil)
    token = karakter_terlarang.split()

    return token

def proses_input_user():
    search = input("Ask Google Buatan Kami😁😁 \n")
    return preprocessing(search)

def corpus():
   
    for i in range(length(berita)):
        return preprocessing(berita[i]['judul'])

    


header()
print(all_berita())
# query = proses_input_user()
# tf_query = calculate_frequency(query)
# print(tf_query)
# print()
# for i in range(length(berita)):
#     proses = preprocessing(berita[i]['judul'])
#     tf = calculate_frequency(proses)
#     df = calculate_document_frequency(query, tf)
#     idf = calculate_idf(df)
#     print(tf)
#     print(df)
#     print(idf)
#     print()

