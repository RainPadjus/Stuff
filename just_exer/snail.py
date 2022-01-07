data = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

data = [[1,2],
        [3,4]]

data2 = [[1,2,3],
        [4,5,6],
        [7,8,9]]
data = [[]]

def snail(data):
    if data==[[]]: return []
    size = len(data)
    r,c = 0, 0
    ans = []
    moving = "right"
    if data[r][c]!= "x": ans.append(data[r][c])
    

    for i in range((len(data)*len(data))):
        #print("ROW {} COLUMN {} next move = {}".format(r,c, moving))
        
        if moving == "right":
            try:
                c+=1
                if data[r][c]!= "x": ans.append(data[r][c])
                if data[r][c] == "x":
                    #print("go right ist X")
                    moving = "down"
                    c-=1
                    #print("MOVING {} r,c = {}{}".format(moving, r, c))
            except:
                c-=1
                moving = "down"
        
        if moving == "down":
            try:
                r+=1
                if data[r][c]!= "x": ans.append(data[r][c])
            
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
                    if data[r][c]!= "x": ans.append(data[r][c])
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
                    if data[r][c]!= "x": ans.append(data[r][c])
                else:
                    moving = "right"
                    r+=1
            except:
                r+=1
                moving = "right"

        data[0][0] = "x"           
        data[r][c] = 'x'
    return(ans)
snail(data)


