import sys
from tkinter import END
from turtle import clearscreen
import os
import random
import tkinter as tk
from tkinter import messagebox

global oneboard, playeronepos, playertwopos, twoboard, players, player, shipsizes, shiprotation, vertical, horizontal
# globalling every variable here so that if it gets called later it doesn't freak out
oneboard = [[" ","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
         ["A",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["B",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["C",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["D",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["E",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["F",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["G",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["H",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["I",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["J",".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
twoboard = [[" ","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
         ["A",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["B",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["C",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["D",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["E",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["F",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["G",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["H",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["I",".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["J",".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
# both board arrays (2d), extremely important in like every aspect of the program. they're arranged
# like this just so they're easier to read, purely cosmetic
playeronepos = []
playertwopos = []
# two lists that store all of the untouched ship positions.
players = 1
player = 1
# variables that govern the current player playing and the player amount
shiprotation = "vertical"
vertical = 1
horizontal= 0
# shiprotation is just used for labels - vertical and horizontal are used in calculations to allow
# the algorithm to check valid tiles during placing in the correct direction
shipsizes = [2, 3, 3, 4, 5]
# array that contains every ship size in order for placement. that's it, it'll just run through this
i = 0
# this i is left over from the CLI version i made before adding the GUI and i don't think it's used
# anywhere but i'm too scared to remove it

def printboard(x, y, z, rep1, rep2, board):
    listboard = list(zip(*board))
    # arranges the entire board array by column rather than by row, asterisk just tells the zip fn
    # that it's working with an array instead of a string. also, the list() is necessary

    col1 = tk.Label(z, text = str(listboard[0]).replace("(", " ").replace(")", "").replace("'", " ").replace(",", "\n").replace(rep1, rep2), font = ("Arial", 15, "bold"))
    col1.place(x = x, y = y)

    col2 = tk.Label(z, text = str(listboard[1]).replace("(", " ").replace(")", "").replace("'", " ").replace(",", "\n").replace(rep1, rep2), font = ("Arial", 15, "bold"))
    col2.place(x = x + 40, y = y)

    col3 = tk.Label(z, text = str(listboard[2]).replace("(", " ").replace(")", "").replace("'", " ").replace(",", "\n").replace(rep1, rep2), font = ("Arial", 15, "bold"))
    col3.place(x = x + 80, y = y)

    col4 = tk.Label(z, text = str(listboard[3]).replace("(", " ").replace(")", "").replace("'", " ").replace(",", "\n").replace(rep1, rep2), font = ("Arial", 15, "bold"))
    col4.place(x = x + 120, y = y)

    col5 = tk.Label(z, text = str(listboard[4]).replace("(", " ").replace(")", "").replace("'", " ").replace(",", "\n").replace(rep1, rep2), font = ("Arial", 15, "bold"))
    col5.place(x = x + 160, y = y)

    col6 = tk.Label(z, text = str(listboard[5]).replace("(", " ").replace(")", "").replace("'", " ").replace(",", "\n").replace(rep1, rep2), font = ("Arial", 15, "bold"))
    col6.place(x = x + 200, y = y)

    col7 = tk.Label(z, text = str(listboard[6]).replace("(", " ").replace(")", "").replace("'", " ").replace(",", "\n").replace(rep1, rep2), font = ("Arial", 15, "bold"))
    col7.place(x = x + 240, y = y)

    col8 = tk.Label(z, text = str(listboard[7]).replace("(", " ").replace(")", "").replace("'", " ").replace(",", "\n").replace(rep1, rep2), font = ("Arial", 15, "bold"))
    col8.place(x = x + 280, y = y)

    col9 = tk.Label(z, text = str(listboard[8]).replace("(", " ").replace(")", "").replace("'", " ").replace(",", "\n").replace(rep1, rep2), font = ("Arial", 15, "bold"))
    col9.place(x = x + 320, y = y)

    col10 = tk.Label(z, text = str(listboard[9]).replace("(", " ").replace(")", "").replace("'", " ").replace(",", "\n").replace(rep1, rep2), font = ("Arial", 15, "bold"))
    col10.place(x = x + 360, y = y)

    col11 = tk.Label(z, text = str(listboard[10]).replace("(", " ").replace(")", "").replace("'", " ").replace(",", "\n").replace(rep1, rep2), font = ("Arial", 15, "bold"))
    col11.place(x = x + 400, y = y)
    # this function was made because a label that just printed the entire board would misalign all of
    # the columns when different sized characters were used, so i thought i would make a gigantic 
    # function that printed each column individually that let me specify the board (appropriately 
    # named "board" parameter), position (x and y parameters), parent tk window (z), and if it would 
    # hide ships or not (rep1 and rep2 - both parameters that would be used in a single replace fn
    # attached to every label). There might be an easier way to do this - this does look better tho

def playerselect():
    menu = tk.Tk()
    menu.geometry("200x100+600+250")
    menu.title("Player Selection")
    # tk.Tk() is just the window itself. geometry sets size and position (x*y+x+y), title just
    # names the window whatever you put in the function.

    playerprompt = tk.Label(menu, text = "How many players?")
    playerprompt.pack(pady = 2, padx = 1)
    # label that explains the two buttons that appear below it. "menu" at the beginning of the
    # function needs to be specified so it knows which tk instance it's a child of

    def oneplay():
        global players
        players = 1
        menu.destroy()

    def twoplay():
        global players, player
        players = 2
        player = 1
        menu.destroy()
    # two functions assigned to the oneplayer and twoplayer buttons that just specify the number
    # of players

    onebutton = tk.Button(menu, width = 6, text = "ONE", background = "#93a3cf", activebackground = 
                          "#707c9e", command = oneplay)
    onebutton.pack(pady = 0, padx = 1)

    twobutton = tk.Button(menu, width = 6, text = "TWO", background = "#93a3cf", activebackground = 
                          "#707c9e", command = twoplay)
    twobutton.pack(pady = 0, padx = 1)
    # oneplayer and twoplayer buttons - each one will just activate their respective function
    # explained above

    menu.mainloop()

def placement():
    global shiprotation, places
    # calling the two globals used in this fn

    menu = tk.Tk()
    menu.geometry("460x500+500+75")
    menu.title("Placement")

    placelabel = tk.Label(menu, text = "Player " + str(player) + " place", font = ("Arial"))
    placelabel.pack(pady = 3, padx = 1)

    if player == 1:
        printboard(5, 40, menu, "?", "?", oneboard)
    else:
        printboard(5, 40, menu, "?", "?", twoboard)
    # first instance of the board printing function in action, "?" is just because nothing needs
    # to be replaced so i just used two characters that never appear.

    entrylabel = tk.Label(menu, text = "Ship rotation is " + str(shiprotation) + "\nThis ship has " + 
                          str(shipsizes[places]) + " segments" + 
                          "\n!SEGMENTS PLACE LEFT TO RIGHT/TOP TO BOTTOM!" + 
                          "\nWhere will you place the ship's head?", font = "Arial")
    entrylabel.place(x = 19, y = 330)
    # vital information on the nature of the ship you're placing - tells you the size and orientation
    # and lets you know how the segments will place

    placeentry = tk.Entry(menu, width = 4)
    placeentry.place(x = 208, y = 413)
    placeentry.focus_set()
    # entrybox where you type the tile you want to shoot. focus_set() just means the moment the
    # window is focused you will start typing in the entrybox

    def place():
        global places, vertical, horizontal
        placingpos = str(placeentry.get())
        # variable pulls from the entrybox early using the .get() function

        if player == 1:
            if len(placingpos) > 1:
                if placingpos[0].isalpha() == True and placingpos[1:].isnumeric() == True:
                    y = (ord(placingpos[0].upper()) - 64)
                    x = int(placingpos[1:])
                    # x and y are easier to work with than say "ord(placingpos[0].upper() - 64", only 
                    # reason this is done

                    if len(placingpos) == 2 or len(placingpos) == 3 and y < 11 - ((shipsizes[places] - 1) * vertical) and y > 0 and x > 0 and x < 11 - ((shipsizes[places] - 1) * horizontal):
                        validpos = True
                        j = 0
                        # validpos used as a flag, j used as an index
                        while j < shipsizes[places]:
                            if (y + j * vertical) < 11 and (x + j * horizontal) < 11:
                                if not oneboard[y + j * vertical][x + j * horizontal] == ".":
                                    validpos = False
                            else:
                                validpos = False
                            j = j + 1
                            # increments j with every segment checked, knows how many to check 
                            # because of shipsizes array. if invalid, flag is triggered

                        if validpos == True:
                            j = 0
                            while j < shipsizes[places]:
                                oneboard[y + j * vertical][x + j * horizontal] = "-"
                                playeronepos.append(str(oneboard[y + j * vertical][0]) + str(oneboard[0][x + j * horizontal]))
                                j = j + 1
                                # adds the position of each segment into the positions array in an "XY"
                                # form where X is a capital letter and y is an integer
                            places = places + 1
                            # increments the index that controls the whole placing process
                            menu.destroy()
                            # any instance of .destroy() throughout the program will just close
                            # the window it refers to
                        else:
                            messagebox.showinfo("Try again", "Invalid Position")
                                
                    else:
                        messagebox.showinfo("Try again", "Invalid Position")
                    
                else:
                    messagebox.showinfo("Try again", "Invalid Position")

            else:
                messagebox.showinfo("Try again", "Invalid Position")
            # this huge error trap basically just checks if the location itself is a valid place on
            # the board, and then checks if EVERY location the segments will be in is a free space
            # before eventually placing them in each spot checked if they're valid. if any of these
            # fail, it creates a messagebox that just lets the user know that. also each check is
            # designed to ensure a character in the string that doesn't exist isn't called, which
            # would cause a logic error.
        else:
            if len(placingpos) > 1:
                if placingpos[0].isalpha() == True and placingpos[1:].isnumeric() == True:
                    j = 0
                    y = (ord(placingpos[0].upper()) - 64)
                    x = int(placingpos[1:])

                    if len(placingpos) == 2 or len(placingpos) == 3 and y < 11 - ((shipsizes[places] - 1) * vertical) and y > 0 and x > 0 and x < 11 - ((shipsizes[places] - 1) * horizontal):
                        validpos = True
                        j = 0
                        while j < shipsizes[places]:
                            if (y + j * vertical) < 11 and (x + j * horizontal) < 11:
                                if not twoboard[y + j * vertical][x + j * horizontal] == ".":
                                    validpos = False
                            else:
                                validpos = False
                            j = j + 1

                        if validpos == True:
                            j = 0
                            while j < shipsizes[places]:
                                twoboard[y + j * vertical][x + j * horizontal] = "-"
                                playertwopos.append(str(twoboard[y + j * vertical][0]) + str(twoboard[0][x + j * horizontal]))
                                j = j + 1
                            places = places + 1
                            menu.destroy()
                        else:
                            messagebox.showinfo("Try again", "Invalid Position")

                    else:
                        messagebox.showinfo("Try again", "Invalid Position")
                    
                else:
                    messagebox.showinfo("Try again", "Invalid Position")

            else:
                messagebox.showinfo("Try again", "Invalid Position") 
        # literally the exact same function as before except for the second player, so "oneboard" 
        # will instead be "twoboard" etc.
                
    placebutton = tk.Button(menu, width = 6, text = "Place", background = "#44d442", 
                            activebackground = "#329c30", command = place)
    placebutton.place(x = 195, y = 434)
    # button to trigger the gigantic function above

    def rotate():
       global shiprotation, vertical, horizontal
       if shiprotation == "vertical":
            shiprotation = "horizontal"
            horizontal = 1
            vertical = 0
       else:
            shiprotation = "vertical"
            horizontal = 0
            vertical = 1
       menu.destroy()
    # function just changes the rotation of the ship and makes the related variables adhere to that

    rotatebutton = tk.Button(menu, width = 6, text = "Rotate", background = "#93a3cf", 
                             activebackground = "#707c9e", command = rotate)
    rotatebutton.place(x = 195, y = 460)
    # button to trigger the rotate function

    menu.bind('<Return>',lambda event:place())
    # this just adds enter as a keybind to trigger the same function as the place button

    menu.mainloop()
    # if there was no mainloop on any of these tk instances they would just be gone after one frame

def viewscreen():
    viewmenu = tk.Tk()
    viewmenu.geometry("450x350+505+135")
    viewmenu.title("Your board")

    if player == 1:
        printboard(0, 40, viewmenu, "?", "?", oneboard)
    else:
        printboard(0, 40, viewmenu, "?", "?", twoboard) 
    
    viewmenu.mainloop()
    # this menu is very simple, it just shows up and displays your entire board with nothing hidden

def firescreen():
    global turn
    # turn needs to be globalled because it is used in this function
    
    menu = tk.Tk()
    menu.geometry("460x500+500+75")
    menu.title("Attacking")

    firelabel = tk.Label(menu, text = "Player " + str(player) + "'s turn", font = "Arial")
    firelabel.pack(pady = 1, padx = 0)
    # label changes based on the current player.

    if player == 1:
        printboard(5, 40, menu, "-", ".", twoboard)
    else:
        printboard(5, 40, menu, "-", ".", oneboard)

    entrylabel = tk.Label(menu, text = "Where will you shoot?", font = "Arial")
    entrylabel.place(x = 143, y = 330)
    # label that just lets the player know what they're actually doing (shooting a tile)

    placeentry = tk.Entry(menu, width = 4)
    placeentry.place(x = 208, y = 354)
    placeentry.focus_set()
    # focus_set() is used here again - this is another entry box the player uses to specify the tile

    def shoot():
        global turn
        placingpos = str(placeentry.get())

        if player == 1:
            if len(placingpos) == 2 or len(placingpos) == 3:
                if placingpos[0].isalpha() == True and placingpos[1:].isnumeric() == True:
                    y = ord(placingpos[0].upper()) - 64
                    x = int(placingpos[1:])
            
                    if y > 0 and y < 11 and x > 0 and x < 11:
                        if twoboard[y][x] == "-":
                            twoboard[y][x] = "x"
                            playertwopos.remove(placingpos.upper())
                            messagebox.showinfo("Successful shot", "Hit!")
                            menu.destroy()
                            if len(playertwopos) == 0:
                                turn = False
                            # turn not being set to false means the player gets to keep shooting
                            # if they hit UNLESS they've already destroyed all the enemy's ships.
                            # "x" is used to mark where they hit previously
                        else:
                            if not twoboard[y][x] == "x":
                                twoboard[y][x] = "o"
                            messagebox.showinfo("Unlucky...", "Miss!")
                            turn = False
                            menu.destroy()
                            # turn is ended because of the miss. "o" is used to mark this out
                        # statement basically just checks if there's a ship on specified tile
                    else:
                        messagebox.showinfo("Try again", "Invalid Position")
                else:
                    messagebox.showinfo("Try again", "Invalid Position")
            else:
                messagebox.showinfo("Try again", "Invalid Position")
            # once again an error trap that checks if the tile selected is a valid one, only simpler
            # because only one tile needs to be checked and it is much more likely to be valid
        else:
            if len(placingpos) == 2 or len(placingpos) == 3:
                if placingpos[0].isalpha() == True and placingpos[1:].isnumeric() == True:
                    y = ord(placingpos[0].upper()) - 64
                    x = int(placingpos[1:])
            
                    if y > 0 and y < 11 and x > 0 and x < 11:
                        if oneboard[y][x] == "-":
                            oneboard[y][x] = "x"
                            playeronepos.remove(placingpos.upper())
                            messagebox.showinfo("Successful shot", "Hit!")
                            if len(playeronepos) == 0:
                                turn = False
                            menu.destroy()
                        else:
                            if not oneboard[y][x] == "x":
                                oneboard[y][x] = "o"
                            messagebox.showinfo("Unlucky...", "Miss!")
                            turn = False
                            menu.destroy()

                else:
                    messagebox.showinfo("Try again", "Invalid Position")
            else:
                messagebox.showinfo("Try again", "Invalid Position")
            # once again the exact same function as before only with the second player instead of
            # the first

    shootbutton = tk.Button(menu, width = 6, text = "Shoot", background = "#44d442", 
                            activebackground = "#329c30", command = shoot)
    shootbutton.place(x = 195, y = 374)
    # button that triggers the shooting function

    menu.bind('<Return>',lambda event:shoot())
    # another enter keybind that also triggers the shooting function

    def view():
        viewscreen()

    viewbutton = tk.Button(menu, width = 12, text = "View Own Board", background = "#93a3cf", 
                           activebackground = "#707c9e", command = view)
    viewbutton.place(x = 172, y = 400)
    # button that triggers the function that activates the viewscreen explained much further above

    menu.mainloop()

def compscreen():
    compmenu = tk.Tk()
    compmenu.geometry("450x400+500+135")
    compmenu.title("Computer's turn")

    if compturn == "hit":
        complabel = tk.Label(compmenu, text = "Computer has hit!\nSpecified position: " + oneboard[y][0]
                             + oneboard[0][x], font = "Arial")
    else:
        complabel = tk.Label(compmenu, text = "Computer has missed!\nSpecified position: " + oneboard[y][0]
                             + oneboard[0][x], font = "Arial")
    complabel.pack(pady = 1, padx = 0)

    printboard(5, 55, compmenu, "?", "?", oneboard)
    # all of this just displays the board with a label that tells you if the computer hit or missed,
    # also telling you WHERE it actually shot so you don't have to play spot the difference

    def exit():
        compmenu.destroy()
    # usually wouldn't make a function for this - kept erroring otherwise and i have no idea why

    okbutton = tk.Button(compmenu, width = 4, text = "OK!", background = "#44d442", 
                         activebackground = "#329c30", command = exit)
    okbutton.place(x = 210, y = 345)
    # this command just triggers the function up above that continues the algorithm basically

    compmenu.bind('<Return>',lambda event:exit())
    # makes enter also close the window

    compmenu.mainloop()

def winscreen():
    menu = tk.Tk()
    menu.geometry("300x150+550+170")
    menu.title("Winner!")

    # whole function below just displays the winner in big text and uses their amount of active ship
    # positions to check that. obviously if they have 0, all of their ships have been destroyed
    if len(playeronepos) == 0 and len(playertwopos) > 0:
        if players == 2:
            winner = tk.Label(menu, text = "Player Two wins!\nGood Game!", font = ("Arial", 20, "bold"))
            winner.pack(pady = 3, padx = 1)
        else:
            winner = tk.Label(menu, text = "Computer wins!\nGood Game!", font = ("Arial", 20, "bold"))
            winner.pack(pady = 3, padx = 1)
    elif len(playertwopos) == 0 and len(playeronepos) > 0:
        if players == 2:
            winner = tk.Label(menu, text = "Player One wins!\nGood Game!", font = ("Arial", 20, "bold"))
            winner.pack(pady = 3, padx = 1)
        else:
            winner = tk.Label(menu, text = "You win!\nGood Game!", font = ("Arial", 20, "bold"))
            winner.pack(pady = 3, padx = 1)
    else:
        winner = tk.Label(menu, text = "Somehow, it's a draw!\nWhat a Game!", font = ("Arial", 20))
        winner.pack(pady = 3, padx = 1)
        # this is only possible because player two gets one final shot even if they've lost all
        # their ships. was a bug, just thought it was funny so i kept it. now both players losing
        # all their ships and drawing is possible and i kind of love that

    finishbutton = tk.Button(menu, width = 6, text = "Finish", background = "#e64b43", 
                             activebackground = "#ab3630", command = sys.exit)
    finishbutton.pack(pady = 1, padx = 1)
    # this button just triggers a function that ends the entire program

    menu.mainloop()


        
playerselect()
player = 1
global places
places = 0
while places < 5:
    placement()
# means the player will get to place 5 ships

places = 0
if players == 2:
    player = 2
    while places < 5:
        placement()
        # allows player 2 to now place if they exist
else:
    places = 0
    while places < 5:
        rng = random.randint(0,1)

        if rng == 0:
            placingpos = "rotate"
        else:
            placingpos = 0 

        if placingpos == "rotate":
            if shiprotation == "vertical":
                shiprotation = "horizontal"
                horizontal = 1
                vertical = 0
            else:
                shiprotation = "vertical"
                horizontal = 0
                vertical = 1
        # this just basically gives the computer a random chance to rotate instead of placing their
        # ship, allowing for more variety

        else:

            y = random.randint(1,10)
            x = random.randint(1,10)
            # computer just picks a random spot to place until it's eventually valid

            if y < 11 - ((shipsizes[places] - 1) * vertical) and y > 0 and x > 0 and x < 11 - ((shipsizes[places] - 1) * horizontal):
                validpos = True
                j = 0
                while j < shipsizes[places]:
                    if (y + j * vertical) < 11 and (x + j * horizontal) < 11:
                        if not twoboard[y + j * vertical][x + j * horizontal] == ".":
                            validpos = False
                    else:
                        validpos = False
                    j = j + 1

                if validpos == True:
                    j = 0
                    while j < shipsizes[places]:
                        twoboard[y + j * vertical][x + j * horizontal] = "-"
                        playertwopos.append(str(twoboard[y + j * vertical][0]) + str(twoboard[0][x + j * horizontal]))
                        j = j + 1
                    places = places + 1
                else:
                    places = places
                    
            else:
                places = places
            # this whole error trap is exactly the same as the one used for players above, no
            # differences apart from the fact that it obviously doesn't display an invalid pos.

global turn
while len(playeronepos) > 0 and len(playertwopos) > 0:
    player = 1
    turn = True
    while turn ==  True:
        firescreen()

    if players == 1:
        turn = True
        hits = 0
        direction = 0
        modifier = 0
        fails = 0
        # all these variables just help the computer to understand better where it SHOULD shoot
        # when they're used later on
        while turn == True:
           
            if hits == 0:
                y = random.randint(1,10)
                x = random.randint(1,10)
            elif hits == 1:
                direction = random.randint(0,1)
                modifiers = [-1,1]
                modifier = random.choice(modifiers)
                if direction == 0:
                    y = y - modifier
                    x = x
                else:
                    y = y
                    x = x - modifier
            else:
                if direction == 0:
                    y = y - modifier
                    x = x
                else:
                    y = y
                    x = x - modifier
            # this just means the computer is going to a. fire at a random square b. if it hits, it
            # will then fire to a random adjacent square and c. if it hits again it keeps going in
            # that directon until it misses (although this direction can be reversed)

            if y < 11 and y > 0 and x < 11 and x > 0:
                if oneboard[y][x] == ".":
                    fails = 0
                    oneboard[y][x] = "o"
                    os.system('cls')
                    compturn = "miss"
                    compscreen()
                    turn = False
                    # very simple, if the computer misses its turn just ends and it opens the tk
                    # window that tells the player that (also tells that tk window what happened)
                elif oneboard[y][x] == "-":
                    modifier = int(modifier/round(fails/5 + 1,0))
                    # modifier is what tells the computer the direction it goes in in terms of 
                    # left/right or up/down, and is a variable so it can be edited mid-function
                    fails = 0
                    # fails is more of an "in a row" kind of thing so if a hit is successful it's
                    # reset
                    oneboard[y][x] = "x"
                    hits = hits + 1
                    playeronepos.remove(str(oneboard[y][0] + oneboard[0][x]))
                    compturn = "hit"
                    compscreen()
                    if len(playeronepos) == 0:
                        turn = False
                    # hits is incremented by 1 here in the event of a valid hit which influences
                    # the firing functions explained further up.
                else:
                    modifier = int(modifier * -1)
                    # modifier is multiplied by -1 to change the direction the computer fires in
                    fails = fails + 1
                    if fails > 5 and fails <= 30:
                        modifier = int(1 * random.choice(modifiers) * round(fails/5 + 1, 0))
                    elif fails > 30:
                        y = random.randint(1,10)
                        x = random.randint(1,10)
                        modifier = 1
                    # failsafe - if the computer errors too many times in a row it'll assume it has
                    # gotten stuck, and start checking further outside its range. if this doesn't work,
                    # it'll just jump to a random tile.
            else:
                modifier = int(modifier * -1)  
                # turns the computer around if it goes off of the edge of the board, otherwise
                # it'd just keep going in a straight line forever and runtime error
    else:
        player = 2
        turn = True
        while turn == True:
            firescreen()
        # this just repeats the player one firing process again only with the second player in mind
winscreen()
# the end of the program - just displays the winner screen which was already explained above


                    
                

        





