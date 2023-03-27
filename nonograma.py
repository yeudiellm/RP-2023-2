#Como paso 1 debemos instalar pygame
#Para instalar podemos entrar a la consola del ambiente donde vamos a trabajar y ejecutar sig comando --> pip install pygame
import pygame

# define el tamaño de la ventana
WIDTH, HEIGHT = 600, 600

# define los colores que se utilizarán en RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# define la matriz que representa el nonograma
nonogram = [
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
]#Calaca

# define una función para dibujar la cuadrícula del nonograma
def draw_grid():
    for i in range(13):
        ## Este código utiliza la biblioteca Pygame para dibujar una línea recta en la pantalla. Aquí está lo que significa cada parte del código:
        ##pygame.draw.line: Esta es la función en la biblioteca Pygame que dibuja una línea.
        ##screen: Esta es la superficie en la que se dibujará la línea. Puede ser toda la ventana o una porción más pequeña de ella.
        ##GRAY: Este es el color de la línea. Puede ser cualquier valor de color válido en Pygame, como una tupla RGB o una constante de color.
        ##(i * 50, 0): Este es el punto de partida de la línea. El primer valor en la tupla es la coordenada x, y el segundo valor es la coordenada y. En este caso, la coordenada x se determina multiplicando la variable del bucle i por 50, y la coordenada y es 0 (es decir, la parte superior de la pantalla).
        ##(i * 50, 600): Este es el punto final de la línea. La coordenada x es la misma que la del punto de partida, y la coordenada y es 600 (es decir, la parte inferior de la pantalla).
        ##En general, este código dibuja una serie de líneas verticales a intervalos de 50 píxeles en la pantalla, desde la parte superior hasta la inferior. El número de líneas dibujadas depende del valor de i en el bucle circundante.
        pygame.draw.line(screen, GRAY, (i * 50, 0), (i * 50, 600)) 
        pygame.draw.line(screen, GRAY, (0, i * 50), (600, i * 50))

# define una función para dibujar el nonograma
def draw_nonogram():
    for i in range(12):
        for j in range(12):
            if nonogram[i][j] == 1:
                pygame.draw.rect(screen, BLACK, (j * 50, i * 50, 50, 50))
            elif nonogram[i][j] == 2:
                pygame.draw.rect(screen, RED, (j * 50, i * 50, 50, 50))

# define una función para verificar si se ha resuelto el nonograma
def check_nonogram():
    for i in range(10):
        for j in range(12):
            if nonogram[i][j] == 1:
                return False
    return True

# inicializa Pygame
pygame.init()

# crea la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# establece el título de la ventana
pygame.display.set_caption("Nonograma")

# crea la superficie de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# define un bucle para mantener la ventana abierta
running = True
while running:

    # maneja los eventos de Pygame
    for event in pygame.event.get():  ##Escucha del evento presente
        if event.type == pygame.QUIT:  ##Verifica que esté abierto el juego
            running = False
            ##Este bloque de código maneja el evento de clic del mouse (MOUSEBUTTONDOWN). Si el usuario hace clic en la ventana del juego, la posición del cursor 
            # se obtiene mediante pygame.mouse.get_pos() y se almacena en x e y. Luego, se calcula la fila y columna correspondientes a la posición del cursor dividiendo las coordenadas por 50. 
            # Estos valores se utilizan para actualizar la matriz nonogram según el valor actual en esa posición. Si el valor actual es 1, se cambia a 2 y viceversa.
            #En general, este código maneja la entrada del usuario en el juego y actualiza la matriz nonogram según las acciones del usuario.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // 50, x // 50
            if nonogram[row][col] == 1:
                nonogram[row][col] = 2
            else:
                nonogram[row][col] = 1
           

    # dibuja la cuadrícula y el nonograma
    screen.fill(WHITE) ## Llena de blanco
    draw_grid() ## Dibuja la cuadricula
    draw_nonogram() ## Llena el nonograma

    # verifica si se ha resuelto el nonograma
    if check_nonogram():
        font = pygame.font.SysFont(None, 100)
        text = font.render("¡GANASTE!", True, BLACK)
        screen.blit(text, (100, 250))

    # actualiza la pantalla
    pygame.display.flip()

# cierra Pygame
pygame.quit()

