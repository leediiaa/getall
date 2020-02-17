import os
result = []
def get_all(pa):
    get_dir=os.listdir(pa)
    for i in get_dir:
        sub_dir = os.path.join(pa,i)
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            result.append(i)
if __name__=="__main__":
    print('请输入需要查询的目录：')
    dir=input()
    get_all(dir)
    print(result)
