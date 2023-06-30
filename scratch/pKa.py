while True:
    try:
       print("Base type?")
       print ('      Input e.g "0" for aromatic amines')
       print ('      Input e.g "1" for aliphatic and non-aromatic amines')
       BT = int(input("Base type: "))
       if BT == 0 or BT == 1:
           #TOTAL ENERGY of BASE    
           d = "Base.out"       
           try:    
                with open(d, "r") as file:
                  lines = file.readlines()
                for i in range(len(lines)-1,-1,-1):
                  if "OPTIMIZATION RUN DONE" in lines[i]:
                      line = lines[i-3].strip()
                      e1 = float(line.split("FINAL SINGLE POINT ENERGY")[1].strip())
                      break   
                print ("---------------------------------------------------------") 
                print ("")  
                print ("Report:")
                print ("-------") 
                print ("")    
                print ("--------------")    
                print ("Data of Base:")    
                print ("--------------")    
                print ("TOTAL ENERGY:",e1,"a.u")    
           except:    
                print("TOTAL ENERGY:","ERROR!","(Non-converged geometric optimization. Optimize the base again!)")    
           
           # HOMO ENERGY OF BASE   
           try:
              with open(d, "r") as f:     
                lines = f.readlines()
                for i in range(len(lines)-1, -1, -1):
                  if "ORBITAL ENERGIES" in lines[i]:
                    for j in range(i+4, len(lines)):
                        values = lines[j].split()
                        if len(values) == 4 and values[1] == '2.0000':
                            homo1 = float(values[3]) 
                            pass
                    break    
              print ("HOMO ENERGY:",homo1,"eV") 
           except:    
                print("HOMO ENERGY:","ERROR!","(Base.out file not found)") 
           #LUMO ENERGY of BASE    
           try:
              with open(d, "r") as f:     
                lines = f.readlines()
                for i in range(len(lines)-1, -1, -1):
                  if "ORBITAL ENERGIES" in lines[i]:
                    for j in range(i+3, len(lines)):
                      cols = lines[j].split()
                      if cols[1] == "0.0000":
                        # extract the value from the fourth column of that row
                        lumo1 = float(cols[3])
                        print ("LUMO ENERGY:",lumo1,"eV")
                        gap1 = abs((homo1) + (-lumo1))
                        print ("Gap ENERGY:",gap1,"eV") 
                        break
                    break    
           except:    
                print("LUMO ENERGY:","ERROR!","(Base.out file not found)")    
               
           #TOTAL Energy (N) of BASE    
           d = "N.out"       
           try:    
                with open(d, "r") as f:    
                   for line in f:    
                           if "FINAL SINGLE POINT ENERGY" in line:    
                             n = float(line.split("FINAL SINGLE POINT ENERGY")[1].strip())
                print ("TOTAL ENERGY (N):",n,"a.u") 
           except:    
                print("TOTAL ENERGY (N):","ERROR!","(N.out file not found)")    
               
           #TOTAL Energy (N-1) of BASE    
           d = "N-1.out"       
           try:    
                with open(d, "r") as f:    
                   for line in f:    
                           if "FINAL SINGLE POINT ENERGY" in line:    
                             n_1 = float(line.split("FINAL SINGLE POINT ENERGY")[1].strip())  
                print ("TOTAL ENERGY (N-1):",n_1,"a.u")    
           except:    
                print("TOTAL ENERGY (N-1):","ERROR!","(N-1.out file not found)")    
               
           #TOTAL Energy (N+1) of BASE    
           d = "N+1.out"       
           try:    
                with open(d, "r") as f:    
                   for line in f:    
                           if "FINAL SINGLE POINT ENERGY" in line:    
                             n1 = float(line.split("FINAL SINGLE POINT ENERGY")[1].strip())  
                print ("TOTAL ENERGY (N+1):",n1,"a.u")
           except:    
                print("TOTAL ENERGY (N+1):","ERROR!","(N+1.out file not found)")    
               
           #%NPSA of BASE    
           d = "S.out"       
           try:    
                with open(d, "r") as f:    
                   for line in f:    
                           if "Nonpolar surface area" in line:   
                             l = line.strip().split()
                             s = float(l[-2]) 
                print ("%NPSA:",s)
           except:    
                print("%NPSA:","ERROR!","(S.out file not found)")    
               
           # Average local ionization energy (ALIE) of Base    
           d = "ALIE1.out"       
           try:        
                with open(d, "r") as f:    
                   for line in f:    
                           if "Average local ionization energy (ALIE)" in line:    
                             a1 = float(line.split(":")[1].strip())
                print ("ALIE:",a1, "a.u")    
           except:    
                print("ALIE:","ERROR!","(ALIE1.out file not found)")    
               
           #-----------------------------------------------------------------------------    
           #TOTAL ENERGY of Conjugate acid.    
               
           d = "Conjugate_acid.out"    
           try:    
                with open(d, "r") as file:
                  lines = file.readlines()
                for i in range(len(lines)-1,-1,-1):
                  if "OPTIMIZATION RUN DONE" in lines[i]:
                      line = lines[i-3].strip()
                      e2 = float(line.split("FINAL SINGLE POINT ENERGY")[1].strip())
                      break       
                print (" ")    
                print ("--------------------------")    
                print ("Data of Conjugate acid:")    
                print ("--------------------------")    
                print ("TOTAL ENERGY:",e2,"a.u")    
           except:    
                print("TOTAL ENERGY:","ERROR!","(Non-converged geometric optimization. Optimize the base again!)")    

           # HOMO ENERGY OF Conjugate acid
           try:
              with open(d, "r") as f:     
                lines = f.readlines()
                for i in range(len(lines)-1, -1, -1):
                  if "ORBITAL ENERGIES" in lines[i]:
                    for j in range(i+4, len(lines)):
                        values = lines[j].split()
                        if len(values) == 4 and values[1] == '2.0000':
                            homo2 = float(values[3]) 
                            pass
                    break    
              print ("HOMO ENERGY:",homo2,"eV") 
           except:    
                print("HOMO ENERGY:","ERROR!","(Conjugate_acid.out file not found)") 
           #LUMO ENERGY of Conjugate acid    
           try:
              with open(d, "r") as f:     
                lines = f.readlines()
                for i in range(len(lines)-1, -1, -1):
                  if "ORBITAL ENERGIES" in lines[i]:
                    for j in range(i+3, len(lines)):
                      cols = lines[j].split()
                      if cols[1] == "0.0000":
                        lumo2 = float(cols[3])
                        print ("LUMO ENERGY:",lumo2,"eV")
                        gap2 = abs((homo2) + (-lumo2))
                        print ("Gap ENERGY:",gap2,"eV") 
                        break
                    break    
           except:    
                print("LUMO ENERGY:","ERROR!","(Conjugate_acid.out file not found)")   
               
           # Average local ionization energy (ALIE) of Conjugate acid    
           d = "ALIE2.out"       
           try:        
                with open(d, "r") as f:    
                   for line in f:    
                           if "Average local ionization energy (ALIE)" in line:    
                             a2 = float(line.split(":")[1].strip())
                print ("ALIE:",a2, "a.u")    
                de = ((e1-e2)*627.509391)
                dg = ((gap1-gap2))
                Xm = (0.5*(n_1-n1)*27.2114)
                da = ((a1-a2)*27.2114)
                print ("--------------------------")
                print ("")
                print ("--------------------------")		
                print ("        Variables:")		
                print ("--------------------------")		
                print ("ΔE: ","{:.2f}".format(de), "kcal/mol")
                print ("ΔHLGap: ","{:.2f}".format(dg),"eV")		
                print ("XM: ","{:.2f}".format(Xm),"eV")		
                print ("%NPSA: ","{:.2f}".format(s))		
                print ("ΔALIEN: ","{:.2f}".format(da),"eV")		
                print ("BaseT: ",BT)				
                pKa = ((0.1074*de) + (-0.1422*dg) + (-0.9132*Xm) + (0.0151*s) + (-1.4887*da) + (3.0608*BT) + (-30.7139))			
                print ("")
                print ("")				
                print ("--------------")				
                print ("USED EQUATION:")				
                print ("--------------")				
                print ("pKa = 0.1074ΔE - 0.1422ΔHLGap - 0.9132XM + 0.0151%NPSA - 1.4887ΔALIEN + 3.0608BaseT - 30.7139")			
                print ("")
                print ("")
                def print_box(result):
                    length = len(result)
                    top_line = '+' + '-' * (length + 2) + '+'
                    empty_line = '| ' + ' ' * length + ' |'
    
                    print(top_line)
                    print(empty_line)
                    print('| ' + result + ' |')
                    print(empty_line)
                    print(top_line)
                result = "The predicted pKa value is: {:.2f}".format(pKa)
                print_box(result)		
                print ("")                		
           except:
            print ("") 
            print("ERROR!")
       else:
         print("The value entered is not a valid integer. Please try again!")
         print ("")
         continue
    except ValueError:
        print("The value entered is not a integer. Please try again!")
        print ("")
        continue