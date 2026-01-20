from flask import Flask, request
import requests
import urllib.parse
import datetime
import os

app = Flask(__name__)

# Niko'nun Karakteri: Kibar, akıllı ve samimi
karakter = "Sen Niko'sun. Yiğit'in akıllı asistanısın. Kesinlikle kaba konuşma. Saygılı ve kısa cevaplar ver."
bellek = ""

@app.route('/sohbet', methods=['GET'])
def sohbet():
    global bellek
    soru = request.args.get('soru')
    if not soru: 
        return "Soru gelmedi kanka."

    simdi = datetime.datetime.now()
    tarih_bilgisi = f"[SİSTEM: Saat {simdi.strftime('%H:%M')}]"

    try:
        # Yapay zekaya gönderilecek tam metin
        tam_mesaj = f"{karakter}\n{tarih_bilgisi}\nHafıza: {bellek}\nYiğit: {soru}"
        url = f"https://text.pollinations.ai/{urllib.parse.quote(tam_mesaj)}?model=openai"
        
        response = requests.get(url, timeout=20)
        
        if response.status_code == 200:
            cevap = response.text.strip()
            # Hafızayı güncelle (Bir sonraki mesajda hatırlaması için)
            bellek = f"{soru} -> {cevap}"
            return cevap
        else:
            return "Şu an cevap veremiyorum Yiğit, tekrar dener misin?"
    except Exception as e:
        return f"Bağlantı hatası oluştu: {str(e)}"

# KRİTİK BÖLÜM: Bulut sunucu (Render) ayarı
if __name__ == '__main__':
    # Render gibi servisler portu 'PORT' çevresel değişkeninden alır
    port = int(os.environ.get("PORT", 5000))
    # '0.0.0.0' sayesinde internetten gelen isteklere açılır
    app.run(host='0.0.0.0', port=port)