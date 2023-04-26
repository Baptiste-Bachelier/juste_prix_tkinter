# Jeu du juste Prix + interface fonctionnel

# Date de création: 13/04/2023
# 24/04/2023
# - jeu fonctionelle

# importation des bibliothèques
from tkinter import *
from random import *
import json
import math

# création de la fenètre Jeu du juste prix
interface = Tk()

# caractéristique de la fenètre
interface.title("Jeu du juste Prix") # titre
interface.iconbitmap('jp image\icon-game.ico') # icon
interface.geometry("800x500") # dimention
interface.maxsize(800,500) # taille maximal
interface.minsize(800,500) # taille minimal
interface.config(bg="white") # couleur

#################################################################################################################################################

# création de la première fenètre: intro_fonction
def intro_fonction():
    # ouverture des variabble de la fonction
    global data_exit_fonction, intro, clic_im_paire, clic_time, clic_normal, win_lose, stop_time, try_player, easy_start, normal_start, hard_start
    def data_exit_fonction():
        global nb_start
        with open('Game_Data.json', 'r+') as file:
            data = json.load(file)
            nb_start =data['nb_start']
    # chargement des données
    data_exit_fonction()
    # frame
    intro = Frame(interface, # chemin
                  )
     # titre
    intro_title = Label(intro, # chemin
                        text="Jeu du juste prix", # text
                        font=("colibri",50), # police et taille du text
                        pady=100 # taille du Label en y
                        )
    intro_title.pack()
    test_txt = Label(intro,
                     text= f"Test n° {nb_start}",
                     font=("colibri", 20)
                     )
    test_txt.pack(side="bottom", anchor="sw")
    # création des bouttons start/stat/quit
    #start
    start = Button(intro, # chemin
                   text="START", # text
                   font=("colibri",10), # police et taille du text
                   command= choice_fonction,
                   width= 10, # largeur du boutton 
                   pady=10, # hauteur du Button en y
                   padx=30 # hauteur du Button en x
                   )
    start.pack(pady=5)
    # stat
    stat = Button(intro, # chemin
                  text="STAT", # text
                  font=("colibri",10), # police et taille du text
                  width= 10, # largeur du boutton 
                  pady=10, # taille du Button en y
                  padx=30 # taille du Button en x
                  )
    stat.pack(pady=5) 
    # quit
    quitter = Button(intro, # chemin
                    text="QUITTER", # text
                    font=("colibri",10), # police et taille du text
                    command=interface.destroy, # commande                     
                    width= 10, # largeur du boutton 
                    pady=10, # taille du Button en y
                    padx=30, # taille du Button en x
                    )
    quitter.pack(pady=5)
    # affichage INTRO
    intro.pack(fill="both", expand=YES)

################################################################################################################################################     

# création de la deuxième fenètre: choice_fonction
def choice_fonction():
    intro.pack_forget()
    # variables globals
    global choice
    # frame
    choice = Frame(interface, # chemin
                   )
    # titre 
    choice_Label = Label(choice, # chemin
                         text="Choisissez un niveau de difficulté", # text
                         font=("colibri", 25),
                         )
    choice_Label.pack(pady=100)
    # création d'une frame pour et/des bouttons pour les niveaux
    lvl_button = Frame(choice, # chemin
                       )
    # boutton facile
    easy_button = Button(lvl_button, # chemin
                         text="1/Facile\n" # text
                              "Le chiffre à trouver est annoncé comme paire ou impaire parmi des nombres entiers", 
                         font=("colibri", 10),  # police et taille du text
                         command= lambda: (play_fonction(),parite_fonction(), easy_button_clic()), # active la commande easy
                         wraplength=200, # largeur maximum du texte
                         width=20, # largeur du boutton 
                         height=10, # longeur du boutton 
                         padx= 15 # taille du Button en x
                         )
    easy_button.pack(side="left",padx=5)
    # boutton normale
    normale_button = Button(lvl_button, # chemin
                            text="2/Normale\n" # text
                                 "Le chiffre à trouver est un nombre entier sans plus d'indication",
                            font=("colibri", 10),  # police et taille du text
                            command= lambda: (play_fonction(), normal_button_clic()), # active la commande normale
                            wraplength=200, # largeur maximum du texte
                            width=20, # largeur du boutton 
                            height=10, # longeur du boutton 
                            padx= 15 # taille du Button en x
                            )
    normale_button.pack(side="left", padx=5)
    # boutton hard
    hard_button = Button(lvl_button, # chemin
                         text="3/Difficile\n" # text
                              "Le chiffre à trouver est un nombre entier et il y a un limite de temps",
                         font=("colibri", 10),  # police et taille du text
                         command=lambda: (play_fonction(),count_fonction(), hard_button_clic()), # active la commande difficile
                         wraplength=200, # largeur maximum du texte
                         width=20, # largeur du boutton 
                         height=10, # longeur du boutton 
                         padx= 15 # taille du Button en x
                         )
    hard_button.pack(side="left",padx=5)
    # affichage de lvl_button
    lvl_button.pack(anchor="center", pady= 10)
    # affichage choice
    choice.pack(fill="both", expand=TRUE)
    
