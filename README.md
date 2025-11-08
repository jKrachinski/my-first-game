# Asteroids Game

A classic Asteroids arcade game clone built with Python and Pygame.

## 📝 Description

This is a Python implementation of the classic Asteroids arcade game. Control a spaceship, shoot asteroids, and survive as long as possible! When asteroids are hit, they split into smaller pieces, increasing the challenge.

## 🎮 Features

- **Player spaceship** with rotation and movement controls
- **Shooting mechanics** with cooldown system
- **Asteroid splitting** - larger asteroids break into smaller ones when destroyed
- **Collision detection** between player, shots, and asteroids
- **Game over** condition when player collides with an asteroid
- **Smooth animations** running at 60 FPS
- **Object-oriented design** with reusable base classes

## 🕹️ Controls

- **W** - Move forward
- **S** - Move backward
- **A** - Rotate left
- **D** - Rotate right
- **SPACE** - Shoot

## 🏗️ Project Structure

- `main.py` - Main game loop and initialization
- `player.py` - Player spaceship class with movement and shooting
- `asteroid.py` - Asteroid class with splitting logic
- `asteroidfield.py` - Manages asteroid spawning
- `shoot.py` - Projectile/bullet class
- `circleshape.py` - Base class for circular game objects
- `constants.py` - Game configuration and constants

## 🚀 Installation

This project uses `uv` for dependency management. Make sure you have Python 3.12+ installed.

```bash
# Install dependencies
uv sync

# Run the game
python main.py
```

## 🎯 Game Mechanics

- **Screen size**: 1280x720
- **Asteroid spawning**: New asteroids spawn periodically from the edges
- **Shot cooldown**: 0.3 seconds between shots
- **Asteroid splitting**: Asteroids split into two smaller asteroids when hit (minimum radius: 20)
- **Victory condition**: Survive and destroy all asteroids (game continues with new spawns)

## 🛠️ Technologies

- **Python 3.12+**
- **Pygame 2.6.1** - Game engine and graphics

## 📄 License

This project is open source and available for educational purposes.
