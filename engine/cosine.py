from engine.funtions import length, ln, proses_data_berita, proses_input_user
from database.berita import berita


# 1. Fungsi akar manual (pengganti math.sqrt)
def akar_sendiri(angka):
    if angka < 0:
        return 0
    return angka ** 0.5

# 2. Menghitung TF untuk Cosine secara manual
def tf_cosine(query):
    result = {}

    for i in query:
        if i in result: # Menambahkan 1 jika key sudah ada didalam dictionary
            result[i] += 1
        else:
            result[i] = 1 # Menambahkan key dan memberikan nilai awal 1

    return result

# 3. Menghitung DF (Document Frequency) untuk Cosine
def df_cosine():
    result = {}
    data = proses_data_berita()

    for item in data:
        kata_ditemukan = []

        for token in item['token']:
            if token not in kata_ditemukan:
                kata_ditemukan += [token]

        for kata in kata_ditemukan:
            if kata in result:
                result[kata] += 1
            else:
                result[kata] = 1

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

    tf_query = tf_cosine(query)
    tf_dokumen = tf_cosine(dokumen['token'])

    vektor_q = {}
    vektor_d = {}

    # Membentuk vektor TF-IDF query
    for i in tf_query:
        if i in idf:
            vektor_q[i] = tf_query[i] * idf[i]

    # Membentuk vektor TF-IDF seluruh kata dokumen
    for i in tf_dokumen:
        vektor_d[i] = tf_dokumen[i] * idf[i]

    # Dot product Q . D
    dot_product = 0
    for i in vektor_q:
        if i in vektor_d:
            dot_product += vektor_q[i] * vektor_d[i]

    # Magnitude
    mag_q = magnitude(vektor_q)
    mag_d = magnitude(vektor_d)

    skor = 0
    if mag_q != 0 and mag_d != 0:
        skor = dot_product / (mag_q * mag_d)

    result['id'] = dokumen['id']
    result['score'] = skor

    return result