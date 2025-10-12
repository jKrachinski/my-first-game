import pygame
from constants import *
import player
import asteroid
from asteroidfield import AsteroidField
from shoot import Shoot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    clock_game = pygame.time.Clock()
    dt = 0
    player.Player.containers = (updatable, drawable) # tem que ser definido antes de qualquer objeto da classe
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shoot.containers = (shots, updatable, drawable)
    
    main_player = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()
    
    
    while True:
        screen.fill("Black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        for element in asteroids:
            if main_player.colision(element):
                print("GAME OVER!")
                return
        
        #drawable.draw(screen)
        for element in drawable:
            element.draw(screen)
        
        
        pygame.display.flip()
        dt = clock_game.tick(60)/1000
        
        


if __name__ == "__main__":
    main()
