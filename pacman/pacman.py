import pygame
import random



def crearProtagonista(spritesDelJuego, x, y):
   
    protagonista = pygame.sprite.Sprite()
   
    protagonista.image = pygame.image.load("pacman.png")
    
   
    protagonista.rect = protagonista.image.get_rect()
    protagonista.rect.x = x
    protagonista.rect.y = y
   
    protagonista.velocidad_x = 0
    protagonista.velocidad_y = 0
   
    spritesDelJuego.add(protagonista)
   
    return protagonista

def aparecerLadoContrario(protagonista):
    
    if (protagonista.rect.right < 0):
        protagonista.rect.left = LARGO_PANTALLA
    elif(protagonista.rect.left > LARGO_PANTALLA):
        protagonista.rect.right = 0

    return protagonista

def aparecerLadoContrarioFantasma(fantasma):
    
    if (fantasma.rect.right < 0):
        fantasma.rect.left = LARGO_PANTALLA
    elif(fantasma.rect.left > LARGO_PANTALLA):
        fantasma.rect.right = 0

    return fantasma    

def crearFantasma(spritesDelJuego, x, y):
   
    fantasma = pygame.sprite.Sprite()
   
    fantasma.image = pygame.image.load("fantasma.png")
   
    fantasma.rect = protagonista.image.get_rect()
    fantasma.rect.x = x
    fantasma.rect.y = y
   
    fantasma.velocidad_x = 0
    fantasma.velocidad_y = 0
   
    spritesDelJuego.add(fantasma)
   
    return fantasma


def crearPared(x , y, ancho, largo):
   
    pared = pygame.sprite.Sprite()
   
    pared.image = pygame.Surface([ancho,largo])
    pared.image.fill(AZUL)
   
    pared.rect = pared.image.get_rect()
    pared.rect.y = y
    pared.rect.x = x
   
    return pared


def createParedes(spritesDelJuego):
   
    listaParedes = pygame.sprite.Group()
   
    pared1 = crearPared(0,0,100,250)
    listaParedes.add(pared1)
   
    spritesDelJuego.add(pared1)
   
    pared2 = crearPared(0,351,100,249)
    listaParedes.add(pared2)
   
    spritesDelJuego.add(pared2)
   
    pared3 = crearPared(100,0,1200,100)
    listaParedes.add(pared3)
   
    spritesDelJuego.add(pared3)
   
    pared4 = crearPared(100,500,1200,100)
    listaParedes.add(pared4)
   
    spritesDelJuego.add(pared4)
    
    pared5 = crearPared(1100,100,100,150)
    listaParedes.add(pared5)
   
    spritesDelJuego.add(pared5)
    
    pared6 = crearPared(1100,351,100,249)
    listaParedes.add(pared6)
   
    spritesDelJuego.add(pared6)
    
    pared7 = crearPared(151,151,100,100)
    listaParedes.add(pared7)
   
    spritesDelJuego.add(pared7)
    
    pared8 = crearPared(310,151,100,100)
    listaParedes.add(pared8)
   
    spritesDelJuego.add(pared8)
    
    pared9 = crearPared(469,151,100,100)
    listaParedes.add(pared9)
   
    spritesDelJuego.add(pared9)
    
    pared10 = crearPared(628,151,100,100)
    listaParedes.add(pared10)
   
    spritesDelJuego.add(pared10)
    
    pared11 = crearPared(787,151,100,100)
    listaParedes.add(pared11)
   
    spritesDelJuego.add(pared11)
    
    pared12 = crearPared(946,151,100,100)
    listaParedes.add(pared12)
   
    spritesDelJuego.add(pared12)
    
    pared13 = crearPared(151,349,100,100)
    listaParedes.add(pared13)
   
    spritesDelJuego.add(pared13)
    
    pared14 = crearPared(310,349,100,100)
    listaParedes.add(pared14)
   
    spritesDelJuego.add(pared14)
    
    pared15 = crearPared(469,349,100,100)
    listaParedes.add(pared15)
   
    spritesDelJuego.add(pared15)
    
    pared16 = crearPared(628,349,100,100)
    listaParedes.add(pared16)
   
    spritesDelJuego.add(pared16)
    
    pared17 = crearPared(787,349,100,100)
    listaParedes.add(pared17)
   
    spritesDelJuego.add(pared17)
    
    pared18 = crearPared(946,349,100,100)
    listaParedes.add(pared18)
    
    spritesDelJuego.add(pared18)
    
    return listaParedes

