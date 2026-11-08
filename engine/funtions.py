from database.berita import berita


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

def all_berita(dokumen):
    lst = []
    for i in range(length(berita)):
        lst += [i]["judul"]
        lst += berita[i]["isi"]

    return lst