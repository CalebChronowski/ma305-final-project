import numpy as np
from math_scripts import *
from equations import equations

pi = np.pi
eqi = equations[0]
eqii = equations[1]

if __name__ == "__main__":
    # part 1
    print("="*42)
    print("part 1: integrating functions")
    print("\t (i.) integrate 4*sqrt(1-x)*dx from 0 to 2")
    print("\t(ii.) integrate (1-x)**-0.5*dx from -1 to 1") 
    print("="*42)

    # 1.a
    print()
    print("1a")
    print("\tsolve eq_i using the Trapezoid rule and the Simpsons 1/3 rule")
    print()

    # Trapezoid rule
    print("\tTrapezoid rule:")
    pi_1a_t = trapezoid_rule(eqi, 0, 1, 1000)
    pi_1a_t_error = pi_1a_t - pi
    print(f"\t\tresult: {pi_1a_t}\n\t\terror: {pi_1a_t_error}")
    print()

    # Simpson's rule
    print("\tSimpson 1/3 rule:")
    pi_1a_s = simpsons_rule(eqi, 0, 1, 1000)
    pi_1a_s_error = pi_1a_s - pi
    print(f"\t\tresult: {pi_1a_s}\n\t\terror: {pi_1a_s_error}")
    print()

    # 1.b
    print()
    print("1b")
    print("\tsolve both equations using the Midpoint rule")
    print()

    # Midpoint rule, equation i
    print("\tMidpoint rule:")
    pi_1b_i = midpoint_rule(eqi, 0, 1, 1000)
    pi_1b_i_error = pi_1b_i - pi
    print(f"\t\tresult: {pi_1b_i}\n\t\terror: {pi_1b_i_error}")
    print()

    try:
        # Midpoint rule, equation ii
        print("\tMidpoint rule:")
        pi_1b_ii = midpoint_rule(eqii, -1, 1, 1000)
        pi_1b_ii_error = pi - pi_1b_ii
        print(f"\t\tresult: {pi_1b_ii}\n\t\terror: {pi_1b_ii_error}")
        print()
    except:
        print("problem with Midpoint rule and eqii")
        
    # part 2
    print()
    print("="*42)
    print("part 2: Sum of Alternating Series")
    print("\t  (i.) approximation of Pi using arctan function")
    print("\t (ii.) Machins Formula using arctan")
    print("\t(iii.) comparison to Madhavas series")
    print("="*42)
    
    #2.1
    print()
    print("2a")
    print("\tAproximation fo Pi using Arctan summation")
    print("Arctan using 1000 intervals")
    pi_2a = approx_pi(1000)
    pi_2a_error = pi - pi_2a
    print(f"\t\tresult: {pi_2a}\n\t\terror: {pi_2a_error}")
    print()
    
    #2.2
    print()
    print("2b")
    print("\tMachins Formula using arctan to approxiate Pi")
    print("Machins formual using 20 intervals")
    pi_2b = machine_rule(20) 
    pi_2b_error = pi - pi_2b
    errordiff_2a_2b = abs(pi_2b_error - pi_2a_error)
    print(f"\t\tresult: {pi_2b}\n\t\terror: {pi_2b_error}")
    print(f"\t\tdiffrence of arctan to machins formula:{errordiff_2a_2b}")
    print("this formula provides a faster and closer approximation to Pi compared to just the Arctan summation")
    print()
    
    #2.3
    print()
    print("2c")
    print("\tComparing Madhavas series to Arctan summation")
    pi_2c= madhava_series(10)
    pi_2c_error= pi - pi_2c
    print("Madhava series using 10 intervals")
    print(f"\t\tresult: {pi_2b}\n\t\terror: {pi_2b_error}")
    errordiff_2b_2c = abs(pi_2c_error - pi_2b_error)
    print(f"\t\tdiffrence of arctan to machins formula:{errordiff_2b_2c}")
    print("Madhavas gives a closer approximation in 10 or less intervals compared to Arcsin")
    print()


    # part 3
    print("="*42)
    print("part 3:\n\tMonte Carlo integrations")
    print("="*42)
    print()
    
    # mc_area
    print("\tMonte Carlo integration of circle in a square")
    pi_3_area = mc_area(100)
    pi_3_area_error = pi - pi_3_area
    print(f"\t\tresult: {pi_3_area}\n\t\terror: {pi_3_area_error}")
    print()

        # mc_area
    print("\tMonte Carlo integration of cone in a sphere")
    pi_3_volume = mc_volume(100)
    pi_3_volume_error = pi - pi_3_volume
    print(f"\t\tresult: {pi_3_volume}\n\t\terror: {pi_3_volume_error}")
    print()
