from tkinter import *
import tkinter.messagebox
# tk window + title
window = Tk()
# Add image file
back_im = PhotoImage(file="BG.png")

#Comment Remove
def rem_com(text):
    tt = ''
    pp = []
    com = True
    for x in text:
        if "//" in x:
            for i in range(x.find("//")):
                tt = tt+x[i]
            pp.append(tt)
            tt = ''
        elif "#" in x:
            continue
        elif "/*" in x:
            com = False
            continue
        elif "*/" in x:
            com = True
            continue
        elif com==True:
            pp.append(x)
    return pp

def front():
    window.title("Waku Compiler")
    # Adjust size
    window.geometry("1080x720")
    # BG Image
    Label(window, image=back_im, border=0).place(x=0, y=0)

    #Printing after comment remove       
    def text_in():
        #Frame create & Locate
        frame = Frame(window)
        frame.place(x= 580,y =200)
        f = open("code.txt","w")
        text = inputtxt.get('1.0', END)
        f.write(text)
        f.close()
        f = open("code.txt","r")
        txt = f.readlines()
        f.close()
        #using file to read code & remove comment
        a = rem_com(txt)
        # create the text widget
        text = Text(frame,font='roboto 10 bold', height=20,width=45,padx=15,pady=10,bg='#0f2337',foreground="#FFFFFF")
        text.grid(row=0, column=0, sticky=EW)

        # create a scrollbar widget and set its command to the text widget
        scrollbar = Scrollbar(frame, orient='vertical', command=text.yview)
        scrollbar.grid(row=0, column=1, sticky=NS)
        #  communicate back to the scrollbar
        text['yscrollcommand'] = scrollbar.set
        c = 1
        # using loop to insert the value and position
        for x in a:
            position = f'{c}.0'
            text.insert(position,f'{x}\n')
            c+=1
    
    # going to next page
    def nxt():
        window.quit()
        tok()
    #Title of the tables     
    Label(window,text="Write your Code Here",width = 33,font='roboto 15 bold', fg='#FFFFFF', bg='#804FFF').place(x=130,y=150)
    Label(window,text="Code after Comment Removed",width = 32,font='roboto 15 bold', fg='#FFFFFF', bg='#804FFF').place(x=580,y=150)

    #Input table placement
    inputtxt =Text(window,font='roboto 10 bold',height = 20,width = 48,padx=15,pady=10,bg="#0f2337",foreground="#FFFFFF")
    inputtxt.place(x=130,y=200)
        

    #Button Create and linkup
    Button(window, text="Remove Comment",font='roboto 15 bold', bg='#107acb',padx=15,pady=10,fg='#FFFFFF', border="0", command=lambda: text_in(),  relief=GROOVE
            ).place(x=212, y=550)
        
    Button(window, text="Next", font='roboto 15 bold', bg='#107acb',padx=90,pady=10,fg='#FFFFFF', border="0", command=lambda: nxt(),  relief=GROOVE
            ).place(x=645, y=550)
            
    window.mainloop()