def crearAlimento(x , y, ancho, largo):
   
    alimento = pygame.sprite.Sprite()
   
    alimento.image = pygame.Surface([ancho, largo])
    alimento.image.fill(BLANCO)
   
    alimento.rect = alimento.image.get_rect()
    alimento.rect.y = y
    alimento.rect.x = x
   
    return alimento
def crearFruta(x , y, ancho, largo):
   
    fruta = pygame.sprite.Sprite()
   
    
    fruta.image= pygame.image.load("fruta.png")
    
   
    fruta.rect = fruta.image.get_rect()
    fruta.rect.y = y
    fruta.rect.x = x
   
    return fruta
def createFruta (spritesDelJuego):

    listaFruta = pygame.sprite.Group()
   
    fruta1 = crearFruta(275,190,30,30)
    listaFruta.add(fruta1)
   
    spritesDelJuego.add(fruta1)

    fruta2 = crearFruta(900,190,30,30)
    listaFruta.add(fruta2)
   
    spritesDelJuego.add(fruta2)
   

    fruta4 = crearFruta(432,190,30,30)
    listaFruta.add(fruta4)
   
    spritesDelJuego.add(fruta4)

    fruta5 = crearFruta(750,190,30,30)
    listaFruta.add(fruta5)
    spritesDelJuego.add(fruta5)

    fruta3 = crearFruta(279,400,30,30)
    listaFruta.add(fruta3)
    spritesDelJuego.add(fruta3)

    fruta6 = crearFruta(432,400,30,30)
    listaFruta.add(fruta6)
    spritesDelJuego.add(fruta6)

    fruta7 = crearFruta(750,400,30,30)
    listaFruta.add(fruta7)
    spritesDelJuego.add(fruta7)

    fruta8 = crearFruta(900,400,30,30)
    listaFruta.add(fruta8)
    spritesDelJuego.add(fruta8)
    

    return listaFruta
