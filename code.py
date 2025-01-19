import math
import time


#Im using time module to put delays in my program.


def calculate_cube(side_length, calc_type):
    if side_length < 0:
        print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
        return
    volume = side_length ** 3
    surface_area = 6 * (side_length ** 2)
    if calc_type == 'V':
        return volume
    elif calc_type == 'S':
        return surface_area
    elif calc_type == 'B':
        return volume, surface_area


def calculate_rectangular_prism(length, width, height, calc_type):
    if length < 0 or width < 0 or height < 0:
        print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
        return
    volume = length * width * height
    surface_area = 2 * (length * width + length * height + width * height)
    if calc_type == 'V':
        return volume
    elif calc_type == 'S':
        return surface_area
    elif calc_type == 'B':
        return volume, surface_area


def calculate_sphere(radius, calc_type):
    if radius < 0:
        print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
        return
    volume = (4/3) * math.pi * (radius ** 3)
    surface_area = 4 * math.pi * (radius ** 2)
    if calc_type == 'V':
        return volume
    elif calc_type == 'S':
        return surface_area
    elif calc_type == 'B':
        return volume, surface_area


def calculate_cylinder(radius, height, calc_type):
    if radius < 0 or height < 0:
        print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
        return
    volume = math.pi * (radius ** 2) * height
    surface_area = 2 * math.pi * radius * (radius + height)
    if calc_type == 'V':
        return volume
    elif calc_type == 'S':
        return surface_area
    elif calc_type == 'B':
        return volume, surface_area


def calculate_cone(radius, height, calc_type):
    if radius < 0 or height < 0:
        print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
        return
    volume = (1/3) * math.pi * (radius ** 2) * height
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    surface_area = math.pi * radius * (radius + slant_height)
    if calc_type == 'V':
        return volume
    elif calc_type == 'S':
        return surface_area
    elif calc_type == 'B':
        return volume, surface_area


def pythagorean_theorem():
    option = input("Press l to calculate one of the legs of a triangle, or h to calculate the hypotenuse: ").lower()
   
    if option == 'l':
        try:
            c = float(input("Enter the hypotenuse (c): "))
            a = float(input("Enter the length of leg a: "))
            if c < 0 or a < 0:
                print("Enter positive values.")
                return
            b = math.sqrt(c ** 2 - a ** 2)
            print(f"The length of leg b is: {b:.2f}")
        except ValueError:
            print("The Hypotenuse must be greater than the leg or you've entered a letter rather than a numerical value.")




   
    elif option == 'h':
        try:
            a = float(input("Enter the length of leg a: "))
            b = float(input("Enter the length of leg b: "))
            if a < 0 or b < 0:
                print("Enter positive values.")
                return
            c = math.sqrt(a ** 2 + b ** 2)
            print(f"The length of the hypotenuse is: {c:.2f}")
        except ValueError:
            print("Please enter numerical values.")
   
    else:
        print("Please choose either l(eg) or h(ypotenuse).")


def main():
    print("Welcome to Ismail's ISU Artifact.")
    time.sleep(1.5)
    print("This is the 3D Shapes Surface Area and Volume Calculator and the Pythagorean Theorem Tool.")
    time.sleep(2.3)
    print("Press 1 for Volume and Surface Area calc, or 2 for Pythagorean theorem tool.")
    time.sleep(3.5)
    choice = input("Please pick if you want to use the volume and surface area calculator or Pythagorean theorem tool. ")


    if choice == '1':
        calc_type = input("What will you calculate?:  V - Volume, S - Surface Area, B - Both: ").upper()
        if calc_type not in ['V', 'S', 'B']:
            print("You didnt pick an option try again.")
            return
        time.sleep(2)
        shape = input("Choose a Shape --- Cube: C, Rectangular Prism: R, Sphere: S, Cylinder: Y, Cone O: ").upper()
        if shape not in ['C', 'R', 'S', 'Y', 'O']:
            print("You did not pick an option, try again.")
            return
        time.sleep(2)


        if shape == 'C':  # Cube
            side_length = float(input("Enter the side length of the cube: "))
            if side_length < 0:
                print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
                return
            time.sleep(1)
            result = calculate_cube(side_length, calc_type)
        elif shape == 'R':  #RectangularPrism
            length = float(input("Enter the length of the rectangular prism: "))
            if length < 0:
                print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
                return
            time.sleep(1)
            width = float(input("Enter the width of the rectangular prism: "))
            if width < 0:
                print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
                return
            time.sleep(1)
            height = float(input("Enter the height of the rectangular prism: "))
            if height < 0:
                print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
                return
            time.sleep(1)
            result = calculate_rectangular_prism(length, width, height, calc_type)
        elif shape == 'S':  # Sphere
            radius = float(input("Enter the radius of the sphere: "))
            if radius < 0:
                print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
                return
            time.sleep(1)
            result = calculate_sphere(radius, calc_type)
        elif shape == 'Y':  # Cylinder
            radius = float(input("Enter the radius of the cylinder: "))
            if radius < 0:
                print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
                return
            time.sleep(1)
            height = float(input("Enter the height of the cylinder: "))
            if height < 0:
                print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
                return
            time.sleep(1)
            result = calculate_cylinder(radius, height, calc_type)
        elif shape == 'O':  # Cone
            radius = float(input("Enter the radius of the cone: "))
            if radius < 0:
                print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
                return
            time.sleep(1)
            height = float(input("Enter the height of the cone: "))
            if height < 0:
                print("Enter a positive value since a 3d shape having a negative dimensions is impossible")
                return
            time.sleep(1)
            result = calculate_cone(radius, height, calc_type)


        if calc_type == 'B':
            volume, surface_area = result
            print(f"The Volume: {volume:.2f}")
            time.sleep(1)
            print(f"The Surface Area: {surface_area:.2f}")
        elif calc_type == 'V':
            print(f"The Volume: {result:.2f}")
        elif calc_type == 'S':
            print(f"Surface Area: {result:.2f}")
#.2 isn’t available for older versions of python
   
    elif choice == '2':
        pythagorean_theorem()
    else:
        print("Please pick either option 1 or 2.")




if __name__ == "__main__":
    main()



