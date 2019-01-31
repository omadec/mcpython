# variables
QUIT="quit"

def playGame( capitalIndex ):
    print( "Starting the game" )

    # Dict that will store the tries.
    # We store the number of tries per states.
    score = {};
    # stores the number of states found
    statesFound = 0
    
    # Loop on all the states
    for state in capitalIndex.keys():
        # Set the flag back to false
        foundCapital = False;

        # Loop while we have not found the capital      
        while( foundCapital != True ):
            userResponse = input("What is the capital of " + state+"? ")
        
            # massage the input value
            userResponse = userResponse.lower();

            # If the input is the quit command
            if( userResponse == QUIT ):
                # Display the score
                displayScore( capitalIndex, score, statesFound)
                
                # We stop the processing
                return

            # Get the capital            
            capital = capitalIndex.get( state )

            # Test if the value is valid, in lowercase
            if( userResponse == capital.lower() ):
                print( "Correct '" + capital + "' is the capital of " + state )

                # Found the value for the current state.
                foundCapital = True;
                # Increment the number of states found
                statesFound = statesFound + 1;
            else:
                # Display error message
                print( "'" + userResponse + "' is not the capital of " + state )
                
            # Increament the number of tries
            stateTries = score.get( state )
            if( stateTries is None ):
                score[state] =  1
            else:
                score[state] = stateTries+1

    # Done with the 50 states
    
    # Display the score
    displayScore( capitalIndex, score, statesFound) 
            
def displayScore( capitalIndex, score, statesFound):
    print()

    #statesFound = len(score.keys())-1;
    tries = 0

    # Loop on all the states
    for state in capitalIndex.keys():
        stateTries = score.get( state )
        if( stateTries != None ):
            tries = tries + stateTries

    print( "Score: found " + str(statesFound) + " state(s) in " + str(tries) + " tries." )


def loadConf( capitalIndex ):
 # Load the file in memory
 print( "Please enter the input file." )
 filename = input("If nothing is used 'us-state-capitals.csv' will be used")
 if( filename is "" ):
     filename = 'us-state-capitals.csv'

 file = open(filename, 'r')
 line = file.readline()

 # We skip the first line with the headers
 if line: 
     line = file.readline()
 
 while line:
     # split the line to get the State and capital.
     # we don't need to GPS corrdonates.
     tab = line.split(',', 2)
        
     # Add the capitals to the corresponding states
     capitalIndex[ tab[0] ] = tab[1];
        
     #print(tab[0] + ' ' + tab[1])
     # use realine() to read next line
     line = file.readline()
 file.close()
        
def main():

 print( "Welcome!" )
 print()

 capitalIndex = {};

 # Load the configuration
 loadConf( capitalIndex )

 # Play the game
 playGame( capitalIndex )

 print( "Thanks for playing" )


if (__name__ == '__main__'): 
    main()

