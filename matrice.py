import random

dictio = "azertyuiopqsdfghjkl mwxcvbn1234567890&œé(-è_çà)=*$ù!:;,><?./§%µ£+°@^`|[{#~"
count = random.randint(0,1000)
line = " "
while True:
    for i in range(count):
        line += (random.choice(dictio))
    print(line)

