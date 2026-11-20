import os
from database.berita import berita
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

    lebar = 50

    print("\033[96m")
    print("╔" + "═" * (lebar - 2) + "╗")
    print("║" + "TheSee".center(lebar - 2) + "║")
    print("║" + "INDONESIAN DISASTER NEWS SEARCH".center(lebar - 2) + "║")
    print("╚" + "═" * (lebar - 2) + "╝")

    print("© ubay x lyra".center(lebar))
    print()
    print("Jangan cari yang gak ada".center(lebar))
    print()


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

# pengurutan berita
def bubble_sort(lst):
    data = lst
    l = length(data)

    for i in range(l-1):
        ok = True
        for j in range(l-1-i):
            if data[j]['score'] < data[j + 1]['score']:
                data[j], data[j + 1] = data[j + 1], data[j]
                ok = False
        if ok:
            break 
    return data

# menampilkan hasil ke layar
def result_bm25(lst):
    no_hasil = 0
    for i in range(3):
        index = lst[i]['id']
        if lst[i]['score'] > 0:
            print(f"id: {berita[index - 1]['id']}")
            print(f"Judul: {berita[index - 1]['judul']}")
            print(f"Tanggal: {berita[index - 1]['tanggal']}")
            print(f"Link: {berita[index - 1]['url']}")
            print(f"Score: {lst[i]['score']}")
            print()
            print()
        else:
            no_hasil += 1

    if no_hasil == 3:
        print(f"{'Tidak Ada Hasil':^40}")
        print()
        print()