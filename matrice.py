import random

dictio = "azertyuiopqsdfghjkl mwxcvbn1234567890&œé(-è_çà)=*$ù!:;,><?./§%µ£+°@^`|[{#~"
count = random.randint(0,1000)
line = " "
while True: ### As here we have an infinite loop the program will run in a loop on your console.
            ### Do not hesitate to press Ctrl + C to kill the program and thus stop the loop.
    for i in range(count):
        line += (random.choice(dictio))
    print(line)

