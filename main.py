import numpy as np
#from matplotlib import pyplot as plt
import PIL.Image
#import glob
from numpy import asarray
from tkinter import *

numm = 0
werr = 0
cyfra = np.zeros(10 * 12 * 7 * 5)
cyfra = cyfra.reshape(10, 12, 7, 5)
white = np.array([255,255,255,255])
#path = "/content/drive/My Drive/neuronowe/normalne/"
#path_noise = "/content/drive/My Drive/neuronowe/szumy/"
path = 'C:/Users/Jakub/Desktop/Neuronowe/normalne/'
path_noise = 'C:/Users/Jakub/Desktop/Neuronowe/szumy/'
for num in range(10):
    for wer in range(3):
        for szum in range(4):
            image = PIL.Image.open(path_noise + 's' + str(num) + '_' + str(wer) + '_' + str(szum) + '.png')
            data = np.array(image.getdata())

            pixel = np.zeros(35)
            #pixel = pixel.reshape(5, 7)
            j = 0
            for i in data:
                #print(data)
                if np.array_equal(white, i):
                    pixel[j] = 0
                else:
                    pixel[j] = 1
                j = j + 1

            x = 0
            y = 0
            for i in range(35):
                if x == 4:
                    x = 0
                    y = y + 1
                if y == 6:
                    y = 0
                cyfra[numm][werr][y][x] = pixel[i]
                x = x + 1
            werr = werr + 1
            if werr == 12:
                numm = numm + 1
                werr = 0
#print (cyfra)
'''
            for i in range(35):
                cyfra[numm][werr][i] = pixel[i]
            werr = werr + 1
            if werr == 12:
                numm = numm + 1
                werr = 0
'''
# wagi
waga = np.random.uniform(low=-1, high=1, size=350)
waga = waga.reshape(10, 35)
tety = np.random.uniform(low=-1, high=1, size=10)
zycie = np.zeros(10)
waga_MVP = np.copy(waga)
zycie_MVP = np.copy(zycie)
tety_MVP = np.copy(tety)

powtorz = 50000
for N in range(powtorz):
    ran_per = np.random.randint(low=0, high=10)
    ran_cyfr = np.random.randint(low=0, high=10)
    ran_wer = np.random.randint(low=0, high=12)
    #w = np.random.randint(low=0, high=4)

    ans = tety[ran_per]
    x = 0
    y = 0
    for i in range(35):
        if x == 4:
            x = 0
            y = y + 1
        if y == 6:
            y = 0
        ans = ans + waga[ran_per][i] * cyfra[ran_cyfr][ran_wer][y][x]
        x = x + 1
    if ans < 0:
        O = -1
    else:
        O = 1
    if ran_per == ran_cyfr:
        P = 1
    else:
        P = -1
    ERR = P - O

    if ERR == 0:
        zycie[ran_per] = zycie[ran_per] + 1

        if zycie[ran_per] > zycie_MVP[ran_per]:
            zycie_MVP[ran_per] = np.copy(zycie[ran_per])
            for k in range(35):
                waga_MVP[ran_per][k] = np.copy(waga[ran_per][k])
    else:
        zycie[ran_per] = 0
        x = 0
        y = 0
        for k in range(35):
            if x == 4:
                x = 0
                y = y + 1
            if y == 6:
                y = 0
            waga[ran_per][k] = waga[ran_per][k] + 0.1 * ERR * cyfra[ran_cyfr][ran_wer][y][x]
            x = x + 1
        for t in range(10):
            tety[ran_per] = tety[ran_per] + 0.1 * ERR

for i in range(10):
    if zycie[i] > zycie_MVP[i]:
        zycie_MVP[i] = np.copy(zycie[i])
        for k in range(35):
            waga_MVP[i][k] = np.copy(waga[i][k])
        for t in range(10):
            tety_MVP[t] = np.copy(tety[t])
print(zycie_MVP[0], zycie_MVP[1], zycie_MVP[2], zycie_MVP[3], zycie_MVP[4],
      zycie_MVP[5], zycie_MVP[6], zycie_MVP[7], zycie_MVP[8], zycie_MVP[9])
