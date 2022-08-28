from tkinter import *
import speedtest #NEED TO INSTALL,SPEEDTEST,SPEEDTEST-CLI

def speedck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    download=str(round(sp.download()/(10**6),3))+"Mbps"
    lab_download.config(text=download)

    upload=str(round(sp.download()/(10**6),3))+"Mbps"
    lab_upload.config(text=upload)



sp = Tk()
sp.title("Internet speed test")
sp.geometry("500x550")
sp.config(bg="Blue")
lab = Label(sp, text="Internet speed", font=("Time New Roman",25,"bold"),bg="Blue",fg="Red")
lab.place(x=60, y=30,height=50,width=380)

lab = Label(sp, text="Download speed", font=("Time New Roman",25,"bold"),bg="Blue",fg="Red")
lab.place(x=60, y=120,height=50,width=380)
lab_download = Label(sp, text="00", font=("Time New Roman",18,"bold"),bg="white",fg="black",relief=RAISED,)
lab_download.place(x=160, y=200,height=50,width=210)

lab = Label(sp, text="Upload speed", font=("Time New Roman",25,"bold"),bg="Blue",fg="Red")
lab.place(x=60, y=280,height=50,width=380)
lab_upload = Label(sp, text="00", font=("Time New Roman",18,"bold"),bg="white",fg="black",relief=RAISED)
lab_upload.place(x=160, y=340,height=50,width=210)


button = Button(sp, text="Check", font=("Time New Roman",18,"bold"),bg="Yellow",fg="black",relief=RAISED,command=speedck)
button.place(x=200, y=420,height=50,width=150)

sp.mainloop()
