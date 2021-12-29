from tkinter import *
from tkinter import messagebox
from random import *
root = Tk()

root.title('TIC TAC TOE')
root.iconbitmap()

clicked = True
count = 0

def lock_screen():
     button_1.config(state=DISABLED)
     button_2.config(state=DISABLED)
     button_3.config(state=DISABLED)
     button_4.config(state=DISABLED)
     button_5.config(state=DISABLED)
     button_6.config(state=DISABLED)
     button_7.config(state=DISABLED)
     button_8.config(state=DISABLED)
     button_9.config(state=DISABLED)

def checkwinn(mark):
    global winner, wincheck, win_coord, text
    text = ""
    winner = False
    wincheck = [button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9]
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if wincheck[each[0]]["text"] == wincheck[each[1]]["text"] == wincheck[each[2]]["text"] == mark:
            winner = True
            wincheck[each[0]].config(bg="lime")
            wincheck[each[1]].config(bg="lime")
            wincheck[each[2]].config(bg="lime")
            text = "CONGRATULATIONS!  "+mark+"  is wineRRR"
            lock_screen()
            break

        elif count == 9 and winner == False:
            text =  "         Draw! \n Noone is winneRRR!"
            lock_screen()
    if text!= '':
        messagebox.showinfo("GAME OVER", str(text))

def checkwin_minimax(mark):
    global wincheck, win_coord
    wincheck = [button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9]
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if wincheck[each[0]]["text"] == wincheck[each[1]]["text"] == wincheck[each[2]]["text"] == mark:
            return True

#--------------PLAYER----------------
def b_click(b):
    global clicked, count

    if b["text"] == "  " and clicked == True:
        b["text"] = "X "
        clicked = False
        count += 1
        checkwinn("X ")
    elif b["text"] == "  " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkwinn("O")
    else:
        messagebox.showerror("Wrong input", " This box is already filled.\n\n Try again!!!")
#1 player
def b_click2(b):
    global clicked, count, winner

    if b["text"] == "  " :
        b["text"] = "X "
        count += 1
        checkwinn("X ")
        if winner == False:
            comp_2()
    else:
        messagebox.showerror("Wrong input", " This box is already filled.\n\n Try again!!!")
#Unbeatable
def b_click3(b):
    global clicked, count, winner

    if b["text"] == "  " :

        b["text"] = "X "
        count += 1
        checkwinn("X ")
        if winner == False:
            unbeat()
    else:
        messagebox.showerror("Wrong input", " This box is already filled.\n\n Try again!!!")

#------------BOT---------------------
def comp_2():
    global clicked, count
    wincheck = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]
    almost_win = ((0, 1, 2), (1, 2, 0), (3, 4, 5), (4, 5, 3), (6, 7, 8), (7, 8, 6), (0, 3, 6), (3, 6, 0), (1, 4, 7), (4, 7, 1), (2, 5, 8), (5, 8, 2), (0, 4, 8), (4, 8, 0), (6, 4, 2), (4, 2, 6), (0, 2, 1), (3, 5, 4), (6, 8, 7), (0, 6, 3), (1, 7, 4), (2, 8, 5), (0, 8, 4), (2, 6, 4))
    for each in almost_win:
        if wincheck[each[0]]["text"] == wincheck[each[1]]["text"] == "O"  and wincheck[each[2]]["text"] != "X " :
            wincheck[each[2]]["text"] = "O"
            count += 1
            checkwinn("O")
            break
        elif wincheck[each[0]]["text"] == wincheck[each[1]]["text"] == "X " and wincheck[each[2]]["text"] != "O" :
            wincheck[each[2]]["text"] = "O"
            count += 1
            checkwinn("O")
            break
        elif count == 1 and button_5["text"] == "  ":
            button_5["text"] = "O"
            count += 1
            break
        elif count == 1 and button_1["text"] == "  ":
            button_1["text"] = "O"
            count += 1
            break
    else:
        for i in range(0,9):
            if wincheck[i]["text"] == "  ":
               wincheck[i]["text"] = "O"
               count += 1
               checkwinn("O")
               break

#1.0
def unbeat():
    global clicked, count,wincheck, bestScore , score
    wincheck = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]
    bestScore = -800
    bestMove = -6
    for i in range(0,9):
        if wincheck[i]["text"] == "  ":
            wincheck[i]["text"] = "O"
            score = minimax(True)
            wincheck[i]["text"] = "  "
            if (score > bestScore):
                bestScore = score
                bestMove = i

    wincheck[bestMove]["text"] = "O"
    count += 1
    checkwinn("O")
    return
