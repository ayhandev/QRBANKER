import requests
import time

def send_payment(data, bank_url):
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(bank_url, json=data, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке данных: {e}")
        return None

def send_with_retry(data, bank_urls, retries=3, delay=5):
    for attempt in range(retries):
        for bank_url in bank_urls:
            print(f"Попытка {attempt + 1}: отправляем в {bank_url}")
            result = send_payment(data, bank_url)
            if result is not None:
                print(f"Ответ от {bank_url}: {result}")
                return result
        print(f"Попытка {attempt + 1} не удалась. Повтор через {delay} секунд...")
        time.sleep(delay)
    print("Все попытки не удались.")
    return None