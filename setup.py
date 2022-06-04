# Generator for Discord Nitro

from random import randint, random, randrange
import time


print("""
███╗░░██╗██╗████████╗██████╗░░█████╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░
""")
time.sleep(2)
print("Creator - SK423D")
time.sleep(2)

print("Unlimited code generation, stop code to stop generation")
time.sleep(3)

t = 10
l_min = (65, 90)
l_maj = (97, 122)
digits = (48, 57)

while True :

    r = ""
    for i in range(16):
        u = randrange(0, 3)
        if u == 0:
            r += chr(randint(l_min[0], l_min[1]))
        elif u == 1:
            r += chr(randint(l_maj[0], l_maj[1]))
        else:
            r += chr(randint(digits[0], digits[1]))
    print("https://discord.gift/" + r)

    with open("Nitro.txt", "a+") as nitrofile:
        nitrofile.write("[UNCHECKED] " + f"https://discord.gift/{r}\n")

        nitrofile.close()