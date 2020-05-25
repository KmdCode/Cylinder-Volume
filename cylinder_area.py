import math

def circle_area(diameter):
    Area=1/4*math.pi*diameter**2
    return Area

def cylinder_volume(diameter, height):
    volume= circle_area(diameter)*height
    return volume

def main():
    a_diameter = int(input("ENTER THE DIAMETER: "))
    b_height = int(input("ENTER THE HEIGHT:"))
    answer=round(cylinder_volume(a_diameter,b_height),2)
    print(answer)

if __name__=='__main__':
    main()