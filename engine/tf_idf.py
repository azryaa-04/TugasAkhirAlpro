# menghitung kemunculan kata disebuah dokumen
def calculate_frequency(token):
    hasil = {}

    for i in token:
        if i in hasil:
            hasil[i] += 1
        else:
            hasil[i] = 1

    return hasil

# menghitung dokumen yang mengandung suatu kata
def calculate_document_frequency(query, documents):
    hasil = {}

    for i in query:
        hasil[i] = 0
        for k in documents:
            # k boleh berupa string dokumen atau daftar token.
            # Bandingkan per token, bukan substring, agar "ai" tidak
            # ikut terhitung di "main"/"lain".
            tokens = k.split() if isinstance(k, str) else k
            if i in tokens:
                hasil[i] += 1

    return hasil

# menghitung seberapa unik dan penting suatu kata
