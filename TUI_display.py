import time
import os
rst = "\033[0m"    
cyc = "\033[96m"  
grc = "\033[92m"  
yec = "\033[93m"   
rec = "\033[91m"   
def adjust_Y(nu_to_ad):
    for i in range(nu_to_ad):
        print()
def ma_mo_d():
    os.system('cls')
    adjust_Y(4)
    print(" "*70+cyc+"CITY HEALTH CENTER")
    print(" "*63+cyc+"SmartQ Health Management System"+rst)
    print()
    print(" "*57+"╔══════════════════════════════════════════╗")
    print(" "*57+"║                "+cyc+"Main Menu"+rst+"                 ║")
    print(" "*57+"╠══════════════════════════════════════════╣")
    print(" "*57+"║ "+grc+"[1] Patient Mode "+rst+"                        ║")
    print(" "*57+"║ "+grc+"[2] Admin Mode   "+rst+"                        ║")
    print(" "*57+"║ "+grc+"[3] Exit         "+rst+"                        ║")
    print(" "*57+"╚══════════════════════════════════════════╝")
def ac_ad_d():
    os.system('cls')
    adjust_Y(10)
    print(" "*57+"╔══════════════════════════════════════════╗")
    print(" "*57+"║           "+yec+"Accessing Admin Mode"+rst+"           ║")
    print(" "*57+"╚══════════════════════════════════════════╝")
def ex_pr_d():
    os.system('cls')
    adjust_Y(10)
    print(" "*57+"╔══════════════════════════════════════════╗")
    print(" "*57+"║      "+yec+"Are you sure you want to exit"+rst+"       ║")
    print(" "*57+"║                                          ║")
    print(" "*57+"║         "+grc+"[1] No           "+rec+"[2] Yes"+rst+"         ║")
    print(" "*57+"╚══════════════════════════════════════════╝")
def pa_mo_d():
    os.system('cls')
    adjust_Y(4)
    print(" "*70+cyc+"CITY HEALTH CENTER")
    print(" "*63+"SmartQ Health Management System"+rst)
    print()
    print(" "*57+"╔══════════════════════════════════════════╗")
    print(" "*57+"║               "+cyc+"Patient Mode           "+rst+"    ║")
    print(" "*57+"╠══════════════════════════════════════════╣")
    print(" "*57+"║ "+grc+"[1] Add Patient to Appointment Queue "+rst+"    ║")
    print(" "*57+"║ "+grc+"[2] View Patient Schedule            "+rst+"    ║")
    print(" "*57+"║ "+grc+"[3] Back to Main Menu                "+rst+"    ║")
    print(" "*57+"╚══════════════════════════════════════════╝")

#Add patient to Queue
def bo_ap_d():
    os.system('cls')
    print(" "*43+"╔════════════════════════════════════════════════════════════════════════╗")
    print(" "*43+"║                            "+cyc+"Book Appointment"+rst+"                            ║")
    print(" "*43+"╚════════════════════════════════════════════════════════════════════════╝")
def re_in_d():
    os.system('cls')
    print(" "*43+"╔════════════════════════════════════════════════════════════════════════╗")
    print(" "*43+"║                       "+cyc+"Review Patient Information"+rst+"                       ║")
    print(" "*43+"╠════════════════════════════════════════════════════════════════════════╣") 
def ces_d():
    print(" "*43+"╠════════════════════════════════════════════════════════════════════════╣")
    print(" "*43+"║    "+rec+"[1] Cancel Booking    "+yec+"[2] Edit Details    "+grc+"[3] Submit Appointment    "+rst+"║")
    print(" "*43+"╚════════════════════════════════════════════════════════════════════════╝")
def ed_in_d():
    os.system('cls') 
    print(" "*43+"╔════════════════════════════════════════════════════════════════════════╗")
    print(" "*43+"║                            "+cyc+"Edit Information"+rst+"                            ║")
    print(" "*43+"╠════════════════════════════════════════════════════════════════════════╣")
def en__ed_in_d():
    print(" "*43+"╠════════════════════════════════════════════════════════════════════════╣")
    print(" "*43+"╚════════════════════════════════════════════════════════════════════════╝")
def pa_bo_su_d():
    print(" "*43+"╔════════════════════════════════════════════════════════════════════════╗")
    print(" "*43+"║                       "+grc+"Patient Booked Successfully"+rst+"                      ║")
    print(" "*43+"╠════════════════════════════════════════════════════════════════════════╣") 
def vi_pa_sc_d():
    print(" "*43+"╔════════════════════════════════════════════════════════════════════════╗")
    print(" "*43+"║                          "+cyc+"View Patient Schedule"+rst+"                         ║")
    print(" "*43+"╚════════════════════════════════════════════════════════════════════════╝")

def ad_mo_d():
    os.system('cls')
    adjust_Y(4)
    print(" "*70+cyc+"CITY HEALTH CENTER")
    print(" "*63+"SmartQ Health Management System"+rst)
    print()
    print(" "*57+"╔══════════════════════════════════════════╗")
    print(" "*57+"║                "+cyc+"Admin Mode"+rst+"                ║")
    print(" "*57+"╠══════════════════════════════════════════╣")
    print(" "*57+"║ "+grc+"[1] View Patient Queue   "+rst+"                ║")
    print(" "*57+"║ "+grc+"[2] Process Next Patient "+rst+"                ║")
    print(" "*57+"║ "+grc+"[3] View All Patients    "+rst+"                ║")
    print(" "*57+"║ "+grc+"[4] View Patient Records "+rst+"                ║")
    print(" "*57+"║ "+grc+"[5] Back to Main Menu    "+rst+"                ║")
    print(" "*57+"╚══════════════════════════════════════════╝")

# feedback notif
def pa_nu_no_fo_d():
    print(" "*43+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(" "*43+"┃                        "+rec+"Patient number not found"+rst+"                        ┃") 
    print(" "*43+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    time.sleep(1.25)
def cu_no_ne_pa_d():
    os.system('cls')
    adjust_Y(10)
    print(" "*43+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(" "*43+"┃                       "+yec+"No Next Patient Available"+rst+"                        ┃")
    print(" "*43+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")                                      
    input(" "*44+cyc+"Enter to proceed")
def num_only_s():
    print(" "*57+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(" "*57+"┃        "+yec+"Please enter numbers only."+rst+"        ┃") 
    print(" "*57+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    time.sleep(1.25)
def num_only_l():
    print(" "*43+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(" "*43+"┃                       "+yec+"Please enter numbers only."+rst+"                       ┃")
    print(" "*43+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    time.sleep(1.25)
def invld_ch_s():
    print(" "*57+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(" "*57+"┃              "+rec+"Invalid choice"+rst+"              ┃")
    print(" "*57+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    time.sleep(1.25)
def invld_ch_l():
    print(" "*43+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(" "*43+"┃                             "+rec+"Invalid Choice"+rst+"                             ┃")
    print(" "*43+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    time.sleep(1.25)
def in_co_d():
    os.system('cls')
    adjust_Y(10)
    print(" "*57+"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(" "*57+"┃               "+rec+"Invalid Code"+rst+"               ┃")
    print(" "*57+"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    time.sleep(1.25)