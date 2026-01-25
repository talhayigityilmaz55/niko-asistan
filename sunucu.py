import os
import google.generativeai as genai
from flask import Flask, request, jsonify

# Render panelinden eklediğin API anahtarını çeker
api_key = os.environ.get("GEMINI_API_KEY")

# Gemini Yapılandırması
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
else:
    print("HATA: GEMINI_API_KEY bulunamadı!")

app = Flask(__name__)

@app.route('/')
def home():
    return "Niko Sunucusu Aktif!"

@app.route('/sor', methods=['POST'])
def ask_gemini():
    try:
        data = request.json
        soru = data.get("soru", "")
        
        if not soru:
            return jsonify({"cevap": "Soru boş olamaz."}), 400

        # Gemini'den yanıt al
        response = model.generate_content(soru)
        return jsonify({"cevap": response.text})
    
    except Exception as e:
        return jsonify({"cevap": f"Sunucu tarafında bir hata oluştu: {str(e)}"}), 500

if __name__ == '__main__':
    # Render için port ayarı önemlidir
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
