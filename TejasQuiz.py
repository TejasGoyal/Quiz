from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from random import randint
import pkg_resources.py2_warn  #important, also use the following line in pyinstaller
#pyinstaller --hidden-import pkg_resources.py2_warn example.py

root=Tk()
root.title("Tejas Goyal")
root.geometry("460x500")

def aboutME():
    response=messagebox.showinfo("Namaste","This is a quiz app based on\nfamous places in Japan.\n\nHope you like it.\nThank you for playing.")


Label(root,text="Do you know which place is related to the image shown",pady=15,padx=90).grid(columnspan=3,row=0,column=0)
places=['DisneyLand',
        'ItsukushimaShrine',
        'KanazawaCastle',
        'Kinkakuji',
        'MountFuji',
        'NaraPark',
        'OsakaCastle',
        'Senso-ji',
        'TokyoSkytree']

answerLabel=Label(text="Click on Start Menu to begin")
answerLabel.grid(row=2,column=1)

show_img=Label(text="Good Luck")
show_img.grid(row=3,column=1)

def game():
    global answerLabel
    answerLabel.grid_forget()

    global show_img
    show_img.grid_forget()
    
    rand_dig=randint(0,len(places)-1)
    pathHere="JPimg/"+str(places[rand_dig])+".jpg"
    jp_image=ImageTk.PhotoImage(Image.open(pathHere))
    show_img=Label(root,image=jp_image)
    show_img.image=jp_image
    show_img.grid(columnspan=3,row=1,column=0,pady=10)
    answerKey=str(places[rand_dig])
    answerLabel=Label(text=answerKey)

    def answerCommand():
        answerLabel.grid(row=2,column=1,pady=10)
        
    Button(root,text="Answer",bg="#E6E6FA",command=answerCommand).grid(row=2, column=0,pady=10)
    Button(root,text="Next",bg="#DC143C",command=game).grid(row=2, column=2,pady=10)


myMenu = Menu(root)
root.config(menu=myMenu,bg='#FF69B4')
file_menu = Menu(myMenu)
myMenu.add_cascade(label="Start", menu=file_menu)
file_menu.add_command(label="New Game", command=game)
file_menu.add_separator()
file_menu.add_command(label="About", command=aboutME)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)



game_frame=Frame(root, width = 500, height = 500)
root.mainloop()


