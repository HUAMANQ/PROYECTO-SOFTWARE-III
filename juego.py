import pygame

def main():
     pygame.init() #inicializa los modulos de pygame
     pantalla=pygame.display.set_mode([800,500])#dimensiones de la ventana 
     pygame.display.set_caption("Juego HQ")#titulo del juego
     salir=False
     reloj=pygame.time.Clock()
     blanco=(255,255,255)#cambia el color de la ventana negra a color blanco
     
     while salir!=True: #loop principal
         for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 salir=True
                 reloj.tick(20)
         pantalla.fill(blanco)
         pygame.display.update()
         
     pygame.quit()


main()
