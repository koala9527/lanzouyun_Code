import TURING
import easygui
import cv2

def identi(names):
    img_data = "./pic/"+str(names)+".png"
    TURING.Pixel_FromPicture(img_data)
    im = cv2.imread(img_data)

    #切割图片，保留有效的图片
    im = im[0:30, 0:99]
    TURING.Filter_Tailor(0,0,99,30)

    #色调分离，将整个图片的颜色分为几个种。下面的函数将图片分成四种颜色分别为：0，85，170，255。将每一个点的rgb平均值放到四个区间对比。这四个区间为：0-64，64-128，128-192，192-255。落在每个区间就会固定一个颜色值，方便后面的图像处理
    TURING.Filter_Posterization(4)

    #二值化，其中的参数是色阶阈值，色阶阈值：一个点分为rgb三个值，三个值的平均值为阈值。该函数的作用就是遍历图像的每一个点的rgb平均值改变点的颜色，大于阈值为白色。小于阈值为黑色，现在设置阈值为95，处理后就会变成黑白色的图片了。
    TURING.Filter_Binaryzation("95")


    #去除杂点，现在是白底黑字，每个像素点周围一共8个点。周围大于8个白点是就由白变黑 ，作用就是去除孤立的颜色点
    TURING.Filter_Despeckle(8,0,0)

    #颜色反转 转前白底黑字 转后黑底白字，只有黑底白字才能进行字符切割。
    TURING.Filter_InverseColor()


    #范围投影字符切割，最重要的一步，非常难解释。为插件作者独创的算法，简单的说一下大概的内容，如有人想仔细了解可以问作者哈哈。作用就是找到切割验证码的字符，识别有几个字符，字符的范围和位置
    #现在是黑底白字的图片，以每一个白点为一个字符范围起始点。字符范围为一个矩形，需要一个终点才能圈成一个矩形，从上往下从左往右遍历找终点，第一步就是识别这个白点的右下角的颜色如果也是白色，终点往下移动，（高度+1），如果是黑色，终点就要往右下角移动（高+1，宽+1），直到遇到图片的边缘或者超过设置的间隙。
    #这时候要注意一个字可能会被切成两个部分，就要设置行间隙和列间隙。下面根据实际情况设置最小的行间隙和列间隙就是8，字符之间的间隔最少为8个像素，还可以设置其他的参数，比如矩形框的宽高范围，不在范围的框框抛弃
    TURING.Incise_ScopeAisle(8,8)

    #获取切割后的数据，范围值是字符串比较长，每个框的数据以竖杠分割，其中一个框的数据有四个，分别是左上角的左边，宽高，图色数据以逗号分割，拿两个点的数据给大家看看
    #8, 13, 8, 10, 00111111000111110110110001000110001000011000100000110011001101100111100000001100 | 30, 11, 8, 10, 00110000000011000110100001001110000100011000000001110010001101011011100001101100
    datas = TURING.Incise_GetCharData()

    # add_num这是要在opencv画框的边缘扩充参数，下面会用插件的捕获到框框数据绘制大一点的框框来制作字库，好看一点
    add_num = 3

    if len(datas)>0:
        datas_list = datas.split("|")
        for j in datas_list:
            data_lists = j.split(",")
            x1 =int(data_lists[0])-add_num  #左上角的x坐标
            y1 = int(data_lists[1])-add_num  #左上角y坐标
            x2 = int(data_lists[0]) +int(data_lists[2])+add_num  #框的宽
            y2 = int(data_lists[1])+int(data_lists[3])+add_num  #框的高
            cv2.rectangle(im,(int(x1),int(y1)),(int(x2),int(y2)),(255,0,255),1)  #绘制框框
        im = cv2.resize(im, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)  # 图太小了，需要宽高各乘以2.5来看下这个图以便人工识别这个图的数字是多少
        cv2.imshow("draw_0", im)
        cv2.moveWindow("draw_0", 800, 300)  # 移动显示图片的窗口，因为默认的位置遮挡了下面的输入弹窗
        #统计识别的字符个数
        data_len = len(datas_list)

        #弹窗显示原始验证码，显示验证码的个数，输入框人工输入数字
        input_data = easygui.enterbox(msg="请输入" + str(data_len) + "个字符添加进入字库：", title=' ', default=' ', strip=True,
                                      image=img_data, root=None)

        for k in range(data_len):
            # 组装字库的内容
            data_lists = datas_list[k].split(",")
            #制作字库
            insert_data = input_data[k] + "|" + data_lists[2] + "," + data_lists[3] + "|" + data_lists[4]
            #添加字库数据进入字库文件
            print("插入数据："+input_data[k] + "|" + data_lists[2] + "," + data_lists[3] + "|" + data_lists[4]  )
            with open("识别库1.lib", 'a+') as f:
                f.write(insert_data + "\n")
        #关闭所有opencv创建的窗口
        cv2.destroyAllWindows()
    else:

        return

#遍历所有的验证码
for i in range(100):
    identi(i)