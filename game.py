from tkinter import *
from tkinter import messagebox as tmsg

root = Tk()
root.maxsize(width=600, height=500)
root.minsize(width=600, height=500)
root.title("Tic Tac Toe")


# restart function
def restart(z):
    if z == 0:
        return
    restart(z - 1)
    var[z] = str(z)
    board[z].config(text=var[z])


def ch(event):
    global texts
    texts = event.widget.cget("text")
    return


def che():
    global texts
    if texts == "Easy":
        movee()
    elif texts == "Medium":
        movem()
    elif texts == "Hard":
        moveh()
    else:
        tmsg.showerror(title="Error", message="Please select a mode")
        restart(9)
    return


# result function e is use and c is declared
def result():
    global f, bit
    f = 0
    for k in range(1, 9):
        if (var[int(bit[k][0])] == var[int(bit[k][1])] and var[int(bit[k][0])] == var[int(bit[k][2])]) and var[
                int(bit[k][0])] == 'X':
            return -10
        if (var[int(bit[k][0])] == var[int(bit[k][1])] and var[int(bit[k][0])] == var[int(bit[k][2])]) and var[
                int(bit[k][0])] == 'O':
            return 10
        if (not var[k] == str(k)) and (not var[k + 1] == str(k + 1)):
            f += 1
    if f == 8:
        return 0
    return


def is_win():
    x = result()
    if x == 10:
        choice = tmsg.askokcancel(title="LOSE", message="You Lose \nWant to play again?")
        if choice:
            restart(9)
        else:
            root.destroy()
            quit()
    if x == -10:
        choice = tmsg.askokcancel(title="WIN", message="You Win \nWant to play again?")
        if choice:
            restart(9)
        else:
            root.destroy()
            quit()
    if x == 0:
        choice = tmsg.askokcancel(title="Draw", message="Match Draw \nWant to play again?")
        if choice:
            restart(9)
        else:
            root.destroy()
            quit()


# computer move hard
def moveh():
    global var
    best_score = -100000
    x: int
    y: int
    score: float
    move: int
    for n in range(1, 10):
        if var[n] == str(n):
            var[n] = 'O'
            score = minmax(1, FALSE)
            var[n] = str(n)
            if score > best_score:
                best_score = score
                move = n
    var[move] = 'O'
    board[move].config(text='O')
    is_win()
    return


def minmax(h: int, sat: bool):
    global var
    for n in range(-10, 20, 10):
        if result() == n:
            return n/h
    if sat:
        best_score = -100000
        for m in range(1, 10):
            if var[m] == str(m):
                var[m] = 'O'
                score = minmax(h + 1, FALSE)
                var[m] = str(m)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 100000
        for m in range(1, 10):
            if var[m] == str(m):
                var[m] = 'X'
                score = minmax(h + 1, TRUE)
                var[m] = str(m)
                best_score = min(score, best_score)
        return best_score


# computer move  medium
def movem():
    a = 0
    if var[5] == '5':
        var[5] = 'O'
        a += 1
        board[5].config(text=var[5])
    elif a == 0:
        for m in [1, 3, 7, 9, 2, 4, 6, 8]:
            if var[m] == str(m):
                var[m] = 'O'
                a += 1
                board[m].config(text=var[m])
                break
    else:
        tmsg.showerror("Error", "Click on right Box")
    is_win()
    return


# computer move easy
def movee():
    for e in range(1, 10, 1):
        if var[e] == str(e):
            var[e] = 'O'
            board[e].config(text='O')
            break
    is_win()
    return


# player move  a and e are used b is unused
def re(event):
    global board, var
    a = 0
    y = event.widget.cget("text")
    for j in range(1, 10):
        if y == str(j):
            var[j] = 'X'
            board[j].config(text='X')
            a += 1
            break
    if a == 0:
        tmsg.showerror("ERROR", "Please click on right box")
        return
    is_win()
    che()


bit = ['0', '123', '456', '789', '147', '258', '369', '159', '357']
var = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
board = [0]
f = 0
texts = ""
# defining frame and label

f4 = Frame(root, bg="white", padx=20, pady=100, width=10)
l1 = Label(f4, text="Some Rule and Regulation:\n\n", font="Averey 10 bold")
l1.pack(pady=5)
l2 = Label(f4, text="1.First select a Mode \n2.Don't click on \nA box which is already \nmarked \n3.First move is your "
                    "\n4.If you win next \nmove is of A.I. \nand vic-versa \n5.If draw happen \nthe one who start fist"
                    "\n in previous match starts \n5.You can also change \nmode between match \n6.X-->Human \n  "
                    "7.O-->A.I.",
                    font="Averey 10", height=300)
l2.pack(fill=Y)
f4.pack(side=RIGHT, fill=Y)
Label(root, text="Welcome to Tic Tac Toe Game ", pady=25, font="Comic 18 bold").pack()
f0 = Frame(root, bg="black", padx=5, pady=4)
l1 = Button(f0, text="Easy", width=8, height=2, anchor='w')
l1.bind("<Button-1>", ch)
l1.pack(side=LEFT, padx=8)

l2 = Button(f0, text="Medium", width=8, height=2, anchor='w')
l2.bind("<Button-1>", ch)
l2.pack(side=LEFT, padx=8)

l3 = Button(f0, text="Hard", width=8, height=2, anchor='w')
l3.bind("<Button-1>", ch)
l3.pack(side=LEFT, padx=8)
f0.focus_set()
f0.pack(pady=20)
for i in range(1, 8, 3):
    fi = Frame(root, bg="black", padx=10, pady=4)
    board.append(i)
    board[i] = Button(fi, text=var[i], width=4, height=2, bg="white", fg="black", font="aris 20 bold")
    board[i].bind("<Button-1>", re)
    board[i].pack(side=LEFT, padx=8, pady=4)
    board.append(i + 1)
    board[i + 1] = Button(fi, text=var[i + 1], width=4, height=2, bg="white", fg="black", font="aris 20 bold")
    board[i + 1].bind("<Button-1>", re)
    board[i + 1].pack(side=LEFT, padx=8, pady=4)
    board.append(i + 2)
    board[i + 2] = Button(fi, text=var[i + 2], width=4, height=2, bg="white", fg="black", font="aris 20 bold")
    board[i + 2].bind("<Button-1>", re)
    board[i + 2].pack(side=LEFT, padx=8, pady=4)

    fi.pack()

root.mainloop()