'''
# wagi
waga = np.random.uniform(low=-1, high=1, size=360)
waga = waga.reshape(10, 36)
zycie = np.zeros(10)
waga_MVP = np.copy(waga)
zycie_MVP = np.zeros(10)

powtorz = 50000
for N in range(powtorz):
    z = np.random.randint(low=0, high=10)
    o = np.random.randint(low=0, high=10)
    u = np.random.randint(low=0, high=12)

    ans = waga[z][35]
    for i in range(35):
        ans += waga[z][i] * cyfra[o][u][i]
    if ans < 0:
        O = -1
    else:
        O = 1
    if z == o:
        P = 1
    else:
        P = -1
    ERR = P - O

    if ERR == 0:
        zycie[z] += 1

        if zycie[z] > zycie_MVP[z]:
            zycie_MVP[z] = np.copy(zycie[z])
            for k in range(36):
                waga_MVP[z][k] = np.copy(waga[z][k])
    else:
        zycie[z] = 0
        for l in range(35):
            waga[z][l] = waga[z][l] + 0.1 * ERR * cyfra[o][u][l]
            waga[z][35] = waga[z][35] + 0.1 * ERR
for i in range(10):
    if zycie[i] > zycie_MVP[i]:
        # Perceptrony_tety_MVP[z] = np.copy(Perceptrony_tety[z])
        zycie_MVP[i] = np.copy(zycie[i])
        for k in range(36):
            waga_MVP[i][k] = np.copy(waga[i][k])
print(zycie_MVP[0], zycie_MVP[1], zycie_MVP[2], zycie_MVP[3], zycie_MVP[4],
      zycie_MVP[5], zycie_MVP[6], zycie_MVP[7], zycie_MVP[8], zycie_MVP[9])
'''
# Sprawdzanie poprawności na danych na których uczymy

ile = 0
perceptr = 0
waga = 0
ans = 0
for perceptr in range(10):
    for wer in range(12):
        for waga in range(10):
            ans = tety_MVP[waga]
            for i in range(35):
                if x == 4:
                    x = 0
                    y = y + 1
                if y == 6:
                    y = 0
                ans = ans + waga_MVP[waga][i] * cyfra[perceptr][wer][y][x]
                x = x + 1
            if ans == 0 or ans > 0:
                if waga == perceptr:
                    ile = ile + 1
print(ile, " / ", 150)

#GUI
root = Tk()
root.title("Neuronowe1")
root.geometry("150x200")
test = np.zeros(35)
for i in range(35):
    test[i] = -1
def paint(event):
    x1, y1 = (event.x), (event.y)
    k = 0
    for i in range(7):
        for j in range(5):
            if x1>j*20 and x1<(j*20+20) and y1>i*20 and y1<(i*20+20):
                wn.create_rectangle( (j*20, i*20), (j*20+20,i*20+20) , fill="black")
                test[k]=1
            k+=1
    checkResult()
def paint2(event):
    x1, y1 = (event.x), (event.y)
    k = 0
    for i in range(7):
        for j in range(5):
            if x1>j*20 and x1<(j*20+20) and y1>i*20 and y1<(i*20+20):
                wn.create_rectangle( (j*20, i*20), (j*20+20,i*20+20) , fill="white", outline="white")
                test[k]=-1
            k+=1
    checkResult()
def allClear():
    wn.delete("all")
    var.set("")
    for i in range(35):
        test[i] = -1
def checkResult():
    var.set("")
    txt = ""
    for z in range(10):
        ans = tety_MVP[z]
        for i in range(35):
            ans += waga_MVP[z][i] * test[i]
        if ans == 0 or ans > 0:
            #print(z)
            txt += str(z) + " "
    var.set(txt)

wn=Canvas(root, width=100, height=140, bg='white')
wn.bind('<Button-1>', paint)
wn.bind('<Button-3>', paint2)
wn.pack()
var = StringVar()
resultLabel = Label(textvariable=var, font = 14)

resultLabel.pack()
clear = Button(text="Clear", command=allClear)
clear.pack()
root.mainloop()