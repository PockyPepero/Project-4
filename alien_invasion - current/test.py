import time, sys
from pygame import mixer

mixer.init()

sound = mixer.Sound('laser.wav')
sound.play()

time.sleep(5)