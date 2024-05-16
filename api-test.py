import requests

# API URL'sini ve API anahtarını tanımlayın
api_url = "https://www.maxmerter.com/"
api_key = ""

# API'ye gönderilecek verileri oluşturun
data = {
    "apiKey": api_key
}

try:
    # POST isteği gönderin
    response = requests.post(api_url, json=data)
    
    # İstek başarılıysa yanıtı alın
    if response.status_code == 200:
        # JSON yanıtını alın
        api_response = response.json()
        
        # API yanıtını işleyin
        if api_response["error"] == 0:
            # API token'ı alın
            api_token = api_response["wk_token"]
            print("API'ye başarıyla bağlandı. API token:", api_token)
        else:
            print("API bağlantı hatası:", api_response["errorMessage"])
    else:
        print("API'ye bağlanırken hata oluştu. HTTP kodu:", response.status_code)

except Exception as e:
    print("Bir hata oluştu:", str(e))