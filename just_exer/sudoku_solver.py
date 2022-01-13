#sudoku solver


##to do( everistik (if we have 1,2,3 in row-> search only thru 4-9))
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


puzzle_3 = [[0,3,4,6,7,8,9,1,2],
  [6,0,2,1,9,5,3,4,8],
  [1,9,0,3,4,2,5,6,7],
  [8,5,9,0,6,1,4,2,3],
  [4,2,6,8,0,3,7,9,1],
  [7,1,3,9,2,0,8,5,6],
  [9,6,1,5,3,7,0,8,4],
  [2,8,7,4,1,9,6,0,5],
  [3,4,5,2,8,6,1,7,0]]
#75 4239

def solve(data):
    
    # making track of zeroes
    zeroes = []
    candidats = []
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == 0: 
                zeroes.append([i,j])
                
                candidats.append(list({1,2,3,4,5,6,7,8,9} - set([data[row][j] for row in range(9)] + data[i])))

    brute_force(len(zeroes)-1, data, zeroes, candidats)
    

def brute_force(n, data, zeroes, candidats):

    for i in data:
        print(i)
    print("\033[F"*10)

    if n >= 0:
        for i in range(len(candidats[n])):
            data[zeroes[n][0]][zeroes[n][1]]=candidats[n][i]
            brute_force(n-1, data, zeroes, candidats)
            if check_board(data):
                print("ALARM!!!")
                print(data)
                break
    else: 
        for i in data:
            print(i)
        print("\033[F"*10)


def check_board(data):
    flag = True
    for x in range(0,7,3):
        for j in range(0,7,3):
            #print("3x3 \n")

            sub = [data[i][x:x+3] for i in range(j,j+3)]
            one = []
            for i in sub:
                for j in i:
                    one.append(j)
            #print(one)
            flag *= (len(set(one)) == len(one) and (0 not in one))


    for i in data:
        flag *= (len(set(one)) == len(one) and (0 not in one))
        #print(i)
    
    for x in range(0,9):
        sub = [data[i][x] for i in range(0,9)]
        flag *= (len(set(sub)) == len(sub) and (0 not in one))
    
    return(flag)

solve(puzzle)


#check_board(puzzle)
