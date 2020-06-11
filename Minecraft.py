
print("This is a type based game emulator")
print("The game will end if you do not type in capital letters")
print("Type GO NORTH to go north or GO EAST to go east.")
print("You can only go north, east, south, or west and only one block at a time")
print("The map is surrounded by ocean which you cannot enter")
print("To win you must light the portal which will take you to safety")
print("Type INVENTORY to view your inventory")
print("Type SURFACE to know what you are standing on")
print("Type PICK UP to pick up what you are standing on")
print("Type CONTROLS to view the controls")
print("--------------------------------------------------------------------------------------------")

def controls() :
    print("The game will end if you do not type in capital letters")
    print("Type GO NORTH to go north or GO EAST to go east.")
    print("You can only go north, east, south, or west and only one block at a time")
    print("The map is surrounded by ocean which you cannot enter")
    print("To win you must light the portal which will take you to safety")
    print("Type INVENTORY to view your inventory")
    print("Type SURFACE to know what you are standing on")
    print("Type PICK UP to pick up what you are standing on")
    print("Type CONTROLS to view the controls")


if input("Type START to begin game:") == "START":
    print("Your ship sank and you have been marooned on an island")
    x = 5
    y = 1
    print("Your co-ordinates are:", x, ",", y)
    print("--------------------------------------------------------------------------------------------")


a = 1
while a == 1:
    action = input("What do you want to do next?  ")
    if action == "GO NORTH" :
        y = y + 1






def move_north() :
    y = y-1


