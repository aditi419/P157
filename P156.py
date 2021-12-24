from tkinter import *
import random
from PIL import ImageTk, Image

root = Tk()
root.title('ENDLESS POKEMON CARD GAME')
root.geometry('900x900')
root.configure(background='orange')

pikachu = ImageTk.PhotoImage(Image.open('pikachu.jpg'))
abra = ImageTk.PhotoImage(Image.open('abra.jpg'))
bulbasour = ImageTk.PhotoImage(Image.open('bulbasour.jpg'))
charmender = ImageTk.PhotoImage(Image.open('charmender.jpg'))
Iyvasour = ImageTk.PhotoImage(Image.open('Iyvasour.jpg'))
jigglypuff = ImageTk.PhotoImage(Image.open('jigglypuff.jpg'))
kadabra = ImageTk.PhotoImage(Image.open('kadabra.jpg'))
meowth = ImageTk.PhotoImage(Image.open('meowth.jpg'))
nidoking = ImageTk.PhotoImage(Image.open('nidoking.jpg'))
paras = ImageTk.PhotoImage(Image.open('paras.jpg'))
persion = ImageTk.PhotoImage(Image.open('persion.jpg'))
ratata = ImageTk.PhotoImage(Image.open('ratata.jpg'))
spuirtle = ImageTk.PhotoImage(Image.open('squirtle.jpg'))

label = Label(root,text='Player 1',bg='red',fg='white')
label.place(relx = 0.2,rely = 0.4,anchor=CENTER)

label2 = Label(root,text='Player 2',bg='red',fg='white')
label2.place(relx = 0.8,rely = 0.4,anchor=CENTER)

player1ScoreLabel = Label(root,text='Player 1 Score',bg='yellow',fg='black')
player1ScoreLabel.place(relx = 0.2,rely = 0.6,anchor = CENTER)

player2ScoreLabel = Label(root,text='Player 2 Score',bg='yellow',fg='black')
player2ScoreLabel.place(relx = 0.8,rely = 0.6,anchor = CENTER)

img = Label(root)
img.place(relx = 0.5,rely = 0.5,anchor=CENTER)

img2 = ImageTk.PhotoImage(Image.open('button.jpg'))

pokemon_list = [pikachu,abra,bulbasour,charmender,Iyvasour,jigglypuff,kadabra,meowth,nidoking,paras,ratata,spuirtle]
power_pokemon = [200,30,60,50,100,70,70,60,90,40,40,50]

player1_score = 0
def player1():
    global player1_score
    random_number = random.randint(0,11)
    random_pokemon = pokemon_list[random_number]
    img['image'] = random_pokemon
    random_power_list = power_pokemon[random_number]
    player1_score = player1_score + random_power_list
    
player2_score = 0
def player2():
    global player2_score
    random_number2 = random.randint(0,11)
    random_pokemon2 = pokemon_list[random_number2]
    img['image'] = random_pokemon2
    random_power_list2 = power_pokemon[random_number2]
    player2_score = player2_score + random_power_list2
    
player1_btn = Button(root,image=img2,command=player1)
player1_btn.place(relx=0.2,rely=0.7,anchor=CENTER)

player2_btn = Button(root,image=img2,command=player2)
player2_btn.place(relx=0.8,rely=0.7,anchor=CENTER)

mainloop()
