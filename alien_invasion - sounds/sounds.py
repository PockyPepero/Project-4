import time, sys
from pygame import mixer

mixer.init()

class Sounds():
    """A class to manage the sounds for the game."""

    def __init__(self, ai_game):
        """Initialize the sounds for the game."""
        
    def _play_laser(self):
        laser_sound = mixer.Sound('laser.wav')
        laser_sound.play()

    def _play_bg_music(self):
        bg_music = mixer.Sound('bg_music.wav')
        bg_music.play(-1)

    def _play_collision(self):
        collision_sound = mixer.Sound('collision.wav')
        collision_sound.play()
        
