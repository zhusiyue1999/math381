import math

# number of vertex
n=62

# number of color
i=10

# define vertex
V=[[1,2],[1,3],[2,3],[2,7],[2,8],[3,4],[3,6],[3,7],[4,5],[4,7],[5,6],[5,11],
   [6,7],[6,10],[6,11],[7,8],[7,10],[8,9],[8,10],[9,10],[9,13],[9,14],[9,16],
   [9,17],[10,11],[10,13],[11,12],[11,13],[12,13],[12,15],[12,20],[13,14],
   [13,15],[14,15],[14,16],[15,16],[15,19],[15,20],[16,17],[16,19],[17,18],
   [17,19],[18,19],[18,22],[18,23],[20,21],[20,22],[20,26],[21,22],[21,22],
   [21,26],[23,24],[23,48],[24,25],[24,38],[24,48],[25,26],[25,27],[25,38],
   [26,27],[26,28],[26,29],[27,28],[27,35],[27,38],[28,29],[28,30],[28,35],
   [29,30],[30,31],[30,34],[30,35],[31,32],[31,33],[31,34],[32,33],[33,34],
   [33,40],[33,41],[34,35],[34,36],[34,40],[34,42],[35,36],[35,37],[35,38],
   [36,37],[36,42],[37,38],[37,39],[37,42],[37,43],[38,39],[38,48],[39,43],
   [39,44],[39,47],[39,48],[40,41],[40,42],[41,42],[41,45],[42,43],[42,44],
   [42,45],[43,44],[44,45],[44,47],[45,46],[46,47],[46,50],[46,51],[47,48],
   [47,50],[48,49],[48,50],[49,50],[49,52],[50,51],[50,52],[51,52],[51,53],
   [52,53],[52,55],[53,54],[54,55],[54,56],[56,57],[56,60],[57,59],[57,60],
   [58,59],[59,60],[60,61],[61,62]]

# objective function
output = ""
for a in range(1,i+1):
    output += "+y_"+str(a)
print("min: "+output+";")

# requires all vertices to be colored with exactly one color
output = ""
for a in range(1,n+1):
    output = ""
    for b in range(1,i+1):
        output += "+x_"+str(a)+"_"+str(b)
    print(output+"=1;")

# requires that a vertex cannot be colored with an unused colored
for a in range(1,n+1):
    for b in range(1,i+1):
        print("x_"+str(a)+"_"+str(b)+"<=y_"+str(b)+";")

# requires that adjacent vertices have different colors
for edge in V:
    for b in range(1,i+1):
        print("x_"+str(edge[0])+"_"+str(b)+"+x_"+str(edge[1])+"_"+str(b)+"<=1;")

# we will not use color 2 if we do not use color 1, etc.
for a in range(2,i+1):
    print("y_"+str(a)+"<="+"y_"+str(int(a)-1)+";")

# two regions that border the same region cannot be colored the same
for a in range(1,n+1):
    for edge in V:
        if edge[0] == a:
            neighbor = edge[1];
            for e in V:
                if e[0] == neighbor:
                    for b in range(1,i+1):
                        print("x_"+str(a)+"_"+str(b)+"+x_"+
                          str(e[1])+"_"+str(b)+"<=1;")
                        
# all variables are binary
output = "bin "
for a in range(1,n+1):
    for b in range(1,i+1):
        if (a>1 or b>1):
            output += ","
        output += "x_"+str(a)+"_"+str(b)
print(output+";")

output = "bin "
for a in range(1,i+1):
    if (a>1):
        output += ","
    output += "y_"+str(a)
print(output+";")
