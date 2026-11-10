import requests

url = input("Enter the URL:")
query_params = {}

while True: 
    key = input("Enter a parameter (press Enter to pass):")
    if not key:
        break    
    value = input(f"Enter the value for '{key}':")
    query_params[key] = value


try:
    response = requests.get(url, params = query_params)
    print(f"İstek Atılan Tam URL: {response.url}")
    print(f"Status Code         : {response.status_code}\n")

    if response.ok:
        data = response.json()
        print("--- Elde Edilen Sonuçlar ---")
        
        if isinstance(data, list):
            for item in data:
                for key, value in item.items():
                    print(f"{key}: {value}")
                print("-" * 30)
        else:
            for key, value in data.items():
                print(f"{key}: {value}\n")
    
    else:
        print("İstek başarısız oldu!")

except requests.exceptions.RequestException as e:
    print(f"Bağlantı/Ağ Hatası Oluştu!: {e}")