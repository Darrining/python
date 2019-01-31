val=input("请输入带有温度表示符号的温度值（例如32C）：")
if val[-1] in ['c','C']:
    f=1.8*float(val[0:-1])+32
    print("转换后的温度为：%.2fF"%f)
elif val[-1] in ['F','f']:
    c=(float(val[0:-1])-32)/1.8
    print("转换后的温度为：%fC"%c)
else :
    print("输出有误")
