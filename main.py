import sys
sys.setrecursionlimit(10 ** 6)

class Challenge :

   
   def Hampers ( self , grid , arrhampers) :
       if not grid : return 0
       def dfs ( i , j , grid , hamperspoints) :
           if i < 0 or j < 0 or i >= row or j >= col or grid [ i ] [ j ] == 0 :
               return
           hamperspoints.append([i , j])
           grid [ i ] [ j ] = 0    # Mark cell as zero to avoid recounting
           dfs ( i + 1 , j , grid , hamperspoints)        
           dfs ( i - 1 , j , grid , hamperspoints)
           dfs ( i , j + 1 , grid , hamperspoints)
           dfs ( i , j - 1 , grid , hamperspoints)
           dfs ( i + 1 , j + 1 , grid , hamperspoints)        
           dfs ( i - 1 , j + 1 , grid , hamperspoints)
           dfs ( i + 1 , j - 1 , grid , hamperspoints)
           dfs ( i - 1 , j - 1 , grid , hamperspoints)
           return
       
       hampers = 0
       #arrhampers =[]
       hamperpoints=[]
       row = len ( grid )
       col = len ( grid [ 0 ] )
       for i in range ( 0 , row ) :    # Traverse grid
           for j in range ( 0 , col ) :
               if grid [ i ] [ j ] == 1 :
                   dfs ( i , j , grid ,hamperpoints)
                   arrhampers.append(hamperpoints)
                   hamperpoints = []
                   hampers += 1
        
       #return hampers
       
       
   def Findcentre ( self , arrhampers , centres) :
        nohampers = len ( arrhampers )
        #centres = []
        for i in range ( 0 , nohampers ) :
            nogifts = arrhampers[i]
            nogifts.sort()
            #print(nogifts)
            x_sigma=0
            y_sigma=0
            min=0
            max=0
            tot_area=0
            for j in range (len(nogifts)):
                if (j == len(nogifts)-1 or nogifts[j][0] != nogifts[j+1][0]):
                    max = j
                    tot_area=tot_area+(nogifts[max][1]-nogifts[min][1])+1
                    y_sigma=y_sigma + (nogifts[max][1]-nogifts[min][1]+1) * (nogifts[max][1]+nogifts[min][1]) * 0.5
                    x_sigma=x_sigma + (nogifts[max][1]-nogifts[min][1]+1)*nogifts[min][0]
                    min=j+1
            center = [x_sigma/tot_area, y_sigma/tot_area]
            centres.append(center)
                 
            
            
            
            
            
if __name__ == '__main__':
    line1= input()
    R,C,k = (int(x) for x in line1.split())
    
    if R < 1 or R > 100 or C < 1 or C > 100 or k < 1 or k > 15 :
      exit(0) 
    
# Initialize matrix
    matrix = []
# For user input
    for i in range(R):          # A for loop for row entries
        matrix.append(list(input())) 
        
    
    #print(matrix)
    result = [list( map(int,i) ) for i in matrix]
    #print(result)
    a = []
    
    
    #print('Number of Hampers : ',Solution().Hampers(result, ))
   
    Challenge().Hampers(result , a)
    #print(a)
    centers = []
    Challenge().Findcentre( a , centers )
    
    centerrev = []
    
    #for i in range (len(centers),0,-1) :
    for i in range (len(centers)) :
        centerrev.append([centers[i][1], R-centers[i][0] -1])
    centerrev.sort()
    
    if  len(centerrev) < k  :
        k = len(centerrev)
    for i in range (k) :
      print(centerrev[i][0], centerrev[i][1])
    
     

    #print(centers)

            
           
