import random
import time
from rich.console import Console


if __name__ == "__main__":
    console = Console()
    dictio = "azertyuiopqsdfghjkl mwxcvbn1234567890&œé(-è_çà)=*$ù!:;,><?./§%µ£+°@^`|[{#~"
    line = " "
    space ="  "
    col = int(input("Choose a number between 0 and 255 for the color, if u choose 0 it's rainbow   "))
    speed = int(input("Choose ur speed 0 : very slow, 1 : slow and 2 : fast as fuck boiiiiiii "))
    rainbow = False


### Ici est gérer l'option rainbow ###

if col == 0 :
    rainbow = True

### Ici est gérer la vitesse ###

if speed == 0 :
    speed = 0.5
elif speed == 1 :
    speed = 0.03
elif speed == 2:
    speed = 0
else : 
    print("Wrong Values")



while True:
    time.sleep(speed)
    count = random.randint(200,500)
    for i in range(count):
        line += random.randint(0,2)*space + (random.choice(dictio)) #Génération de la ligne de char avec des espaces
    if rainbow == True : ### Rainbow color choice ###
        console.print(line, style = "color({})".format(random.randint(1,255)), highlight = False) 
    else :
        console.print(line, style = "color({})".format(col), highlight = False)
    line = " "
     