def createAlimentos(spritesDelJuego):
   
    listaAlimentos = pygame.sprite.Group()
   
    alimento1 = crearAlimento(200,120,5,5)
    listaAlimentos.add(alimento1)
   
    spritesDelJuego.add(alimento1)

    alimento2 = crearAlimento(275,120,5,5)
    listaAlimentos.add(alimento2)
   
    spritesDelJuego.add(alimento2)

    alimento3 = crearAlimento(355,120,5,5)
    listaAlimentos.add(alimento3)
   
    spritesDelJuego.add(alimento3)

    alimento4 = crearAlimento(433,120,5,5)
    listaAlimentos.add(alimento4)
   
    spritesDelJuego.add(alimento4)

    alimento5 = crearAlimento(520,120,5,5)
    listaAlimentos.add(alimento5)
   
    spritesDelJuego.add(alimento5)

    alimento6 = crearAlimento(595,190,5,5)
    listaAlimentos.add(alimento6)
   
    spritesDelJuego.add(alimento6)

    alimento7 = crearAlimento(595,120,5,5)
    listaAlimentos.add(alimento7)
   
    spritesDelJuego.add(alimento7)

    alimento8 = crearAlimento(680,120,5,5)
    listaAlimentos.add(alimento8)
   
    spritesDelJuego.add(alimento8)

    alimento9 = crearAlimento(750,120,5,5)
    listaAlimentos.add(alimento9)
   
    spritesDelJuego.add(alimento9)

    alimento10 = crearAlimento(830,120,5,5)
    listaAlimentos.add(alimento10)
   
    spritesDelJuego.add(alimento10)

    alimento11 = crearAlimento(910,120,5,5)
    listaAlimentos.add(alimento11)
   
    spritesDelJuego.add(alimento11)

    alimento12 = crearAlimento(990,120,5,5)
    listaAlimentos.add(alimento12)
   
    spritesDelJuego.add(alimento12)

    alimento13 = crearAlimento(1070,120,5,5)
    listaAlimentos.add(alimento13)
   
    spritesDelJuego.add(alimento13)




    alimento14 = crearAlimento(200,300,5,5)
    listaAlimentos.add(alimento14)
   
    spritesDelJuego.add(alimento14)

    alimento15 = crearAlimento(275,300,5,5)
    listaAlimentos.add(alimento15)
   
    spritesDelJuego.add(alimento15)

    alimento16 = crearAlimento(355,300,5,5)
    listaAlimentos.add(alimento16)
   
    spritesDelJuego.add(alimento16)

    alimento17 = crearAlimento(433,300,5,5)
    listaAlimentos.add(alimento17)
   
    spritesDelJuego.add(alimento17)

    alimento18 = crearAlimento(520,300,5,5)
    listaAlimentos.add(alimento18)
   
    spritesDelJuego.add(alimento18)

    alimento19 = crearAlimento(595,300,5,5)
    listaAlimentos.add(alimento19)
   
    spritesDelJuego.add(alimento19)

    alimento20 = crearAlimento(595,300,5,5)
    listaAlimentos.add(alimento20)
   
    spritesDelJuego.add(alimento20)

    alimento21 = crearAlimento(680,300,5,5)
    listaAlimentos.add(alimento21)
   
    spritesDelJuego.add(alimento21)

    alimento22 = crearAlimento(750,300,5,5)
    listaAlimentos.add(alimento22)
   
    spritesDelJuego.add(alimento22)

    alimento23 = crearAlimento(830,300,5,5)
    listaAlimentos.add(alimento23)
   
    spritesDelJuego.add(alimento23)

    alimento24 = crearAlimento(910,300,5,5)
    listaAlimentos.add(alimento24)
   
    spritesDelJuego.add(alimento24)

    alimento25 = crearAlimento(990,300,5,5)
    listaAlimentos.add(alimento25)
   
    spritesDelJuego.add(alimento25)

    alimento26 = crearAlimento(1070,300,5,5)
    listaAlimentos.add(alimento26)
   
    spritesDelJuego.add(alimento26)



    alimento27 = crearAlimento(200,480,5,5)
    listaAlimentos.add(alimento27)
   
    spritesDelJuego.add(alimento27)

    alimento28 = crearAlimento(275,480,5,5)
    listaAlimentos.add(alimento28)
   
    spritesDelJuego.add(alimento28)

    alimento29 = crearAlimento(355,480,5,5)
    listaAlimentos.add(alimento29)
   
    spritesDelJuego.add(alimento29)

    alimento30 = crearAlimento(433,480,5,5)
    listaAlimentos.add(alimento30)
   
    spritesDelJuego.add(alimento30)

    alimento31 = crearAlimento(520,480,5,5)
    listaAlimentos.add(alimento31)
   
    spritesDelJuego.add(alimento31)

    alimento32 = crearAlimento(595,480,5,5)
    listaAlimentos.add(alimento32)
   
    spritesDelJuego.add(alimento32)

    alimento33 = crearAlimento(595,480,5,5)
    listaAlimentos.add(alimento33)
   
    spritesDelJuego.add(alimento33)

    alimento34 = crearAlimento(680,480,5,5)
    listaAlimentos.add(alimento34)
   
    spritesDelJuego.add(alimento34)

    alimento35 = crearAlimento(750,480,5,5)
    listaAlimentos.add(alimento35)
   
    spritesDelJuego.add(alimento35)

    alimento36 = crearAlimento(830,480,5,5)
    listaAlimentos.add(alimento36)
   
    spritesDelJuego.add(alimento36)

    alimento37 = crearAlimento(910,480,5,5)
    listaAlimentos.add(alimento37)
   
    spritesDelJuego.add(alimento37)

    alimento38 = crearAlimento(990,480,5,5)
    listaAlimentos.add(alimento38)
   
    spritesDelJuego.add(alimento38)

    alimento39 = crearAlimento(1070,480,5,5)
    listaAlimentos.add(alimento39)
   
    spritesDelJuego.add(alimento39)
   
   
    
    return listaAlimentos

