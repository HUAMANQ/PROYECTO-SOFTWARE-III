import pygame

import pygame
 
"""
Constantes globales
"""
 
# colores
NEGRO = (255, 0, 255) 
BLANCO = (255, 255, 255) 
AZUL = (0, 0, 255)
 
# dimensiones de la pantalla
LARGO_PANTALLA  = 800
ALTO_PANTALLA = 600

def main():
     #ccolores de la ventana del juego
     pygame.init() #inicializa los modulos de pygame
     
     '''pantalla=pygame.display.set_mode([800,500])#dimensiones de la ventana '''
     
    ''' pygame.display.set_caption("Juego HQ")#titulo del juego'''
     salir=False
     reloj=pygame.time.Clock()
     blanco=(0,255,0)#cambia el color de la ventana negra a color blanco
class Pared(pygame.sprite.Sprite):
    """ Pared con la que el protagonista puede encontrarse. """
    def __init__(self, x, y, largo, alto):
        """ Constructor para la pared con la que el protagonista puede encontrarse """
        #  Llama al constructor padre
        pygame.sprite.Sprite.__init__(self)
 
        # construye una pared azul con las dimensiones especificadas por los parametros
        self.image = pygame.Surface([largo, alto])
        self.image.fill(AZUL)
 
        # establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
         
         
# llamamos a esta función para que la biblioteca Pygame pueda autoiniciarse.
pygame.init()
 
# creamos una pantalla de 800x600
pantalla = pygame.display.set_mode([LARGO_PANTALLA, ALTO_PANTALLA])
 
# creamos el título de la ventana
pygame.display.set_caption("Juego HQ")
 
# lista que almacena todos los sprites
listade_todoslos_sprites = pygame.sprite.Group()
 
# construimos las paredes. (x_pos, y_pos, largo, alto)
pared_list = pygame.sprite.Group()
 
pared = Pared(0,0,10,600)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
 
pared = Pared(10,0,790,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
 
pared = Pared(10,200,100,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)


# creamos al objeto 
protagonista = Protagonista(50, 50)
protagonista.paredes = pared_list
 
listade_todoslos_sprites.add(protagonista)
 
reloj = pygame.time.Clock()
 
hecho = False
 


while salir!=True: #loop principal
         for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 salir=True
                 reloj.tick(20)
         pantalla.fill(blanco)
         pygame.display.update()
listade_todoslos_sprites.update()

main()
