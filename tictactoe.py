from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Tic Tac Toe")

winner=False
count=0
x=True


    
def button_disable():
    b_1.config(state=DISABLED)
    b_2.config(state=DISABLED)
    b_3.config(state=DISABLED)
    b_4.config(state=DISABLED)
    b_5.config(state=DISABLED)
    b_6.config(state=DISABLED)
    b_7.config(state=DISABLED)
    b_8.config(state=DISABLED)
    b_9.config(state=DISABLED)
    
    
    
#to find the winner
def game_over():
    global winner
    global count
    # row
    if b_1["text"]==b_2["text"]==b_3["text"]:
        if b_1["text"]=="X":
            b_1.config(bg="red")
            b_2.config(bg="red")
            b_3.config(bg="red")
            messagebox.showinfo("Congrates!!","X Won the game!!")
            winner=True
            button_disable()
        elif b_1["text"]=="O":
            b_1.config(bg="red")
            b_2.config(bg="red")
            b_3.config(bg="red")
            messagebox.showinfo("Congrates!!","O Won the game!!")
            winner=True
            button_disable()
    
    elif b_4["text"]==b_5["text"]==b_6["text"]:
        if b_4["text"]=="X":
            b_4.config(bg="red")
            b_5.config(bg="red")
            b_6.config(bg="red")
            messagebox.showinfo("Congrates!!","X Won the game!!")
            winner=True
            button_disable()
        elif b_4["text"]=="O":
            b_4.config(bg="red")
            b_5.config(bg="red")
            b_6.config(bg="red")
            messagebox.showinfo("Congrates!!","O Won the game!!")
            winner=True
            button_disable()
    elif b_7["text"]==b_8["text"]==b_9["text"]:
        if b_7["text"]=="X":
            b_7.config(bg="red")
            b_8.config(bg="red")
            b_9.config(bg="red")
            messagebox.showinfo("Congrates!!","X Won the game!!")
            winner=True
            button_disable()
        elif b_7["text"]=="O":
            b_7.config(bg="red")
            b_8.config(bg="red")
            b_9.config(bg="red")
            messagebox.showinfo("Congrates!!","O Won the game!!")
            winner=True
            button_disable()
    #column
    elif b_1["text"]==b_4["text"]==b_7["text"]:
        if b_1["text"]=="X":
            b_7.config(bg="red")
            b_8.config(bg="red")
            b_9.config(bg="red")
            messagebox.showinfo("Congrates!!","X Won the game!!")
            winner=True
            button_disable()
        elif b_1["text"]=="O":
            b_7.config(bg="red")
            b_8.config(bg="red")
            b_9.config(bg="red")
            messagebox.showinfo("Congrates!!","O Won the game!!")
            winner=True
            button_disable()
    elif b_2["text"]==b_5["text"]==b_8["text"]:
        if b_2["text"]=="X":
            b_2.config(bg="red")
            b_5.config(bg="red")
            b_8.config(bg="red")
            messagebox.showinfo("Congrates!!","X Won the game!!")
            winner=True
            button_disable()
        elif b_2["text"]=="O":
            b_2.config(bg="red")
            b_5.config(bg="red")
            b_8.config(bg="red")
            messagebox.showinfo("Congrates!!","O Won the game!!")
            winner=True
            button_disable()
    elif b_3["text"]==b_6["text"]==b_9["text"]:
        if b_3["text"]=="X":
            b_3.config(bg="red")
            b_6.config(bg="red")
            b_9.config(bg="red")
            messagebox.showinfo("Congrates!!","X Won the game!!")
            winner=True
            button_disable()
        elif b_3["text"]=="O":
            b_3.config(bg="red")
            b_6.config(bg="red")
            b_9.config(bg="red")
            messagebox.showinfo("Congrates!!","O Won the game!!")
            winner=True
            button_disable()
    #diagonal
    elif b_1["text"]==b_5["text"]==b_9["text"]:
        if b_1["text"]=="X":
            b_1.config(bg="red")
            b_5.config(bg="red")
            b_9.config(bg="red")
            messagebox.showinfo("Congrates!!","X Won the game!!")
            winner=True
            button_disable()
        elif b_1["text"]=="O":
            b_1.config(bg="red")
            b_5.config(bg="red")
            b_9.config(bg="red")
            messagebox.showinfo("Congrates!!","O Won the game!!")
            winner=True
            button_disable()
    elif b_3["text"]==b_5["text"]==b_7["text"]:
        if b_3["text"]=="X":
            b_3.config(bg="red")
            b_5.config(bg="red")
            b_7.config(bg="red")
            messagebox.showinfo("Congrates!!","X Won the game!!")
            winner=True
            button_disable()
        elif b_3["text"]=="O":
            b_3.config(bg="red")
            b_5.config(bg="red")
            b_7.config(bg="red")
            messagebox.showinfo("Congrates!!","O Won the game!!")
            winner=True
            button_disable()
    elif winner==False and count==9:
        messagebox.showinfo("Tie","It's a Tie!!")
        button_disable()

            
            
def clicked(b):
   
    global count,x
    if b["text"]==" " and x==True:
        b.config(text="X")
        x=False
        count+=1
        game_over()
    elif b["text"]==" " and x==False: 
        b.config(text="O")
        x=True
        count+=1
        game_over()
    
    else:
        messagebox.showerror("Error","This button is already seleted!!")
                    





    
def reset():
    global b_1,b_2,b_3,b_4,b_5,b_6,b_7,b_8,b_9
    global count,x,winner
    count=0
    x=True
    winner=False


    #create buttons
    b_1=Button(root,text=" ",font=20,height=3,width=6,command=lambda:clicked(b_1))
    b_2=Button(root,text=" ",font=20,height=3,width=6,command=lambda:clicked(b_2))
    b_3=Button(root,text=" ",font=20,height=3,width=6,command=lambda:clicked(b_3))
    b_4=Button(root,text=" ",font=20,height=3,width=6,command=lambda:clicked(b_4))
    b_5=Button(root,text=" ",font=20,height=3,width=6,command=lambda:clicked(b_5))
    b_6=Button(root,text=" ",font=20,height=3,width=6,command=lambda:clicked(b_6))
    b_7=Button(root,text=" ",font=20,height=3,width=6,command=lambda:clicked(b_7))
    b_8=Button(root,text=" ",font=20,height=3,width=6,command=lambda:clicked(b_8))
    b_9=Button(root,text=" ",font=20,height=3,width=6,command=lambda:clicked(b_9))

        #arranging buttons
    b_1.grid(row=1,column=0)
    b_2.grid(row=1,column=1)
    b_3.grid(row=1,column=2)

    b_4.grid(row=2,column=0)
    b_5.grid(row=2,column=1)
    b_6.grid(row=2,column=2)

    b_7.grid(row=3,column=0)
    b_8.grid(row=3,column=1)
    b_9.grid(row=3,column=2)

#reset button
reset_button=Button(root,text="RESET",padx=40,pady=20,bg="green",fg="white",command=reset)
reset_button.grid(row=0,columnspan=3)

reset()
root.mainloop()