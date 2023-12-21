def moveDisks(n,start=1,destination=3,intermediate=2):
    """ Assumes n is an integer >=1 """
    if n>=2:  
        moveDisks(n-1, start,intermediate,destination) 
    print("Move disk from ", start, " to ", destination)
    
    if n>=2:  
        moveDisks(n-1, intermediate,destination,start)

def moveDisks4(n,st1=1, st2=2, destination=4, inter1=2, inter2=3):
    if n >= 2:
        moveDisks(n-1, st2, inter2, destination)
    print("Move disk from ", st2, " to ", destination)
    if n >= 2:
        moveDisks(n-1, st1, inter1, destination)
    print("Move disk from ", st1, " to ", destination)
    if n>=2:
        moveDisks4(n-1, inter1, inter2, destination, inter2, st1)



moveDisks4(3)