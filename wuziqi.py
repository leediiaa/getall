#1代表白，-1代表黑，0代表无子
test_list = [
    [1, 0, 1, 0, 0,0],
    [-1, 0, -1,-1, -1,0],
    [1, 0, 0, 0, 0,0],
    [1, 0, 0, 0, 0,0],
    [1, 0, 0, 0, 1,0],
    [0,0,0,0,0,0],
]
# 判断上下是否超过五个  |   这个方向
def test_count(x,y,number,rows,cols):
    minx = x
    numbers = 1
    while minx >0:
        minx -= 1
        if test_list[minx][y] == number:
            numbers += 1
        else: break

    maxx = x
    while maxx < rows-1:
        maxx += 1
        if test_list[maxx][y] == number:
            numbers += 1
        else:
            break
    if numbers >= 5: # 超过5个结束循环
        return True

    # 判断左右最大数  -- 这个方向
    miny = y
    numbers = 1
    while miny > 0:
        miny -= 1
        if test_list[x][miny] == number:
            numbers += 1
        else:
            break

    maxy = y
    while maxy < cols-1:
        maxy += 1
        if test_list[x][maxy] == number:
            numbers += 1
        else:
            break

    if numbers >= 5:
        return True


    # / 方向的个数
    minx = x
    maxy = y
    numbers = 1
    while minx > 0 and maxy < cols - 1:
        minx -= 1
        maxy += 1
        if test_list[minx][maxy] == number:
            numbers += 1
        else:
            break

    maxx = x
    miny = y
    while maxx < rows-1 and miny > 0:
        maxx += 1
        miny -= 1
        if test_list[maxx][miny] == number:
            numbers += 1
        else:
            break

    if numbers >= 5:
        return True
    # \ 方向的个数
    minx = x
    miny = y
    numbers = 1
    while miny > 0 and minx > 0:
        miny -= 1
        minx -= 1
        if test_list[minx][miny] == number:
            numbers += 1
        else:
            break

    maxx = x
    maxy = y
    while maxy < cols -1 and maxx < rows - 1:
        maxx += 1
        maxy += 1
        if test_list[maxx][maxy] == number:
            numbers += 1
        else:
            break
    if numbers >= 5:
        return True

    return False

def test_win(test_list):
    row = len(test_list) # 行数
    col = len(test_list[0]) # 列数
    for i in range(row):
        for j in range(col): # 获取到每一个位子的元素
            number = test_list[i][j] # 当前下标的数值
            if number == 1 or number == -1:
                res = test_count(i,j,number,row,col)# 调用函数判断
                if res:
                    if number == 1:
                        print('白棋获胜')
                    else:
                        print('黑棋获胜')
                return  print('平局')
test_win(test_list)
