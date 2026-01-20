from flask import Flask, request
import requests
import urllib.parse
import datetime
import os

app = Flask(__name__)

# Niko'nun Karakter Tanımı
karakter = "Sen Niko'sun. Yiğit'in akıllı ve samimi asistanısın. Kısa ve öz cevaplar ver."
bellek = ""

@app.route('/')
def home():
    return "Niko Sunucusu Aktif! Yiğit, her şey yolunda."

@app.route('/sohbet', methods=['GET'])
def sohbet():
    global bellek
    soru = request.args.get('soru')
    if not soru: 
        return "Soru gelmedi Yiğit."

    simdi = datetime.datetime.now()
    tarih_bilgisi = f"[Sistem Zamanı: {simdi.strftime('%H:%M')}]"

    try:
        # Yapay zekaya (AI) gönderilecek format
        tam_mesaj = f"{karakter}\n{tarih_bilgisi}\nHafıza: {bellek}\nYiğit: {soru}"
        url = f"https://text.pollinations.ai/{urllib.parse.quote(tam_mesaj)}?model=openai"
        
        response = requests.get(url, timeout=20)
        
        if response.status_code == 200:
            cevap = response.text.strip()
            # Kısa süreli hafıza güncelleme
            bellek = f"{soru} -> {cevap}"
            return cevap
        else:
            return "Şu an cevap veremiyorum, AI servisinde bir yoğunluk olabilir."
    except Exception as e:
        return f"Bağlantı hatası: {str(e)}"

# Render için kritik Port ayarı
if __name__ == '__main__':
    # Render PORT'u otomatik verir, biz de onu yakalıyoruz
    port = int(os.environ.get("PORT", 10000))
    # host='0.0.0.0' dış dünyadan erişim için zorunludur
    app.run(host='0.0.0.0', port=port)
