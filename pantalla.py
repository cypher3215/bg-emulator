import pygame
import numpy as np
import time

# Inicializar pygame
pygame.init()

# Dimensiones de la pantalla de la Game Boy
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 144

# Crear la ventana de Pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Emulador Game Boy")

# Colores (simulados para Game Boy: blanco y negro, pero puedes agregar más si lo deseas)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clase para manejar la "pantalla" de la Game Boy
class GameBoyScreen:
    def __init__(self):
        # Inicializar la pantalla con píxeles blancos
        self.pixels = np.ones((SCREEN_HEIGHT, SCREEN_WIDTH, 3), dtype=np.uint8) * 255  # Fondo blanco
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    def update_screen(self):
        # Convertir el arreglo de píxeles a una imagen de Pygame
        pygame.surfarray.blit_array(self.surface, self.pixels)
        screen.blit(self.surface, (0, 0))  # Dibujar en la ventana principal

    def set_pixel(self, x, y, color):
        """Poner un píxel en la posición (x, y) con un color"""
        self.pixels[y, x] = color

# Función principal para ejecutar la emulación
def main():
    running = True
    gameboy_screen = GameBoyScreen()  # Crear objeto de la pantalla

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Simulación de un juego: cambiamos algunos píxeles de ejemplo
        for y in range(50, 100):
            for x in range(50, 100):
                # Vamos a cambiar algunos píxeles a negro, simulando algo en la pantalla
                gameboy_screen.set_pixel(x, y, BLACK)

        # Actualizar la pantalla
        gameboy_screen.update_screen()

        # Actualizar la ventana de Pygame
        pygame.display.flip()

        # Simulación de retraso (esto es solo para no ir demasiado rápido)
        time.sleep(0.01)

    pygame.quit()

if __name__ == "__main__":
    main()
