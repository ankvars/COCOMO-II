import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("COCOMO SIMULATOR")
LARGE_FONT = ("Verdana", 18)
SMALL_FONT = ("Verdana", 13)

def show_frame(frame):
    frame.tkraise()


pageone = tk.Frame(window, width=1024, height=600)
pagetwo = tk.Frame(window, width=1024, height=600)
pagethree = tk.Frame(window, width=1024, height=600)
pagefour = tk.Frame(window, width=1024, height=600)
pagefive = tk.Frame(window, width=1024, height=600)
pagesix = tk.Frame(window, width=1024, height=600)
pageseven = tk.Frame(window, width=1024, height=600)

pageone.tkraise()

for frame in (pageone, pagetwo, pagethree, pagefour, pagefive, pagesix,pageseven):
    frame.place(x=0, y=0)


def pagepanch():

    EAF = 1.0

    if ccdloc1.current() == 0:
        EAF = EAF*(.75)
    elif cdloc1.get() == "LOW":
        EAF = EAF*(.88)
    elif cdloc1.get() == "NOMINAL":
        EAF = EAF*(1)
    elif (cdloc1.get() == "HIGH"):
        EAF = EAF*(1.15)
    elif (cdloc1.get() == "VERY HIGH"):
        EAF = EAF*(1.40)

    if ccdloc2.current() == 0:
        EAF = EAF*(.94)
    if ccdloc2.current() == 1:
        EAF = EAF * (1)
    if cdloc2.get() == "HIGH":
        EAF = EAF*(1.08)
    if cdloc2.get() == "VERY HIGH":
        EAF = EAF*(1.16)

    if cdloc3.get() == "VERY LOW":
        EAF = EAF*(.70)
    elif (cdloc3.get() == "LOW"):
        EAF = EAF*(.85)
    elif (cdloc3.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cdloc3.get() == "HIGH"):
        EAF = EAF*(1.15)
    elif (cdloc3.get() == "VERY HIGH"):
        EAF = EAF*(1.30)

    if cdloc4.get() == "NOMINAL":
        EAF = EAF*(1)
    elif cdloc4.get() == "HIGH":
        EAF = EAF*(1.11)
    elif cdloc4.get() == "VERY HIGH":
        EAF = EAF*(1.30)

    if cdloc5.get() == "NOMINAL":
        EAF = EAF*(1)
    elif cdloc5.get() == "HIGH":
        EAF = EAF*(1.06)
    elif cdloc5.get() == "VERY HIGH":
        EAF = EAF*(1.21)

    if (cdloc6.get() == "LOW"):
        EAF = EAF*(.87)
    elif (cdloc6.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cdloc6.get() == "HIGH"):
        EAF = EAF*(1.15)
    elif (cdloc6.get() == "VERY HIGH"):
        EAF = EAF*(1.30)

    if (cdloc7.get() == "LOW"):
        EAF = EAF*(.94)
    elif (cdloc7.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cdloc7.get() == "HIGH"):
        EAF = EAF*(1.07)
    elif (cdloc7.get() == "VERY HIGH"):
        EAF = EAF*(1.15)

    if (cdloc8.get() == "VERY LOW"):
        EAF = EAF*(1.46)
    elif (cdloc8.get() == "LOW"):
        EAF = EAF*(1.19)
    elif (cdloc8.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cdloc8.get() == "HIGH"):
        EAF = EAF*(.86)
    elif (cdloc8.get() == "VERY HIGH"):
        EAF = EAF*(.71)

    if (cdloc9.get() == "VERY LOW"):
        EAF = EAF*(1.29)
    elif (cdloc9.get() == "LOW"):
        EAF = EAF*(1.13)
    elif (cdloc9.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cdloc9.get() == "HIGH"):
        EAF = EAF*(.91)
    elif (cdloc9.get() == "VERY HIGH"):
        EAF = EAF*(.82)

    if (cdloc10.get() == "VERY LOW"):
        EAF = EAF*(1.42)
    elif (cdloc10.get() == "LOW"):
        EAF = EAF*(1.17)
    elif (cdloc10.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cdloc10.get() == "HIGH"):
        EAF = EAF*(.86)
    elif (cdloc10.get() == "VERY HIGH"):
        EAF = EAF*(.70)

    if (cdloc11.get() == "VERY LOW"):
        EAF = EAF * (1.24)
    elif (cdloc11.get() == "LOW"):
        EAF = EAF * (1.10)
    elif (cdloc11.get() == "NOMINAL"):
        EAF = EAF * (1)
    elif (cdloc11.get() == "HIGH"):
        EAF = EAF * (.90)

    if (cdloc12.get() == "VERY LOW"):
        EAF = EAF*(1.14)
    elif (cdloc12.get() == "LOW"):
        EAF = EAF*(1.07)
    elif (cdloc12.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cdloc12.get() == "HIGH"):
        EAF = EAF*(.95)

    if (cdloc13.get() == "VERY LOW"):
        EAF = EAF*(1.24)
    elif (cdloc13.get() == "LOW"):
        EAF = EAF*(1.10)
    elif (cdloc13.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cdloc13.get() == "HIGH"):
        EAF = EAF*(.91)
    elif (cdloc13.get() == "VERY HIGH"):
        EAF = EAF*(.82)

    if (cdloc14.get() == "VERY LOW"):
        EAF = EAF*(1.24)
    elif (cdloc14.get() == "LOW"):
        EAF = EAF*(1.10)
    elif (cdloc14.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cdloc14.get() == "HIGH"):
        EAF = EAF*(.91)
    elif (cdloc14.get() == "VERY HIGH"):
        EAF = EAF*(.83)

    if (cdloc15.get() == "VERY LOW"):
        EAF = EAF*(1.23)
    elif (cdloc15.get() == "LOW"):
        EAF = EAF*(1.08)
    elif (cdloc15.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cdloc15.get() == "HIGH"):
        EAF = EAF*(1.04)
    elif (cdloc15.get() == "VERY HIGH"):
        EAF = EAF*(1.10)

    if typesystemloc.current() == 0:
        a = 2.4
        b = 1.05
        x = 0.38

    elif typesystemloc.current() == 1:
        a = 3.0
        b = 1.12
        x = .35

    else:
        a = 3.6
        b = 1.20
        x = .32

    effort = a * ((int(eloc.get())/1000) ** b) * EAF
    tdev = 2.5 * ((effort) ** x)
    cost = tdev * float(ecmm.get())


    pagesix = tk.Frame(window, width=1024, height=600)
    pagesix.place(x=0,y=0)
    leffort = tk.Label(pagesix, text= "Required Effort is :    " + str(effort) + "  Person Month", font = LARGE_FONT, background="black", foreground="red")
    leffort.place(x=20, y=50)

    ltdev = tk.Label(pagesix, text="Development time is :    " + str(tdev) + "  Months", font=LARGE_FONT, background="black", foreground="red")
    ltdev.place(x=20, y=100)

    lcost = tk.Label(pagesix, text="Total Cost is :    " + str(cost) + "  dollars", font=LARGE_FONT, background="black", foreground="red")
    lcost.place(x=20, y=150)

    bnext = tk.Button(pagesix, text="Calculate Again", width=15,background="grey", command=lambda :show_frame(pagetwo))
    bnext.place(x=600, y=500)


    bthank = tk.Button(pagesix, text="ThankYou", width=15, background="grey", command=lambda:show_frame(pageseven))
    bthank.place(x=800, y=500)



