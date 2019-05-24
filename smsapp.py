import http.client
from tkinter import messagebox
from tkinter import *


def sendMsg():
    conn = http.client.HTTPConnection("api.msg91.com")
    num = e1.get()
    msg = e2.get()

    payload = "{ \"sender\":\"JACKIE\", \"route\": \"4\", \"country\": \"91\", \"sms\": [ { \"message\":\""+msg+"\",\"to\": [ \""+num+"\" ] } ] }"
    headers = {
        'authkey': "",#PLEASE ENTER THE AUTHKEY BEFORE EXECUTING THE PROGRAM
        'content-type': "application/json"
        }

    conn.request("POST", "/api/v2/sendsms?country=91&sender=&route=&mobiles=&authkey=&encrypt=&message=&flash=&unicode=&schtime=&afterminutes=&response=&campaign=", payload, headers)

    res = conn.getresponse()
    data = res.read()
    messagebox.showinfo(title='Status', message=(data.decode("utf-8")))

master = Tk()

Label(master, text='Receiver Number').grid(row=1, column=0)
e1 = Entry(master, width=20)
e1.grid(row=1, column=1)

Label(master, text='Message').grid(row=2, column=0)
e2=Entry(master, width=20)
e2.grid(row=2, column=1)

Button(master, text='Send',  command = sendMsg).grid(row=4, columnspan = 2)
mainloop()
