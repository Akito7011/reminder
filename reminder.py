import time
from plyer import notification
def remainder(): 
        Reminder=input("Enter that task ")
        reminder_interval=int(input("Enter the time (in hrs) "))
        notification.notify(title = "**Its time",
         message = "kindly do "+Reminder,
          timeout=10
         )
        time.sleep(reminder_interval*3600)