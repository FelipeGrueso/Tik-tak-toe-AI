import random
i = "         "
turno = True

print("---------")
print("|",i[0],i[1],i[2],"|")
print("|",i[3],i[4],i[5],"|")
print("|",i[6],i[7],i[8],"|")
print("---------")
i = list(i)

        
coordenadas = {"['1', '1']": 0, "['1', '2']": 1, "['1', '3']": 2, "['2', '1']": 3, "['2', '2']": 4, "['2', '3']": 5, "['3', '1']": 6, "['3', '2']": 7, "['3', '3']": 8}

while True:
    
    try:
        if turno == True:
            k = input("Enter the coordinates: ")
            if int(k[0]) < 4 and int(k[2])< 4:
                k = str(k.split())
                

                if i[coordenadas[k]] != "X" and i[coordenadas[k]] != "O":
                    
                        i[coordenadas[k]] = "X"
                        print("---------")
                        print("|",i[0],i[1],i[2],"|")
                        print("|",i[3],i[4],i[5],"|")
                        print("|",i[6],i[7],i[8],"|")
                        print("---------")
                        turno = not True

                else:
                    print("This cell is occupied! Choose another one!")

             
            else:
                print("Coordinates should be from 1 to 3!")

         
        elif turno == False:
            idx = [ k for k in range(len(i)) if i[k] == " " ]
            
            k = random.choice(idx)
            for key, value in coordenadas.items():
                if k == value:
                    k = key
            
            if i[coordenadas[k]] != "X" and i[coordenadas[k]] != "O":
                
                print("Making move level \"easy\"")
                i[coordenadas[k]] = "O"
                turno = not False
                print("---------")
                print("|",i[0],i[1],i[2],"|")
                print("|",i[3],i[4],i[5],"|")
                print("|",i[6],i[7],i[8],"|")
                print("---------")
            
                

        if i[0]==i[1]==i[2] == "O" or i[0]==i[1]==i[2] == "X":
            print(i[0], "wins")
            break
                                 

        elif i[3]==i[4]==i[5] == "O" or i[3]==i[4]==i[5] == "X":
            print(i[3], "wins")
            break
    
        elif i[6]==i[7]==i[8] == "O" or i[6]==i[7]==i[8] == "X":
            print(i[6], "wins")
            break

        elif i[0]==i[3]==i[6] == "O" or i[0]==i[3]==i[6] == "X":
            print(i[0], "wins")
            break 

        elif i[1]==i[4]==i[7] == "O" or i[1]==i[4]==i[7] == "X":        
            print(i[1], "wins")
            break
    
        elif i[2]==i[5]==i[8] == "O" or i[2]==i[5]==i[8] == "X":
            print(i[2], "wins")
            break
    
        elif i[0]==i[4]==i[8]== "O" or i[0]==i[4]==i[8]== "X":
            print(i[4], "wins")
            break
                
        elif i[2]==i[4]==i[6] == "O" or i[2]==i[4]==i[6] == "X":
            print(i[4], "wins")
            break

        elif i.count(" ") == 0:
            print("Draw")
            break
               
                            
    except Exception:
        print("You should enter numbers!")
