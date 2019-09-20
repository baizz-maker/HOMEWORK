print("输入1进行加解密\n" "输入2进行键值转换\n" "输入3进行QRcode指令")
i=input("请输入选择：")
if (i=="1"):
    import base64
    print(" 键入1进行加密\n" "键入2进行解密\n")
    ii=input("请输入选择：")
    if (ii=="1"):
        result=input("请输入字符串：")
        try:
          print(base64.b64encode(result.encode('utf-8')))
        except:
          print("非法输入")
    elif(ii=="2"):
        result=input("请输入字符串：")
        try:
            print(base64.b64encode(result.decode("utf-8")))
        except:
            print("非法输入")
elif(i=="2"):
    print('请输入几组字符串\n'"格式：{“key”+空格+:+空格+“value”,...}")
    mid=input("在此输入：")
    dic=eval(mid)
    try:
        dict1={}
        dict1=dict([val,key] for key, val in dic.items())
        import json
        result1=json.dumps(dict1)
        result2=dict1
        print("json字符串为:\n",result1)
        print("新字典为:\n",result2)
        print("其类型分别为：\n",type(result1),type(result2))
    except:
        print('非法输入')
if(i=="3"):
    import qrcode
    h=input("请输入文件名：")
    f1=open(h,"r")
    f2=f1.read()
    img=qrcode.make(data=f2)
    img.save("二维码.jpg")





















