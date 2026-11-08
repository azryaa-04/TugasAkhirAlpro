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

def terlarang(kalimat):
    data = [",",".","?","!","/","-","(", ")"]

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

def stopwords(kalimat):
    data = ["di","ke","dari","pada","bagi","oleh","daripada","kepada","dan",
          "atau","tetapi","melainkan","sedangkan","padahal","karena","jika",
          "maka","sehingga","agar","walaupun","meskipun","saya","aku","kamu",
          "anda","dia","ia","mereka","kita","kami","ini","itu","yang","pun",
          "tersebut","adalah","merupakan","yaitu","yakni","ada","berada","jadi",
          "menjadi","dapat","bisa","boleh","harus","tentu","akan","telah","sedang",
          "sudah","belum","sempat"
          ]

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
    pertama = True
    for kata in hasil_kata:
            gabung = gabung + " " + kata
            
    return gabung
