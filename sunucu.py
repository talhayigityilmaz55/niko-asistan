from flask import Flask, request, jsonify

app = Flask(__name__)

# Ana sayfa (Tarayıcıdan girdiğinde 404 hatası almamak için)
@app.route('/')
def home():
    return "Niko AI Sistemi Aktif ve Calisiyor!"

# Uygulamanın soru soracağı kapı (API)
@app.route('/sor', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        soru = data.get("soru", "").lower()
        
        # Basit Cevap Mantığı
        if "merhaba" in soru:
            cevap = "Merhaba efendim, ben Niko. Sizi dinliyorum."
        elif "ara" in soru:
            cevap = "Hemen arama komutunu hazırlıyorum."
        else:
            cevap = "Mesajınızı aldım, sizin için araştırıyorum."
            
        return jsonify({"cevap": cevap})
    except Exception as e:
        return jsonify({"hata": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
