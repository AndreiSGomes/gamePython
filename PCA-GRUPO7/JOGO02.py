import pygame # importei o pygame
pygame.init() # iniciando o pygame
x = 400 #quando começar o jogo ela vai começar no centro
y = 300 #quando começar o jogo ela vai começar no centro
velocidade = 20 # velocidade de 5px
fundo = pygame.image.load('fundo1.jpg') #carregando a imagem de fundo
personagem = pygame.image.load('Personagem02.png')

janela = pygame.display.set_mode((800,600)) #Criei a janela
pygame.display.set_caption("War C-19") #NOME DA JOGO NA TELA

janela_aberta = True
while janela_aberta: #Deixando a janela aberta
    pygame.time.delay(50) #para aparacer o objeto e atualizar tudo

    for event in pygame.event.get(): #Deixando a janela aberta e fechando quando apertar o x
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed() # Quando for pressionado uma tecla di teclado
    if comandos [pygame.K_UP]: #botão de cima W
        y-= velocidade  # Quado for aperta a tecla de cima do teclado a imagem vai 5px pra frente
    if comandos[pygame.K_DOWN]: #Tras
        y+= velocidade
    if comandos[pygame.K_RIGHT]: # Direita X+= DIREITA
        x+= velocidade
    if comandos[pygame.K_LEFT]: # Frente X-=ESQUERDA
        x-= velocidade  # todos os if precisam está identado com o aliamento for para deixar a tecla aperta e saltar quantos px for necessario




    janela.blit(fundo, (0,0)) #colando a imagem, começando do canto 0 e indo até o final ponta a ponta
    janela.blit(personagem, (x,y))

    #pygame.draw.circle(janela, (0,255,85),(x,y),50) #objeto vai aparecer na janela, é a cor do objeto, o proxmo é a posição primeiro x depois y, o proximo é o tamanho do objeto 50px
    pygame.display.update() # atualizar a tela após o desenhi


    #pygame.quit()

asasa