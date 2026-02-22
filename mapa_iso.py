import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración
ANCHO, ALTO = 800, 600
TILE_WIDTH = 64
TILE_HEIGHT = 32
MAP_WIDTH = 10
MAP_HEIGHT = 10
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mapa Isométrico Pygame")
clock = pygame.time.Clock()

# Función para coordenadas isométricas
def cart_to_iso(x, y):
    iso_x = (x - y) * TILE_WIDTH // 2
    iso_y = (x + y) * TILE_HEIGHT // 2
    return iso_x + ANCHO // 2, iso_y + ALTO // 4  # Offset para centrar

# Crear tile surface coloreado (procedural)
def crear_tile(color):
    tile = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
    tile.fill(color)
    return pygame.transform.rotate(tile, 45)  # Rotar para isométrico

# Mapa de ejemplo (0=agua, 1=pasto, 2=tierra)
mapa = [
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 2],
    [1, 0, 0, 0, 1, 1, 1, 2, 2, 2],
    [0, 0, 1, 1, 1, 0, 0, 1, 2, 2],
    [0, 1, 1, 2, 2, 0, 1, 1, 1, 2],
    [1, 1, 2, 2, 2, 1, 1, 0, 0, 1],
    [2, 2, 2, 1, 1, 1, 0, 0, 1, 1],
    [1, 2, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 1, 2, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 2, 0, 1, 1, 0, 1, 1]
]

tiles = {
    0: crear_tile((0, 100, 200)),  # Agua
    1: crear_tile((0, 200, 100)),  # Pasto
    2: crear_tile((150, 100, 50))  # Tierra
}

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((50, 50, 100))  # Fondo cielo

    # Dibujar tiles en orden inverso para profundidad (de fondo a frente)
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH - 1, -1, -1):  # Orden Z para isométrico
            tile_type = mapa[y][x]
            iso_x, iso_y = cart_to_iso(x, y)
            screen.blit(tiles[tile_type], (iso_x, iso_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
