# Program to multiply two matrices using nested loops
import random

@profile
def main():
    N = 250
    
    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    
    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        #for j in range(len(Y[0])):                # This was up to and including ver 3
            # iterate through rows of Y
            #for k in range(len(Y)):               # These two lines are the intitial version
            #    result[i][j] += X[i][k] * Y[k][j] #
            #result[i][j] = sum(X[i][k] * Y[k][j] for k in range(len(Y)))  # This line is version 2
            #result[i][j] = sum([X[i][k] * Y[k][j] for k in range(len(Y))])  # This line is version 3
        result[i][:] = sum([prod[0]*prod[1] for prod in zip(X[i][:],Y[:][:])])) for  # This line is version 4

    for r in result:
        print(r)

if __name__ == "__main__":
    main()
