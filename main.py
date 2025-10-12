import pygame
from constants import *
import player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock_game = pygame.time.Clock()
    dt = 0
    
    main_player = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        screen.fill("Black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        main_player.draw(screen)
        main_player.update(dt)
        
        pygame.display.flip()
        dt = clock_game.tick(60)/1000
        
        


if __name__ == "__main__":
    main()
