import os,sys
from login import login
from tkinter import Tk,Label,Entry,Button,Checkbutton,IntVar
from encrypt import encryptedPassword

def click():
   login(entry1.get(),entry2.get())
   return

def service():
   if checkvar.get() == 1 :
    os.system('sc create ruijie binpath= "' + sys.executable + ' -u ' + entry1.get() + ' -e ' + encryptedPassword(entry2.get()) + '" start= auto')
   else:
    os.system('sc delete ruijie')
   return

'''
def reg():
   name = 'ruijie'
   path = sys.argv[0] + ' -u ' + entry1.get() + ' -e ' + encryptedPassword(entry2.get())
   KeyName = 'Software\Microsoft\Windows\CurrentVersion\Run'
   key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
   if checkvar.get() == 1 :
    win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
   else:
    win32api.RegDeleteValue(key, name)
   win32api.RegCloseKey(key)
   return
'''

def gui():
 window = Tk()
 window.title('锐捷上网认证')
 window.geometry('260x100')
 labe1 = Label(window,text="账号：")
 labe2 = Label(window,text="密码：")
 labe1.grid(row=0)
 labe2.grid(row=1)
 global entry1,entry2,checkvar
 entry1 = Entry(window)
 entry2 = Entry(window,show="*")
 entry1.grid(row=0, column=1,columnspan=3)
 entry2.grid(row=1, column=1, columnspan=3)
 button = Button(window, text="登录",command=click)
 button.grid(row=3, column=1, pady=10)
 checkvar = IntVar(master=window)
 check = Checkbutton(window, text="开机自启", variable=checkvar, onvalue = 1, offvalue = 0, command=service)
 check.grid(row=3,column=2)
 window.mainloop()
 return