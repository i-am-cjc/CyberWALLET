SCREEN Monster Hunger
DELAY 0.5
INC notepad
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
RTYPE As the monster is taking it's last breaths it manages to take a chunk out of Dani who bleeds out within minutes :(
JUMP LEFT_OR_RIGHT
LABEL SHOOT
SCREEN BANG!
RTYPE You grab the gun and hit the monster dead between those bright red eyes. Fading, the eyes close and you live another day.
LABEL LEFT_OR_RIGHT
RTYPE As you stand up, shocked by what's going on you try to see where you can escape this nightmarish hell...
LABEL MAIN_CORRIDOR
RTYPE You walk down the corridor and you can go either right or left (Use the right and left buttons)
BJUMP LEFT_CORRIDOR
LABEL RIGHT_CORRIDOR
VJUMP HAS_LAMP RIGHT_CORRIDOR_MAIN
RTYPE You're in a dead end but you can see a Lamp. 
RTYPE Left Button to GET LAMP or right button to leave
BJUMP GET_LAMP
LABEL RIGHT_CORRIDOR_MAIN
RTYPE You're in a dead end, there is nothing here.
RTYPE Press Left to do nothing or Right to go back
BJUMP RIGHT_CORRIDOR_MAIN
JUMP MAIN_CORRIDOR
LABEL GET_LAMP
RTYPE You get the lamp and suddenly the corridor isn't scary anymore and you can see!
SET HAS_LAMP
JUMP RIGHT_CORRIDOR_MAIN
LABEL LEFT_CORRIDOR
VJUMP HAS_LAMP LEFT_CORRIDOR_LIGHT
RTYPE It's dark here, you can't see anything, you head back to the way you came to try another way
JUMP MAIN_CORRIDOR
LABEL LEFT_CORRIDOR_LIGHT
RTYPE Heading down here with the lamp you can see the light at the end of the tunnel.
RTYPE You escape from this nightmare and go back to bed.
LABEL GAME_OVER
SCREEN Game Over
RTYPE Thanks for playing Monster Hunger 1.2
SLEEP 5