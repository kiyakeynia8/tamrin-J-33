def kiya_contour_area(contour):
    area = 0
    x = contour[0: ,0: , 0]
    y = contour[0: ,0: , 1]
    lx = len(x)
    j = lx-1
    for i in range(lx):
        area += (x[j] + x[i]) * (y[j] - y[i])
        j = i
    return area[0] / 2