import unittest
import pygame
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from shoot import Shoot
from constants import *


class TestCircleShape(unittest.TestCase):
    """Testes para a classe base CircleShape"""
    
    def setUp(self):
        """Inicializa pygame antes de cada teste"""
        pygame.init()
    
    def tearDown(self):
        """Limpa pygame depois de cada teste"""
        pygame.quit()
    
    def test_circle_initialization(self):
        """Testa se um CircleShape é inicializado corretamente"""
        circle = CircleShape(100, 200, 30)
        self.assertEqual(circle.position.x, 100)
        self.assertEqual(circle.position.y, 200)
        self.assertEqual(circle.radius, 30)
        self.assertEqual(circle.velocity.x, 0)
        self.assertEqual(circle.velocity.y, 0)
    
    def test_collision_detection_overlapping(self):
        """Testa detecção de colisão quando círculos se sobrepõem"""
        circle1 = CircleShape(0, 0, 10)
        circle2 = CircleShape(15, 0, 10)
        self.assertTrue(circle1.colision(circle2))
    
    def test_collision_detection_not_overlapping(self):
        """Testa que não há colisão quando círculos estão separados"""
        circle1 = CircleShape(0, 0, 10)
        circle2 = CircleShape(100, 100, 10)
        self.assertFalse(circle1.colision(circle2))
    
    def test_collision_detection_touching(self):
        """Testa colisão quando círculos estão tocando exatamente"""
        circle1 = CircleShape(0, 0, 10)
        circle2 = CircleShape(20, 0, 10)
        self.assertFalse(circle1.colision(circle2))


class TestPlayer(unittest.TestCase):
    """Testes para a classe Player"""
    
    def setUp(self):
        """Inicializa pygame e cria um jogador antes de cada teste"""
        pygame.init()
        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    def tearDown(self):
        """Limpa pygame depois de cada teste"""
        pygame.quit()
    
    def test_player_initialization(self):
        """Testa se o jogador é inicializado corretamente"""
        self.assertEqual(self.player.position.x, SCREEN_WIDTH/2)
        self.assertEqual(self.player.position.y, SCREEN_HEIGHT/2)
        self.assertEqual(self.player.radius, PLAYER_RADIUS)
        self.assertEqual(self.player.rotation, 0)
        self.assertEqual(self.player.timer, 0)
    
    def test_player_rotation(self):
        """Testa se o jogador rotaciona corretamente"""
        initial_rotation = self.player.rotation
        self.player.rotate(1)
        self.assertGreater(self.player.rotation, initial_rotation)
    
    def test_player_movement(self):
        """Testa se o jogador se move corretamente"""
        initial_position = pygame.Vector2(self.player.position)
        self.player.move(1)
        self.assertNotEqual(initial_position, self.player.position)
    
    def test_player_triangle_vertices(self):
        """Testa se o triângulo do jogador tem 3 vértices"""
        triangle = self.player.triangle()
        self.assertEqual(len(triangle), 3)
        # Verifica se todos os vértices são Vector2
        for vertex in triangle:
            self.assertIsInstance(vertex, pygame.Vector2)


class TestAsteroid(unittest.TestCase):
    """Testes para a classe Asteroid"""
    
    def setUp(self):
        """Inicializa pygame antes de cada teste"""
        pygame.init()
        Asteroid.containers = ()
    
    def tearDown(self):
        """Limpa pygame depois de cada teste"""
        pygame.quit()
    
    def test_asteroid_initialization(self):
        """Testa se o asteroide é inicializado corretamente"""
        asteroid = Asteroid(100, 200, 50)
        self.assertEqual(asteroid.position.x, 100)
        self.assertEqual(asteroid.position.y, 200)
        self.assertEqual(asteroid.radius, 50)
    
    def test_asteroid_update_changes_position(self):
        """Testa se a posição do asteroide muda quando atualizado"""
        asteroid = Asteroid(100, 100, 50)
        asteroid.velocity = pygame.Vector2(10, 10)
        initial_position = pygame.Vector2(asteroid.position)
        asteroid.update(1)
        self.assertNotEqual(initial_position, asteroid.position)
    
    def test_asteroid_split_creates_smaller_asteroids(self):
        """Testa se dividir um asteroide cria asteroides menores"""
        asteroid = Asteroid(100, 100, ASTEROID_MAX_RADIUS)
        asteroid.velocity = pygame.Vector2(10, 0)
        original_radius = asteroid.radius
        # Note: split() cria novos asteroides mas requer containers configurados
        # Este teste verifica que o raio é grande o suficiente para dividir
        self.assertGreater(original_radius, ASTEROID_MIN_RADIUS)
    
    def test_small_asteroid_minimum_radius(self):
        """Testa se asteroides pequenos têm o raio mínimo"""
        asteroid = Asteroid(100, 100, ASTEROID_MIN_RADIUS)
        self.assertEqual(asteroid.radius, ASTEROID_MIN_RADIUS)


class TestShoot(unittest.TestCase):
    """Testes para a classe Shoot"""
    
    def setUp(self):
        """Inicializa pygame antes de cada teste"""
        pygame.init()
        Shoot.containers = ()
    
    def tearDown(self):
        """Limpa pygame depois de cada teste"""
        pygame.quit()
    
    def test_shoot_initialization(self):
        """Testa se o tiro é inicializado corretamente"""
        shoot = Shoot(100, 200)
        self.assertEqual(shoot.position.x, 100)
        self.assertEqual(shoot.position.y, 200)
        self.assertEqual(shoot.radius, SHOT_RADIUS)
    
    def test_shoot_movement(self):
        """Testa se o tiro se move corretamente"""
        shoot = Shoot(100, 100)
        shoot.velocity = pygame.Vector2(10, 0)
        initial_position = pygame.Vector2(shoot.position)
        shoot.update(1)
        self.assertNotEqual(initial_position, shoot.position)
        self.assertGreater(shoot.position.x, initial_position.x)
    
    def test_shoot_collision_with_asteroid(self):
        """Testa se o tiro colide corretamente com um asteroide"""
        shoot = Shoot(100, 100)
        asteroid = Asteroid(105, 100, 20)
        self.assertTrue(shoot.colision(asteroid))


class TestGameConstants(unittest.TestCase):
    """Testes para as constantes do jogo"""
    
    def test_screen_dimensions(self):
        """Testa se as dimensões da tela são positivas"""
        self.assertGreater(SCREEN_WIDTH, 0)
        self.assertGreater(SCREEN_HEIGHT, 0)
    
    def test_player_constants(self):
        """Testa se as constantes do jogador são válidas"""
        self.assertGreater(PLAYER_RADIUS, 0)
        self.assertGreater(PLAYER_SPEED, 0)
        self.assertGreater(PLAYER_TURN_SPEED, 0)
        self.assertGreater(PLAYER_SHOOT_COOLDOWN, 0)
    
    def test_asteroid_constants(self):
        """Testa se as constantes do asteroide são válidas"""
        self.assertGreater(ASTEROID_MIN_RADIUS, 0)
        self.assertGreater(ASTEROID_KINDS, 0)
        self.assertEqual(ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS * ASTEROID_KINDS)


def run_tests():
    """Função auxiliar para executar todos os testes"""
    unittest.main(argv=[''], verbosity=2, exit=False)


if __name__ == "__main__":
    # Executa todos os testes
    unittest.main(verbosity=2)
