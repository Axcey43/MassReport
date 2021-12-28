#id you skid give me credits (Axcey#4370)

import colorama
import requests

from colorama import Fore, init, Style

b = Style.BRIGHT
sent = 0


class Axcey:
    def Main(self):
        print(f'''
{b+Fore.BLUE}
       ▄████████ ▀████    ▐████▀  ▄████████    ▄████████ ▄██   ▄   
      ███    ███   ███▌   ████▀  ███    ███   ███    ███ ███   ██▄ 
      ███    ███    ███  ▐███    ███    █▀    ███    █▀  ███▄▄▄███ 
      ███    ███    ▀███▄███▀    ███         ▄███▄▄▄     ▀▀▀▀▀▀███ 
    ▀███████████    ████▀██▄     ███        ▀▀███▀▀▀     ▄██   ███ 
      ███    ███   ▐███  ▀███    ███    █▄    ███    █▄  ███   ███ 
      ███    ███  ▄███     ███▄  ███    ███   ███    ███ ███   ███ 
      ███    █▀  ████       ███▄ ████████▀    ██████████  ▀█████▀  {Fore.RESET}

{b+Fore.BLACK}─────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
{b+Fore.BLUE}Axcey Reporter{Fore.RESET} {b+Fore.RED}[Menu]{Fore.RESET}
                {b+Fore.MAGENTA}└─{Fore.RESET}[{b+Fore.BLUE}1{Fore.RESET}] {b+Fore.RED}Guild Report{Fore.RESET}
                {b+Fore.MAGENTA}└─{Fore.RESET}[{b+Fore.BLUE}2{Fore.RESET}] {b+Fore.RED}Member Report{Fore.RESET}
                                                               
    ''')
        choice = input(f'{b+Fore.BLUE}> Choice{Fore.RESET}: ')
        if choice == '1':
            self.GuildReport()
            input()
            self.Main()
        elif choice == '2':
            self.MemberReport()
            input()
            self.Main()
        else:
          print(f'[{Fore.RED}!{Fore.RESET}] {Fore.RED}Invalid Token{Fore.RESET}')

    def MemberReport(self):
        print(f'''
{b+Fore.BLUE}Axcey Reporter{Fore.RESET} {b+Fore.RED}[Member Report]{Fore.RESET}
[{b+Fore.BLUE} {1} {Fore.RESET}] Illegal Content        
[{b+Fore.BLUE} {2} {Fore.RESET}] Harassment            
[{b+Fore.BLUE} {3} {Fore.RESET}] Spam or phishing links 
[{b+Fore.BLUE} {4} {Fore.RESET}] Hateful Content        
[{b+Fore.BLUE} {5} {Fore.RESET}] NSFW Content          
    ''')
        user = input(f'{b+Fore.BLUE}> User ID{Fore.RESET}: ')
        message = input(f'{b+Fore.BLUE}> Message ID{Fore.RESET}: ')
        reason = input(f'{b+Fore.BLUE}> Option{Fore.RESET}: ')
        token = input(f'{b+Fore.BLUE}> Token{Fore.RESET}: ')
        global sent
        headers = {
            "Authorization": token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
            "Content-Type": "application/json"
        }

        json = {
        "user_id": user, 
        "message_id": message, 
        "reason": reason
        }

        while True:
            r = requests.post(f"https://discord.com/api/v8/report",
                              headers=headers,
                              json=json)
            if r.status_code == 201:
                print(
                    f"{Fore.GREEN} > Sent Report{Fore.RESET} \x1b[38;5;21m[%s"
                    % sent + '\x1b[38;5;21m]\033[0m')
                sent += 1
            elif r.status_code == 401:
                print(
                    f'[{Fore.RED}!{Fore.RESET}] {Fore.RED}Invalid Token {Fore.RESET}'
                )
            else:
                print(
                    f'[{Fore.RED}!{Fore.RESET}] {Fore.RED}Failed to send report{Fore.RESET}'
                )

    def GuildReport(self):
        print(f'''
{b+Fore.BLUE}Axcey Reporter{Fore.RESET} {b+Fore.RED}[Guild Report]{Fore.RESET}
[{b+Fore.BLUE} {1} {Fore.RESET}] Illegal Content        
[{b+Fore.BLUE} {2} {Fore.RESET}] Harassment            
[{b+Fore.BLUE} {3} {Fore.RESET}] Spam or phishing links 
[{b+Fore.BLUE} {4} {Fore.RESET}] Hateful Content       
[{b+Fore.BLUE} {5} {Fore.RESET}] NSFW Content          
    ''')
        guild = input(f'{b+Fore.BLUE}> Guild ID{Fore.RESET}: ')
        channel = input(f'{b+Fore.BLUE}> Channel ID{Fore.RESET}: ')
        message = input(f'{b+Fore.BLUE}> Message ID{Fore.RESET}: ')
        option = input(f'{b+Fore.BLUE}> Option{Fore.RESET}: ')
        token = input(f'{b+Fore.BLUE}> Token{Fore.RESET}: ')
        global sent
        headers = {
            "Authorization": token,
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
            "Content-Type": "application/json"
        }

        json = {
            "guild_id": guild,
            "channel_id": channel,
            "message_id": message,
            "reason": option
        }

        while True:
            r = requests.post(f"https://discord.com/api/v6/report",
                              headers=headers,
                              json=json)
            if r.status_code == 201:
                print(
                    f'{Fore.GREEN} > Sent Report{Fore.RESET} \x1b[38;5;21m[%s'
                    % sent + '\x1b[38;5;21m]\033[0m')
                sent += 1
            elif r.status_code == 401:
                print(
                    f'[{Fore.RED}!{Fore.RESET}] {Fore.RED}Invalid Token {Fore.RESET}'
                )
            else:
                print(
                    f'[{Fore.RED}!{Fore.RESET}] {Fore.RED}Failed to send report{Fore.RESET}'
                )

if __name__ == "__main__":
    Axcey().Main()