import math

# nx is the board size in x-axis, and ny is the board size in y-axis.
nx=4
ny=7

# define a function to check if the position is on the board
def existence(x,y,nx,ny):
  if (x>=1 and y>=1 and x<nx and y<ny):
    return(1)
  else:
    return(0)

# moves knights can make
knightMoves=[[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]

# objective function
output = ""
for a in range(1,nx+1):
    for b in range(1,ny+1):
        output += "+x_"+str(a)+"_"+str(b)+"_b"+"+x_"+str(a)+"_"+str(b)+"_w"
print("min: "+output+";")

# each square can have at most one knight
for a in range(1,nx+1):
    for b in range(1,ny+1):
        print("+x_"+str(a)+"_"+str(b)+"_b"+"+x_"+str(a)+"_"+str(b)+"_w"+"<=1;")
        
# each square should be attacked by black knight 
for a in range(1,nx+1):
    for b in range(1,ny+1):
        output=""
        for move in knightMoves:
            x = a+move[0]
            y = b+move[1]
            if (existence(x,y,nx+1,ny+1)):
                output+= "+x_"+str(x)+"_"+str(y)+"_b"
        print(output +">=1;")

# each square should be attacked by white knight
for a in range(1,nx+1):
    for b in range(1,ny+1):
        output=""
        for move in knightMoves:
            x = a+move[0]
            y = b+move[1]
            if (existence(x,y,nx+1,ny+1)):
                output+= "+x_"+str(x)+"_"+str(y)+"_w"
        print(output +">=1;")

        
# all variables are binary
output = "bin "
for a in range(1,nx+1):
    for b in range(1,ny+1):
        if (a>1 or b>1):
            output += ","
        output += "x_"+str(a)+"_"+str(b)+"_b"+",x_"+str(a)+"_"+str(b)+"_w"
print(output+";")
