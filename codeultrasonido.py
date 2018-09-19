#!/usr/bin/env python
# -*- coding: utf-8 -*-
#importare la libreria pygame y la libreria pyserial
from random import randint
#se importara tkinter y timeit para medir el tiempo de ejecucion de un codigo
from timeit import timeit
import pygame, sys, time, serial  #Importa pygame, sistema, tiempo y pyserial
from pygame.locals import *  # importa todo desde pygame / local
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096) #activar cuando queramos poner audio
pygame.mixer.music.set_volume(1.0)
print("Este programa funciona en conjunto con 3 ultrasonidos de arduino y gracias a los puertos serie, \n a medida que uno toca una diferente parte de una matriz \n suenan diferentes sonidos o se muestran diferentes colores")

#configurando lector de serial - arduino  ES IMPORTANTE MODIFICAR ESTO, ES DIFERENTE EN CADA PC(COM), 
arduino = serial.Serial('COM13', 115200)


# Colores
negro = (0, 0, 0)  
morado = (136, 78, 160)
cafe = (203, 67, 53)
verde = (88, 214, 141)
azul = (93, 173, 226)
rojo = (231, 76, 60)
blanco = (255,255, 255)
amarillo = (255, 255, 102) # mas colores en https://htmlcolorcodes.com/es/tabla-de-colores/
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0


pygame.init()  # instruccion obligatoria para iniciar con pygame
ventana = pygame.display.set_mode((600, 600))  # esta tupla es el ancho y largo de la ventana
pygame.display.set_caption("Matriz de 3 X 3")  # muestra titulo de la ventana

velocidad = 5



