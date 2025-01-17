import func


user_select = int(input("Choose a shape: 1 for Circle, 2 for Rectangle, 3 for Triangle :: "))

if user_select == 1:
    radius = int(input("You have selected shape circle.Please enter the radius :: "))
    print(func.area_circle(radius))
elif user_select == 2:
    length = int(input("You have selected shape rectangle.Please enter the length :: "))
    width  = int(input("You have selected shape rectangle.Please enter the width :: "))
    print(func.area_rectangle(length, width))
elif user_select == 3:
    base = int(input("You have selected shape triangle.Please enter the base ::"))
    height = int(input("You have selected shape triangle.Please enter the height :: "))
    print(func.area_triangle(base, height))
    
    
    
    

#n1 = int(input("Enter the first number"))
#n2 = int(input("Enter the second number"))

#print(func.add(n1, n2))
#print(func.sub(n1, n2))
#1print(func.prod(n1, n2))