#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen, PIPE, check_call
from colorama import Fore, Style

def colorprint(verbosity, text):
    if verbosity == "fatal":
        print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)
    if verbosity == "warn":
        print(Fore.YELLOW + text + Style.RESET_ALL)
    if verbosity == "info":
        print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)

logo = ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)

def decode_vigenere(vigenere_msg, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    vigenere_msg_int = [ord(i) for i in vigenere_msg]
    text_msg = ''
    for i in range(len(vigenere_msg_int)):
        value = (vigenere_msg_int[i] - key_as_int[i % key_length]) % 26
        text_msg += chr(value + 65)
    return text_msg

def vigenere_decoder():
    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "Bu bölümde şifreli vigenere mesajlarını decode edebilirsiniz.")
        colorprint("info", "Lütfen şifreli mesajı girin.")
        colorprint("warn", "9-->Üst menüye dön.")
        colorprint("fatal", "0-->Çık")

        vigenere_msg = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/vigenere_decoder" + Style.RESET_ALL + ")-->")

        colorprint("info", "Lütfen anahtarı giriniz.")

        key = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/vigenere_decoder" + Style.RESET_ALL + ")-->")

        if vigenere_msg == "9":
            return
        elif vigenere_msg == "0":
            sys.exit()
        else:
            text_msg = decode_vigenere(vigenere_msg, key)
            succesprint ("Mesajınız dönüştürüldü.")
            print ("Mesaj:\n--> %s" %text_msg)

        colorprint("info", "Başka bir mesaj dönüştürmek ister misiniz? E/H")
        choice = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/vigenere_decoder" + Style.RESET_ALL + ")-->")

        if choice == 'H':
            return

if __name__ == "__main__":
    vigenere_decoder()
