from tkinter import *
import datetime
import winsound
from PIL import Image, ImageTk

root = Tk()
root.title("Alarm Clock - 24hrs format")
root.config(bg="black")
root.geometry("490x360")
root.resizable(False, False)

hours = StringVar()
minutes = StringVar()

clock = ImageTk.PhotoImage(Image.open("alarm.jpg"))
image_label = Label(image=clock)
image_label.place(x=0, y=0)

def set_alarm():
    alarm_time = f"{hours.get()}:{minutes.get()}:00"
    if alarm_time != ": :00":
        root.after(1000, alm_clock, alarm_time)

def alm_clock(alarm_time):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        alarm_label = Label(root, text="Wake Up...!", bg="yellow", font=("georgia", 20, "italic"))
        alarm_label.grid(padx=200, pady=10, row=2, column=2)
        play_alarm()
        return
    root.after(1000, alm_clock, alarm_time)

def play_alarm():
    winsound.Beep(500, 2000)  # Beep sound for 2 seconds

Label(root, text="Set Alarm", font=("georgia", 18, "italic"), bg="white", fg="black").place(x=320, y=60)
Label(root, text="Hours", font=("georgia", 16, "italic"), bg="white", fg="dark grey").place(x=310, y=130)
Label(root, text="Minutes", font=("georgia", 16, "italic"), bg="white", fg="dark grey").place(x=390, y=130)

hours_spinbox = Spinbox(root, textvariable=hours, from_=0, to=23, width=4, font=("georgia", 17, "italic"))
hours_spinbox.place(x=310, y=170)

minutes_spinbox = Spinbox(root, textvariable=minutes, from_=0, to=59, width=4, font=("georgia", 17, "italic"))
minutes_spinbox.place(x=390, y=170)

set_btn = Button(root, text="Set alarm", command=set_alarm, bg="white", fg="dark grey", font=("georgia", 16, "italic"))
set_btn.place(x=320, y=240)

root.mainloop()
