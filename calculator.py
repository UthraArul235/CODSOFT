import tkinter as tk

#main window

root=tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.configure(bg="#d7f0f7")

#display the label

display=tk.Label(root,text="",anchor="e",bg="#2f3640",fg="white",font=("Arial",34),padx=10,pady=10)
display.pack(fill="both",padx=20,pady=20)
expression=""

#update the display

def press(value):
    global expression
    expression+=str(value)
    display.config(text=expression)
    
#clear All
    
def clear():
    global expression
    expression=expression[:-1]
    display.config(text="")
    
#Deleting the last character
    
def delete():
    global expression
    expression=expression[:-1]
    display.config(text=expression)
    
#calculate the result
    
def equal():
    global expression
    try:
        result=str(eval(expression))
        display.config(text=result)
        expression=result
    except:
        display.config(text="Error")
        expression=""
#Button layout frame
        
frame=tk.Frame(root,bg="#2f3640")
frame.pack(padx=20,pady=10)

#Button details

buttons=[("AC",clear),("DE",delete),(".",lambda:press(".")),("/",lambda:press("/")),
         ("7",lambda:press("7")),("8",lambda:press("8")),("9",lambda:press("9")),("*",lambda:press("*")),
         ("4",lambda:press("4")),("5",lambda:press("5")),("6",lambda:press("6")),("-",lambda:press("-")),
         ("1",lambda:press("1")),("2",lambda:press("2")),("3",lambda:press("3")),("+",lambda:press("+")),
         ("00",lambda:press("00")),("0",lambda:press("0")),("=",equal)]

#create buttons

row=0
col=0
for text,command in buttons:
    btn=tk.Button(frame,text=text,command=command,bg="#3d3d3d",fg="white",font=("Arial",18),width=5,height=2,bd=0,relief="ridge")
    btn.grid(row=row,column=col,padx=5,pady=5)
    col+=1
    if text == "=":
        btn.grid(columnspan=2)
        break
    if col>3:
        col=0
        row+=1
root.mainloop()
