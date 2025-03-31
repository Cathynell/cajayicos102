import numpy as np

def solve_quadratic(a, b, c):
    roots = np.roots([a, b, c])
    return roots

def solve_cubic(a, b, c, d):
    roots = np.roots([a, b, c, d])
    return roots

def solve_quartic(a, b, c, d, e):
    roots = np.roots([a, b, c, d, e])
    return roots 

def main():
    print("Choose the type of equation to solve:")
    print("1. Quadratic Equation (ax^2 + bx + c = 0)")
    print("2. Cubic Equation (ax^3 + bx^2 + cx + d = 0)")
    print("3. Quartic Equation (ax^4 + bx^3 + cx^2 + dx + e = 0)")
    
    user_input = int(input("Enter your choice (1, 2, or 3): "))
    
    if user_input == 1:
        a, b, c = map(float, input("Enter coefficients a, b, c: ").split())
        roots = solve_quadratic(a, b, c)
    elif user_input == 2:
        a, b, c, d = map(float, input("Enter coefficients a, b, c, d: ").split())
        roots = solve_cubic(a, b, c, d)
    elif user_input == 3:
        a, b, c, d, e = map(float, input("Enter coefficients a, b, c, d, e: ").split())
        roots = solve_quartic(a, b, c, d, e)
    else:
        print("Invalid choice!")
        return
    
    print("The roots of the equation are:", roots)

main()