def enter():
    show_frame(pagetwo)

def about():
    messagebox.showinfo("About", "This Cocomo Simulator is developed by Ankit Varshney\nFaculty No. : 17COB034\nSerial No. : 13")

def exitt():
    if tk.messagebox.askokcancel("Warning", "Do you want to exit"):
        window.destroy()


menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Enter", command=lambda:show_frame(pagetwo))
filemenu.add_command(label="About", command=about)
filemenu.add_command(label="Exit", command=exitt)

menubar.add_cascade(label="File", menu=filemenu)
window.config(menu=menubar)


#pageone

label = tk.Label(pageone, text="COCOMO SIMULATOR", font=("Verdana", 52), foreground="red", background="black")
label.place(x=150, y=50)

benter = tk.Button(pageone, text="Enter", width=20, background="grey", command=lambda:show_frame(pagetwo))
benter.place(x=450, y=300)

babout = tk.Button(pageone ,text="About", width=20, background="grey", command=about)
babout.place(x=450, y=400)

bexit = tk.Button(pageone, text="Exit", width=20, background="grey", command=exitt)
bexit.place(x=450, y=500)


#pagetwo

ltype=tk.Label(pagetwo, text="Calculate Effort and Cost By : ", font=LARGE_FONT)
ltype.place(x=10, y=20)

knowchoice=tk.StringVar()
choice = ("Lines Of Code", "Function Point")
choicecombo = ttk.Combobox(pagetwo, textvariable=knowchoice, state="readonly")
choicecombo.place(x=400, y=30)
choicecombo['values']=choice


bback=tk.Button(pagetwo, text="Back", width=10, background="grey", command=lambda:show_frame(pageone))
bback.place(x=750,y=550)

def ksloc():
    if choicecombo.current() == 0:
        show_frame(pagethree)
    elif choicecombo.current() == 1:
        show_frame(pagefour)

bnext=tk.Button(pagetwo, text="Next", width=10, background="grey", command=ksloc)
bnext.place(x=850, y=550)

#pagethree


ltype = tk.Label(pagethree, text="Type of system : ", font=LARGE_FONT)
ltype.place(x=10, y=20)
knowtype = tk.StringVar()
type = ("Organic", "Semi Detached", "Embedded")
typesystemloc = ttk.Combobox(pagethree, textvariable=knowtype, state="readonly")
typesystemloc.place(x=250, y=30)
typesystemloc['values'] = type
typesystemloc.current(0)
chosentype = typesystemloc.current()