################################################################################################################################################

# création de la deuxième fenètre: play_fonction
def play_fonction():
    choice.pack_forget()
    # variables globals
    global parite_fonction, count_fonction, easy_button_clic, normal_button_clic, hard_button_clic, minimum_entry, maximum_entry, juste_prix_entry, lim_button, juste_prix_validation
    play = Frame(interface, # chemin
                  )
        # création du conteur de temps
    def count_fonction():
        global count_text
        count_text = Label(play,
                            text=None,
                            font=("colibri", 40),
                            )
        count_text.pack(pady=50)
        # création de l'affichage de la parité
    def parite_fonction():
        global parite
        parite = Label(play,
                        text=None,
                        font=("colibri", 20),
                        ) 
        parite.pack(pady=75)    
    # information du minimum
    min_play_text = Label(play, # chemin
                           text=None, # text
                           font=("colibri", 40),
                           wraplength=350,
                           height=3,
                           width=5
                           )
    min_play_text.pack(side= "left", anchor="ne",padx= 75, pady=75)
     # information du maximum
    max_play_text = Label(play, # chemin
                           text=None, # text
                           font=("colibri", 40),
                           wraplength=350,
                           height=3,
                           width=5                           
                           )
    max_play_text.pack(side= "right", anchor="ne",padx=75, pady=75)
    # entrée du "juste prix"
    juste_prix_entry = Entry(play, # chemin
                             textvariable=None, # text
                             font=("colibri", 15), # police et taille du text
                             validate="key", # règle de validation
                             )
    juste_prix_entry.place(x=290, y=180)
    juste_prix_entry.configure(
        validatecommand=(juste_prix_entry.register(number_isdigit), '%S')
    )
    juste_prix_entry.bind("<KeyRelease>", lambda event: entry_ok_player())
    # boutton valiter
    juste_prix_validation = Button(play, # chemin
                                    text="valider", # text
                                    font=("colibri", 12), # police et taille du text
                                    state=DISABLED, # etat du button
                                    command= lambda: (game()),
                                    width=24
                                    )
    juste_prix_validation.place(x=290, y=210)
    # création conteur d'essaie
    try_player_text = Label(play,
                            text=None,
                            font=("colibri", 15),
                            )
    try_player_text.pack()
    # affichage du niveau de difficulté
    lvl_text = Label(play,
                     text= None,
                     font=("colibri", 16)
                     )
    lvl_text.place(x=0, y=0)

    
    ################################## frame min_max ######################################

    min_max = Frame(play, # chemin
                     )
    # minimum
    minimum_text = Label(min_max, # chemin
                          text="Le minimum est de:", # text
                          font=("colibri", 10), # police et taille du text
                          )
    minimum_entry = Entry(min_max, # chemin
                           text=None, # text
                           font=("colibri", 10), # police et taille du text
                           validate="key", # règle de validation
                           )
    minimum_entry.configure(
        validatecommand=(
            minimum_entry.register(number_isdigit), '%S'
            )
        )
    # enpaquetage de minimum
    minimum_text.pack(pady=5, 
                       padx= 50
                       )
    minimum_entry.pack(pady=5, 
                        padx= 50
                        )
    # maximum
    maximum_text = Label(min_max, # chemin
                          text="Le maximum est de:", # text
                          font=("colibri", 10), # police et taille du text
                          )
    maximum_entry = Entry(min_max, # chemin
                           text=None,
                           font=("colibri", 10), # police et taille du text
                           validate="key", # règle de validation
                           )
    maximum_entry.configure(
        validatecommand=(
            maximum_entry.register(number_isdigit), '%S'
            )
        )
    # enpaquetage du maximum
    maximum_text.pack(pady=5, 
                      padx= 50
                      )
    maximum_entry.pack(pady=5, 
                       padx= 50
                       )
    minimum_entry.bind("<KeyRelease>", lambda event: entry_ok())
    maximum_entry.bind("<KeyRelease>", lambda event: entry_ok())
    # boutton valider
    lim_button = Button(min_max, # chemin
                         text="valider", # text
                         font=("colibri", 10), # police et taille du text
                         command=lambda: (key_fonction(), 
                                          min_max.place_forget(), 
                                          min_play_text.config(text=minimum_entry.get()),
                                          max_play_text.config(text=maximum_entry.get()),
                                          ), # a définir
                         state=DISABLED # etat du button
                         )
    lim_button.pack(fill="x", 
                    pady=5, 
                    padx= 50
                    )
    # affichage de min_max
    min_max.place(x=277, y=150)
    
