import os
from database.berita import berita, test
from engine.preprocessing import case_folding, terlarang, stopwords, tokenisasi


# menghitung logaritma natural basis (e) dengan metode deret Taylor 
def ln(x):
    z = (x - 1) / (x + 1)
    result = z
    
    for i in range(3,153):
        if i % 2 == 1:
            result += (z**i) / i

    result *= 2
    return result

# Menghitung panjang
def length(x):
    result = 0

    for i in x:
        result += 1

    return result

# tahap praproses
def preprocessing(query):
    huruf_kecil = case_folding(query)
    karakter_terlarang = terlarang(huruf_kecil)
    kata_stopword = stopwords(karakter_terlarang)
    token = tokenisasi(kata_stopword)

    return token

# header program utama
def header():
    os.system("cls")
    print(f"{'Search Engine Techseek':^40}")
    print(f"{'-'*40:^40}")

# proses inputan user
def proses_input_user():
    search = input("Ask Google Buatan Kami😁😁 \n")
    return preprocessing(search)

# proses pengolahan berita
def proses_data_berita():
    lst = []
    for i in berita:
        data = {
            'id': i['id'],
            'token': preprocessing(i['isi'])
        }
        lst += [data]
    
    return lst