lksloc=tk.Label(pagethree,text="Enter the LOC : ", font=LARGE_FONT)
lksloc.place(x=10, y=60)

eloc = ttk.Entry(pagethree, width=40)
eloc.place(x=250, y=70)

#Cost per month

lcm = ttk.Label(pagethree, text="Cost per Month", font = LARGE_FONT)
lcm.place(x=650, y=40)
ld = ttk.Label(pagethree, text="(in dollars)", font = SMALL_FONT)
ld.place(x=670, y=70)
ecmm = ttk.Entry(pagethree, width=15)
ecmm.place(x=850, y=45)


#Cost Drivers

lcdloc = ttk.Label(pagethree, text="Cost Drivers", font=LARGE_FONT)
lcdloc.place(x=20, y=120)

lcdloc1 = ttk.Label(pagethree, text="1- Required Software Reliability", font=SMALL_FONT)
lcdloc1.place(x=60, y=150)
cdloc1 = tk.StringVar()
ccdloc1 = ttk.Combobox(pagethree, width=10, textvariable=cdloc1, state="readonly")
ccdloc1.place(x=500, y=150)
ccdloc1['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccdloc1.current(2)



lcdloc2 = ttk.Label(pagethree, text="2- Size of Application Database", font=SMALL_FONT)
lcdloc2.place(x=60, y=175)
cdloc2 = tk.StringVar()
ccdloc2 = ttk.Combobox(pagethree, textvariable=cdloc2, width=10, state="readonly")
ccdloc2.place(x=500, y=175)
ccdloc2['values'] = ("LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccdloc2.current(1)


lcdloc3 = ttk.Label(pagethree, text="3- Complexity of The Product", font=SMALL_FONT)
lcdloc3.place(x=60, y=200)
cdloc3 = tk.StringVar()
ccdloc3 = ttk.Combobox(pagethree, textvariable=cdloc3, width=10, state="readonly")
ccdloc3.place(x=500, y=200)
ccdloc3['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccdloc3.current(2)


lcdloc4 = ttk.Label(pagethree, text="4- Runtime Performance Constraints", font=SMALL_FONT)
lcdloc4.place(x=60, y=225)
cdloc4 = tk.StringVar()
ccdloc4 = ttk.Combobox(pagethree, textvariable=cdloc4, width=10, state="readonly")
ccdloc4.place(x=500, y=225)
ccdloc4['values'] = ("NOMINAL", "HIGH", "VERY HIGH")
ccdloc4.current(0)


lcdloc5 = ttk.Label(pagethree, text="5- Memory Constraints", font=SMALL_FONT)
lcdloc5.place(x=60, y=250)
cdloc5 = tk.StringVar()
ccdloc5 = ttk.Combobox(pagethree, textvariable=cdloc5, width=10, state="readonly")
ccdloc5.place(x=500, y=250)
ccdloc5['values'] = ("NOMINAL", "HIGH", "VERY HIGH")
ccdloc5.current(0)


lcdloc6 = ttk.Label(pagethree, text="6- Volatility of the virtual machine environment", font=SMALL_FONT)
lcdloc6.place(x=60, y=275)
cdloc6 = tk.StringVar()
ccdloc6 = ttk.Combobox(pagethree, textvariable=cdloc6, width=10, state="readonly")
ccdloc6.place(x=500, y=275)
ccdloc6['values'] = ("LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccdloc6.current(1)


lcdloc7 = ttk.Label(pagethree, text="7- Required turnabout time", font=SMALL_FONT)
lcdloc7.place(x=60, y=300)
cdloc7 = tk.StringVar()
ccdloc7 = ttk.Combobox(pagethree, textvariable=cdloc7, width=10, state="readonly")
ccdloc7.place(x=500, y=300)
ccdloc7['values'] = ("LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccdloc7.current(1)


lcdloc8 = ttk.Label(pagethree, text="8- Analyst capability", font=SMALL_FONT)
lcdloc8.place(x=60, y=325)
cdloc8 = tk.StringVar()
ccdloc8 = ttk.Combobox(pagethree, textvariable=cdloc8, width=10, state="readonly")
ccdloc8.place(x=500, y=325)
ccdloc8['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccdloc8.current(2)

lcdloc9 = ttk.Label(pagethree, text="9- Applications experience ", font=SMALL_FONT)
lcdloc9.place(x=60, y=350)
cdloc9 = tk.StringVar()
ccdloc9 = ttk.Combobox(pagethree, textvariable=cdloc9, width=10, state="readonly")
ccdloc9.place(x=500, y=350)
ccdloc9['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccdloc9.current(2)


lcdloc10 = ttk.Label(pagethree, text="10- Software engineer capability", font=SMALL_FONT)
lcdloc10.place(x=60, y=375)
cdloc10 = tk.StringVar()
ccdloc10 = ttk.Combobox(pagethree, textvariable=cdloc10, width=10, state="readonly")
ccdloc10.place(x=500, y=375)
ccdloc10['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccdloc10.current(2)


lcdloc11 = ttk.Label(pagethree, text="11- Virtual machine experience", font=SMALL_FONT)
lcdloc11.place(x=60, y=400)
cdloc11 = tk.StringVar()
ccdloc11 = ttk.Combobox(pagethree, textvariable=cdloc11, width=10, state="readonly")
ccdloc11.place(x=500, y=400)
ccdloc11['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH")
ccdloc11.current(2)


lcdloc12 = ttk.Label(pagethree, text="12- Programming language experience", font=SMALL_FONT)
lcdloc12.place(x=60, y=425)
cdloc12 = tk.StringVar()
ccdloc12 = ttk.Combobox(pagethree, textvariable=cdloc12, width=10, state="readonly")
ccdloc12.place(x=500, y=425)
ccdloc12['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH")
ccdloc12.current(2)


lcdloc13 = ttk.Label(pagethree, text="13- Application of software engineering methods", font=SMALL_FONT)
lcdloc13.place(x=60, y=450)
cdloc13 = tk.StringVar()
ccdloc13 = ttk.Combobox(pagethree, textvariable=cdloc13, width=10, state="readonly")
ccdloc13.place(x=500, y=450)
ccdloc13['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccdloc13.current(2)


lcdloc14 = ttk.Label(pagethree, text="14- Use of software tools", font=SMALL_FONT)
lcdloc14.place(x=60, y=475)
cdloc14 = tk.StringVar()
ccdloc14 = ttk.Combobox(pagethree, textvariable=cdloc14, width=10, state="readonly")
ccdloc14.place(x=500, y=475)
ccdloc14['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccdloc14.current(2)


lcdloc15 = ttk.Label(pagethree, text="15- Required development schedule", font=SMALL_FONT)
lcdloc15.place(x=60, y=500)
cdloc15 = tk.StringVar()
ccdloc15 = ttk.Combobox(pagethree, textvariable=cdloc15, width=10, state="readonly")
ccdloc15.place(x=500, y=500)
ccdloc15['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccdloc15.current(2)


bback = tk.Button(pagethree, text="Back", width=10, background = "grey", command = lambda:show_frame(pagetwo))
bback.place(x=750,y=550)

bnext=tk.Button(pagethree, text="Next", width=10, background="grey", command=pagepanch)
bnext.place(x=850, y=550)


#pagefour

ltype = tk.Label(pagefour, text="Type of system : ", font=LARGE_FONT)
ltype.place(x=10, y=20)
knowtype = tk.StringVar()
type = ("Organic", "Semi Detached", "Embedded")
typesystem = ttk.Combobox(pagefour, textvariable=knowtype, state="readonly")
typesystem.place(x=250, y=30)
typesystem['values'] = type
typesystem.current(0)
chosentype = typesystem.current()



#complexity factors

lcf = ttk.Label(pagefour, text="Complexity Factors", font=LARGE_FONT)
lcf.place(x=10,y=100)

digit = (0, 1, 2, 3, 4, 5)

lcf1 = ttk.Label(pagefour, text="1- Backup and recovery", font=SMALL_FONT)
lcf1.place(x=20, y=150)
cf1 = tk.IntVar()
ccf1=ttk.Combobox(pagefour, textvariable=cf1, width=4, state="readonly")
ccf1.place(x=400, y=155)
ccf1['values'] = digit
ccf1.current(4)

lcf2 = ttk.Label(pagefour, text="2- Data Communication", font=SMALL_FONT)
lcf2.place(x=20, y=175)
cf2 = tk.IntVar()
ccf2=ttk.Combobox(pagefour, textvariable=cf2, width=4, state="readonly")
ccf2.place(x=400, y=180)
ccf2['values'] = digit
ccf2.current(4)

lcf3 = ttk.Label(pagefour, text="3- Distributed Processing", font=SMALL_FONT)
lcf3.place(x=20, y=200)
cf3 = tk.IntVar()
ccf3=ttk.Combobox(pagefour, textvariable=cf3, width=4, state="readonly")
ccf3.place(x=400, y=205)
ccf3['values'] = digit
ccf3.current(4)

lcf4 = ttk.Label(pagefour, text="4- Performance critical", font=SMALL_FONT)
lcf4.place(x=20, y=225)
cf4 = tk.IntVar()
ccf4=ttk.Combobox(pagefour, textvariable=cf4, width=4, state="readonly")
ccf4.place(x=400, y=230)
ccf4['values'] = digit
ccf4.current(4)

lcf5 = ttk.Label(pagefour, text="5- Existing operating environment", font=SMALL_FONT)
lcf5.place(x=20, y=250)
cf5 = tk.IntVar()
ccf5=ttk.Combobox(pagefour, textvariable=cf5, width=4, state="readonly")
ccf5.place(x=400, y=255)
ccf5['values'] = digit
ccf5.current(4)

lcf6 = ttk.Label(pagefour, text="6- On-line data entry", font=SMALL_FONT)
lcf6.place(x=20, y=275)
cf6 = tk.IntVar()
ccf6=ttk.Combobox(pagefour, textvariable=cf6, width=4, state="readonly")
ccf6.place(x=400, y=280)
ccf6['values'] = digit
ccf6.current(4)

lcf7 = ttk.Label(pagefour, text="7- Input transaction over multiple screens", font=SMALL_FONT)
lcf7.place(x=20, y=300)
cf7 = tk.IntVar()
ccf7=ttk.Combobox(pagefour, textvariable=cf7, width=4, state="readonly")
ccf7.place(x=400, y=305)
ccf7['values'] = digit
ccf7.current(4)

lcf8 = ttk.Label(pagefour, text="8- Master files updated online", font=SMALL_FONT)
lcf8.place(x=20, y=325)
cf8 = tk.IntVar()
ccf8=ttk.Combobox(pagefour, textvariable=cf8, width=4, state="readonly")
ccf8.place(x=400, y=330)
ccf8['values'] = digit
ccf8.current(4)

lcf9 = ttk.Label(pagefour, text="9- Information domain values complex", font=SMALL_FONT)
lcf9.place(x=20, y=350)
cf9 = tk.IntVar()
ccf9 = ttk.Combobox(pagefour, textvariable=cf9, width=4, state="readonly")
ccf9.place(x=400, y=355)
ccf9['values'] = digit
ccf9.current(4)

lcf10 = ttk.Label(pagefour, text="10- Internal Processing complex", font=SMALL_FONT)
lcf10.place(x=20, y=375)
cf10 = tk.IntVar()
ccf10=ttk.Combobox(pagefour, textvariable=cf10, width=4, state="readonly")
ccf10.place(x=400, y=380)
ccf10['values'] = digit
ccf10.current(4)

lcf11 = ttk.Label(pagefour, text="11- Code designed for reuse", font=SMALL_FONT)
lcf11.place(x=20, y=400)
cf11 = tk.IntVar()
ccf11 = ttk.Combobox(pagefour, textvariable=cf11, width=4, state="readonly")
ccf11.place(x=400, y=405)
ccf11['values'] = digit
ccf11.current(4)

lcf12 = ttk.Label(pagefour, text="12- Conversion/installation in design", font=SMALL_FONT)
lcf12.place(x=20, y=425)
cf12 = tk.IntVar()
ccf12 = ttk.Combobox(pagefour, textvariable=cf12, width=4, state="readonly")
ccf12.place(x=400, y=430)
ccf12['values'] = digit
ccf12.current(4)

lcf13 = ttk.Label(pagefour, text="13- Multiple installations", font=SMALL_FONT)
lcf13.place(x=20, y=450)
cf13 = tk.IntVar()
ccf13 = ttk.Combobox(pagefour, textvariable=cf13, width=4, state="readonly")
ccf13.place(x=400, y=455)
ccf13['values'] = digit
ccf13.current(4)

lcf14 = ttk.Label(pagefour, text="14- Application designed for change", font=SMALL_FONT)
lcf14.place(x=20, y=475)
cf14 = tk.IntVar()
ccf14 = ttk.Combobox(pagefour, textvariable=cf14, width=4, state="readonly")
ccf14.place(x=400, y=480)
ccf14['values'] = digit
ccf14.current(4)


#Cost Drivers

lcd = ttk.Label(pagefour, text="Cost Drivers", font=LARGE_FONT)
lcd.place(x=470, y=100)

lcd1 = ttk.Label(pagefour, text="1- Required Software Reliability", font=SMALL_FONT)
lcd1.place(x=480, y=150)
cd1 = tk.StringVar()
ccd1 = ttk.Combobox(pagefour, textvariable=cd1, width=10, state="readonly")
ccd1.place(x=920, y=150)
ccd1['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccd1.current(2)

lcd2 = ttk.Label(pagefour, text="2- Size of Application Database", font=SMALL_FONT)
lcd2.place(x=480, y=175)
cd2 = tk.StringVar()
ccd2 = ttk.Combobox(pagefour, textvariable=cd2, width=10, state="readonly")
ccd2.place(x=920, y=175)
ccd2['values'] = ("LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccd2.current(1)

lcd3 = ttk.Label(pagefour, text="3- Complexity of The Product", font=SMALL_FONT)
lcd3.place(x=480, y=200)
cd3 = tk.StringVar()
ccd3 = ttk.Combobox(pagefour, textvariable=cd3, width=10, state="readonly")
ccd3.place(x=920, y=200)
ccd3['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccd3.current(2)

lcd4 = ttk.Label(pagefour, text="4- Runtime Performance Constraints", font=SMALL_FONT)
lcd4.place(x=480, y=225)
cd4 = tk.StringVar()
ccd4 = ttk.Combobox(pagefour, textvariable=cd4, width=10, state="readonly")
ccd4.place(x=920, y=225)
ccd4['values'] = ("NOMINAL", "HIGH", "VERY HIGH")
ccd4.current(0)

lcd5 = ttk.Label(pagefour, text="5- Memory Constraints", font=SMALL_FONT)
lcd5.place(x=480, y=250)
cd5 = tk.StringVar()
ccd5 = ttk.Combobox(pagefour, textvariable=cd5, width=10, state="readonly")
ccd5.place(x=920, y=250)
ccd5['values'] = ("NOMINAL", "HIGH", "VERY HIGH")
ccd5.current(0)

lcd6 = ttk.Label(pagefour, text="6- Volatility of the virtual machine environment", font=SMALL_FONT)
lcd6.place(x=480, y=275)
cd6 = tk.StringVar()
ccd6 = ttk.Combobox(pagefour, textvariable=cd6, width=10, state="readonly")
ccd6.place(x=920, y=275)
ccd6['values'] = ("LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccd6.current(1)

lcd7 = ttk.Label(pagefour, text="7- Required turnabout time", font=SMALL_FONT)
lcd7.place(x=480, y=300)
cd7 = tk.StringVar()
ccd7 = ttk.Combobox(pagefour, textvariable=cd7, width=10, state="readonly")
ccd7.place(x=920, y=300)
ccd7['values'] = ("LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccd7.current(1)

lcd8 = ttk.Label(pagefour, text="8- Analyst capability", font=SMALL_FONT)
lcd8.place(x=480, y=325)
cd8 = tk.StringVar()
ccd8 = ttk.Combobox(pagefour, textvariable=cd8, width=10, state="readonly")
ccd8.place(x=920, y=325)
ccd8['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccd8.current(2)


lcd9 = ttk.Label(pagefour, text="9- Applications experience ", font=SMALL_FONT)
lcd9.place(x=480, y=350)
cd9 = tk.StringVar()
ccd9 = ttk.Combobox(pagefour, textvariable=cd9, width=10, state="readonly")
ccd9.place(x=920, y=350)
ccd9['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccd9.current(2)

lcd10 = ttk.Label(pagefour, text="10- Software engineer capability", font=SMALL_FONT)
lcd10.place(x=480, y=375)
cd10 = tk.StringVar()
ccd10 = ttk.Combobox(pagefour, textvariable=cd10, width=10, state="readonly")
ccd10.place(x=920, y=375)
ccd10['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccd10.current(2)

lcd11 = ttk.Label(pagefour, text="11- Virtual machine experience", font=SMALL_FONT)
lcd11.place(x=480, y=400)
cd11 = tk.StringVar()
ccd11 = ttk.Combobox(pagefour, textvariable=cd11, width=10, state="readonly")
ccd11.place(x=920, y=400)
ccd11['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH")
ccd11.current(2)

lcd12 = ttk.Label(pagefour, text="12- Programming language experience", font=SMALL_FONT)
lcd12.place(x=480, y=425)
cd12 = tk.StringVar()
ccd12 = ttk.Combobox(pagefour, textvariable=cd12, width=10, state="readonly")
ccd12.place(x=920, y=425)
ccd12['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH")
ccd12.current(2)

lcd13 = ttk.Label(pagefour, text="13- Application of software engineering methods", font=SMALL_FONT)
lcd13.place(x=480, y=450)
cd13 = tk.StringVar()
ccd13 = ttk.Combobox(pagefour, textvariable=cd13, width=10, state="readonly")
ccd13.place(x=920, y=450)
ccd13['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccd13.current(2)

lcd14 = ttk.Label(pagefour, text="14- Use of software tools", font=SMALL_FONT)
lcd14.place(x=480, y=475)
cd14 = tk.StringVar()
ccd14 = ttk.Combobox(pagefour, textvariable=cd14, width=10, state="readonly")
ccd14.place(x=920, y=475)
ccd14['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccd14.current(2)

lcd15 = ttk.Label(pagefour, text="15- Required development schedule", font=SMALL_FONT)
lcd15.place(x=480, y=500)
cd15 = tk.StringVar()
ccd15 = ttk.Combobox(pagefour, textvariable=cd15, width=10, state="readonly")
ccd15.place(x=920, y=500)
ccd15['values'] = ("VERY LOW", "LOW", "NOMINAL", "HIGH", "VERY HIGH")
ccd15.current(2)

EAF = 1.0
di = 0
def result():
    EAF = 1.0

    if ccd1.current() == 0:
        EAF = EAF*(.75)
        print(1)
    elif cd1.get() == "LOW":
        EAF = EAF*(.88)
    elif cd1.get() == "NOMINAL":
        EAF = EAF*(1)
    elif cd1.get() == "HIGH":
        EAF = EAF*(1.15)
    elif cd1.get() == "VERY HIGH":
        EAF = EAF*(1.40)

    if (cd2.get() == "LOW"):
        EAF = EAF *(.94)
    elif ccd2.current() == 1:
        EAF = EAF *(1)
        print(2,8)
    elif (cd2.get() == "HIGH"):
        EAF = EAF *(1.08)
    elif (cd2.get() == "VERY HIGH"):
        EAF = EAF *(1.16)

    if (cd3.get() == "VERY LOW"):
        EAF = EAF *(.70)
    elif (cd3.get() == "LOW"):
        EAF = EAF *(.85)
    elif (cd3.get() == "NOMINAL"):
        EAF = EAF *(1)
    elif (cd3.get() == "HIGH"):
        EAF = EAF *(1.15)
    elif (cd3.get() == "VERY HIGH"):
        EAF = EAF*(1.30)

    if (cd4.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cd4.get() == "HIGH"):
        EAF = EAF*(1.11)
    elif (cd4.get() == "VERY HIGH"):
        EAF = EAF*(1.30)

    if (cd5.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cd5.get() == "HIGH"):
        EAF = EAF*(1.06)
    elif (cd5.get() == "VERY HIGH"):
        EAF = EAF*(1.21)

    if (cd6.get() == "LOW"):
        EAF = EAF*(.87)
    elif (cd6.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cd6.get() == "HIGH"):
        EAF = EAF*(1.15)
    elif (cd6.get() == "VERY HIGH"):
        EAF = EAF*(1.30)

    if (cd7.get() == "LOW"):
        EAF = EAF*(.94)
    elif (cd7.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cd7.get() == "HIGH"):
        EAF = EAF*(1.07)
    elif (cd7.get() == "VERY HIGH"):
        EAF = EAF*(1.15)

    if (cd8.get() == "VERY LOW"):
        EAF = EAF*(1.46)
    elif (cd8.get() == "LOW"):
        EAF = EAF*(1.19)
    elif (cd8.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cd8.get() == "HIGH"):
        EAF = EAF*(.86)
    elif (cd8.get() == "VERY HIGH"):
        EAF = EAF*(.71)

    if (cd9.get() == "VERY LOW"):
        EAF = EAF*(1.29)
    elif (cd9.get() == "LOW"):
        EAF = EAF*(1.13)
    elif (cd9.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cd9.get() == "HIGH"):
        EAF = EAF*(.91)
    elif (cd9.get() == "VERY HIGH"):
        EAF = EAF*(.82)

    if (cd10.get() == "VERY LOW"):
        EAF = EAF*(1.42)
    elif (cd10.get() == "LOW"):
        EAF = EAF*(1.17)
    elif (cd10.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cd10.get() == "HIGH"):
        EAF = EAF*(.86)
    elif (cd10.get() == "VERY HIGH"):
        EAF = EAF*(.70)

    if (cd12.get() == "VERY LOW"):
        EAF = EAF*(1.14)
    elif (cd12.get() == "LOW"):
        EAF = EAF*(1.07)
    elif (cd12.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cd12.get() == "HIGH"):
        EAF = EAF*(.95)

    if (cd13.get() == "VERY LOW"):
        EAF = EAF*(1.24)
    elif (cd13.get() == "LOW"):
        EAF = EAF*(1.10)
    elif (cd13.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cd13.get() == "HIGH"):
        EAF = EAF*(.91)
    elif (cd13.get() == "VERY HIGH"):
        EAF = EAF*(.82)

    if (cd14.get() == "VERY LOW"):
        EAF = EAF*(1.24)
    elif (cd14.get() == "LOW"):
        EAF = EAF*(1.10)
    elif (cd14.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cd14.get() == "HIGH"):
        EAF = EAF*(.91)
    elif (cd14.get() == "VERY HIGH"):
        EAF = EAF*(.83)

    if (cd15.get() == "VERY LOW"):
        EAF = EAF*(1.23)
    elif (cd15.get() == "LOW"):
        EAF = EAF*(1.08)
    elif (cd15.get() == "NOMINAL"):
        EAF = EAF*(1)
    elif (cd15.get() == "HIGH"):
        EAF = EAF*(1.04)
    elif cd15.get() == "VERY HIGH":
        EAF = EAF*(1.10)


    if typesystem.current() == 0:
        a = 2.4
        b = 1.05
        x = .38

    elif typesystem.current() == 1:
        a = 3.0
        b = 1.12
        x = .35

    else:
        a = 3.6
        b = 1.20
        x = .32



    di = cf1.get() + cf2.get() + cf3.get() + cf4.get() + cf5.get() + cf6.get() + cf7.get() + cf8.get() + cf9.get() + cf10.get() + cf11.get() + cf12.get() + cf13.get() + cf14.get()
    caf = 0.65 + (0.01 * di)
    if cwf.current() == 0:
        ufp = (7 * int(eft1.get())) + (5 * int(eft2.get())) + (3 * int(eft3.get())) + (4 * int(eft4.get())) + (3 * int(eft5.get()))
    elif cwf.current() == 1:
        ufp = (10 * int(eft1.get())) + (7 * int(eft2.get())) + (4 * int(eft3.get())) + (5 * int(eft4.get())) + (4 * int(eft5.get()))
    else:
        ufp = (15 * int(eft1.get())) + (10 * int(eft2.get())) + (6 * int(eft3.get())) + (7 * int(eft4.get())) + (6 * int(eft5.get()))

    fp = ufp * caf
    sloc = fp * int(tlf.get())

    effort = a * ((sloc / 1000) ** b) * EAF
    tdev = 2.5 * ((effort) ** x)

    prod = fp / effort

    cost = tdev * float(ecm.get())

    leffort = tk.Label(pagesix, text="Required Effort is :    " + str(effort) + "  Person Month", font=LARGE_FONT, background="black", foreground="blue")
    leffort.place(x=20, y=50)

    ltdev= tk.Label(pagesix, text="Development time is :    " + str(tdev) + "  Months", font=LARGE_FONT, background="black", foreground="green")
    ltdev.place(x=20, y=100)

    lcost = tk.Label(pagesix, text="Total Cost is :    " + str(cost) + "  dollars", font=LARGE_FONT, background="black", foreground="red")
    lcost.place(x=20, y=150)

    #lprod = tk.Label(pagesix, text="Productivity is :    " + str(prod) + "  ", font=LARGE_FONT, background="black", foreground="red")
    #lprod.place(x=20, y=200)

    bnext = tk.Button(pagesix, text="Calculate Again", width=15, background="grey", command=lambda: show_frame(pagetwo))
    bnext.place(x=600, y=500)

    bthank = tk.Button(pagesix, text="ThankYou", width=15, background="grey", command=lambda: show_frame(pageseven))
    bthank.place(x=800, y=500)

    show_frame(pagesix)

bback = tk.Button(pagefour, text="Back", width=10, background="grey", command=lambda:show_frame(pagetwo))
bback.place(x=750, y=550)

bnext = tk.Button(pagefour, text="Next", width=10, background="grey", command=lambda:show_frame(pagefive))
bnext.place(x=850, y=550)



#pagefive

#weighting factor

lwf = ttk.Label(pagefive, text="Project Type", font=LARGE_FONT)
lwf.place(x=20, y=20)

wf = ("Simple", "Average", "Complex")
cwf = ttk.Combobox(pagefive, width=12, state="readonly")
cwf.place(x=300, y=25)
cwf['values'] = wf
cwf.current(0)

#Cost per month

lcm = ttk.Label(pagefive, text="Cost per Month", font = LARGE_FONT)
lcm.place(x=500, y=100)
ld = ttk.Label(pagefive, text="(in dollars)", font = SMALL_FONT)
ld.place(x=520, y=130)
ecm = ttk.Entry(pagefive, width=15)
ecm.place(x=700, y=105)

#language factor

llf = ttk.Label(pagefive, text="Language Factor", font=LARGE_FONT)
llf.place(x=500, y=25)
tlf = ttk.Entry(pagefive, width=12)
tlf.place(x=725, y=32)


#function type

ft = ttk.Label(pagefive, text="Function Type", font=LARGE_FONT)
ft.place(x=20, y=80)

lweight = ttk.Label(pagefive, text="Weight", font=LARGE_FONT)
lweight.place(x=300, y=80)

ft1 = ttk.Label(pagefive, text="1-  Internal Logical File", font=SMALL_FONT)
ft1.place(x=30, y=120)
eft1 = ttk.Entry(pagefive, width=10)
eft1.place(x=310, y=120)

ft2 = ttk.Label(pagefive, text="2-  External Interface File", font=SMALL_FONT)
ft2.place(x=30, y=150)
eft2 = ttk.Entry(pagefive, width=10)
eft2.place(x=310, y=150)

ft3 = ttk.Label(pagefive, text="3-  External Input", font=SMALL_FONT)
ft3.place(x=30, y=180)
eft3 = ttk.Entry(pagefive, width=10)
eft3.place(x=310, y=180)

ft4 = ttk.Label(pagefive, text="4-  External Output", font=SMALL_FONT)
ft4.place(x=30, y=210)
eft4 = ttk.Entry(pagefive, width=10)
eft4.place(x=310, y=210)

ft5 = ttk.Label(pagefive, text="5-  External Inquiry", font=SMALL_FONT)
ft5.place(x=30, y=240)
eft5 = ttk.Entry(pagefive, width=10)
eft5.place(x=310, y=240)

bback = tk.Button(pagefive, text="Back", width=10, background="grey", command=lambda : show_frame(pagefour))
bback.place(x=750, y=550)

bnext = tk.Button(pagefive, text="Next", width=10, background="grey", command=result)
bnext.place(x=850, y=550)


thank = tk.Label(pageseven, text="Thanks A Lot", font=("Verdana", "40"), foreground="red")
thank.place(x=300, y=250)

window.geometry("1024x600+10+20")

window.mainloop()