i = input("Enter cells: ")
i = i.replace("_"," ")
if i.count("X") > i.count("O"):
    turno = not True
else:
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
        k = input("Enter the coordinates: ")
        if int(k[0]) < 4 and int(k[2])< 4:
            k = str(k.split())
            

            if i[coordenadas[k]] != "X" and i[coordenadas[k]] != "O":
                
                if turno == True:
                    i[coordenadas[k]] = "X"
                    turno = not turno
                    print("---------")
                    print("|",i[0],i[1],i[2],"|")
                    print("|",i[3],i[4],i[5],"|")
                    print("|",i[6],i[7],i[8],"|")
                    print("---------")
         
                else:
                    i[coordenadas[k]] = "O"
                    turno = not turno
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

                elif i.count(" ") > 0:
                    print("Game not finished")
                    break
                   
            else:
                print("This cell is occupied! Choose another one!")

             
        else: 
            print("Coordinates should be from 1 to 3!")
             
    except Exception:
        print("You should enter numbers!")