def tok():
    window.title("Waku Compiler")
    # Adjust size
    window.geometry("1080x720")
    # BG Image
    Label(window, image=back_im, border=0).place(x=0, y=0)
    
    #taking variable from fun function where all the background work is done
    a_op,keya,inde,sep,str=fun()
    op = ''
    key = ''
    ind = ''
    se = ''

    #converting list to string   
    for x in a_op:
        op+=x+'  '
    for x in keya:
        key+=x+'  '
    for x in sep:
        se+=x+'  '
    for x,y in inde:
        ind+=y+'  '
    
    #Title
    Label(window,text="Tokenization",width = 46,font='roboto 15 bold', bg='#804FFF',fg='#FFFFFF').place(x=300,y=150)
    #Creating frame
    frame1 = Frame(window,bg="#0f2337",padx=5,pady=5)
    frame1.place(x=300,y=200)

    #Table values as row and column
    l1 = Label(frame1, text = "Operators   :",font='roboto 12 bold', bg='#0f2337',fg='#FFFFFF')
    l2 = Label(frame1, text = op,font='roboto 12 ', bg='#0f2337',fg='#FFFFFF')
    l3 = Label(frame1, text = "Separator   :",font='roboto 12 bold',bg='#0f2337', fg='#FFFFFF')
    l4 = Label(frame1, text = se,font='roboto 12 ',bg='#0f2337', fg='#FFFFFF')
    l5 = Label(frame1, text = "Keywords   :",font='roboto 12 bold',bg='#0f2337', fg='#FFFFFF')
    l6 = Label(frame1, text = key,font='roboto 12 ',bg='#0f2337', fg='#FFFFFF')
    l7 = Label(frame1, text = "Identifiers  :",font='roboto 12 bold',bg='#0f2337', fg='#FFFFFF')
    l8 = Label(frame1, text = ind,font='roboto 12 ',bg='#0f2337', fg='#FFFFFF')
    
    l1.grid(row = 0, column = 0, sticky = EW,padx=30, pady = 5)
    l2.grid(row = 0, column = 1, sticky = EW,padx=30, pady = 5)
    l3.grid(row = 1, column = 0, sticky = EW,padx=30, pady = 5)
    l4.grid(row = 1, column = 1, sticky = EW,padx=30, pady = 5)
    l5.grid(row = 2, column = 0, sticky = EW,padx=30, pady = 5)
    l6.grid(row = 2, column = 1, sticky = EW,padx=30, pady = 5)
    l7.grid(row = 3, column = 0, sticky = EW,padx=30, pady = 5)
    l8.grid(row = 3, column = 1, sticky = EW,padx=30, pady = 5)
    
    l0=Label(frame1, text = f"",font='roboto 12',bg='#0f2337', fg='#FFFFFF')
    l0.grid(row = 4, column = 4, sticky = EW)
    
    l9 =Label(frame1, text = "Strings       :",font='roboto 12 bold',bg='#0f2337', fg='#FFFFFF')
    l9.grid(row = 5, column = 0, sticky = E,padx=30, pady = 5)
    c = 5
    for x in str:
        l=Label(frame1, text = f"-> {x}",font='roboto 12',bg='#0f2337', fg='#FFFFFF')
        l.grid(row = c, column = 1, sticky = EW,padx=30, pady = 5)
        c+=1
    
    #functions for buttons
    def nxt():
        window.quit()
        sym(inde)
    def back():
        window.quit()
        front()

    #Button Creation  
    Button(window, text="Home",font='roboto 15 bold', bg='#107acb',padx=20,pady=10,fg='#FFFFFF', border="0", command=lambda: back(),  relief=GROOVE
            ).place(x=320, y=550)
        
    Button(window, text="Next", font='roboto 15 bold', bg='#107acb',padx=20,pady=10,fg='#FFFFFF', border="0", command=lambda: nxt(),  relief=GROOVE
            ).place(x=700, y=550)
    # running main loop
    window.mainloop()

def sym(inde):
    window.title("Waku Compiler")
    # Adjust size
    window.geometry("1080x720")
    # BG Image
    Label(window, image=back_im, border=0).place(x=0, y=0)
    # Title
    Label(window,text="Symbol Table Management",width = 29,font='roboto 15 bold', bg='#804FFF',fg='#FFFFFF').place(x=370,y=150)

    #Frame  
    frame1 = Frame(window,bg="#0f2337",padx=5,pady=5)
    frame1.place(x=370,y=200)

    #Table Information    
    l0=Label(frame1, text = f"ID",font='roboto 12 bold',bg='#42627b', fg='#FFFFFF')
    l0.grid(row = 0, column = 0, sticky = EW)
    l1=Label(frame1, text = f"Variable",font='roboto 12 bold',bg='#42627b', fg='#FFFFFF')
    l1.grid(row = 0, column = 1, sticky = EW)
    l2=Label(frame1, text = f"Type",font='roboto 12 bold',bg='#42627b', fg='#FFFFFF')
    l2.grid(row = 0, column = 2, sticky = EW)
    c = 1
    for x,y in inde:
        l3=Label(frame1, text = f"{c}",font='roboto 12',bg='#0f2337', fg='#FFFFFF')
        l3.grid(row = c, column = 0, sticky = EW,padx=30, pady = 1)
        l4=Label(frame1, text = f"{y}",font='roboto 12',bg='#0f2337', fg='#FFFFFF')
        l4.grid(row = c, column = 1, sticky = EW,padx=30, pady = 1)
        l5=Label(frame1, text = f"{x}",font='roboto 12',bg='#0f2337', fg='#FFFFFF')
        l5.grid(row = c, column = 2, sticky = EW,padx=30, pady = 1)
        c+=1
    
    #Functions for Button
    def exit():
        window.quit()
        window.destroy()
    def back():
        window.quit()
        front()

    #Button Creation   
    Button(window, text="Home",font='roboto 15 bold', bg='#107acb',padx=20,pady=10,fg='#FFFFFF', border="0", command=lambda: back(),  relief=GROOVE
            ).place(x=320, y=550)
        
    Button(window, text="Exit", font='roboto 15 bold', bg='#107acb',padx=20,pady=10,fg='#FFFFFF', border="0", command=lambda: exit(),  relief=GROOVE
            ).place(x=700, y=550)
    # running main loop
    window.mainloop()

