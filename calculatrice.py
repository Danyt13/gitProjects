import tkinter as tk

racine = tk.Tk()
racine.title("Calculatrice")



def carre0():
    x = 1
    y = 0
    print("0")


#création de widgets
bouton_carre0 = tk.Button(racine, text="0", command=carre0)
bouton_carre1 = tk.Button(racine, text="1")
bouton_carre2 = tk.Button(racine, text="2")
bouton_carre3 = tk.Button(racine, text="3")
bouton_carre4 = tk.Button(racine, text="4")
bouton_carre5 = tk.Button(racine, text="5")
bouton_carre6 = tk.Button(racine, text="6")
bouton_carre7 = tk.Button(racine, text="7")
bouton_carre8 = tk.Button(racine, text="8")
bouton_carre9 = tk.Button(racine, text="9")
bouton_carre10 = tk.Button(racine, text="+")
bouton_carre11 = tk.Button(racine, text="-")
bouton_carre12 = tk.Button(racine, text="*")
bouton_carre13 = tk.Button(racine, text="/")
bouton_carre14 = tk.Button(racine, text="=")
bouton_carre15 = tk.Button(racine, text=".")
canvas = tk.Canvas(racine, width=250, height=90, bg="black", bd=10, relief="raised")
canvas.grid(column=0, row=5, rowspan=4)


#placement des widgets
bouton_carre0.grid(column=1, row=8)
bouton_carre1.grid(column=1, row=7)
bouton_carre2.grid(column=2, row=7)
bouton_carre3.grid(column=3, row=7)
bouton_carre4.grid(column=1, row=6)
bouton_carre5.grid(column=2, row=6)
bouton_carre6.grid(column=3, row=6)
bouton_carre7.grid(column=1, row=5)
bouton_carre8.grid(column=2, row=5)
bouton_carre9.grid(column=3, row=5)
bouton_carre10.grid(column=4, row=8)
bouton_carre11.grid(column=4, row=7)
bouton_carre12.grid(column=4, row=6)
bouton_carre13.grid(column=4, row=5)
bouton_carre14.grid(column=3, row=8)
bouton_carre15.grid(column=2, row=8)






racine.mainloop()