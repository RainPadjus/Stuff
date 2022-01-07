data = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]


def snail(data):
    size = len(data)
    r,c = 0, 0
    
    moving = "right"
    print(data[r][c])
    #data[r][c] = "x"

    for i in range(len(data)*len(data)):
        print("ROW {} COLUMN {}".format(r,c))
        
        if moving == "right":
            try:
                c+=1
                print(data[r][c])
                #data[r][c] = "x"
                if data[r][c] == "x":
                    moving = "dowm"
                    c-=1
            except:
                c-=1
                moving = "down"
        
        if moving == "down":
            try:
                r+=1
                print(data[r][c])
                #data[r][c] = "x"
                if data[r][c] == "x":
                    moving = "left"
                    r -=1
            except:
                r-=1
                moving = "left"

        if moving == "left":
            try:
                c-=1
                if c>-1:
                    print(data[r][c])
                    #data[r][c] = "x"
                else:
                    moving = "up"
                    #c +=1
                if data[r][c] == "x":
                    moving = "up"
                    c +=1
            except:
                c+=1
                moving = "up"

        if moving == "up":
            try:
                r-=1
                if (r > -1) and (data[r][c] != "x"):
                    print(data[r][c])
                else:
                    moving = "right"
                    r+=1
            except:
                r+=1
                moving = "right"

        data[0][0] = "x"           
        data[r][c] = 'x'
snail(data)