def colisionAlimento(protagonista,alimentos,PUNTO):
    lista_impactos_alimentos = pygame.sprite.spritecollide(protagonista, alimentos, True)
    for colision in lista_impactos_alimentos:
        PUNTO+=25
        pacmanComeBola = pygame.mixer.Sound("pacmancome.wav")

        pygame.mixer.Sound.play(pacmanComeBola)   
    return PUNTO

def colisionFantasmasPacmanVidaMenos(protagonista, fantasma):


    lista_impactos_fantasmasPacman = pygame.sprite.collide_rect(protagonista, fantasma)

    

    if lista_impactos_fantasmasPacman:

        protagonista.rect.x = 50

        protagonista.rect.y = 50

        protagonista.velocidad_x = 0

        protagonista.velocidad_y = 0

    return lista_impactos_fantasmasPacman

def cambioVelocidadProtagonista(protagonista, x, y):
    protagonista.velocidad_x += x
    protagonista.velocidad_y += y
    
def cambioVelocidadFantasma(fantasma,x,y):
    fantasma.velocidad_x += x*0.008
    fantasma.velocidad_y += y*0.008

def updateProtagonista(protagonista, paredes):
   
    protagonista.rect.x += protagonista.velocidad_x
   
    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, paredes, False)
    for bloque in lista_impactos_bloques:
       
        if protagonista.velocidad_x <= 0:
           
            protagonista.rect.left = bloque.rect.right
       
        else:
           
            protagonista.rect.right = bloque.rect.left
   
    protagonista.rect.y += protagonista.velocidad_y
   
    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, paredes, False)
    for bloque in lista_impactos_bloques:
       
        if protagonista.velocidad_y <= 0:
           
            protagonista.rect.top = bloque.rect.bottom
       
        else:
           
            protagonista.rect.bottom = bloque.rect.top

def updateFantasma(fantasma, paredes):
   
    fantasma.rect.x += fantasma.velocidad_x
   
    lista_impactos_bloques = pygame.sprite.spritecollide(fantasma, paredes, False)
    for bloque in lista_impactos_bloques:
       
        if fantasma.velocidad_x <= 0:
           
            fantasma.rect.left = bloque.rect.right

        else:
           
            fantasma.rect.right = bloque.rect.left
            
        fantasma.velocidad_x = -fantasma.velocidad_x
   
    fantasma.rect.y += fantasma.velocidad_y
   
    lista_impactos_bloques = pygame.sprite.spritecollide(fantasma, paredes, False)
    for bloque in lista_impactos_bloques:
       
        if fantasma.velocidad_y <= 0:
           
            fantasma.rect.top = bloque.rect.bottom
            
        else:
           
            fantasma.rect.bottom = bloque.rect.top

        fantasma.velocidad_y = -fantasma.velocidad_y
            
def gestionarEventos(protagonista, isRunning):
   
    for evento in pygame.event.get():


        if evento.type == pygame.QUIT:
           
            isRunning = False
        if evento.type == pygame.KEYDOWN:


            if evento.key == pygame.K_LEFT:
                cambioVelocidadProtagonista(protagonista, -6,0)
           
            if evento.key == pygame.K_RIGHT:
                cambioVelocidadProtagonista(protagonista, 6,0)


            if evento.key == pygame.K_UP:
                cambioVelocidadProtagonista(protagonista, 0,-6)
            if evento.key == pygame.K_DOWN:
                cambioVelocidadProtagonista(protagonista, 0,6)
        if evento.type == pygame.KEYUP:


            if evento.key == pygame.K_LEFT:
                protagonista.velocidad_x = 0
           
            if evento.key == pygame.K_RIGHT:
                protagonista.velocidad_x = 0


            if evento.key == pygame.K_UP:
                protagonista.velocidad_y= 0
            if evento.key == pygame.K_DOWN:
                protagonista.velocidad_y= 0
           
    return isRunning

def puntuacion(pantalla, PUNTO):
    letra = pygame.font.Font(None, 15).render("Puntuacion: " + str(PUNTO), True, (255,255,255))
    pantalla.blit(letra,[30,10])

