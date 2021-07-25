def list(size):
    matrix =[]
    for k in range(size):
        matrix.append(0)
    return matrix

def PlaceQueens(Q,r):
    if r==len(Q):
        print_list(Q)
    else :
        for j in range(len(Q)):
            legal = True
            for i in range(r):
                if((Q[i]==j)or(Q[i]==j+r-i)or(Q[i]==j-r+i)):
                    legal = False               
            if legal :
                Q[r]=j
                PlaceQueens(Q,r+1)

def print_list(m):
     QueenPos=[]
     for l in range(len(m)):
         for j in range(len(m)):
             if j==m[l]:
                 QueenPos.append(m[l])

     print(QueenPos)
                    

size =input("input of chess board size : ")
PlaceQueens(list(int(size)),0)
    