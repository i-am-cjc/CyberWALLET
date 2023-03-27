SCREEN Monster Hunger
DELAY 0.5
MOD4
SLEEP 1
RTYPE notepad
SLEEP 1
SCREEN Breakfast
RTYPE You're just enjoying a Full English Breakfast at the local diner.
RTYPE As you're paying you see a sign that says @Tips Optional@.
RTYPE Press the left button to leave a tip, or the right to leave.
BJUMP JUST_THE_TIP
RTYPE You walk away without leaving a tip and head to work
JUMP BED
LABEL JUST_THE_TIP
RTYPE You leave a few coins in the tip jar, Dani the shop owner thanks you as you leave for work.
SET TIP
LABEL BED
RTYPE You go to bed, after a long day of work.
RTYPE You awaken in a dark cave, a pistol sits besides you looking to be locked and loaded.
RTYPE A growling in the distance grows louder and louder, and 2 red glowing eyes getting larger and larger...
RTYPE You realise you have two choices:
RTYPE Left Button: Grab the Pistol and Shoot the monster...
RTYPE Right Button: Sit there and hope it's friendly...
RTYPE Choose your action: 
BJUMP SHOOT
RTYPE You choose not to shoot, the eyes get larger and the growling louder. 
VJUMP TIP SAVED
SCREEN UR DED M8
RTYPE You were eaten by the Monster
JUMP GAME_OVER
LABEL SAVED
SCREEN KARMA IS A BITCH
RTYPE Suddenly, Dani appears from the darkness and grabs the gun, shooting the monster and saving your life.
JUMP GAME_OVER
LABEL SHOOT
SCREEN BANG!
RTYPE You grab the gun and hit the monster dead between those bright red eyes. Fading, the eyes close and you live another day.
LABEL GAME_OVER
SCREEN Game Over
RTYPE Thanks for playing Monster Hunger 1.2
SLEEP 5