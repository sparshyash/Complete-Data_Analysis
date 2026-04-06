# Generators 

# A generator function is a special type of function that returns an iterator object. Instead of using return to send back a single value, generator functions use yield to produce a series of results over time. The function pauses its execution after yield, maintaining its state between iterations.

def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt  # Uses yield instead  of return to produce iterate object 
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)
    
# Creation 

def fun():
    yield 1            
    yield 2            
    yield 3            
 
# Driver code to check above generator function
for val in fun(): 
    print(val)
    

sq = (x*x for x in range(1, 6))
for i in sq:
    print(i)
    
    

