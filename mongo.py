from pymongo import MongoClient

# MongoDB'ye bağlan
client = MongoClient('mongodb://localhost:27017/')

# Kullanılacak veritabanını seç
db = client['Hemşireler']

# Kullanılacak koleksiyonu seç
collection = db['hemsire_id']

# Eklenecek veriyi oluştur
nurse_data = {
    "nurse_id": "12345678",
    "password": "muhammedsumbul"
}

# Veriyi koleksiyona ekle
result = collection.insert_one(nurse_data)

# Eklenen verinin ObjectId'sini alabilirsiniz
print(f"Veri eklendi. ObjectId: {result.inserted_id}")

# Bağlantıyı kapat
client.close()
