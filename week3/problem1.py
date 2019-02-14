class Iteratefirstn: 
    """Iterator for looping over the first n."""    
    def __init__(self, max):         
        self.max = max  
        self.index = 0
	
    def __iter__(self):
        return self
	
    def __next__(self):
        if self.index > self.max:
            raise StopIteration         
		
        self.index = self.index + 1
		
        return self.index

# Main method
def main():
    print( "Problem 1:" )   
     
    max = 1000000
     
    iterator = iter(Iteratefirstn(max))
     
    sum_of_first_n = sum( iterator )
     
    print( "Sum of first " + str(max) + " elements using an iterator class = " + str(sum_of_first_n) )

    res_generator = sum(i for i in range(0, max+2))    
    
    print( "Sum of first " + str(max) + " elements using a generator       = " + str(res_generator) )
    

main()