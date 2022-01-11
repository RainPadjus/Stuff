#sudoku solver

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


puzzle_solved = [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]]

def solve(data):
    
    # making track of zeroes
    zeroes = []
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == 0: zeroes.append((i,j))

    # brute force zero places:
    
    #for place in zeroes:
        #for place in zeroes:




    #cheking_sudoku_true:
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
            flag *= (len(set(one)) == len(one))
        
    
    for i in data:
        flag *= (len(set(one)) == len(one))
        #print(i)
    
    for x in range(0,9):
        sub = [data[i][x] for i in range(0,9)]
        flag *= (len(set(sub)) == len(sub))
    print("Final flag:", flag)

    print(zeroes)

#solve(puzzle)





zer = [0,0,0,0]
answer = True
def test(n):
    if n >= 0 and True:
        for i in range(10):
            #print("level {}, i = {}".format(n,i))
            zer[n] = i
            test(n-1)
            if sum(zer) == 28:
                print("HOPP:", 0)
                print("ZER: ", zer)
                break
            print(zer)
    else: pass


test(3)
