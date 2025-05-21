#def_of_option.py
from allvariables import *
from TUI_display import *
def create_fh():
    if os.path.exists(PRfile):
        pass
    else:
        with open(PRfile,"w", encoding='utf-8') as file:
            file.write("\n╔"+("═"*190)+"╗")
            file.write("\n║"+(" "*87)+"Patients Records"+(" "*87+"║"))
            file.write("\n╠"+("═"*21)+"╤"+("═"*36)+"╤"+("═"*5)+"╤"+("═"*8)+"╤"+("═"*13)+"╤"+("═"*14)+"╤"+("═"*51)+"╤"+("═"*22)+"╤"+("═"*12)+"╣")
            file.write("\n║     Visit Date      │"+(" "*16)+"Name"+(" "*16)+"│ Age │ Gender │  Birthdate  │ Phone Number │"+(" "*22)+"Address"+(" "*22)+"│ Health Check Schedle │   Status   ║")
            file.write("\n╟"+("─"*21)+"┼"+("─"*36)+"┼"+("─"*5)+"┼"+("─"*8)+"┼"+("─"*13)+"┼"+("─"*14)+"┼"+("─"*51)+"┼"+("─"*22)+"┼"+("─"*12)+"╢")
def in_info(question):
    while True:
        res = input(question).title()
        if res != "":
            if question == " "*44+"Name"+(" "*21)+": " or question == " "*44+"Address"+(" "*18)+": ":
                if res.isdigit():
                    if question == " "*44+"Name"+(" "*21)+": ":
                        print(" "*44+yec+"Name cannot be numbers only."+rst)
                    elif question == " "*44+"Address"+(" "*18)+": ":
                        print(" "*44+yec+"Address cannot be numbers only."+rst)
                else:
                    break
            elif question == " "*44+"Age"+(" "*22)+": ":
                if res.isdigit():
                    if int(res) > 100 or int(res) < 1:
                        print(" "*44+rec+"Invalid age"+rst)
                    else:
                        res = res
                        break
                else:
                    print(" "*44+yec+"Please enter numbers only."+rst)
            elif question == " "*44+"Phone Number (11 digits) : ":
                if res.isdigit():
                    if len(res) != 11:
                        print(" "*44+rec+"Invalid number"+rst)
                    else:
                        res = res
                        break
                else:
                    print(" "*44+yec+"Please enter numbers only."+rst)   
            elif question == " "*44+"Gender (M/F)"+(" "*13)+": ":
                if res.isalpha():
                    if res == "Male" or res == "Female" or res == "M" or res == "F":
                        if res == "M":
                            res = "Male"
                            break
                        elif res == "F":
                            res = "Female"
                            break
                        break
                    else:
                        print(" "*44+rec+"Invalid Gender"+rst)
                else:
                    print(" "*44+yec+"Please enter letters only."+rst)
            elif question == " "*44+"Birthdate (YYYY-MM-DD)   : ":
                if len(res)== 10 and res[0:4].isdigit() and int(res[0:4]) > 1900  and int(res[0:4]) < 2025 and (res[4:5] == " "or res[4:5] == '/'or res[4:5] =='-') and res[5:7].isdigit() and int(res[5:7]) >= 1 and int(res[5:7])  <= 12 and (res[4:5] == " "or res[4:5] == '/'or res[4:5] =='-') and res[8:10].isdigit() and int(res[8:10]) >= 1 and int(res[8:10])  <= 31:
                    res = res[0:4]+"-"+res[5:7]+"-"+res[8:10]
                    break
                else:
                    print(" "*44+rec+"Invalid Date"+rst)
        elif res == "":
            print(" "*44+yec+"This field cannot be empty."+rst)
    return res
def ge_pnu():
    pnu = ""
    while True:
        for i in range(4):
            rnum=str(randint(0,9))
            pnu+=rnum
        if pnu in allpnu:
            continue
        else:
            break
    return pnu
def ge_psc():       
    global rdate
    global t
    global t24
    if len(allpsc) == 0: #if wala pa naka una sa karon na time
        while t < len(otime) and otime[t] < t24:
            t += 1
        if t >= len(otime):
            rdate = rdate + timedelta(days=1)
            t = 0
        sch = rdate.strftime("%Y-%m-%d ") + avti[otime[t]]
        t += 1
        return sch
    elif len(allpsc) != 0: #if naa nay ga una and mag based sa ga una og sa oras sheshhhhh     
        lst = allpsc[-1][11:]
        lst_key = None
        for k, v in avti.items(): #ari akong gi kuha ang last nga time og akoa sab gi kuha kong unsa iyaang key 
            if v == lst:
                lst_key = k
                break
        if lst_key is not None and otime.index(lst_key) < len(otime) - 1: #compare an key sa last
            t = otime.index(lst_key) + 1
            sch = rdate.strftime("%Y-%m-%d ") + avti[otime[t]]
            t += 1
            return sch
        else:
            rdate = rdate + timedelta(days=1)
            t = 0
            sch = rdate.strftime("%Y-%m-%d ") + avti[otime[t]]
            t += 1
            return sch
def file_handling():
    s = 0
    space = [20, 35, 4, 7, 12, 13, 50,21, 11]    
    with open(PRfile, "a",encoding='utf-8') as file:
        for r in allpnu:
            for c in pstatus.get(r):
                if space[s] == 20:
                    file.write("\n║ "+c+(" "*(space[s]-len(c))))
                elif space[s] == 11:
                    file.write("│ "+c+(" "*(space[s]-len(c)))+"║")
                else:
                    file.write("│ "+c+(" "*(space[s]-len(c))))
                s+=1
            s=0