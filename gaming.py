#1:input
game = input ("enter the games name:")
console = input ("enter the consoles name:")
country_region = input ("enter where you live:")
#2:game=if,elif,else statement
if game == "TETRIS":
    message = "Tetris is at number 11th spot that is a connecting game"
    print(message)
elif game == "FINAL FANTASY":
    message = "FINAL FANTASY is the 15th biggest and the 38th oldest franchise and it was made in December 18, 1987"
    print(message)
elif game == "SUPER MARIO BROS.":
    message = "SUPER MARIO BROS. is the 9th popular selling game of nintendo it was made in September 13, 1985"
    print(message)
elif game == "MINECRAFT":
    message = "MINECRAFT is the top 1 selling video game in the world"
    print(message)
elif game == "GTA V":
    message = "GTA V is the biggest GTA game of all GTA games released in September 17, 2013"
    print(message)
elif game == "Wii SPORTS":
    message = "Wii SPORTS is the biggest Wii and the Wii U game in the intier history"
    print(message)
elif game == "RED DEAD REDPITION II":
    message = "RED DEAD REDPITION II is the 4th best selling game in the worldd released in October 26, 2018"
    print(message)
#3:console=if,elif,else statement
if console == "XBOX":
    text= "Xbox has its 2 biggest competitors"
    print(text)
elif console == "PLAYSTATION":
    text = "SONY was NINTENDO's oldest friend until NINTENDO join with philips and SONY got so mad that they build thier first console naming it PLAYSTATION"
    print(text)
elif console == "NINTENDO SWITCH":
    text = "NINTENDO SWITCH is the hated console for many reasons like joycon drift and home menu themes"
    print(text)
elif console == "PC":
    text = "PC is the biggest console in the world passing all the consoles eachother"
    print(text)
elif console == "STEAM DECK":
    text = "the STEAM DECK its self is the biggest competitor of all the nintendo switch and its better than the newest release switch 2"
    print(text)
#4:print
print(f"your favourate game is {game} and {message} wow thats nice")
print(f"and your console is {console} and {text} wow thats nice")                        