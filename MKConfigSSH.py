#!/usr/bin/python3
# App Configuracion Mikrotik Automatizada

from sys import stderr, stdin, stdout
from turtle import clear
import paramiko

def user():

    control=False
                    
    while control==False:
        
        username=input("Ingrese nombre de usuario del Equipo: ")
        
        long=len(username) #Calcular la longitud del nomre de usuario
            
        y=username.isalnum() #Calcula que la cadena contenga valores alfanuméricos
        
        if y== False: # La cadena contiene valores no alfanuméricos
                print("El nombre de usuario puede contener solo letras y números")
            
        if long < 6: 
                print("El nombre de usuario debe contener al menos 6 caracteres")
            
        if long > 12: 
                print("El nombre de usuario no puede contener más de 12 caracteres")
            
        if long >5 and long <13 and y ==True:
            control=True #Verdadero si el tamaño es mayor a 5 y menor a 13
            print("Usuario creado exitosamente")
    
    return username
 

def passwd():

    control=False

    password=input("Ingrese Contraseña del Equipo: ")

    while control==False:

        validar=False #que se vayan cumpliendo los requisitos uno a uno.
        long=len(password) #Calcula la longitud de la contraseña
        espacio=False  #variable para identificar espacios
        mayuscula=False #variable para identificar letras mayúsculas
        minuscula=False #variable para contar identificar letras minúsculas
        numeros=False #variable para identificar números
        y=password.isalnum()#si es alfanumérica retona True
        control=True #verifica que hayan mayuscula, minuscula, numeros y no alfanuméricos
        
        for carac in password: #ciclo for que recorre caracter por caracter en la contraseña

            if carac.isspace()==True: #Saber si el caracter es un espacio
                espacio=True #si encuentra un espacio se cambia el valor user

            if carac.isupper()== True: #saber si hay mayuscula
                mayuscula=True #acumulador o contador de mayusculas
                
            if carac.islower()== True: #saber si hay minúsculas
                minuscula=True #acumulador o contador de minúsculas
                
            if carac.isdigit()== True: #saber si hay números
                numeros=True #acumulador o contador de numeros
                            
        if espacio==True: #hay espacios en blanco
                print("La contraseña no puede contener espacios")
        else:
            validar=True #se cumple el primer requisito que no hayan espacios
                       
        if long <8 and validar==True:
            print("Mínimo 8 caracteres")
            validar=False #cambia a Flase si no se cumple el requisito móinimo de caracteres

        if mayuscula == True and minuscula ==True and numeros == True and y== False and validar ==True:
           validar = True #Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
        else:
           control=False #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple
           
        if validar == True and control==False:
           print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")

        if validar == True and control ==True:
            control=True
           
           
    return password

  
def main():

    addr = '0.0.0.0'
    username=''
    password=''
    port = 22
    validar = False
    
    while validar == False:
        
        if addr == "0.0.0.0":
            
            print("Bienvenido al Sistema de Configuracion Mikrotik")
        
            addr=input("Ingrese IP del Equipo: ")

            username=user()

            password=passwd()
                
            print("Ingrese numero de puerto: ")
            
            port = input()

            validar = True

        else:
            
            print("Se usará Puerto por defecto")

            validar = False

    if addr != "0.0.0.0":
        
        #SSH Connect...
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(addr, port, username, password)
        #stdin, stdout, stderr = client.exec_command('ip firewall connection print terse')
        stdout = client.exec_command("ip address add address= 192.168.1.1/24 interface=lan1")
        #print(stdout.read().decode("ascii").strip("\n"))
        #for line in stdout:
        #    print(line.strip('\n'))
        
        # Close the client itself
        client.close()

    else: print("Direccion IP Faltante, comience nuevamente.")
    
    

main()