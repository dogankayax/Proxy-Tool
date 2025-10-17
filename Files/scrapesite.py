from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from colorama import Fore, init

init(autoreset=True)
 
def scrape_site(proxy_list):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--headless=new") 

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 30)  

    try:
        driver.get("https://proxyscrape.com/online-proxy-checker")
        time.sleep(3)

        print(f"{Fore.GREEN}\n📝 Proxy listesi yükleniyor...")
        textarea = wait.until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@class='form-control flex-grow-1']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
        time.sleep(1)
        textarea.clear()
        textarea.send_keys(proxy_list)

       
        print(f"{Fore.GREEN}\n🔍 Proxy'ler kontrol ediliyor...")
        check_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space()='Check proxies']]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", check_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", check_button)

        print(f"{Fore.GREEN}\n⏳ Sonuçlar bekleniyor...")

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#table-checking tbody tr")))
        
        time.sleep(10)
        
        wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "#table-checking tbody tr")) > 0)
        
        time.sleep(5)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find("table", {"id": "table-checking"})
        results = []

        if table:
            tbody = table.find("tbody")
            rows = tbody.find_all("tr")
            print(f"{Fore.GREEN}\n📋 Bulunan satır sayısı: {len(rows)}")
            
            for row in rows:
                cols = row.find_all("td")
                data = [c.get_text(strip=True) for c in cols]
                results.append(data)

                print(f"{Fore.YELLOW}Satır verisi: {data}")

        print("\n" + "="*50)
        print(f"{Fore.MAGENTA}📊 PROXY KONTROL SONUÇLARI:")
        print("="*50)
        
        if results:
            for r in results:
                try:
                    if len(r) >= 6:  
                        ip = r[1] if len(r) > 1 else "N/A"
                        port = r[2] if len(r) > 2 else "N/A"
                        country = r[3] if len(r) > 3 else "N/A"
                        status = r[5] if len(r) > 5 else "N/A"
                        print(f"{Fore.GREEN}IP: {ip} | Port: {port} | Country: {country} | Status: {status}")
                    else:
                        print(f"{Fore.RED}Eksik veri: {r}")
                except Exception as e:
                    print(f"{Fore.RED}Hatalı satır: {r} - Hata: {e}")
        else:
            print(f"{Fore.RED}❌ Hiç sonuç bulunamadı!")

        return results

    except Exception as e:
        print(f"{Fore.RED}❌ Hata oldu: {e}")
        import traceback
        traceback.print_exc()
        return []

    finally:
        driver.quit()

    