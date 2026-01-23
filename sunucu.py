import os
import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)

# BURAYA GEMINI API KEY GELECEK
genai.configure(api_key="AIzaSyBKSSNYH1AjKgfg1CzFHbRssaKF10vhVIM")
model = genai.GenerativeModel('gemini-pro')

@app.route('/sor', methods=['POST'])
def niko_cevap():
    veriler = request.json
    soru = veriler.get('soru', '').lower()
    
    # Özel Komut Kontrolü (Niko'nun fiziksel işleri anlaması için)
    komut = "yok"
    if "ara" in soru: komut = "arama_yap"
    elif "fotoğraf" in soru or "resim çek" in soru: komut = "foto_cek"
    elif "video" in soru: komut = "video_cek"
    elif "kaydet" in soru or "ses kaydı" in soru: komut = "ses_kaydi"

    # Gemini'den cevap al
    response = model.generate_content(soru)
    
    return jsonify({
        "cevap": response.text,
        "komut": komut
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

