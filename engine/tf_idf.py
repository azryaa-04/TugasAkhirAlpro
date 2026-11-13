from database.berita import berita, test
from engine.funtions import ln, length, preprocessing
import math


# menghitung kemunculan kata disebuah dokumen / tf
def calculate_frequency(query):
    result = {}

    for i in query:
        if i in result: # Menambahkan 1 jika key sudah ada didalam dictionary
            result[i] += 1
        else:
            result[i] = 1 # Menambahkan key dan memberikan nilai awal 1

    return result

# menghitung dokumen yang mengandung suatu kata / df
def calculate_document_frequency(query, dokumen):
    result = {}

    for i in query:
        result[i] = 0 # Menambahkan key kedalam dictionary dengan value awal 0
        for k in dokumen:
            if i in k['token']: # Lalu menambahkan 1 ke value jika key nya ada di berita
                result[i] += 1

    return result

# menghitung seberapa unik dan penting suatu kata / idf
n = length(test) 
def calculate_idf(dokumen):
    result = {}
    
    for i in dokumen:
        result[i] = math.log10((n / dokumen[i])) # mengkonversi hasil fungsi ln() ke string
        # result[i] = math.log10(((n ) / (dokumen[i] ))) # mengkonversi hasil fungsi ln() ke string
        
    return result

# Menghitung bobot TF-IDF setiap kata pada setiap berita
def calculate_tfidf(tf, idf):
    result = {}

    for i in tf:
        result[i] = tf[i] * idf[i]

    # for kata in tf:
    #     result[kata] = {}

    #     for i in range(length(berita)):
    #         dokumen = berita[i]['judul']# + " " + berita[i]['isi']
    #         token = preprocessing(dokumen)

    #         tf_dokumen = calculate_frequency(token)

    #         if kata in tf_dokumen:
    #             result[kata][f"Berita ke-{i+1}"] = (
    #                 tf_dokumen[kata] * idf[kata]
    #                 )

    return result