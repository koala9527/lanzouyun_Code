import TURING
import easygui
def identifys(names):
    #打开图片，同样的处理图片
    TURING.Pixel_FromPicture("./verify/" + str(names) + ".png")
    TURING.Filter_Tailor(0, 0, 99, 30)
    TURING.Filter_Posterization(4)
    TURING.Filter_Binaryzation("95")
    TURING.Filter_Despeckle(8, 0, 0)
    # 颜色反转 （）转后黑底白字，转前白底黑字
    TURING.Filter_InverseColor()
    TURING.Incise_ScopeAisle(8, 8)
    TURING.Lib_Load("识别库1.lib")  #加载识别字库
    识别结果 =TURING.OCR(0, 1)  #获取识别结果，可以设置结果格式，可以显示相似度，和x，y坐标等等。是一个字符串，以|分割，
    result =识别结果.split("|")[0]
    #来个弹框来肉眼证明结果的准确性
    choices_data = easygui.ccbox(msg='识别结果是'+result, title=' ', choices=('True', 'false'), image="./verify/" + str(names) + ".png")
    return choices_data
suc = 0
for i in range(100):
    res = identifys(i)
    if res:
        #统计正确的数量
        suc =suc+1
print(suc)