def tileDefectiveChessBoard(n,i,j): # Wrapper function
    assert n>0 and n==int(n) ,"n (first parameter) should be an integer bigger than zero and power of two"

    def tileDefectiveChessBoardRec(A, tileIndex, startX, endX, startY, endY, i, j):
        n = endX -startX +1
        if n == 1 :
            return 
        if n == 2 :
            X = [startX, endX]
            Y = [startY, endY] 
            for i1 in X :
                for i2 in Y :
                    if i1!=i or i2!=j:
                        A[i1][i2] = tileIndex
            return tileIndex+1
        

        else :
            midX = (startX +endX)//2
            midY = (startY +endY )//2

            if  i <=midX  and   j <=midY :
                A[midX][midY+1] = A[midX+1][midY] = A[midX+1][midY+1] = tileIndex
                tileIndex+=1
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,startX,midX,startY,midY,i,j)
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,startX,midX,midY+1,endY,midX,midY+1)
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,midX+1,endX,startY,midY,midX+1,midY)
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,midX+1,endX,midY+1,endY,midX+1,midY+1)
                return tileIndex

            elif  i <=midX and midY< j :
                A[midX][midY] = A[midX+1][midY] = A[midX+1][midY+1] = tileIndex
                tileIndex += 1
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,startX,midX,startY,midY,midX,midY)
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,startX,midX,midY+1,endY,i,j)
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,midX+1,endX,startY,midY,midX+1,midY)
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,midX+1,endX,midY+1,endY,midX+1,midY+1)
                return tileIndex

            elif midX< i  and  j <=midY:
                A[midX][midY] = A[midX][midY+1] = A[midX+1][midY+1] = tileIndex
                tileIndex += 1
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,startX,midX,startY,midY,midX,midY)
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,startX,midX,midY+1,endY,midX,midY+1)
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,midX+1,endX,startY,midY,i,j)
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,midX+1,endX,midY+1,endY,midX+1,midY+1)
                return tileIndex

            else:
                A[midX][midY]= A[midX][midY+1] = A[midX+1][midY] = tileIndex
                tileIndex += 1
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,startX,midX,startY,midY,midX,midY)
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,startX,midX,midY+1,endY,midX,midY+1)
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,midX+1,endX,startY,midY,midX+1,midY)
                tileIndex = tileDefectiveChessBoardRec(A,tileIndex,midX+1,endX,midY+1,endY,i,j)
                return tileIndex

            


    A = [[1 for v in range(n)] for u in range(n)]
    A[i][j] = 0 # zero indicates the missng cell
    tileDefectiveChessBoardRec(A,1,0,len(A)-1,0,len(A)-1,i,j) #set the parameter tileIndex to 1
    return A