def mostrarVidas(pantalla, vidas):

    letra = pygame.font.Font(None, 15).render("Vidas: " + str(vidas), True, (255,255,255))

    pantalla.blit(letra,[30,30])

def gameOver(pantalla):

    pantalla.fill((128,0,128))


    gameOver_texto = pygame.font.Font(None, 50).render("Game Over, PRESS [X] to finish.", True, (0,0,255))
    pacman_muere = pygame.mixer.Sound("pacman-dies.mp3")

    pygame.mixer.Sound.play(pacman_muere)

    text_rect = gameOver_texto.get_rect()

    text_rect.center = (LARGO_PANTALLA // 2, ALTO_PANTALLA // 2)

    pantalla.blit(gameOver_texto, text_rect)
       
    pygame.display.update()

def youWin(pantalla):

    pantalla.fill((128,0,128))


    youWin_texto = pygame.font.Font(None, 50).render("You Win!!!, PRESS [X] to finish.", True, (0,0,255))

    text_rect = youWin_texto.get_rect()

    text_rect.center = (LARGO_PANTALLA // 2, ALTO_PANTALLA // 2)

    pantalla.blit(youWin_texto, text_rect)

def colisionFruta (protagonista,fruta):

    colision_con_fruta = pygame.sprite.spritecollide(protagonista, fruta, True)
    if colision_con_fruta:
        pacmanComeFruta = pygame.mixer.Sound("pacman-siren.mp3")
    

    return colision_con_fruta
    





NEGRO = (0,0,0)
BLANCO = (255,255,255)
AZUL = (0,0,255)


LARGO_PANTALLA = 1200
ALTO_PANTALLA = 600



pygame.init()
pygame.mixer.init()

PUNTO = 0
vidas = 3
sonido_inicio = pygame.mixer.Sound("canciondenicio.wav")
pygame.mixer.Sound.play(sonido_inicio)


pantalla = pygame.display.set_mode([LARGO_PANTALLA, ALTO_PANTALLA])



pygame.display.set_caption('Desplazamiento entre paredes')


spritesDelJuego = pygame.sprite.Group()


protagonista = crearProtagonista(spritesDelJuego, 50, 300)
alimento = createAlimentos(spritesDelJuego)
fruta = createFruta(spritesDelJuego)
fantasma = crearFantasma(spritesDelJuego, 100, 100)



listaParedes = createParedes(spritesDelJuego)


reloj = pygame.time.Clock()


isRunning = True



while isRunning:

    
    if vidas > 0:
     
        isRunning = gestionarEventos(protagonista, isRunning)
        cambioVelocidadFantasma(fantasma,random.randrange(1,2),random.randrange(1,2))   
        updateProtagonista(protagonista, listaParedes)
        aparecerLadoContrario(protagonista)
        updateFantasma(fantasma, listaParedes)
        aparecerLadoContrarioFantasma(fantasma)
        PUNTO=colisionAlimento(protagonista,alimento,PUNTO)
        colisionFruta (protagonista,fruta)
            

        if colisionFantasmasPacmanVidaMenos(protagonista, fantasma):
            vidas=vidas-1
        
        pantalla.fill(NEGRO)
   
        spritesDelJuego.draw(pantalla)
        puntuacion(pantalla, PUNTO)
        mostrarVidas(pantalla,vidas)

     
    elif vidas == 0 or vidas<0:

        gameOver(pantalla)
        fantasma.velocidad_x = 0

        fantasma.velocidad_y = 0

        fantasma.rect.x = 300

        fantasma.rect.y = 100
        for evento in pygame.event.get():


            if evento.type == pygame.QUIT:
           
                isRunning = False
    if PUNTO == 975:
        youWin(pantalla)

        fantasma.velocidad_x = 0

        fantasma.velocidad_y = 0

        fantasma.rect.x = 300


        fantasma.rect.y = 100
        for evento in pygame.event.get():


            if evento.type == pygame.QUIT:
           
                isRunning = False
        

    
    pygame.display.flip()
   
    reloj.tick(60)


pygame.quit()


