import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

current_dir = os.path.dirname(__file__)
files_dir = os.path.join(current_dir, 'Files')
sys.path.append(files_dir)

try:
    from Files.getproxy import getproxy
    from Files.scrapesite import scrape_site
except ImportError as e:
    print(f"{Fore.RED}Error importing modules: {e}")
    sys.exit(1)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_logo():
    logo = f"""{Fore.RED}
    ____                            ______            __
   / __ \_________  _  ____  __    /_  __/___  ____  / /
  / /_/ / ___/ __ \| |/_/ / / /_____/ / / __ \/ __ \/ / 
 / ____/ /  / /_/ />  </ /_/ /_____/ / / /_/ / /_/ / /  
/_/   /_/   \____/_/|_|\\__, /     /_/  \\____/\\____/_/   
                      /____/                            
"""
    print(logo)


def display_menu():
    menu = f"""
    1.{Fore.WHITE} Proxyleri Al 

    2.{Fore.WHITE} Sadece Proxyleri Kontrol Et
                
    3.{Fore.RED} Çıkış Yap
    """
    print(menu)


def clean_proxy_list(proxy_list):

    cleaned_proxies = []
    
    for proxy in proxy_list:
        if proxy.strip():  
            cleaned_proxy = proxy.strip()
            cleaned_proxy = cleaned_proxy.replace('http://', '').replace('https://', '')
            
            
            cleaned_proxy = cleaned_proxy.strip()
            
         
            unwanted_chars = '()[]{}"\',;'
            for char in unwanted_chars:
                cleaned_proxy = cleaned_proxy.replace(char, '')
            
            
            cleaned_proxy = cleaned_proxy.strip()
            
            if cleaned_proxy:  
                cleaned_proxies.append(cleaned_proxy)
    
    return cleaned_proxies


def load_and_clean_proxies(file_path):
   
    try:
        if not os.path.exists(file_path):
            print(f"{Fore.RED}Hata: Dosya bulunamadı - {file_path}")
            return []
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        proxies = content.splitlines()
        
        print(f"{Fore.GREEN}Yüklenen satır sayısı: {len(proxies)}")
        
        proxies = [proxy for proxy in proxies if proxy.strip()]
        print(f"{Fore.GREEN}Boş olmayan satır sayısı: {len(proxies)}")
        
        separated_proxies = []
        for line in proxies:
            import re
            ip_port_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}:\d{2,5}\b'
            matches = re.findall(ip_port_pattern, line)
            
            if matches:
                separated_proxies.extend(matches)
            else:
                separated_proxies.append(line)
        
        print(f"{Fore.GREEN}Ayrıştırılan proxy sayısı: {len(separated_proxies)}")
        
        cleaned_proxies = clean_proxy_list(separated_proxies)
        
        print(f"{Fore.GREEN}Temizlenen proxy sayısı: {len(cleaned_proxies)}")
        
        # if cleaned_proxies:
        #     output_file = "cleaned_proxies.txt"
        #     with open(output_file, 'w', encoding='utf-8') as f:
        #         for proxy in cleaned_proxies:
        #             f.write(proxy + '\n')
        #     print(f"{Fore.CYAN}Temizlenmiş proxy'ler '{output_file}' dosyasına kaydedildi")
        
        if cleaned_proxies:
            print(f"{Fore.CYAN}İlk 10 temizlenmiş proxy örneği:")
            for i, proxy in enumerate(cleaned_proxies[:10]):
                print(f"  {i+1}. {proxy}")
        else:
            print(f"{Fore.YELLOW}Uyarı: Hiç proxy bulunamadı!")
        
        return cleaned_proxies
        
    except Exception as e:
        print(f"{Fore.RED}Dosya okuma hatası: {e}")
        import traceback
        traceback.print_exc()
        return []


def check_proxies_option():
    try:
        proxy_path = input(f"{Fore.YELLOW}\nTaranacak Proxy Dosyasının Yolunu Girin: ").strip()
        
        if not proxy_path:
            print(f"{Fore.RED}Hata: Dosya yolu boş olamaz!")
            return
        
        cleaned_proxies = load_and_clean_proxies(proxy_path)
        
        if cleaned_proxies:
            print(f"{Fore.GREEN}Proxy kontrolü başlatılıyor...")
            scrape_site(proxy_list=cleaned_proxies)
        else:
            print(f"{Fore.RED}Kontrol edilecek proxy bulunamadı!")
            
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}İşlem kullanıcı tarafından iptal edildi.")
    except Exception as e:
        print(f"{Fore.RED}Beklenmeyen bir hata oluştu: {e}")
        import traceback
        traceback.print_exc()


def main():
    """Main function"""
    try:
        clear_screen()
        display_logo()
        
        while True:
            display_menu()
            
            try:
                choice = input(f"{Fore.YELLOW}\nYapmak İstediğiniz İşlemi Girin: ").strip()
                
                if choice == "1":
                    print(f"{Fore.GREEN}Proxy alma işlemi başlatılıyor...")
                    getproxy()
                    
                elif choice == "2":
                    check_proxies_option()
                    
                elif choice == "3":
                    print(f"{Fore.CYAN}Çıkış yapılıyor...")
                    break
                    
                else:
                    print(f"{Fore.RED}Geçersiz seçim! Lütfen 1, 2 veya 3 girin.")
                    
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}Menüden çıkılıyor...")
                break
            except Exception as e:
                print(f"{Fore.RED}Beklenmeyen bir hata oluştu: {e}")
                
    except Exception as e:
        print(f"{Fore.RED}Kritik hata: {e}")
    finally:
        print(f"{Fore.CYAN}Tool kapatıldı.")


if __name__ == "__main__":
    main()