from engine.funtions import length, ln, proses_data_berita
from database.berita import berita, berita

# 1. Fungsi akar manual (pengganti math.sqrt)
def akar_sendiri(angka):
    if angka < 0:
        return 0
    return angka ** 0.5

# 2. Menghitung TF untuk Cosine secara manual
def tf_cosine(query, dokumen):
    result = {}
    for i in query:
        result[i] = 0
        for k in dokumen:
            if i == k:
                result[i] += 1
    return result

# 3. Menghitung DF (Document Frequency) untuk Cosine
def df_cosine(query):
    result = {}
    data = proses_data_berita()
    for i in query:
        result[i] = 0
        for item in data:
            ada = 0
            for token in item['token']:
                if token == i:
                    ada = 1
                    break
            if ada == 1:
                result[i] += 1
    return result

# 4. Menghitung IDF Cosine
def idf_cosine(df):
    result = {}
    n = length(berita)
    for i in df:
        if df[i] == 0:
            result[i] = 0
        else:
            result[i] = ln(n / df[i])
    return result

# 5. Menghitung Magnitude dari sebuah vektor
def magnitude(vektor):
    jumlah = 0
    for i in vektor:
        jumlah += vektor[i] ** 2
    return akar_sendiri(jumlah)

# 6. Menghitung Skor Cosine per Dokumen
def score_cosine(query, dokumen, idf):
    result = {}
    tf = tf_cosine(query, dokumen['token'])
    
    vektor_q = {}
    vektor_d = {}
    
    for i in query:
        tf_q_val = 0
        for q_item in query:
            if q_item == i:
                tf_q_val += 1
        
        vektor_q[i] = tf_q_val * idf[i]
        vektor_d[i] = tf[i] * idf[i]
        
    dot_product = 0
    for i in query:
        dot_product += vektor_q[i] * vektor_d[i]
        
    mag_q = magnitude(vektor_q)
    mag_d = magnitude(vektor_d)
    
    skor = 0
    if mag_q != 0 and mag_d != 0:
        skor = dot_product / (mag_q * mag_d)
        
    # Ambil ID dokumen secara aman
    dok_id = dokumen['id']
    result[dok_id] = skor
    return result

# 7. Fungsi utama pencetakan skor Cosine
def print_skor_cosine(query):
    data = proses_data_berita()
    df = df_cosine(query)
    idf = idf_cosine(df)
    
    list_skor_cosine = []
    
    for i in range(length(berita)):
        item_berita = berita[i]
        item_proses = data[i]
        
        hasil_skor = score_cosine(query, item_proses, idf)
        dok_id = item_proses['id']
        skor = hasil_skor[dok_id]
        
        tanggal_berita = "-"
        if 'tanggal' in item_berita:
            tanggal_berita = item_berita['tanggal']
            
        url_berita = "-"
        if 'url' in item_berita:
            url_berita = item_berita['url']

        list_skor_cosine.append({
            'judul': item_berita['judul'],
            'url': url_berita,
            'tanggal': tanggal_berita,
            'skor': skor
        })

    # Bubble Sort manual dari tinggi ke rendah
    for x in range(length(list_skor_cosine)):
        for y in range(x + 1, length(list_skor_cosine)):
            if list_skor_cosine[x]['skor'] < list_skor_cosine[y]['skor']:
                temp = list_skor_cosine[x]
                list_skor_cosine[x] = list_skor_cosine[y]
                list_skor_cosine[y] = temp

    batas_tampil = 5
    if length(list_skor_cosine) < 5:
        batas_tampil = length(list_skor_cosine)

    # Cetak hasil 5 teratas
    for i in range(batas_tampil):
        item = list_skor_cosine[i]
        print(f"\n{item['judul']}")
        print(f"{item['tanggal']}")
        print(f"{item['url']}")
        print(f"Score Cosine: {item['skor']}")