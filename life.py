import pygame
import time
import numpy as np

# Initializing Colors (using a black and blue theme here, others are included in patterns.py)
background = (10, 10, 40)
grid = (30, 30, 60)
nextDeath = (200, 200, 225)
nextAlive = (255, 255, 215)


# Game Rules
def update(screen, cells, size, progress=False):
    updatedCells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, column in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, column-1:column+2]) - cells[row, column]
        color = background if cells[row, column] == 0 else nextAlive

        if cells[row, column] == 1:
            if alive < 2 or alive > 3:
                if progress:
                    color = nextDeath

            elif 2 <= alive <= 3:
                updatedCells[row, column] = 1
                if progress:
                    color = nextAlive

        else:
            if alive == 3:
                updatedCells[row, column] = 1

                if progress:
                    color = nextAlive

        
        pygame.draw.rect(screen, color, (column * size, row * size, size-1, size-1))

    return updatedCells


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((60, 80))
    screen.fill(grid)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running 
                    update(screen, cells, 10)

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(grid)

        if running:
            cells = update(screen, cells, 10, progress=True)
            pygame.display.update()


        time.sleep(0.001)

if __name__ == '__main__':
    main()






