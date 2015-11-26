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

'''def main():
     #ccolores de la ventana del juego
     pygame.init() #inicializa los modulos de pygame
     
     pantalla=pygame.display.set_mode([800,500])#dimensiones de la ventana
      pygame.display.set_caption("Juego HQ")#titulo del juego
    salir=False
     reloj=pygame.time.Clock()
     blanco=(0,255,0)#cambia el color de la ventana negra a color blanco
'''
# Establecemos el largo y alto de cada segmento de la serpiente
largodel_segmento = 15
altodel_segmento = 15
# Margen entre cada segmento
margendel_segmento = 3
 
#Velocidad inicial
cambio_x = largodel_segmento + margendel_segmento
cambio_y = 0

     
class Protagonista(pygame.sprite.Sprite):
    """ esta clase representa la barra inferior que controla el protagonista. """
 
    # establecemos el vector velocidad
    cambio_x = 0
    cambio_y = 0
    paredes = None
     
    # funcion Constructor 
    def __init__(self, x, y):
        #  llama al constructor padre
        pygame.sprite.Sprite.__init__(self)
  
        # establecemos el alto y largo
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLANCO)
 
        # establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
     
    def cambiovelocidad(self, x, y):
        """ Cambia la velocidad del protagonista. """


        def cambiovelocidad(self, x, y):
            """ Cambia la velocidad del protagonista. """

        self.cambio_x += x
        self.cambio_y += y
         
    def update(self):
        """ Cambia la velocidad del protagonista. """
        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x

        # hemos chocado contra la pared despues de esta actualizacion?
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.paredes, False)
        for bloque in lista_impactos_bloques:
            #si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado izquierdo del objeto que hemos tocado-
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            else:
                # en caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = bloque.rect.right
 
        # desplazar arriba/izquierda
        self.rect.y += self.cambio_y
          
        # comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.paredes, False) 
        for bloque in lista_impactos_bloques:
                 
            # reseteamos nuestra posicion basandonos en la parte superior/inferior del objeto.
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top 
            else:
                self.rect.top = bloque.rect.bottom
    
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
 
pared = Pared(10,10,500,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
 
pared = Pared(10,10,10,500)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(10,500,500,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
 
pared = Pared(500,10,10,500)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
 
pared = Pared(40,40,50,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(70,70,10,50)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(100,100,10,50)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(140,120,10,50)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(110,140,70,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(200,200,10,100)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(210,240,200,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(10,10,500,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
 
pared = Pared(10,10,10,500)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(10,500,500,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
 
pared = Pared(500,10,10,500)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
 
pared = Pared(40,40,50,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(70,70,10,50)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(100,100,10,50)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(140,120,10,50)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(110,140,70,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(200,200,10,100)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(210,240,200,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(300,120,10,50)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(300,140,70,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(40,200,10,100)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(210,400,270,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(280,280,10,100)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(300,100,200,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(400,300,10,100)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(300,300,170,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(100,300,10,100)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(300,200,170,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

pared = Pared(60,300,10,100)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(60,300,170,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(60,430,170,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(60,460,170,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

listade_todoslos_sprites.add(pared)
pared = Pared(130,270,10,240)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(35,350,10,150)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

#para abrir paredes 
listade_todoslos_sprites.add(pared)
pared = Pared(400,35,10,185)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(220,40,10,140)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)


listade_todoslos_sprites.add(pared)
pared = Pared(170,35,10,210)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(250,40,10,170)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)


listade_todoslos_sprites.add(pared)
pared = Pared(170,300,10,100)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(480,340,10,140)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

listade_todoslos_sprites.add(pared)
pared = Pared(500,300,10,100)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(450,30,10,140)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)


listade_todoslos_sprites.add(pared)
pared = Pared(320,430,10,70)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(350,340,10,140)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)


listade_todoslos_sprites.add(pared)
pared = Pared(250,270,10,70)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(450,240,10,70)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(370,270,10,70)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(450,430,10,70)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(390,430,10,70)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(420,410,10,70)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(290,410,10,70)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(310,340,10,50)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

listade_todoslos_sprites.add(pared)
pared = Pared(60,60,100,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(200,130,100,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(20,135,65,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(20,100,30,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(170,360,70,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(170,40,50,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(260,70,100,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(70,240,110,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(50,170,100,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)
pared = Pared(20,200,100,10)
pared_list.add(pared)
listade_todoslos_sprites.add(pared)

# creamos al objeto 
protagonista = Protagonista(20, 20)
protagonista.paredes = pared_list
 
segementos_dela_serpiente = []
for i in range(15):
    x = 250 - (largodel_segmento + margendel_segmento) * i
    y = 30
    segmento = Protagonista(x, y)
    segementos_dela_serpiente.append(segmento)
    listade_todoslos_sprites.add(segmento)
 
  
reloj = pygame.time.Clock()
hecho = False
  
while not hecho:
      
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
  
        # Establecemos la velocidad basándonos en la tecla presionada
        # Queremos que la velocidad sea la suficiente para mover un segmento
        # más el margen.
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                cambio_x = (largodel_segmento + margendel_segmento) * -1
                cambio_y = 0
            if evento.key == pygame.K_RIGHT:
                cambio_x = (largodel_segmento + margendel_segmento)
                cambio_y = 0
            if evento.key == pygame.K_UP:
                cambio_x = 0
                cambio_y = (altodel_segmento + margendel_segmento) * -1
            if evento.key == pygame.K_DOWN:
                cambio_x = 0
                cambio_y = (altodel_segmento + margendel_segmento)
                       
    # Eliminamos el último segmento de la serpiente
    # .pop() este comando elimina el último objeto de una lista.
    segmento_viejo = segementos_dela_serpiente.pop()
    listade_todoslos_sprites.remove(segmento_viejo)
     
    # Determinamos dónde aparecerá el nuevo segmento
    x = segementos_dela_serpiente[0].rect.x + cambio_x
    y = segementos_dela_serpiente[0].rect.y + cambio_y
    segmento = Protagonista(x, y)
     
    # Insertamos un nuevo segmento en la lista
    segementos_dela_serpiente.insert(0, segmento)
    listade_todoslos_sprites.add(segmento)
     
    pantalla.fill(NEGRO)
     
    listade_todoslos_sprites.draw(pantalla)
 
    #listade_todoslos_sprites.update()
    # -- Dibujamos todo
    # Limpiamos la pantalla
    pantalla.fill(NEGRO)
     
    listade_todoslos_sprites.draw(pantalla)
  # Actualizamos la pantalla

    pygame.display.flip()
 
    reloj.tick(5)
             
pygame.quit()

#main()

