from tkinter import *
import time;
import csv

root=Tk()
searchValue=StringVar()
def GetGame():
    path = 'C:\\Users\\hp\\Downloads\\Project 1st Semester\\vgsales.csv'
    file=open(path, "r")
    reader = csv.reader(file)
    print(searchValue.get())
    for line in reader:
        try:
            if line[1] == searchValue.get():
                t = line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], \
                    line[12], line[13], line[14], line[15]
                answer.delete(1.0, END)
                answer.insert(END, t)
                print("Platform", t[2], "\n", "Year", t[3], "\n", "Genre", t[4], "\n", "Publisher", t[5], "\n", "NA_Sales",t[6], "\n", "EU_Sales", t[7], "\n", "JP_Sales", t[8], "\n", "Other_Sales", t[9], "\n", "Global_Sales",t[10], "\n", "Critic_Score", line[11], "\n", "Critic_Count", line[12], "\n", "User_Score", line[13],"\n", "User_Count", line[14], "\n", "Rating", line[15])
                break

        except:
            if line[1] != searchValue:
                    pass
mframe=Frame(root,bg="blue")
tframe=Frame(mframe,bg="blue")
root.title("Object Oriented Programming Project Of Data Science")
time=time.asctime(time.localtime(time.time()))
lbl=Label(tframe,font=("calibri",50,"bold"),text="Data Analysis Of 15 Years Of Video Games",fg="Black",bd=20)
lbl.pack()
lbl2=Label(tframe,font=("calibri",40,"bold"),text=time,fg="Black",bd=20)
lbl2.pack()
#YE WO ENTRY HY JAHA GAME KA NAAM LIKHTY HY
entry=Entry(tframe,width=100,textvariable=searchValue)
entry.pack()
search=Button(tframe,text="Search",width=50,height=1, command = GetGame)
search.pack()
tframe.pack()

bframe=Frame(mframe)
bar=Scrollbar(bframe)
bar.pack(side=RIGHT, fill=Y)
#ANS WO HY JAHA ANSWER OUTPUT MA ARAH HY 
answer=Text(bframe,width=100,height=30)#,yscrollcommand=bar.set)
bar.config(command=answer.yview)
answer.pack()
bframe.pack()
mframe.pack()
root.mainloop()

