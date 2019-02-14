
# Main method
def main():
    print( "Problem 2:" )   
     
    input = "gone"
    
    G = (c * 4 for c in input) 

    # Test and verify that iter(G) and G are the same things.
    print( "iter(G) is G  = " + str(iter(G) is G ) )
     
    # What does this tell you about the nature of a Generator object/expression?
    print( "An iterator has been generated dynamically for the generator" )

    # Assign Iter(G) to an iterator object called it1 and 
    it1 = iter( G )

    # advance it to the next element by using next method. 
    res1 = next(it1)
    
    # Instantiate a new Iter(G) object called it2. 
    it2 = iter( G )
    
    # Use the next method and advance it to the next element. 
    res2 = next( it2 )

    # Observe the result and compare it with the results of it1.
    print( "res1 = " + res1  )
    print( "res2 = " + res2  )

    # Does the new Iter(G) object start the iterator from the start of the string object? 
    # Write down your understanding/conclusion from this experiment.
    print( "The object is the iterator, we have only one instance."  )
    print( "The second call to iter( G ) returns the same as it2 = it1" )
    
    # How can you get back the Iter(G) to point back to the beginning of the string? 
    print( "To get a new iterator the generator needs to be recreated." )
    G = (c * 4 for c in input) 
    it3 = iter( G )

    res3 = next( it3 )
    print( "res1 == res3 => " + str(res1 == res3 ) )

main()