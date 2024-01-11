def fun(n):
    rs = []
    for i in range(n):
        rs.append(rs[:])
    return rs
print(fun(3))
