def kiya_boundingRect(contour):
    ob = 0
    ab = 0

    for c in contour:
        c = (c[0])
        
        if c[0] > ob:
            ob = c[0]

        if c[1] > ab:
            ab = c[1]

    ok = ob
    ak = ab

    for c in contour:
        c = (c[0])
        
        if c[0] < ok:
            ok = c[0]

        if c[1] < ak:
            ak = c[1]

    return ok,ak,(ob+1)-ok,(ab+1)-ak