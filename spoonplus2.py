def menu():
    print("键入a返回功能菜单\n""键入b退出程序")


def tittle():
    print("输入1进行加解密\n" "输入2进行键值转换\n" "输入3进行QRcode指令")


def wrong():
    print("非法操作")


import base64
tittle()
i=input("请键入选择：")
while i=="1":
    print(" 键入1进行加密\n" "键入2进行解密\n")
    ii=input("请键入选择：")
    if (ii=="1"):
        result=input("请键入待加密字符串：")
        try:
          print(base64.b64encode(result.encode('utf-8')))
          menu()
          i=input("请键入选择：")
          if i=="a":
           tittle()
           i=input("请输入选择：")
          else:
              print("感谢使用")
              break
        except:
            wrong()
            menu()
            i=input("请键入选择：")
            if i == "a":
                tittle()
                i = input("请输入选择：")
            else:
                print("感谢使用")
                break
    elif(ii=="2"):
        result=input("请键入待解密字符串：")
        try:
            print(base64.b64encode(result.decode("utf-8")))
            menu()
            i=input("请键入选择：")
        except:
            wrong()
            menu()
            i=input("请键入选择：")
            if i == "a":
                tittle()
                i = input("请输入选择：")
            else:
                print("感谢使用")
                break
while i=="2":
    print('请分别输入几组字符串\n'"格式：键+空格+键+。。。\n""值+空格+值+。。。\n")
    p=input("请键入键：")
    q=input("请输入值：")
    try:
        list1 = p.split(" ")
        list2 = q.split(" ")
        dict1 = dict(zip(list1, list2))
        dict2 = {}
        for key, value in dict1.items():
            if value not in dict2:
                dict2[value] = [key]
            else:
                dict2[value].append(key)
        print(dict2)
        import json
        result1=json.dumps(dict1)
        result2=dict2
        print("json字符串为:\n",result1)
        print("新字典为:\n",result2)
        print("其类型分别为：\n",type(result1),type(result2))
        menu()
        i=input("请键入选择：")
        if i == "a":
            tittle()
            i = input("请输入选择：")
        else:
            print("感谢使用")
            break
    except:
        wrong()
        menu()
        i=input("请键入选择：")
        if i=="a":
            tittle()
            i= input("请输入选择；")
        else:
            print("感谢使用")
            break
while i=="3":
    import qrcode
    h=input("请输入文件名：")
    try:
        f1=open(h,"r")
        f2=f1.read()
        img=qrcode.make(data=f2)
        img.save("二维码.jpg")
        menu()
        i=input("请键入选择：")
        if i == "a":
            tittle()
            i = input("请输入选择；")
        else:
            print("感谢使用")
            break
    except:
        wrong()
        menu()
        i = input("请键入选择：")
        if i == "a":
            tittle()
            i = input("请输入选择；")
        else:
            print("感谢使用")
            break





