def minimax( isMaximizing):

    if (checkwin_minimax("O")):
        return 1
    elif (checkwin_minimax("X ")):
        return -1
    elif (count == 9 and winner == False):
        return 0

    if (isMaximizing):
        bestScore = 800
        for i in range(0,9):
            if wincheck[i]["text"] == "  ":
                wincheck[i]["text"] = "O"
                score = minimax( False)
                wincheck[i]["text"] = "  "
                if (score < bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = -800
        for i in range(0,9):
            if wincheck[i]["text"] == "  ":
                wincheck[i]["text"] = "X "
                score = minimax(True)
                wincheck[i]["text"] = "  "
                if (score > bestScore):
                    bestScore = score
        return bestScore

# 2.0
def unbeatt():
    global clicked, count, wincheck, bestMove
    wincheck = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]
    bestScore = -800
    bestMove = 0

    for i in range(0,9):
        if wincheck[i]["text"]=="  ":
            wincheck[i]["text"]="O"
            score = minimaxx(True)
            if score >bestScore:
                bestScore=score
            wincheck[i]["text"] = "  "
            bestMove = i
    return bestMove

    wincheck[bestMove]["text"] = "O"
    count += 1
    checkwinn("O")
def minimaxx(Maximizing):
    global clicked, count, wincheck, bestMove
    wincheck = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]
    if (checkwin_minimax("O")):
        return 1
    elif (checkwin_minimax("X ")):
        return -1
    elif (count == 9 and winner == False):
        return 0
    if Maximizing:
        bestScore = 800
        for i in range(0, 9):
            if wincheck[i]["text"] == "  ":
                wincheck[i]["text"] = "X "
                score = minimaxx(False)
                if score < bestScore:
                    bestScore = score
                wincheck[i]["text"] = "  "
        return bestScore


    else:
        bestScore = -800
        for i in range(0, 9):
            if wincheck[i]["text"] == "  ":
                wincheck[i]["text"] = "O"
                score = minimaxx(True)
                if int(score) > bestScore:
                    bestScore = score
                wincheck[i]["text"] = "  "
                bestMove = i
        return bestScore


    #-----------------MAIN----------------

 # 3.0





 # ----------------- MAIN ----------------------
def reset():
    global button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9
    global clicked,count
    clicked=True
    count=0
    button_1 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg= "aqua", command=lambda: b_click (button_1))
    button_2 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click (button_2))
    button_3 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click (button_3))

    button_4 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click (button_4))
    button_5 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click (button_5))
    button_6 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click (button_6))

    button_7 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click (button_7))
    button_8 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click (button_8))
    button_9 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click (button_9))

    button_1.grid(row=1, column=0)
    button_2.grid(row=1, column=1)
    button_3.grid(row=1, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)

def _1player_():
    global button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9
    global clicked,count
    clicked=True
    count=0

    button_1 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg= "aqua", command=lambda: b_click2 (button_1))
    button_2 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click2 (button_2))
    button_3 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click2 (button_3))

    button_4 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click2 (button_4))
    button_5 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click2 (button_5))
    button_6 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click2 (button_6))

    button_7 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click2 (button_7))
    button_8 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click2 (button_8))
    button_9 = Button (root, text="  ", font=( "Ink Free",50 ), padx=60, pady=60, bg="aqua", command=lambda: b_click2 (button_9))

    button_1.grid(row=1, column=0)
    button_2.grid(row=1, column=1)
    button_3.grid(row=1, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)

def UNBEAT():
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9
    global clicked, count
    clicked = True
    count = 0

    button_1 = Button(root, text="  ", font=("Ink Free", 50), padx=60, pady=60, bg="aqua",
                      command=lambda: b_click3(button_1))
    button_2 = Button(root, text="  ", font=("Ink Free", 50), padx=60, pady=60, bg="aqua",
                      command=lambda: b_click3(button_2))
    button_3 = Button(root, text="  ", font=("Ink Free", 50), padx=60, pady=60, bg="aqua",
                      command=lambda: b_click3(button_3))

    button_4 = Button(root, text="  ", font=("Ink Free", 50), padx=60, pady=60, bg="aqua",
                      command=lambda: b_click3(button_4))
    button_5 = Button(root, text="  ", font=("Ink Free", 50), padx=60, pady=60, bg="aqua",
                      command=lambda: b_click3(button_5))
    button_6 = Button(root, text="  ", font=("Ink Free", 50), padx=60, pady=60, bg="aqua",
                      command=lambda: b_click3(button_6))

    button_7 = Button(root, text="  ", font=("Ink Free", 50), padx=60, pady=60, bg="aqua",
                      command=lambda: b_click3(button_7))
    button_8 = Button(root, text="  ", font=("Ink Free", 50), padx=60, pady=60, bg="aqua",
                      command=lambda: b_click3(button_8))
    button_9 = Button(root, text="  ", font=("Ink Free", 50), padx=60, pady=60, bg="aqua",
                      command=lambda: b_click3(button_9))

    button_1.grid(row=1, column=0)
    button_2.grid(row=1, column=1)
    button_3.grid(row=1, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)

menu = Menu(root)
root.config(menu=menu)

options_menu=Menu(menu,tearoff=False)
menu.add_cascade(label="options", menu=options_menu)
options_menu.add_command(label="2 player", command= reset)
options_menu.add_command(label="1 player", command= _1player_)
options_menu.add_command(label="Unbeatable", command= UNBEAT )

UNBEAT()
root.mainloop()