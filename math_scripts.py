import numpy as np

# Part 1
def trapezoid_rule(fn, a, b, n):
    delta_x = (b - a)/n
    x = np.linspace(a, b, n)
    sum = 0
    for i in range(0, len(x)):
        xi = a + (i+1) * delta_x
        sum += fn(xi)
    return delta_x * ( 0.5 * fn(x[0]) + sum + 0.5 * fn(x[n-1]))


def simpsons_rule(fn, a, b, n):
    # https://www.wolframalpha.com/input?i=integral+from+0+to+1+of+4+*+%281-x**2%29+**+0.5+using+simpson+rule+at+10+iteration 
    # I am not getting expected results for equation i
    # look into this

    delta_x = (b - a) / n
    x = np.linspace(a, b, n)
    
    # f(x_0)
    fx0 = fn(x[0])
    
    # sum of odds
    sum1 = 0
    for i in range(0, len(x)-1):
        xi = a + (i+1) * delta_x
        if i % 2 == 0:
            sum1 += 4*fn(xi)
    
    # sum of evens
    sum2 = 0
    for i in range(0, len(x)-2):
        xi = a + (i+1) * delta_x
        if i % 2 == 1:
            sum2 += 2*fn(xi)
    
    # f(x_n)
    fxn= fn(x[n-1])
    
    return (delta_x / 3) * (fx0 + sum1 + sum2 + fxn)


def midpoint_rule(fn, a, b, n):
    # https://www.wolframalpha.com/input?i=integral+from+0+to+1+of+4+*+%281-x**2%29+**+0.5+using+midpoint+rule+at+10+iteration
    # also slightly off
    delta_x = (b - a)/n
    x = np.linspace(a, b, n)
    sum = 0
    for i in range(0, len(x)):
        xi = a + (2*(i+1) - 1) * delta_x * 0.5
        sum += fn(xi)
    return delta_x * sum


#part 2
def arctan(x,N):
    result=0.0
    for n in range(1,N+1):
        count=((-1)**(n+1)*((x)**(2*n-1)/(2*n-1)))
        result += count 
    return result

def approx_pi(N):
    return 4*arctan(1,N)

def machine_rule(N):
    return 16*arctan(1/5,N)-4*arctan(1/239,N)

def madhava_series(N):
    
    result=0
    for n in range(N):
        count=((-1)**n)/(2*n+1)/3**n
        result=count+result
    
    return np.sqrt(12)*result


# Part 3

def mc_area(N):
    '''
    inputs:
        N: number of iterations
    outputs:
        area: estimated area
    '''    
    dim = 2 # change this to 3 for mc_volume()


    def in_circle(x, y):
        '''
        inputs:
            x: x coordinate
            y: y coordinate
        output:
            in_circle: True if in the circle x**2 + y**2 <= 1
        '''
        
        if x**2 + y**2 < 1:
            return True
        else:
            return False


    def get_random_points(N, dim):
        '''
        inputs:
            N: number of iterations
            dim: number of dimensions
        outputs:
            arr: an array of random points of dimension N by dim
        '''
        basic_array = np.random.rand(N, dim) # array of random values from 0 to 1

        # arange elements to range from -1 to 1
        array = (basic_array - 0.5*np.ones((N, dim))) * 2
        return array        


    def calculate_pi(points):
        '''
        inputs:
            points: array of points
        output:
            pi: approximated value of pi
        '''
        points = get_random_points(N, dim)
        circle = 0
        total = 0
        for point in points:
            total += 1
            if in_circle(point[0], point[1]):
                circle +=1
        r = circle / total
        pi = 4 * r
        return pi
    
    points =get_random_points(N, dim)
    pi = calculate_pi(points)
    return pi


def mc_volume(N):
    '''
    inputs:
        N: number of iterations
    outputs:
        area: estimated area
    '''
    print(f"computing volume of ice cream cone with N =  {N}  Monte Carlo iterations")    
    dim = 3 # change this to 3 for mc_volume()

    def in_cone(x, y, z):
        '''
        inputs:
            x: x coordinate
            y: y coordinate
            z: z coordinate
        output:
            in_cone: True if in the cone x**2 + y**2 >= z**2
        '''
        
        if z**2 > (x**2 + y**2):
            return True
        else:
            return False
        
    def in_sphere(x, y, z):
        '''
        inputs:
            x: x coordinate
            y: y coordinate
            z: z coordinate
        output:
            in_sphere: True if in the sphere x**2 + y**2 + (z - 1)**2 < 1
        '''
        if x**2 + y**2 + (z - 1)**2 < 1:
            return True
        else:
            return False
    
    def get_random_points(N, dim):
        '''
        inputs:
            N: number of iterations
            dim: number of dimensions
        outputs:
            arr: an array of random points of dimension N by dim
        '''         
        basic_array = np.random.rand(N, dim) # array of random values from 0 to 1
        # arange all elements from -1 to 1
        array = (basic_array - 0.5*np.ones((N, dim))) * 2
        # z was actually supposed to be from 0 to 2, so we will bad every value (-1 to 1) by +1
        array.T[2] = array.T[2] + np.ones((1, N))        
        return array

    def calculate_pi(points):
        '''
        inputs:
            points: array of points
        output:
            pi: approximated value of pi
        '''
        ice_cream = 0
        total = 0

        for point in points:
            x, y, z = point[0], point[1], point[2]
            total += 1
            if in_cone(x, y, z) and in_sphere(x, y, z):
                ice_cream += 1
        
        r = ice_cream / total
        pi = 8 * r # search zone is 2*2*2 cube

        return pi

    points = get_random_points(N, dim)
    pi = calculate_pi(points)

    return pi
        
if __name__ == "__main__":
    from equations import equations
    eqi, eqii = equations[0], equations[1]
    midpoint_rule(eqii,-1,1, 1000)