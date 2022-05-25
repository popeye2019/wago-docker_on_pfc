import os

#Detecting operating system 
if(os.name == 'nt') :      #windows
    os.system('cls')          #clear terminal screen

elif(os.name == 'posix'):  #linux
    os.system('clear')          #clear terminal screen

#Main program
print("Hello world! This program is running!! :)")

name = input("What's your name my friend? ")

print(f'Hello {name}, I hope you learn something from this tutorial :)')

print("This program has ended...")