# pip install pyfiglet

import pyfiglet

for i in range(20):
    text = input("enter a text")
    font = (pyfiglet.figlet_format(text))
    print(font)
