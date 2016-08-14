import math
def inTriangle(A, B, C, P):
    dot_product = lambda p1,p2: float((p1[0]*p2[0]) + (p1[1]*p2[1]))
    lenth = lambda point: float((point[0]**2 + point[1]**2)**.5)
    angle = lambda p1,p2: float(math.degrees(
        math.acos(dot_product(p1,p2)/(lenth(p1)*lenth(p2)))))
    points = [A,B,C]
    for point in points[:]:
        other_points = points[:]
        other_points.remove(point)
        print "looking at", point, other_points
        vector1 = (other_points[0][0] - point[0],other_points[0][1] - point[1])
        vector2 = (other_points[1][0] - point[0], other_points[1][1] - point[1])
        vector3 = (P[0] - point[0], P[1] - point[1])
        try:
            angle1 = angle(vector1, vector2)
            angle2 = angle(vector1, vector3)
            angle3 = angle(vector2, vector3)
            print "vectors are", vector1, vector2, vector3
            print "angles are", angle1, angle2, angle3, angle2+angle3, (angle2+angle3)-angle1
            if angle2+angle3 - angle1 > .001:
                return False
        except ValueError:
            return False

    return True

def main():
    print inTriangle((1,1),(3,4),(6,2),(3,4))

if __name__ == "__main__":
    main()
        

