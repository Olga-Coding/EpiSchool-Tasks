from cmath import sqrt


def solve_quadratic(a,b,c): 
    disc = b**2 - 4*a*c 
    if (disc < 0): 
        # no solutions 
            print ('None')
    elif (disc == 0): 
        # one solution 
            sol1 = 0 
            print (sol1)
    elif (disc > 0): 
        # # two solutions to calculate 
            x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
            x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
            print (x1,x2)

solve_quadratic(-2,0,-16)