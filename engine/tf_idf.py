from database.berita import berita
from engine.funtions import ln, length
import math
# menghitung kemunculan kata disebuah dokumen
def calculate_frequency(query):
    result = {}

    for i in query:
        if i in result: # Menambahkan 1 jika key sudah ada didalam dictionary
            result[i] += 1
        else:
            result[i] = 1 # Menambahkan key dan memberikan nilai awal 1

    return result

# menghitung dokumen yang mengandung suatu kata
def calculate_document_frequency(query, dokumen):
    result = {}

    for i in query:
        result[i] = 0 # Menambahkan key kedalam dictionary dengan value awal 0
        for k in dokumen:
            if i in k: # Lalu menambahkan 1 ke value jika key nya ada di berita
                result[i] += 1

    return result

# menghitung seberapa unik dan penting suatu kata
n = length(berita) 
def calculate_idf(dokumen):
    result = {}
    
    for i in dokumen:
        result[i] = ln(((n) / (dokumen[i]))) # mengkonversi hasil fungsi ln() ke string
        # result[i] = math.log10(((n ) / (dokumen[i] ))) # mengkonversi hasil fungsi ln() ke string
        
    return result

# Menghitung bobot kata
def calculate_tfidf(tf, idf):
    result = {}

    for i in tf:
        result[i] = tf[i] * idf[i] # Menghitung hasil dari calculate_tf dan calculate_idf

    return result