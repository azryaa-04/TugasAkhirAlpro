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
    hasil = {}

    for i in query:
        hasil[i] = 0 # Menambahkan key kedalam dictionary dengan value awal 0
        for k in dokumen:
            if i in k: # Lalu menambahkan 1 ke value jika key nya ada di berita
                hasil[i] += 1

    return hasil

# menghitung logaritma natural basis (e) dengan metode deret Taylor 
def ln(x):
    z = (x - 1) / (x + 1)
    result = z
    
    for i in range(3,153):
        if i % 2 == 1:
            result += (z**i) / i

    result *= 2
    return result

# menghitung seberapa unik dan penting suatu kata
def calculate_idf(dokumen):
    result = {}
    for i in dokumen:
        idf = str(ln(50/dokumen[i])) # mengkonversi hasil fungsi ln() ke string
        result[i] = float(idf[:5]) # mengambil hanya 3 angka dibelakang koma dan jadikan float lagi
        
    return result

# Menghitung bobot kata
def calculate_tfidf(tf, idf):
    result = {}

    for i in tf:
        result[i] = tf[i] * idf[i] # Menghitung hasil dari calculate_tf dan calculate_idf

    return result