def fun():    
    # header and comment remove and making a single string
    def rem_com(text):
        tt = ''
        com = True
        for x in text:
            if "//" in x:
                for i in range(x.find("//")):
                    tt = tt+x[i]
            elif "#" in x:
                continue
            elif "/*" in x:
                com = False
                continue
            elif "*/" in x:
                com = True
                continue
            elif com==True:
                tt  = tt+ x
            
        return tt
            
    #Taking Input from files
    f = open("code.txt","r")
    p = f.readlines()
    f.close()
    #operators
    operators = ['+','-','/','*','**','%','+=','-=','*=','/=','%=','<<=','>>=','&=','^=','|=','!=','<','>','>=','<=','!','^','~','++','--','=','&&','||','&','|','==',]
    a_op = []
    #alphabet
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','_']
    num = ['0','1','2','3','4','5','6','7','8','9']
    #comment & remove
    rtext = rem_com(p)
    #split words
    txt = rtext.split()
    #keywords
    keyw = ["auto","double","bool","int","struct","break","else","long","switch","case","enum","register","typedef","char","extern","return","union","const","short","float","unsigned","continue","for","signed","void","defult","goto","sizeof","volatile","do","if","static","while"]
    keya = []
    #indentifiers
    indw = ["auto","double","bool","int","struct","long","char","void","float"]
    inde = []
    kg = False
    ind = ''
    typ = ''
    #Getting Key word and identifiers
    for i in range(len(txt)):
        #identifiers detect
        if txt[i-1] in indw and txt[i][0] in alpha:
            if '()' in txt[i]:
                inde.append(["Function",txt[i]])
            else:
                if ';' in txt[i]:
                    for x in txt[i]:
                        if x!=';':
                            ind+=x
                    p=ind.split(',')
                    for x in p:
                        inde.append([txt[i-1],x])
                    ind = ''

                else:
                    kg=True
                    typ=txt[i-1]
        if kg==True:
            if ';' in txt[i]:
                for x in txt[i]:
                    if x!=';':
                        ind+=x
                p=ind.split(',')
                for x in p:
                    inde.append([typ,x])
                ind = ''
                kg=False
                typ = ''
            else:
                ind+=txt[i]
        
        #keywords detect
        if txt[i] in keyw:
            keya.append(txt[i])
            
    #String
    str = []
    gt = ''
    sr=False

    #getting sep
    sep = []
    sb= False
    tb= False
    for x in rtext:
        if x==',' or x==';':
            sep.append(x)
        if x=='{':
            sb = True
        if x=='}' and sb==True:
            sb=False
            sep.append("{}")
        if x=='[':
            tb = True
        if x==']' and sb==True:
            tb=False
            sep.append("[]")
        if x=="\"" and sr==True:
            sr=False
            str.append(gt)
            gt = ''
        elif x=="\"":
            sr=True
        elif sr==True:
            gt = gt+x

    #getting operators
    for x in operators:
        if x in rtext:
            a_op.append(x)

    #Removing Duplicate using set
    a_op = set(a_op)
    keya = set(keya)
    sep = set(sep)

    #passing Variables
    return a_op,keya,inde,sep,str

if __name__ == '__main__':
    front()
