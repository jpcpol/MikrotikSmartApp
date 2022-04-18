#!/usr/bin/python3
# App Configuracion Mikrotik Automatizada

from sys import stderr, stdin, stdout
from turtle import clear
import paramiko

def main():

    addr = "0.0.0.0"
    user = "admin"
    passw = ""
    port = 22
    dato = "No"
    
    if addr == "0.0.0.0" :
        print("Bienvenido al Sistema de Configuracion Mikrotik")
        
        print("Ingrese direecion IP: ")
        
        addr = input()

        print("Ingrese Usuario: ")
       
        user = input()

        print("Ingrese Password: ")
        
        passw = input()

        print("Desea Cambiar el puerto SSH? Si/No")
        
        dato = input()

        if dato == "Si":
                
            print("Ingrese numero de puerto: ")
            port = input()

        else:
            
            print("Se usará Puerto por defecto")

    if addr != "0.0.0.0":
        
        #SSH Connect...
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(addr, port, user, passw)
        #stdin, stdout, stderr = client.exec_command('ip firewall connection print terse')
        stdin, stdout, stderr = client.exec_command("ip address add address= 192.168.1.1/24 interface=lan1")
        print(stdout.read().decode("ascii").strip("\n"))
        #for line in stdout:
        #    print(line.strip('\n'))
        
        # Close the client itself
        client.close()

    else: print("Direccion IP Faltante, comience nuevamente.")
    

main()