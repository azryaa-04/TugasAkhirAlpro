# Fungsi konversi menjadi huruf kecil
def case_folding(query): 
    ALPHABET  = ('A','B','C','D','E','F','G', 'H', 'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    
    hasil = ""
   
    for i in query:
        if i in ALPHABET: # Jika hasil perulangan ada di variabel huruf besar maka:
            for k in range(26): # Perulangan untuk mengakses variabel ALPHABET menggunakan index
                if i == ALPHABET[k]: # Jika i itu sama dengan HURUF BESAR maka: 
                    hasil= hasil + alphabet[k] # ganti dengan huruf kecil lalu tambahkan ke hasil
        else:
            hasil = hasil + i # jika huruf kecil maka langsung tambahkan ke variabel hasil

    return hasil

# Fungsi menghilang karakter selain huruf
def terlarang(kalimat):
    data = [
    ".", ",", "!", "?", ";", ":", "'", '"',
    "(", ")", "[", "]", "{", "}",
    "-", "_", "/", "\\", "|",
    "@", "#", "$", "%", "^", "&",
    "*", "+", "=", "~", "`",
    "<", ">", "\n", "\t"]

    hasil = ""

    for karakter in kalimat:
        simbol_ketemu = False
        for simbol in data :
            if karakter == simbol:
                simbol_ketemu = True
                break
        if simbol_ketemu == False:
            hasil = hasil + karakter

    return hasil

# Menghilangkan kata yang kurang membantu hasil pencarian
def stopwords(kalimat):
    data = [
    "yang", "dan", "di", "ke", "dari", "ini", "itu",
    "dengan", "untuk", "pada", "dalam", "oleh", "karena",
    "sebagai", "adalah", "akan", "telah", "sudah", "belum",
    "dapat", "bisa", "juga", "atau", "tetapi", "namun",
    "agar", "hingga", "sampai", "serta", "antara",
    "setelah", "sebelum", "ketika", "saat", "jika",
    "maka", "bagi", "para", "lebih", "sangat", "hanya",
    "masih", "lagi", "pun", "tidak", "bukan", "ada",
    "jadi", "yakni", "yaitu", "tersebut", "setiap",
    "beberapa", "semua", "seluruh", "suatu", "sebuah",
    "menjadi", "terhadap", "melalui", "menurut", "sejak",
    "sejumlah", "sekitar", "termasuk", "resmi", "guna",
    "mencatat", "menyebutkan", "melaporkan"]

    kata_list = []
    tampung = ""
    
    for huruf in kalimat:
        if huruf == " ":
            if tampung != "":
                kata_list = kata_list + [tampung]
                tampung = ""
        else:
            tampung = tampung + huruf
            
    if tampung != "":
        kata_list = kata_list + [tampung]
        
    hasil_kata = []
    for kata in kata_list:
        stopword_ditemukan = False
        for stopwords in data:
            if kata == stopwords:
                stopword_ditemukan = True
                break
        if stopword_ditemukan == False:
            hasil_kata = hasil_kata + [kata]
            
    gabung = ""
    for kata in hasil_kata:
            gabung = gabung + " " + kata
            
    return gabung

def tokenisasi(kalimat):
    token = []
    sementara = ""
    
    kalimat_awal = kalimat + " "
    
    for karakter in kalimat_awal:
        if karakter != " ":
            sementara = sementara + karakter
        else:
            if sementara != "":
                token =  token +[sementara]
                sementara = "" 
                
    return token