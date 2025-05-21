from allvariables import *
from def_of_option import *
create_fh()
def mode():
    os.system('cls')
    while True:
        ma_mo_d()
        try:
            ch = int(input(" "*59+cyc+"Enter number of your Choice: "+rst))  
            if ch == 1:
                os.system('cls')
                patient_mode()
                os.system('cls')
            elif ch == 2:
                ac_ad_d()
                ach=input(" "*58+cyc+"Please Enter Administration CODE : "+rst)
                if ach == "hello world":
                    os.system('cls')
                    admin_mode()
                    os.system('cls')
                else:
                    in_co_d()
            elif ch == 3:
                while True:
                    ex_pr_d()
                    try:
                        ch1 = int(input(" "*59+cyc+"Enter the number of your Choice: "+rst))
                        if ch1 == 1:
                            break
                        elif ch1 == 2:
                            break
                        else:
                            invld_ch_s()
                            continue
                    except ValueError:
                        num_only_s()
                if ch1 == 1:
                    continue
                elif ch1 == 2:
                    file_handling()
                    break
            else:
                invld_ch_s()
        except ValueError:
            num_only_s()
def patient_mode():
    while True:
        pa_mo_d()
        try:
            ch = int(input(" "*59+cyc+"Enter number of your Choice: "+rst))
            if ch == 1:
                os.system('cls')
                add_patient_to_queue()
                os.system('cls')
            elif ch == 2:
                os.system('cls')
                view_patient_schedule()
                os.system('cls')
            elif ch == 3:
                break
            else:
                invld_ch_s()
        except ValueError:
            num_only_s()
    return
def add_patient_to_queue():
    i=0
    bo_ap_d()
    inna = in_info(" "*44+"Name"+(" "*21)+": ")
    inag = in_info(" "*44+"Age"+(" "*22)+": ")
    inge = in_info(" "*44+"Gender (M/F)"+(" "*13)+": ")
    inbi = in_info(" "*44+"Birthdate (YYYY-MM-DD)   : ")
    ince = in_info(" "*44+"Phone Number (11 digits) : ")
    inad = in_info(" "*44+"Address"+(" "*18)+": ")
    p_info = [inna,inag,inge,inbi,ince,inad]
    label = ["Name","Age","Gender","Birthdate","Phone Num","Address"] 
    while True:   
        re_in_d()
        for e_info in p_info:
            print(" "*43+"║ "+label[i]+(" "*(11-len(label[i])))+": "+e_info+(" "*(58-len(e_info)))+"║")
            i+=1
        i=0
        ces_d()
        try:
            ch = int(input(" "*44+cyc+"Enter the number of your choice: "+rst))
            if ch == 1:
                return
            elif ch == 2:
                while True:
                    ed_in_d()
                    for e_info in p_info:
                        print(" "*43+f"║ [{i+1}] "+label[i]+(" "*(11-len(label[i])))+": "+e_info+(" "*(54-len(e_info)))+"║")
                        i+=1
                    i=0  
                    en__ed_in_d()
                    try:
                        ech = int(input(" "*44+cyc+"Enter the number you want to edit: "+rst))
                        if ech == 1:
                            inna = in_info(" "*44+"Name"+(" "*21)+": ")
                        elif ech == 2:
                            inag = in_info(" "*44+"Age"+(" "*22)+": ")
                        elif ech == 3:
                            inge = in_info(" "*44+"Gender (M/F)"+(" "*13)+": ")
                        elif ech == 4:  
                            inbi = in_info(" "*44+"Birthdate (YYYY-MM-DD)   : ")  
                        elif ech == 5:    
                            ince = in_info(" "*44+"Phone Number (11 digits) : ")
                        elif ech == 6:    
                            inad = in_info(" "*44+"Address"+(" "*18)+": ")
                        else:
                            invld_ch_l()
                            continue
                        p_info = [inna,inag,inge,inbi,ince,inad]
                        break
                    except ValueError:
                        num_only_l()
            elif ch == 3:
                break
            else:                        
                invld_ch_l()
        except ValueError:
            num_only_l()
    gepn = ge_pnu()
    geps = ge_psc()
    pnumid.update({gepn:[inna,inag,inge,inbi,ince,inad,geps]})
    pstatus.update({gepn:[inquire,inna,inag,inge,inbi,ince,inad,geps,"Pending"]})
    allpnu.append(gepn)
    allpsc.append(geps)
    pa_bo_su_d()
    print(" "*43+"║ "+cyc+"Save your Patient Number : "+yec+f"{gepn}"+(" "*40)+rst+"║")
    print(" "*43+"║ "+cyc+"Your Schedule            : "+yec+f"{geps}"+(" "*25)+rst+"║")
    print(" "*43+"╚"+("═"*72)+"╝")
    input(" "*44+cyc+"Press Enter to Proceed"+rst)
    os.system('cls')
