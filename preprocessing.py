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