while True:
    #decodificando y modificando serial para ser entendido por arduino y dividido en 3 variables segun ultrasonidos
  #  rawString = arduino.readline()
    rawString = arduino.readline()
  #  print(rawString) #no es necesario imprimir esto (ademas esta en bytes - obj)
    new = rawString.decode("utf-8") 
 #   print(new)  # ya esta confirmado
    x = (new[:].find("X"))
    y = (new[:].find("Y"))
    z = (new[:].find("Z"))

    ArduinoUno = new[x+1:y]
    ArduinoDos = new[y+1:z]
    ArduinoTres = new[z+1:]


    ArduinoUno =  int(ArduinoUno)
    ArduinoDos = int(ArduinoDos) 
    ArduinoTres = int(ArduinoTres) 

  #  print(ArduinoUno)
  #  print(ArduinoDos)
  #  print(ArduinoTres)
  #  print(ArduinoUno, "holaone")


    # arduino.close()
    ventana.fill(blanco)
    
  #  print(ArduinoUno, "holatwo")
    
    if (ArduinoUno >0 and ArduinoUno< 10):
   #     print(" A es menor a 10")
        rectangulo1 = pygame.draw.rect(ventana, rojo, (400, 0, 200, 200), 0) 
        pygame.display.update()
        
        if a==1:
            jhjh = pygame.mixer.stop()
            jhjh = pygame.mixer.Sound(r'C:\Users\Qualqum experience\Downloads\sonido\bella.wav')
            jhjh.play()
            b=0
            c=0
            d=0
            e=0
            f=0
            g=0
            h=0
            i=0

        a = a + 1
        
            



    else:
        rectangulo1 = pygame.draw.rect(ventana, blanco, (400, 0, 200, 200), 0)
        pygame.display.update()


       
    if (ArduinoUno >9 and ArduinoUno< 20):
    #    print(" A es menor a 20")
        rectangulo2 = pygame.draw.rect(ventana, amarillo, (400, 200, 200, 200), 0)
        pygame.display.update()
        if b==1:
            jhjh = pygame.mixer.stop()
            jhjh = pygame.mixer.Sound(r'C:\Users\Qualqum experience\Downloads\sonido\abba.wav')
            jhjh.play()
            a=0
            
            c=0
            d=0
            e=0
            f=0
            g=0
            h=0
            i=0
        b = b + 1

    else:
        rectangulo2 = pygame.draw.rect(ventana, blanco, (400, 200, 200, 200), 0)
        
        pygame.display.update()
       
    if (ArduinoUno >19 and ArduinoUno< 30):
     #   print(" A es menor a 30")
        rectangulo3 = pygame.draw.rect(ventana, verde, (400, 400, 200, 200), 0) # reparar
        pygame.display.update()
        if c==1:
            jhjh = pygame.mixer.stop()
            jhjh = pygame.mixer.Sound(r'C:\Users\Qualqum experience\Downloads\sonido\adele.wav')
            jhjh.play()
            a=0
            b=0
            
            d=0
            e=0
            f=0
            g=0
            h=0
            i=0
        c = c + 1
    else:
        rectangulo3 = pygame.draw.rect(ventana, blanco, (400, 400, 200, 200), 0)
        pygame.display.update()
        
       

    if (ArduinoDos >0 and ArduinoDos< 10):
     #   print("B es menor a 10")
        rectangulo4 = pygame.draw.rect(ventana, cafe, (200, 0, 200, 200), 0)
        pygame.display.update()
        if d==1:
            jhjh = pygame.mixer.stop()
            jhjh = pygame.mixer.Sound(r'C:\Users\Qualqum experience\Downloads\sonido\bose.wav')
            jhjh.play()
            a=0
            b=0
            c=0
            
            e=0
            f=0
            g=0
            h=0
            i=0
        d = d + 1
    else:
        rectangulo4 = pygame.draw.rect(ventana, blanco, (200, 0, 200, 200), 0)
        pygame.display.update()
  
    if (ArduinoDos >9 and ArduinoDos< 20):
     #   print(" B es menor a 20")
        rectangulo5 = pygame.draw.rect(ventana, azul, (200, 200, 200, 200), 0)
        pygame.display.update()
        if e==1:
            jhjh = pygame.mixer.stop()
            jhjh = pygame.mixer.Sound(r'C:\Users\Qualqum experience\Downloads\sonido\katyperry.wav')
            jhjh.play()

            a=0
            b=0
            c=0
            d=0
            
            f=0
            g=0
            h=0
            i=0
        e = e + 1
    else:
        rectangulo5 = pygame.draw.rect(ventana, blanco, (200, 200, 200, 200), 0)
        pygame.display.update()
        
    if (ArduinoDos >19 and ArduinoDos< 30):
    #    print(" B es menor a 30")
        rectangulo6 = pygame.draw.rect(ventana, amarillo, (200, 400, 200, 200), 0)
        pygame.display.update()
        if f==1:
            jhjh = pygame.mixer.stop()
            jhjh = pygame.mixer.Sound(r'C:\Users\Qualqum experience\Downloads\sonido\laplayer.wav')
            jhjh.play()
            a=0
            b=0
            c=0
            d=0
            e=0
            
            g=0
            h=0
            i=0
        f = f + 1
    else:
        rectangulo6 = pygame.draw.rect(ventana, blanco, (200, 400, 200, 200), 0)
        pygame.display.update()
        


    if (ArduinoTres >0 and ArduinoTres< 10):
        print(" C es menor a 10")
        rectangulo7 = pygame.draw.rect(ventana, morado, (0, 0, 200, 200), 0)
        pygame.display.update()
        if g==1:
            jhjh = pygame.mixer.stop()
            jhjh = pygame.mixer.Sound(r'C:\Users\Qualqum experience\Downloads\sonido\mevoy.wav')
            jhjh.play()
            a=0
            b=0
            c=0
            d=0
            e=0
            f=0
            
            h=0
            i=0
        g = g + 1
    else:
        rectangulo7 = pygame.draw.rect(ventana, blanco, (0, 0, 200, 200), 0)
        pygame.display.update()
        
    if (ArduinoTres >9 and ArduinoTres< 20):
        print(" C es menor a 20")
        rectangulo8 = pygame.draw.rect(ventana, verde, (0, 200, 200, 200), 0)
        pygame.display.update()
        if h==1:
            jhjh = pygame.mixer.stop()
            jhjh = pygame.mixer.Sound(r'C:\Users\Qualqum experience\Downloads\sonido\miley.wav')
            jhjh.play()
            a=0
            b=0
            c=0
            d=0
            e=0
            f=0
            g=0
            
            i=0
        h = h + 1

    else:
        rectangulo8 = pygame.draw.rect(ventana, blanco, (0, 200, 200, 200), 0)
        pygame.display.update()
        
    if (ArduinoTres >19 and ArduinoTres< 30):
        print(" C es menor a 30")
        rectangulo9 = pygame.draw.rect(ventana, azul, (0, 400, 200, 200), 0)
        pygame.display.update()
        if i==1:
            jhjh = pygame.mixer.stop()
            jhjh = pygame.mixer.Sound(r'C:\Users\Qualqum experience\Downloads\sonido\sia.wav')
            jhjh.play()
            a=0
            b=0
            c=0
            d=0
            e=0
            f=0
            g=0
            h=0
            
        i = i + 1

    else:
        rectangulo9 = pygame.draw.rect(ventana, blanco, (0, 400, 200, 200), 0)
        pygame.display.update()
    #Desde este momento creare la parte de deteccion de derecha izquierda etc
    if(ArduinoUno>1 and ArduinoUno<30):
        print("Arduino uno es menor a 30")
    #Desde este momento terminare la creacion de deteccion de izquierda derecha etc.
   
    for evento in pygame.event.get():
        if evento.type == QUIT:  # Que el usuario presiona el boton quit
            pygame.quit()  # ejecuta comando quit, sale de pygame
            sys.exit()  #sale del programa sys.
        pygame.display.update() # ver si se puede borrar esta linea
    
     
        #pygame.draw.line(ventana, azul, [0, 0], [700, 500], 50)  #De esta manera se genera una linea
        pygame.display.flip() # que hace esto?
        #pygame.draw.rect((200,200), verde, [55, 500, 10, 5])
        #pygame.draw.rect((200,100), verde, (752, 700, 100, 50))



