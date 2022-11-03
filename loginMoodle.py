from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import hashlib
from useAES256 import AESCipher


def checkPass():
    try:
        # Sul file vengono scritti nel seguente ordine: hash_pass, cipher_ID_login, cipher_pass_login
        credentials_file = open("credentials.txt", "r")
        credenziali = credentials_file.readlines()

        # Password per lo sblocco del programma
        raw_pass = getpass("Inserisci la password per lo sblocco del programma: ").strip()  # Password in chiaro
        hash_pass = hashlib.sha256(raw_pass.encode()).hexdigest()  # Hash della password (sblocco programma)

        # Se la password (sblocco programma) è valida
        if hash_pass == credenziali[0].strip():
            cipher_machine = AESCipher(raw_pass)  # Creo l'oggetto per cifrare e decifrare AES-CBC 128
            username_login = cipher_machine.decrypt(credenziali[1].strip())
            password_login = cipher_machine.decrypt(credenziali[2].strip())
            interact(username_login, password_login)
        else:
            exit()
    except:  # Se il file non esiste lo creo
        # Sul file vengono scritti nel seguente ordine: hash_pass, cipher_ID_login, cipher_pass_login
        print("Non c'è nessun file con le credenziali, creane uno nuovo: ")
        credentials_file = open("credentials.txt", "w")

        # Password per lo sblocco del programma
        raw_pass = getpass("Inserisci la password per lo sblocco del programma: ").strip()  # Password in chiaro
        hash_pass = hashlib.sha256(raw_pass.encode()).hexdigest()  # Hash della password (sblocco programma)
        credentials_file.write(hash_pass + "\n")
        cipher_machine = AESCipher(raw_pass)  # Creo l'oggetto per cifrare e decifrare AES-CBC 128

        # Prendo il nome utente
        cipher_ID_login = cipher_machine.encrypt(input("Inserisci il nome utente: ").strip())
        credentials_file.write(cipher_ID_login.decode() + "\n")

        # Prendo la password per il login
        cipher_pass_login = cipher_machine.encrypt(getpass("Inserisci la password per il login: ").strip())
        credentials_file.write(cipher_pass_login.decode())
        interact(cipher_machine.decrypt(cipher_ID_login), cipher_machine.decrypt(cipher_pass_login))  # Passo all'interazione con il browser fornendo username e password


def interact(username, password):
    drive = webdriver.Firefox()
    drive.get("https://moodledidattica.univr.it/")
    elem = drive.find_element(By.ID, "form_username")  # Prendo il campo dove inserire l'username
    elem.send_keys(username)
    elem = drive.find_element(By.ID, "form_password")  # Prendo il campo dove inserire la password
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)


if __name__ == '__main__':
    checkPass()
