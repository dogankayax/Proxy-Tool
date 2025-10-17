import requests
from fake_useragent import UserAgent
from colorama import init,Fore

ua  = UserAgent()
init(autoreset=True)
def getproxy():
    url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&skip=0&limit=2000"
    headers = {
        "User-Agent":ua.random

    }

    response = requests.get(url,headers=headers)
    print(f"{Fore.GREEN}[+]{Fore.RESET} Proxyler alındı.\n")
    print(f"{Fore.YELLOW}--------------------\n{Fore.RESET}")
    print(f"{Fore.LIGHTBLACK_EX} {response.text}")
    print(f"{Fore.YELLOW}--------------------\n{Fore.RESET}")

