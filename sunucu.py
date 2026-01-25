import os  # İşletim sistemi kütüphanesini ekliyoruz
import google.generativeai as genai
from flask import Flask, request, jsonify

# API anahtarını kodun içine yazmıyoruz! 
# Render panelinden tanımlayacağımız "GEMINI_API_KEY" isimli değişkeni çağırıyoruz.
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("HATA: API anahtarı bulunamadı! Lütfen Render panelinden tanımlayın.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

@app.route('/sor', methods=['POST'])
def ask_gemini():
    try:
        data = request.json
        soru = data.get("soru", "")
        response = model.generate_content(soru)
        return jsonify({"cevap": response.text})
    except Exception as e:
        return jsonify({"cevap": f"Sunucu hatası: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