def view_patient_schedule():
    label = ["Name","Age","Gender","Birthdate","Phone Num","Address","Schedule"]
    l = 0
    vi_pa_sc_d()
    entry = input(" "*44+cyc+"Enter Your Patient Number: "+rst)
    if entry in allpnu:
            print(" "*43+"╔"+("═"*72)+"╗")
            print(" "*43+f"║ Patient Number: {entry}"+(" "*51)+"║")
            print(" "*43+"╠"+("═"*72)+"╣")
            for info in pnumid.get(entry):
                if l == 6:
                    print(" "*43+"╠"+("═"*72)+"╣")
                    print(" "*43+"║ "+cyc+label[l]+(" "*(10-len(label[l])))+": "+yec+info+(" "*(59-len(info)))+rst+"║")
                    print(" "*43+"╚"+("═"*72)+"╝")
                else:
                    print(" "*43+"║ "+label[l]+(" "*(10-len(label[l])))+": "+info+(" "*(59-len(info)))+"║")
                l+=1    
            l=0
    else:
        pa_nu_no_fo_d()
    input(" "*44+cyc+"Press Enter to proceed"+rst)
def admin_mode():
    while True:
        ad_mo_d()
        try:
            ch = int(input(" "*59+cyc+"Enter number of your Choice: "+rst))
            if ch == 1:
                os.system('cls')
                view_patient_queue()
                os.system('cls')
            elif ch == 2:
                os.system('cls')
                process_next_patient()
                os.system('cls')
            elif ch == 3:
                os.system('cls')
                view_all_patients()
                os.system('cls')
            elif ch == 4:
                os.system('cls')
                view_patients_records() 
                os.system('cls')
            elif ch == 5:
                break 
            else:
                invld_ch_s()
        except ValueError:
            num_only_s()
    return
def view_patient_queue():
    i=0
    print(" "*40+"╔"+("═"*80)+"╗")
    print(" "*40+f"║                                 "+cyc+"Patient Queue"+rst+"                                  ║")
    print(" "*40+"╠"+("═"*5)+"╤"+("═"*11)+"╤"+("═"*40)+"╤"+("═"*21)+"╣")
    print(" "*40+f"║ No. │ Patient # │"+(" "*18)+"Name"+(" "*18)+"│      Schedule       ║")
    print(" "*40+"╟"+("─"*5)+"┼"+("─"*11)+"┼"+("─"*40)+"┼"+("─"*21)+"╢")
    for p in allpnu:
        print(" "*40+f"║  {i+1}"+(" "*(3-len(str(i))))+ "│"+(" "*3)+allpnu[i]+(" "*4)+"│"+" "+pstatus.get(p)[1]+(" "*(39-len(pstatus.get(p)[1])))+"│ "+pstatus.get(p)[7]+" ║")
        i+=1
    print(" "*40+"╚"+("═"*5)+"╧"+("═"*11)+"╧"+("═"*40)+"╧"+("═"*21)+"╝")
    input(" "*43+cyc+"Press Enter to Proceed"+rst)
