from time import sleep
from player import Player


sleep(5)
print("Start Maplestory Bot!")
player = Player()

try:
    while True:
        player.autoAttack()
except Exception as e:
    player.log(e)
    pass