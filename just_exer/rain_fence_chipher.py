def encode_rail_fence_cipher(string, n):
    level = 1
    buff = ""
    geo = [[" " for i in range(len(string))] for i in range(n)]


    for i in range(len(string)):
        print("{} on row {} colum {}".format(string[i], level-1, i))
        
        geo[level-1][i] = string[i]

        #buff += str(string[i]) +str(level)
        
        if level==1:
            moving="down"
        if level==n:
            moving="up"

        if moving == "down": level+=1
        if moving == "up": level -=1
        

    print(geo)

    for i in geo:
        for j in i:
            if j != " ": buff+=j
    print(buff)



def decode_rail_fence_cipher(string, n):
    pass


encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3)
