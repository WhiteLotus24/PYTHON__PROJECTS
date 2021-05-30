from Tkinter import Label, Tk 
import time
app_window = Tk() 
app_window.title("White Lotus, TIME IS MONEY...") 
app_window.geometry("350x150") 
# app_window.resizable(0,0)
text_font= ("Digital-7", 80,)
background = "#000000"
foreground= "cyan"
border_width = 25
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)
def digital_clock(): 
   time_live = time.strftime("%H:%M:%S  %p")
   label.config(text=time_live)
   label.after(200, digital_clock)
digital_clock()
app_window.mainloop()
