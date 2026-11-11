from engine.funtions import length, header, preprocessing, proses_input_user, proses_data_berita
from engine.tf_idf import calculate_frequency, calculate_document_frequency, calculate_idf, calculate_tfidf

header()
query = proses_input_user()
data = proses_data_berita()
tf = calculate_frequency(query)
df = calculate_document_frequency(query, data)
idf = calculate_idf(df)
print(calculate_tfidf(tf,idf))



