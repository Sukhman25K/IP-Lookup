import requests, json, re, tkintermapview, requests, base64, urllib.request
from tkinter import *
from tkinter import messagebox, PhotoImage
import tkinter.ttk as ttk
from Constants import API_KEY


class IPLookUp():
    def __init__(self,Window):
        self.Window = Window 
        self.WindowDimensions()
        self.CanvasSetUp()
        self.frmStart = Frame(self.Window,bg='grey',height=350,width=650)
        self.frmStart.place(rely=0.5,relx=0.5,anchor='center')
        self.lblTitle = Label(self.Window,text='IP Look Up',bg='grey',fg='black',font=('algerian',20,'underline')).place(anchor='center',rely=0.08,relx=0.5)
        self.entryIP = Entry(self.frmStart,font=('Calibri',16),width=30)
        self.entryIP.insert(0,'IP Address')
        self.entryIP.place(anchor=CENTER,relx=0.5,rely=0.5)
        self.entryIP.bind("<FocusIn>", lambda args: self.entryIP.delete(0, 'end'))
        self.btnSubmit = Button(self.frmStart,text='Look Up',command=self.LookUp,bd=0,bg='black',fg='white',activebackground='grey',width=7,font=('Berlin Sans fb demi',24)).place(anchor='center',relx=0.5,rely=0.75)
        self.frmDetails = Frame(self.Window,bg='grey',height=350,width=650)
        self.CurrentFrame = self.frmStart

    def WindowDimensions(self):
        screenWidth = self.Window.winfo_screenwidth()                
        screenHeight = self.Window.winfo_screenheight()                 
        x = (screenWidth - 800) / 2                                   
        y = (screenHeight - 500) / 2
        self.Window.geometry('%dx%d+%d+%d' % (800,500,x,y))
        self.Window.resizable(0,0)

    def CanvasSetUp(self):
        self.BackCanvas = Canvas(Window,background = 'grey',highlightthickness=0)
        self.BackCanvas.place(x=0,y=0,width = 800,height = 500)

    def LookUp(self):
        if self.Validate():
            Details = json.loads(self.API(self.entryIP.get()))
            if "Error" not in Details:
                self.CurrentFrame.place_forget()
                self.frmDetails.place(rely=0.5,relx=0.5,anchor='center')
                self.lblCountry = Label(self.frmDetails,font=('Arial Rounded MT Bold',17),bg='grey',fg='black',text=(f"Country: {Details['country_name']}/{Details['country_code2']}")).place(anchor='w',rely=0.05)
                self.lblRegion = Label(self.frmDetails,font=('Arial Rounded MT Bold',17),bg='grey',fg='black',text=(f"Region: {Details['district']}")).place(anchor='w',rely=0.2)
                self.Image = self.GetImage(Details)
                self.imgFlag = Label(self.frmDetails,image=self.Image).place(anchor='w',rely=0.5)
                self.lblISP = Label(self.frmDetails,font=('Arial Rounded MT Bold',17),bg='grey',fg='black',text=(f"ISP: {Details['organization']}")).place(anchor='w',rely=0.8)
                self.lblIPAddress = Label(self.frmDetails,font=('Arial Rounded MT Bold',17),bg='grey',fg='black',text=(f"IP: {Details['ip']}")).place(anchor='w',rely=0.95)
                self.Map = tkintermapview.TkinterMapView(self.frmDetails,width=300,height=1500,corner_radius=0)
                self.Map.place(anchor='e',relx=1)
                self.Map.set_position(float(Details['latitude']),float(Details['longitude']),marker=True)
                self.Map.set_zoom(10)
            else:
                messagebox.showerror('Error','Invalid IP address')
                return False

    def API(self,IP):
        api_url = 'https://api.ipgeolocation.io/ipgeo?apiKey={}&ip={}'.format(API_KEY,IP)
        response = requests.get(api_url)
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            return ("Error:", response.status_code, response.text)

    def Validate(self):
        if not(re.match('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$',self.entryIP.get())):
            messagebox.showerror('Error','Provide a valid IP address')
            return False
        return True
    
    def GetImage(self,Details):
        u = urllib.request.urlopen(Details['country_flag'])
        raw_data = u.read()
        u.close()
        return PhotoImage(data=base64.encodebytes(raw_data))


if __name__ == '__main__':
    Window = Tk()
    IPLookup = IPLookUp(Window)
    Window.mainloop()
