import numpy as np

def isEmpty(Arr):
    # Cek list kosong
    return len(Arr) == 0

def findSide(p1,p2,p3):
    # Memeriksa point p3 apakah disebelah kiri atau kanan garis yang dibentuk p1 dan p2
    aX = p1[0]
    aY = p1[1]
    bX = p2[0]
    bY = p2[1]
    cX = p3[0]
    cY = p3[1]

    val = ((bX - aX)*(cY - aY) - (bY - aY)*(cX - aX))
    thresh = 1e-9
    if val >= thresh:
        return 1
    elif val <= -thresh:
        return -1
    else:
        return 0

def DividePoints(ArrPoints,point1,point2):
    # Membagi point menjadi 2 sebelah kiri garis dan sebelah kanan garis
    tempArr = ArrPoints
    right = []
    left = []
    for i in tempArr:
        det = findSide(point1,point2,i)
        if(det>0):
            left.append(i)
        elif(det<0):
            right.append(i)

    return left, right

def Jarak(p1,p2,p3):
    # Mengembalikan jarak dari titik p3 dengan garis yang dibentuk p1 dan p2
    a = np.array(p1)
    b = np.array(p2)
    c = np.array(p3)
    Dist = np.cross(b-a,c-a)/np.linalg.norm(b-a)
    return Dist

def findHull(ArrP,p1,p2,solution):
    # Algoritma dalam mencari ConvexHull setelah point-point sudah dibagi 2
    if(isEmpty(ArrP)): 
        return
    else:
        farthestPoint = ArrP[0]
        maxDistance = 0.0

        for i in ArrP:
            tempJarak = Jarak(p1,p2,i)
            if(tempJarak >= maxDistance):
                maxDistance = tempJarak
                farthestPoint = i

        solution.remove([p1,p2])
        solution.append([p1,farthestPoint])
        solution.append([farthestPoint,p2])
        S1,temp = DividePoints(ArrP,p1,farthestPoint)
        S2,temp = DividePoints(ArrP,farthestPoint,p2)

        findHull(S1,p1,farthestPoint,solution)
        findHull(S2,farthestPoint,p2,solution)


def ConvexHull(points):
    # Algoritma dalam mencari ConvexHull dari sekumpulan point-point
    hull = []
    tempArr = points.copy()
    tempArr.sort()
    p1 = tempArr[0]
    p2 = tempArr[-1]
    hull.append([p1,p2])
    hull.append([p2,p1])
    S1,S2 = DividePoints(tempArr,p1,p2)

    findHull(S1,p1,p2,hull)
    findHull(S2,p2,p1,hull)

    for i in range(len(hull)):
        hull[i]=[points.index(hull[i][0]),points.index(hull[i][1])]

    return hull

