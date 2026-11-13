from engine.funtions import length, ln, proses_data_berita
from database.berita import test, berita


def avgdl():
    result = []
    data = proses_data_berita()
        
    for l in range(length(data)):
        panjang = length(data[l]['token'])
        result += [panjang]

    jumlah = 0
    p = length(result)

    for i in result:
        jumlah += i

    return jumlah / p

def tf_bm25(query, dokumen):
    result = {}

    for i in query:
        result[i] = 0 # Menambahkan key kedalam dictionary dengan value awal 0
        for k in dokumen:
            if i in k: # Lalu menambahkan 1 ke value jika key nya ada di berita
                result[i] += 1

    return result


def idf_bm25(df):
    result = {}

    for i in df:
        result[i] = ln(1 + ((length(berita) - df[i] + 0.5) / (df[i] + 0.5)))

    return result

def scoreBM25(query, dokumen, df):
    result = {}

    k1 = 1.2
    b = 0.75
    K = k1 * ( 1 - b + b *  length(dokumen['token']) / avgdl() )
    tf = tf_bm25(query, dokumen['token'])
    idf = idf_bm25(df)

    score = 0
    for i in idf:
        score += idf[i] * ( tf[i] * (k1 + 1) ) / ( tf[i] + K )
    result[dokumen['id']] = score

    return result