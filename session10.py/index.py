from tkinter import *
from tkinter import messagebox

window = Tk()       #window là tên biến còn Tk() là module gốc
window.geometry("500x400")          #kich thuoc cua so
window.title("Sign in/Sign up")     #ten cua so (tren goc trai)

greeting = Label(window, text = "welcome to my app", bg="green")
greeting.grid(row=0, column=12)     #grid chinh sua vi tri hien thi


def validateInfo(username, password):
    usernameValue = userInput.get()        #2 bien nay lay gia tri
    passwordValue = passwordInput.get()    #tu input qua ham get()
    result = ''
    if (usernameValue == "mindx"):         #so sanh gia tri duoc lay
        if (passwordValue == "1234"):      #tu input voi gia tri goc
            result = "success"             #de kiem tra username, pass
        else:
            result = "cannot found"
    else:
        result = "cannot found"
    answerLabel = Label(window, text=result)    #hien ket qua trong
    answerLabel.grid(row=3, column=1)           #moi truong hop Đ/S


userlabel = Label(window, text="username")  #Label giong print() nhma cua so
userlabel.grid(row=1, column=0)     
userInput = Entry(window)           #Entry giong input() nhma cua so
userInput.grid(row=1, column=1)


passwordLabel = Label(window, text="password")
passwordLabel.grid(row=2, column=0)
passwordInput = Entry(window, show="*")
passwordInput.grid(row=2, column=1)


buttonSignIn = Button(text="Sign in", bg="green",padx="16", pady="8",
 command=lambda:[validateInfo(userInput.get(), passwordInput.get())])
buttonSignIn.grid(row=3, column=12)
#lambda se cho code chay 1 lan roi tat (neu k co thi code chay lien tuc)
#padx pady chinh sua kich thuoc chieu ngang chieu doc cua button


window.mainloop()