def view_all_patients():
    s=0
    space = [20, 35, 4, 7, 12, 13, 50,21, 11]    
    print("╔"+("═"*190)+"╗")
    print("║"+(" "*86)+"View All Patients"+(" "*87+"║"))
    print("╠"+("═"*21)+"╤"+("═"*36)+"╤"+("═"*5)+"╤"+("═"*8)+"╤"+("═"*13)+"╤"+("═"*14)+"╤"+("═"*51)+"╤"+("═"*22)+"╤"+("═"*12)+"╣")
    print("║     Visit Date      │"+(" "*16)+"Name"+(" "*16)+"│ Age │ Gender │  Birthdate  │ Phone Number │"+(" "*22)+"Address"+(" "*22)+"│ Health Check Schedle │   Status   ║")
    print("╟"+("─"*21)+"┼"+("─"*36)+"┼"+("─"*5)+"┼"+("─"*8)+"┼"+("─"*13)+"┼"+("─"*14)+"┼"+("─"*51)+"┼"+("─"*22)+"┼"+("─"*12)+"╢")
    for r in pstatus.values():
        for c in r:
            if space[s] == 11:
                print("│ "+c+(" "*(space[s]-len(c)))+"║",end="")
            elif space[s] == 20:
                print("║ "+c+(" "*(space[s]-len(c))),end="")
            else:
             print("│ "+c+(" "*(space[s]-len(c))),end="")
            s+=1
        s=0
        print()
    print("╚"+("═"*21)+"╧"+("═"*36)+"╧"+("═"*5)+"╧"+("═"*8)+"╧"+("═"*13)+"╧"+("═"*14)+"╧"+("═"*51)+"╧"+("═"*22)+"╧"+("═"*12)+"╝")
    input(cyc+"  Press Enter to Proceed"+rst)
def process_next_patient():
    s = 0
    space = [20, 35, 4, 7, 12, 13, 50,21, 11]    
    i = 0
    label = ["Name","Age","Gender","Birthdate","Phone Num","Address","Schedule"]
    while True:
        if len(allpnu) != 0:
            while True:
                os.system('cls') 
                print(" "*43+"╔"+("═"*72)+"╗")
                print(" "*43+f"║ "+cyc+"Patient Number: "+yec+f"{allpnu[0]}"+(" "*51)+rst+"║")
                print(" "*43+"╚"+("═"*72)+"╝")
                for info in pnumid.get(allpnu[0]):
                    print(" "*43+"│ "+label[i]+(" "*(11-len(label[i])))+": "+info+(" "*(58-len(info)))+"│")
                    i+=1
                i=0
                print(" "*43+"╔"+("═"*72)+"╗")
                print(" "*43+"║         "+rec+"[1] Exit          "+yec+"[2] Unattended          "+grc+"[3] Attended         "+rst+"║")
                print(" "*43+"╚"+("═"*72)+"╝")
                try:
                    ch=int(input(" "*43+cyc+"  Enter your choice: "+rst))
                    if ch == 1:
                        break
                    elif ch == 2:
                        pstatus.get(allpnu[0])[8] = "Unattended"
                        with open(PRfile, "a",encoding='utf-8') as file:
                            for info0 in pstatus.get(allpnu[0]):
                                if space[s] == 20:
                                    file.write("\n║ "+info0+(" "*(space[s]-len(info0))))
                                elif space[s] == 11:
                                    file.write("│ "+info0+(" "*(space[s]-len(info0)))+"║")
                                else:
                                    file.write("│ "+info0+(" "*(space[s]-len(info0))))
                                s+=1
                            s=0
                        allpnu.remove(allpnu[0])
                        break
                    elif ch == 3:
                        pstatus.get(allpnu[0])[8] = "Attended"
                        with open(PRfile, "a",encoding='utf-8') as file:
                            for info0 in pstatus.get(allpnu[0]):
                                if space[s] == 20:
                                    file.write("\n║ "+info0+(" "*(space[s]-len(info0))))
                                elif space[s] == 11:
                                    file.write("│ "+info0+(" "*(space[s]-len(info0)))+"║")
                                else:
                                    file.write("│ "+info0+(" "*(space[s]-len(info0))))
                                s+=1
                            s=0
                        allpnu.remove(allpnu[0])
                        break
                    else:
                        invld_ch_l()
                        continue
                except ValueError:
                    num_only_l()
                    continue
            if ch == 1:
                break
        else:
            cu_no_ne_pa_d()
            break
def view_patients_records():
    with open(PRfile,"r",encoding="utf-8") as file:
        info = file.read()
        print(info)
    print("╚"+("═"*21)+"╧"+("═"*36)+"╧"+("═"*5)+"╧"+("═"*8)+"╧"+("═"*13)+"╧"+("═"*14)+"╧"+("═"*51)+"╧"+("═"*22)+"╧"+("═"*12)+"╝")
    input(cyc+"  Press Enter to Proceed"+rst)
if __name__ == '__main__':
    mode()