from Analysis import NetworkAnalysis as NA

#for history using filing to write the history in txt file.
#w is to clear the content of file and then write 
hist = open("history.txt","w",encoding="utf-8")



while True:
    #Main menu
    print(           "\n"
                     "1. Series Resistor \n",
                     "2. Parallel Resistor \n",
                     "3. Series Capacitor \n",
                     "4. Parallel Capacitor \n",
                     "5. Series Inductor \n",
                     "6. Parallel Inductor \n",
                     "7. VDR for 2 Resistors \n",
                     "8. VDR for 3 Resistors \n",
                     "9. CDR for 2 Branches \n",
                    "10. CDR for 3 Branches \n",
                    "11. Voltages on Capacitor on time t \n",
                    "12. Current through inductor on time t \n",
                    "13. History \n"
                    "0. exit")
    
    
    #getting input
    user_req = int(input("Enter a number from 1 to 13: "))
    
    #Input Validation
    if user_req < 0 :
        print()
        print("Please Enter Valid input")
        print()
        continue
    
    # at user input(user_req) 1 and 2 , same input is requried like r1 and r2
    #so combined it into if else statement, Same as below
    
    
    #Series and parallel Resistors
    if user_req == 1 or user_req==2 :
        r1 = float(input("R1: ")) #user input 1 and 2 both requried r1
        r2 = float(input("R2: ")) #user input 1 and 2 both requried r2
        
        if user_req == 1 :
            print(f"Rt:  {NA.s_res(r1,r2):.3f}Ω")
            hist.write(f"Rt:  {NA.s_res(r1,r2):.3f}ohms\n")
        else:
            print(f"Rt:  {NA.p_res(r1,r2):.3f}Ω")
            hist.write(f"Rt:  {NA.p_res(r1,r2):.3f}ohms\n")
            
            
        
        
    #Series and parallel Capacitors
    elif user_req == 3 or user_req == 4 :
        C1 = float(input("C1: "))
        C2 = float(input("C2: "))
        
        if user_req == 3:
            print(f"Ceq: {NA.s_cap(C1,C2):.3f}F")
            hist.write(f"Ceq:  {NA.s_cap(C1,C2):.3f}F\n")

        else:
            print(f"Ceq: {NA.p_cap(C1,C2):.3f}F")   
            hist.write(f"Ceq:  {NA.p_cap(C1,C2):.3f}F\n"  )

          
    #Series and parallel Inductors  
    elif user_req == 5 or user_req== 6:
        L1 = float(input("L1: "))
        L2 = float(input("L2: "))
        
        if user_req == 5:
            print(f"Leq: {NA.s_ind(L1, L2):.3f}H")
            hist.write(f"Leq:  {NA.s_ind(L1, L2):.3f}H \n")

        else:
            print(f"Leq: {NA.p_ind(L1, L2):.3f}H")
            hist.write("Leq:  {NA.p_ind(L1, L2)):.3f}H\n")
            
    
    
    #VDR for 2 and 3 elements/components
    elif user_req == 7 or user_req == 8:
        V = float(input("Voltages: "))
        e1 = float(input("R1: "))
        e2 = float(input("R2: "))
        
        if user_req == 7:
            print(f"Vr1 , Vr2: {NA.vdr2(V, e1, e2)}V")
            hist.write(f"Vr1 , Vr2:  {NA.vdr2(V, e1, e2)}V \n")

        else:
            e3 = float(input("R3: "))
            print(f"Vr1 , Vr2 , Vr3: {NA.vdr3(V, e1, e2, e3)}V")
            hist.write(f"Vr1 , Vr2 , Vr3:  {NA.vdr3(V, e1, e2, e3)}V \n")

            

    #CDR for 2 and 3 branches
    elif user_req == 9 or user_req == 10:
        i = float(input("Current: "))
        e1 = float(input("R1: "))
        e2 = float(input("R2: "))
        
        if user_req == 9:
            print(f"Ir1 , Ir2: {NA.cdr2(i, e1, e2)}A")
            hist.write(f"Ir1 , Ir2:  {NA.cdr2(i, e1, e2)}A \n")

        else:
            e3 = float(input("R3: "))
            print(f"Ir1, Ir2, Ir3: {NA.cdr3(i, e1, e2, e3)}A")
            hist.write(f"Ir1, Ir2, Ir3:  {NA.cdr3(i, e1, e2, e3)}A \n")

          
    #V(t) of Capacitor of RC and i(t) of RL Circuit  
    elif user_req == 11 or user_req==12 :
        R = float(input("Resistor: "))
        t = float(input("T: "))
        if user_req == 11:
            Vo = float(input("Enter Volatge Vo: "))
            C = float(input("Capacitor C(uF): "))
            print(f"Vc(  {t} ): {NA.Vc(Vo, C, R, t):.3f} mV")
            hist.write(f"Vc(  {t}  ):  {NA.Vc(Vo, C, R, t):.3f} mV \n")

        else:
            io = float(input("Enter current io: "))
            L = float(input("Inductor L(mH): "))
            print(f"IL(  {t} ): {NA.IL(io, L, R, t):.3f} uA")
            hist.write(f"IL( {t} ):  {NA.IL(io, L, R, t):.3f} uA \n")

    
    
    elif user_req == 13:
        hist.close()

        #displaying history
        print()
        print("History")
        print()
        data = open("history.txt")
        for x in iter(data):
            print(x)

        data.close()
        
        hist = open("history.txt","a")
    
    
    #Exit and confirmation
    elif user_req == 0:


        print()
        print("Do you really want to exit")
        print("Press 1 to cancel or 2 to exit")
        user_req = int(input("Enter 1 or 2: "))
        if user_req == 1:
            continue
        else:
            break
        


        
hist.close()






        