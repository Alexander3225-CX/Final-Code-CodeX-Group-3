import os
import time
from TUI_display import*
from random import randint
from datetime import datetime, timedelta
rst = "\033[0m"    
cyc = "\033[96m"  
grc = "\033[92m"  
yec = "\033[93m"   
rec = "\033[91m" 
rdate = datetime.today()
t24 = int(rdate.strftime("%H%M"))  
inquire = rdate.strftime("%Y-%m-%d %I:%M %p") 
t = 0
avti = { 800:"08:00 AM",  820: "08:20 AM",  840: "08:40 AM",
         900:"09:00 AM",  920: "09:20 AM",  940: "09:40 AM",
        1000:"10:00 AM", 1020: "10:20 AM", 1040: "10:40 AM",
        1100:"11:00 AM", 1120: "11:20 AM", 1140: "11:40 AM",
        1300:"01:00 PM", 1320: "01:20 PM", 1340: "01:40 PM",
        1400:"02:00 PM", 1420: "02:20 PM", 1440: "02:40 PM",
        1500:"03:00 PM", 1520: "03:20 PM", 1540: "03:40 PM"}
otime = avti.keys()
otime = tuple(otime)
pstatus= {}
pnumid = {}
pstatus= dict(pstatus)
pnumid = dict(pnumid)
allpsc  =[]
allpnu = []
PRfile = "Patients.txt"