################################## fin de frame min_max ######################################
    def win_lose_fonction():
        win_lose_frame = Frame(play,
                                   )
        win_lose_text = Label(win_lose_frame,
                              text=win_lose,
                              font=("colibri",40),
                              )
        restart = Button(win_lose_frame,
                         text="acceuil",
                         font=("colibri", 15),
                         command=lambda : (intro_fonction(), play.pack_forget())
                         )
        win_lose_text.pack(side="top", anchor="n")
        restart.pack(side="bottom", anchor="s", padx=5, fill="x")
        win_lose_frame.place(x=195, y=150)
        minimum_entry.delete(0, END)
        maximum_entry.delete(0,END)
        # retour a la normale    
        
############################################# Fonction jeu ###################################################################################################        

    
    def countdown():
        global win_lose, all_time, time_used_players
        time_used_players += 1
        all_time-= 1
        if all_time >= 0 and stop_time == False:
            count_text.config(text=str(all_time))
            play.after(1000, countdown)  
        if all_time == 0 and stop_time == False:
            data_entry_fonction()
            win_lose = "vous avez perdu" 
            win_lose_fonction()
        return all_time    
            
            
                
    # fonction key
    def key_fonction():
        global key, all_time, save_all_time
        key_list = [ i for i in range(int(minimum_entry.get()), int(maximum_entry.get())+1)]
        shuffle(key_list)
        key = key_list[0]
        if clic_im_paire == True: 
            if key%2 == 0:
                parite.config(text="pair")
            else:
                parite.config(text="impair")
        all_time = 0        
        if clic_time == True:
            ecart = int(maximum_entry.get()) -int(minimum_entry.get())
            if ecart == 0:
                all_time = 2
            else:    
                all_time = round(10+ math.log((ecart**2/2))+1)
                save_all_time = all_time
            countdown()
                              
        
    def game():
        global win_lose, stop_time, try_player, time_used_players
        try_player += 1
        try_player_text.config(text="nombre d'essai: {}".format(try_player))
        if key > int(juste_prix_entry.get()):
            min_play_text.config(text=juste_prix_entry.get())
        elif key < int(juste_prix_entry.get()): 
            max_play_text.config(text=juste_prix_entry.get())
        elif key == int(juste_prix_entry.get()):
            stop_time = True
            data_entry_fonction()
            win_lose = "Vous avez gagné"
            win_lose_fonction()
            time_used_players = 0
        juste_prix_entry.delete(0,'end')
        juste_prix_validation.config(state=DISABLED)
###############################################################################################################################################

    def data_entry_fonction():
        with open('Game_Data.json', 'r+') as file:
            data = json.load(file)
        with open('Game_Data.json', 'w+') as file:
            data['nb_start'] += 1
            data['nb_start_easy'] += 1 if easy_start == True else 0
            data['nb_start_normal'] += 1 if normal_start == True else 0
            data['nb_start_hard'] += 1 if hard_start == True else 0
            data['lim_minimum'].append(int(minimum_entry.get()))
            data['lim_maximum'].append(int(maximum_entry.get()))
            data['key'].append(key)
            data['time_used'].append(time_used_players) if hard_start == True else None
            data['lim_time'].append(save_all_time) if hard_start == True else None
            json.dump(data, file)
            file.close()             
        
###############################################################################################################################################               
        
    def easy_button_clic():
        global clic_im_paire, easy_start
        easy_start += 1
        clic_im_paire = True
        lvl_text.config(text="Facile")
        return clic_im_paire, easy_start
    
    def normal_button_clic():
        global normal_start, clic_normal
        clic_normal = True
        normal_start += 1
        lvl_text.config(text="Normal")
        return clic_normal, normal_start
    
    def hard_button_clic():
        global clic_time, hard_start
        hard_start += 1
        clic_time = True
        lvl_text.config(text="Difficile")
        return clic_time, hard_start         
        
################################################################################################################################################

    # affichage de play
    play.pack(fill="both", expand=TRUE)    
    

################################################################################################################################################

    # validation entrer rempli
    def entry_ok():
        if minimum_entry.get() != '' and maximum_entry.get() != '' and int(minimum_entry.get()) <= int(maximum_entry.get()):
            lim_button.config(state=NORMAL)
        else:
            lim_button.config(state=DISABLED) 
    
    def entry_ok_player():
        if juste_prix_entry.get() != '' and int(min_play_text.cget("text")) <= int(juste_prix_entry.get()) <= int(max_play_text.cget("text")):
            juste_prix_validation.config(state=NORMAL)
        else:     
            juste_prix_validation.config(state=DISABLED)
            
# validation chiffre 
def number_isdigit(char):
    return char.isdigit()               
                  
              
        

################################################################################################################################################

   # variable
clic_im_paire = False
clic_time = False
clic_normal = False
win_lose = None
stop_time = False
easy_start = 0
normal_start = 0
hard_start = 0
try_player = 0
time_used_players = 0



################################################################################################################################################


# lancement du jeu
intro_fonction()
# affichage de la fonction
interface.mainloop()     