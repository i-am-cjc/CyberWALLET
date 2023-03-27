SCREEN Monster Hunger
DELAY 0.5
MOD4
SLEEP 1
RTYPE notepad
SLEEP 1
SCREEN GO HUNT!
RTYPE You awaken in a dark cave, a pistol sits besides you looking to be locked and loaded.
RTYPE A growling in the distance grows louder and louder, and 2 red glowing eyes getting larger and larger...
RTYPE You realise you have two choices:
RTYPE Left Button: Grab the Pistol and Shoot the monster...
RTYPE Right Button: Sit there and hope it's friendly...
RTYPE Choose your action: 
BJUMP SHOOT
RTYPE You choose not to shoot, the eyes get larger and the growling louder. 
SCREEN UR DED M8
RTYPE You were eaten by the Monster
JUMP GAME_OVER
LABEL SHOOT
SCREEN BANG!
RTYPE You grab the gun and hit the monster dead between those bright red eyes. Fading, the eyes close and you live another day.
LABEL GAME_OVER
SCREEN Game Over
RTYPE Thanks for playing Monster Hunger 1.2
SLEEP 5