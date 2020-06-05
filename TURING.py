#================================================================
#         《我的眼睛 -- 图灵识别》v2.7.3.20190925
#----------------------------------------------------------------
#        【作者】：鱼头之王（FishBOSS）
#        【ＱＱ】：1204400520
#        【Ｑ群】：460472698(免费)/314452472(免费)/866837563(付费)
#        【创建】：2019.03.25
#        【更新】：2019.09.26
#        【注意】：插件需要手动注册一次
#================================================================
import win32com.client

#创建全局COM对象
global TURING
TURING = win32com.client.Dispatch('TURING.FISR')

#关于
def About():
    return TURING.About()



#句柄_关联窗口（目前仅支持系统的普通窗口"normal","gdi","aero" "window" | "km"）
def Link(hwnd, Mode = "normal"):
    b = TURING.Link(hwnd, Mode)     #后台截图设置项
    return b[0]

#句柄_解除窗口关联
def UnLink(Mode = ""):
    TURING.UnLink(Mode)
    return 

#句柄_查找窗口句柄[句柄]
def Window_FindHwnd(sClass, sTile = ""):
    h = TURING.Window_FindHwnd(sClass,sTile)
    return h[0]

#句柄_得到窗口大小[左,上,右,下]
def Window_GetSize(iHwnd = 0):
    r = TURING.Window_GetSize(iHwnd)
    return r[0]

#句柄_获取祖窗口句柄[顶级句柄]
def Window_GetAncestor(iHwnd = 0):
    h = TURING.Window_GetAncestor(iHwnd)
    return h[0]

#句柄_取指定坐标下句柄[坐标下句柄]
def Window_GetPointHwnd(x, y):
    h = TURING.Window_GetPointHwnd(x, y)
    return h[0]

#句柄_移动窗口位置
def Window_MoveTo(iHwnd = 0, iLeft = 0, iTop = 0, iWidth = 0, iHeight = 0):
    TURING.Window_MoveTo(iHwnd, iLeft, iTop, iWidth, iHeight)
    return

#枚举所有顶层窗口句柄
def Window_Enum(iClass = "", iTitle = ""):
    s = TURING.Window_Enum(iClass, iTitle)
    return s[0]

#枚举指定窗口的所有子句柄
def Window_EnumChild(iHwnd = 0, iClass = "", iTitle = ""):
    s = TURING.Window_EnumChild(iHwnd, iClass, iTitle)
    return s[0]

#对窗口进行假激活后并获得焦点（窗口不会置前）
def Window_FakeActive(iHwnd = 0):
    TURING.Window_FakeActive(iHwnd)
    return



#来源_获取屏幕像素数据
def Pixel_FromScreen(iLeft, iTop, iRight, iBottom, Mode = 0):
    TURING.Pixel_FromScreen(iLeft, iTop, iRight, iBottom, Mode)
    return

#来源_获取图片像素数据
def Pixel_FromPicture(ImagePath, Mode = 0):
    TURING.Pixel_FromPicture(ImagePath, Mode)
    return

#来源_获取获取鼠标图案数据[热点坐标]
def Pixel_FromMouse(iWidth = 32, iHeight = 32):
    TURING.Pixel_FromMouse(iWidth, iHeight)
    return

#来源_像素预览[点击图像位置的坐标]
def Pixel_Preview(Mode = 0, Value = False):
    s = TURING.Pixel_Preview(Mode, Value)
    return s[0].split(",")



#来源_图像的像素数据保存为图片
def SaveImageData(SaveImagePath):
    TURING.SaveImageData(SaveImagePath)
    return

#来源_获取颜色图层像素，处理结果图像为黑白图（黑底白字），返回图层数量
def Pixel_ColorImageData(Interval = 2, Num = "15"):
    n = TURING.Pixel_ColorImageData(Interval, Num)
    return n[0]

#来源_获取通道图像（仅支持RGB通道）
def Pixel_ChannelImageData(Model = False):
    TURING.Pixel_ChannelImageData(Model)
    return

#来源_拆分图像数据,上限10个
def Pixel_CutImageData(iLeft, iTop, iRight, iBottom, Serial = 1):
    TURING.Pixel_CutImageData(iLeft, iTop, iRight, iBottom, Serial)
    return

#来源_配置图像数据 拆分,上限10个
def Pixel_SetImageData(Serial = 1):
    TURING.Pixel_SetImageData(Serial)
    return

#来源_配置图像数据 切割
def Pixel_SetImageDataCut(Serial = 0):
    TURING.Pixel_SetImageDataCut(Serial)
    return

#来源_配置字库数据 [返回字库对应的文字]
def Pixel_SetImageDataLib(Index = 0):
    s = TURING.Pixel_SetImageDataLib(Index)
    return s[0]

#来源_配置图像像素数据为图中图（默认1找图场景，2绘图图像）
def Pixel_SetSceneImageData(Mode = 1):
    TURING.Pixel_SetSceneImageData(Mode)
    return

#来源_配置图层图像数据，处理结果图像为黑白图（黑底白字）
def Pixel_SetLayerImageData(Num = 0):
    TURING.Pixel_SetLayerImageData(Num)
    return

#来源_获取图像的像素数据，模式（默认0:宽|高|图像数据，1:宽|高，2:全部设置到剪切板）
def GetImageData(value):
    Pixels = TURING.GetImageData(value)
    return Pixels[0]

#来源_载入图像的像素数据
def LoadImageData(ImageData):
    TURING.LoadImageData(ImageData)
    return

#来源_获取图片大小[宽,高]
def GetImageSize(ImagePath):
    s = TURING.GetImageSize(ImagePath)
    return s[0].split(",")

#来源_图片格式转换 jpg 默认 80% 压缩率
def ImageFormatConverter(ImagePath, ImageSavePath, value = 80):
    TURING.ImageFormatConverter(ImagePath, ImageSavePath, value)
    return



#来源_获取剪切板图像数据
def Pixel_GetClpImageData():
    TURING.Pixel_GetClpImageData()
    return

#来源_设置剪切板图像数据
def Pixel_SetClpImageData():
    TURING.Pixel_SetClpImageData()
    return

#来源_设置剪切板屏幕像素
def Pixel_SetClpScreenData(left, top, right, bottom):
    TURING.Pixel_SetClpScreenData(left, top, right, bottom)
    return

#来源_设置剪切板图片像素
def Pixel_SetClpPictureData(ImagePath):
    TURING.Pixel_SetClpPictureData(ImagePath)
    return

#来源_剪切板图像数据保存为图片
def Pixel_SaveClpImageData(ImagePath):
    TURING.Pixel_SaveClpImageData(ImagePath)
    return



#滤镜_二值化 
#色阶阈值（范围：0-255）
#或者：指定颜色串BBGGRR-BDGDRD（"0000FF-000080|00FFFF"）(反色效果："@BBGGRR-DBDGDR")
#或者：通过最大类间方差法[Otsu]取得（"auto"）
def Filter_Binaryzation(Value = "128"):
    TURING.Filter_Binaryzation(Value)
    return

#滤镜_灰度  模式（默认0:标准，1:Photoshop算法）
def Filter_Gray(Mode = 0):
    TURING.Filter_Gray(Mode)
    return

#滤镜_色调分离  色阶阈值（范围：2~255）
def Filter_Posterization(Value = 3):
    TURING.Filter_Posterization(Value)
    return

#滤镜_清除杂点
def Filter_Despeckle(Value = 6, Interval = 0, Mode = 1):
    TURING.Filter_Despeckle(Value, Interval, Mode)
    return

#滤镜_去掉直线  点数百分比（范围：1~100）
def Filter_EraseLine(Value = 50):
    TURING.Filter_EraseLine(Value)
    return

#滤镜_获取轮廓
def Filter_Outline():
    TURING.Filter_Outline()
    return

#滤镜_提取色块
def Filter_ExtractBlock(iWidth = 3, iHeight = 3, Num = 8):
    TURING.Filter_ExtractBlock(iWidth, iHeight, Num)
    return

#滤镜_倾斜矫正
def Filter_SlantCorrect():
    TURING.Filter_SlantCorrect()
    return

#滤镜_旋转纠正[角度]
def Filter_RotateCorrect(Angle = 45, Value = 1):
    n = TURING.Filter_RotateCorrect(Angle, Value)
    return n[0]

#滤镜_颠倒颜色   效果：白多变黑
def Filter_InverseColor(Mode = 1):
    TURING.Filter_InverseColor(Mode)
    return

#滤镜_膨胀腐蚀
def Filter_DilationErosion(Mode = 1):
    TURING.Filter_DilationErosion(Mode)
    return

#滤镜_细化抽骨
def Filter_ThinBone():
    TURING.Filter_ThinBone()
    return

#滤镜_有效图像(模式<默认空:裁剪黑边，auto:四角相同色裁剪>)
def Filter_ValidCut(Mode = ""):
    TURING.Filter_ValidCut(Mode)
    return

#滤镜_等比缩放
def Filter_Zoom(xTimes = 2, yTimes = 2):
    TURING.Filter_Zoom(xTimes, yTimes)
    return

#滤镜_缩放归一化
def Filter_ZoomOne(iScaleWidth, iScaleHeight):
    TURING.Filter_ZoomOne(iScaleWidth, iScaleHeight)
    return

#滤镜_延伸裁剪
def Filter_Tailor(iLeft, iTop, iRight, iBottom):
    TURING.Filter_Tailor(iLeft, iTop, iRight, iBottom)
    return

#滤镜_固定镜像
def Filter_Mirror(Direction = 0):
    TURING.Filter_Mirror(Direction)
    return

#滤镜_固定移位
def Filter_Shift(Value, Direction = 0):
    TURING.Filter_Shift(Value, Direction)
    return

#滤镜_筛选色点
def Filter_CheckPoints(Kind = 1, Num = 0, isMax = True):
    TURING.Filter_CheckPoints(Kind, Num, isMax)
    return

#滤镜_像素描边
def Filter_PixelStroke(Value = "FFFFFF", fColor = "FFFFFF", bColor = "000000"):
    TURING.Filter_PixelStroke(Value, fColor, bColor)
    return

#滤镜_颜色选留（@不保留选中颜色）
#指定颜色串BBGGRR-BDGDRD（"0000FF-000080|00FFFF"）(反选效果："@BBGGRR-DBDGDR")
def Filter_ColorChoose(value = "000000"):
    TURING.Filter_ColorChoose(value)
    return

#滤镜_色块选留
def Filter_BlockChoose(iWidth, iHeight, fColor = "FFFFFF", bColor = "000000"):
    TURING.Filter_BlockChoose(iWidth, iHeight, fColor, bColor)
    return

#滤镜_固定旋转  旋转的正负度数值，正数顺时针（默认45，范围：正负0~360）
def Filter_Rotate(angle = 45):
    TURING.Filter_Rotate(angle)
    return

#滤镜_固定移位  像素移位特征串|开始行列数（移动数值：正数向左移动，负数向右移动）
def Filter_Shift(Value, Direction = 0):
    TURING.Filter_Shift(Value, Direction)
    return

#滤镜_祛除斑点
def Filter_DispelSpot(Sensitivity = 25, Num = 2):
    TURING.Filter_ColorChoose(Sensitivity, Num)
    return

#滤镜_查找互补色
def Filter_Complementary():
    s = TURING.Filter_Complementary()
    return s

#滤镜_差异提取
def Filter_DiffeExtract(ImageData1, ImageData2, Similarity = 1.0):
    n = TURING.Filter_DiffeExtract(ImageData1, ImageData2, Similarity)
    return n[0]

#(通用图像处理)柔化指定图像（类似模糊） 
def Filter_Softness():
    TURING.Filter_Softness()
    return

#(通用图像处理)图像中的颜色进行扩散（类似磨砂玻璃） 
def Filter_Diffuse():
    TURING.Filter_Diffuse()
    return

#(通用图像处理)电影底片效果（反向颜色：RGB三种颜色分别取255的差值） 
def Filter_Negative():
    TURING.Filter_Negative()
    return

#(通用图像处理)呈现一种暗调，对比度对比度明显的效果 
def Filter_Negative():
    TURING.Filter_Negative()
    return




#切割_固定位置
def Incise_FixedLocation(qx, qy, iWidth, iHeight, Interval, num):
    n = TURING.Incise_FixedLocation(qx, qy, iWidth, iHeight, Interval, num)
    return n[0]

#切割_随机方位
def Incise_RandomOrientation(width = 0, height = 0):
    n = TURING.Incise_RandomOrientation(width, height)
    return n[0]

#切割_连通区域
def Incise_ConnectedArea(Through, width = 0, height = 0):
    n = TURING.Incise_ConnectedArea(Through, width, height)
    return n[0]

#切割_范围投影
def Incise_ScopeAisle(Row = 2, Column = 1, width = 0, height = 0):
    n = TURING.Incise_ScopeAisle(Row, Column, width, height)
    return n[0]

#切割_颜色分层
def Incise_ColorLayered(Interval, num, width = 0, height = 0, Value = 6, Row = 3, Column = 2):
    n = TURING.Incise_ColorLayered(Interval, num, width, height, Value, Row, Column)
    return n[0]

#切割_自适应矩形（体验版）
def Incise_Adaptive(width = 0, height = 0):
    n = TURING.Incise_Adaptive(width, height)
    return n[0]

#切割_修改字符切割图像数据
def Incise_ModifyCharData(num, iLeft = 0, iTop = 0):
    TURING.Incise_ModifyCharData(num, iLeft, iTop)
    return

#切割_清除切割图像数据
def Incise_EraseData():
    TURING.Incise_EraseData()
    return

#切割_追加图像数据为切割数据（传入多个图像）
def Incise_AddCharData(iLeft = 0, iTop = 0):
    n = TURING.Incise_AddCharData(iLeft, iTop)
    return n[0]

#切割_获取切割字符的信息（字符串：左,上,宽,高,点阵|左,上,宽,高,点阵|……）
#默认0:全部数据，1:左,上，2:左,上,宽,高，3:宽,高,点阵
def Incise_GetCharData(Mode = 0):
    s = TURING.Incise_GetCharData(Mode)
    return s[0]

#切割_合并切割字符数据(后面参数的字符合并到前面字符，并删除后面的字符)
def Incise_JoinCharData(Num1, Num2):
    n = TURING.Incise_JoinCharData(Num1, Num2)
    return n[0]

#切割_切割字符大小归一化
def Incise_CharSizeOne(iWidth, iHeight):
    TURING.Incise_CharSizeOne(iWidth, iHeight)
    return

#切割_字符预览[点击图像位置的坐标]
def Incise_Preview(num):
    s = TURING.Incise_Preview(num)
    return s[0].split(",")



#字库_加载识别字库
def Lib_Load(LibPath):
    n = TURING.Lib_Load(LibPath)
    return n[0]

#字库_加载识别字库_扩展
def Lib_LoadEx(LibStr):
    n = TURING.Lib_LoadEx(LibStr)
    return n[0]

#字库_创建系统字体识别字库
def Lib_Create(iFont, iSize, iText = ""):
    n = TURING.Lib_Create(iFont, iSize, iText)
    return n[0]

#字库_添加新的识别字库,上限10个
def Lib_Add(Serial = 1):
    TURING.Lib_Add(Serial)
    return

#字库_设置使用哪个识别字库,上限10个
def Lib_Use(Serial = 1):
    TURING.Lib_Use(Serial)
    return

#字库_追加识别字库,上限10个
def Lib_AddData(Serial = 1):
    n = TURING.Lib_AddData(Serial)
    return n[0]

#字库_内部的图像数据追加为识别字库
def Lib_AddImageData(iText):
    TURING.Lib_AddImageData(iText)
    return

#字库_获取字库数量下标值[下标数量]
def Lib_UBound(Serial = 0):
    n = TURING.Lib_UBound(Serial)
    return n[0]

#字库_清空字库数据 ，字库编号（默认0:当前字库，1~10:指定编号字库）
def Lib_EraseData(Serial):
    TURING.Lib_EraseData(Serial)
    return

#字库_分析切割字符的字体与字号   Mode样式，默认"0|0"（格式：0正常,1粗体,2斜体,3粗斜体|0中文字体，1英文字体）
def Lib_AnalyzeFontSize(Text, Mode):
    s = TURING.Lib_AnalyzeFontSize(Text, Mode)
    return s[0]

#字库_点阵预览[点击图像位置的坐标]
def Lib_Preview(num):
    s = TURING.Lib_Preview(num)
    return s[0].split(",")

#字库_分享字库文件
def Lib_Share(LibPath):
    TURING.Lib_Share(LibPath)
    return

#字库_生成二进制字符串点阵
def Lib_Generate():
    s = TURING.Lib_Generate()
    return s

#字库_获取字库的单个数据信息（模式（默认0：全部，1：文字,宽,高，2：文字，3：宽,高，4：点阵））
def Lib_GetCharData(Serial, Mode):
    s = TURING.Lib_GetCharData(Serial, Mode)
    return s[0]

#字库_字符切割数据   切割后的每个字符图像  "5,8|01010101001" = 切割后的每个字符图像
def Lib_OneCharData(num):
    s = TURING.Lib_OneCharData(num)
    return s[0]

#字库_存储识别字库
def Lib_Save(Text, Lattice, LibPath):
    TURING.Lib_Save(Text, Lattice, LibPath)
    return

#字库_存储识别字库_扩展
def Lib_SaveEx(Text, Index, LibPath):
    TURING.Lib_SaveEx(Text, Index, LibPath)
    return

#识别_点阵比对（参数1：百分比相似度，参数2：0:返回文字，1:返回文字和每个字坐标）
def OCR(Similar = 0, Mode = 0, Interval = 0):
    s = TURING.OCR(Similar, Mode, Interval)
    return s[0]

#识别_点阵比对_增强版 （参数1：百分比相似度，参数2：0:返回文字，1:返回文字和每个字坐标）
def OCRex(Similar = 0, Mode = 0, Interval = 0):
    s = TURING.OCRex(Similar, Mode, Interval)
    return s[0]



#图色_获取指定位置颜色（0：普通取色，1：增强取色（半透明窗体），2：取内部数据颜色）
def GetPixelColor(x, y, Mode = 0):
    s = TURING.GetPixelColor(x, y, Mode)
    return s[0]

#图色_屏幕区域找色(x,y)
def FindColor(iLeft, iTop, iRight, iBottom, iColor, Direction, Similarity):
    z = TURING.FindColor(iLeft, iTop, iRight, iBottom, iColor, Direction, Similarity)
    return z[0].split(",")

#图色_屏幕区域找多色多坐标(x,y|x,y|……)
def FindColorExS(iLeft, iTop, iRight, iBottom, iColorS, Direction, Similarity):
    z = TURING.FindColorExS(iLeft, iTop, iRight, iBottom, iColorS, Direction, Similarity)
    return z[0].split("|")

#图色_屏幕区域找图 (x,y)
def FindImage(iLeft, iTop, iRight, iBottom, ImagePath, Similarity):
    z = TURING.FindImage(iLeft, iTop, iRight, iBottom, ImagePath, Similarity)
    return z[0].split(",")

#图色_屏幕指定区域内查找多点颜色[返回首个颜色的屏幕坐标]
def FindMultiColor(left, top, right, bottom, color, offsetColorS, similarity):
    z = TURING.FindMultiColor(left, top, right, bottom, color, offsetColorS, similarity)
    return z[0].split(",")

#图色_屏幕区域找所有图(x,y|x,y|……)
def FindImageS(iLeft, iTop, iRight, iBottom, ImagePath, Similarity):
    z = TURING.FindImageS(iLeft, iTop, iRight, iBottom, ImagePath, Similarity)
    return z[0].split("|")

#图色_屏幕区域找其中图(id,x,y)
def FindImageEx(iLeft, iTop, iRight, iBottom, ImagePathS, Similarity):
    z = TURING.FindImageEx(iLeft, iTop, iRight, iBottom, ImagePathS, Similarity)
    return z[0].split(",")

#图色_屏幕区域找所有图所有坐标 (id,x,y|id,x,y|……)
def FindImageExS(iLeft, iTop, iRight, iBottom, ImagePathS, Similarity):
    z = TURING.FindImageExS(iLeft, iTop, iRight, iBottom, ImagePathS, Similarity)
    return z[0].split("|")

#图色_鼠标形状识别
def FindMouseShape(Model = 0):
    n = TURING.FindMouseShape(Model = 0)
    return n[0]

#图色_多边形识别（体验版）
def FindShape(Distance, Length):
    s = TURING.FindShape(Distance, Length)
    return s[0]

#16进制颜色值分解为RGB分量[R, G, B]，16进制颜色值（格式：BBGGRR）
def ToRGB(color):
    s = TURING.ToRGB(color)
    return s[0]

#RGB颜色分量合并为16进制颜色值（格式：BBGGRR） 
def ToColor(R, G, B):
    s = TURING.ToColor(R, G, B)
    return s[0]

#得到指定的16进制颜色值的中文名称（黑、灰、白、红、橙、黄、绿、青、蓝、紫）
def ToColorName(sColor):
    s = TURING.ToColorName(sColor)
    return s[0]




#键盘按键
def KM_KeyPress(Asck):
    TURING.KM_KeyPress(Asck)
    return

#键盘按下
def KM_KeyDown(Asck):
    TURING.KM_KeyDown(Asck)
    return

#键盘弹起
def KM_KeyUp(Asck):
    TURING.KM_KeyUp(Asck)
    return

#输入内容
def KM_SendString(theStr):
    TURING.KM_SendString(theStr)
    return

#单击鼠标左键
def KM_LeftClick(mouX = 0, mouY = 0):
    TURING.KM_LeftClick(mouX, mouY)
    return

#双击鼠标左键
def KM_LeftDbClick(mouX = 0, mouY = 0):
    TURING.KM_LeftDbClick(mouX, mouY)
    return

#鼠标左键按下
def KM_LeftDown(mouX = 0, mouY = 0):
    TURING.KM_LeftDown(mouX, mouY)
    return

#鼠标左键弹起
def KM_LeftUp(mouX = 0, mouY = 0):
    TURING.KM_LeftUp(mouX, mouY)
    return

#单击鼠标中键
def KM_MiddleClick(mouX = 0, mouY = 0):
    TURING.KM_MiddleClick(mouX, mouY)
    return

#鼠标中键按下
def KM_MiddleDown(mouX = 0, mouY = 0):
    TURING.KM_MiddleDown(mouX, mouY)
    return

#鼠标中键弹起
def KM_MiddleUp(mouX = 0, mouY = 0):
    TURING.KM_MiddleUp(mouX, mouY)
    return

#单击鼠标右键
def KM_RightClick(mouX = 0, mouY = 0):
    TURING.KM_RightClick(mouX, mouY)
    return

#鼠标右键按下
def KM_RightDown(mouX = 0, mouY = 0):
    TURING.KM_RightDown(mouX, mouY)
    return

#鼠标右键弹起
def KM_RightUp(mouX = 0, mouY = 0):
    TURING.KM_RightUp(mouX, mouY)
    return

#鼠标移动函数
def KM_MoveTo(mouX, mouY):
    TURING.KM_MoveTo(mouX, mouY)
    return

#获取鼠标当前位置
def KM_GetCursorPos():
    z = TURING.KM_GetCursorPos()
    return z.split(",")

#延迟函数
def KM_Delay(mSec):
    TURING.KM_Delay(mSec)
    return



#绘图_创建画布
def Draw_CreateCanvas(iWidth = 256, iHeight = 256, cR = 0, cG = 0, cB = 0):
    TURING.Draw_CreateCanvas(iWidth, iHeight, cR, cG, cB)
    return

#绘图_画点
def Draw_Point(x, y, cR = 255, cG = 0, cB = 0):
    TURING.Draw_Point(x, y, cR, cG, cB)
    return

#绘图_画线
def Draw_Line(x1, y1, x2, y2, cR = 255, cG = 0, cB = 0):
    TURING.Draw_Line(x1, y1, x2, y2, cR, cG, cB)
    return

#绘图_矩形
def Draw_Rectangle(iLeft, iTop, iRight, iBottom, cR = 255, cG = 0, cB = 0):
    TURING.Draw_Rectangle(iLeft, iTop, iRight, iBottom, cR, cG, cB)
    return

#绘图_方块
def Draw_Block(iLeft, iTop, iRight, iBottom, cR = 255, cG = 0, cB = 0, Alpha = 100):
    TURING.Draw_Block(iLeft, iTop, iRight, iBottom, cR, cG, cB, Alpha)
    return

#绘图_圆形
def Draw_Circle(x, y, Radius, R = 255, G = 0, B = 0, Fill = False, Alpha = 100):
    TURING.Draw_Circle(x, y, Radius, R, G, B, Fill, Alpha)
    return

#绘图_文字
def Draw_Text(x, y, text, FontSizeMode = "宋体|9|0|0", cR = 255, cG = 0, cB = 0):
    TURING.Draw_Text(x, y, text, FontSizeMode, cR, cG, cB)
    return

#绘图_图像
def Draw_Image(x, y, FilePath = "", Alpha = 100):
    TURING.Draw_Image(x, y, FilePath, Alpha)
    return

#绘图_填充[左上右下]
def Draw_Fill(x, y, Through = False, cR = 255, cG = 0, cB = 0):
    s = TURING.Draw_Fill(x, y, Through, cR, cG, cB)
    return s[0]

#绘图_图像数据备份，上限4096个
def Draw_Backups(Serial = 1, Model = 0):
    TURING.Draw_Backups(Serial, Model)
    return

#绘图_图像数据还原，上限4096个
def Draw_Recover(Serial = 1, Model = 0):
    TURING.Draw_Recover(Serial, Model)
    return

#绘图_生成验证码   返回验证码中计算的结果
def Draw_CAPTCHA():
    n = TURING.Draw_CAPTCHA()
    return n

#绘图_生成gif文件
def FileSaveGIF(LoadName, SaveName, Delay = 100):
    TURING.FileSaveGIF(LoadName, SaveName, Delay)
    return

#遍历指定目录下所有文件夹和文件名（单层目录遍历） [文件夹名\|文件名|…]
def Files_Search(sPath, sType = "", value = False):
    s = TURING.Files_Search(sPath, sType, value)
    return s[0]

#下载网络文件命令
def FileDownload(sUrl, SaveName):
    TURING.FileDownload(sUrl, SaveName)

#多个文件进行合并为一个文件 
def Files_Merge(FilesPath, SaveFile):
    b = TURING.Files_Merge(FilesPath, SaveFile)
    return b[0]

#对已合并的文件拆分为多个文件
def Files_Split(FilePath, SaveFolder):
    b = TURING.Files_Split(FilePath, SaveFolder)
    return b[0]

#压缩一个文件（自创算法,效率还是不错的）
def Files_Dried(OriginalFile, ZipPath):
    b = TURING.Files_Dried(OriginalFile, ZipPath)
    return b[0]

#解压一个文件（自创算法,效率还是不错的） 
def Files_UnDried(ZipFile, OutputFile):
    b = TURING.Files_UnDried(ZipFile, OutputFile)
    return b[0]




#抓取屏幕坐标与颜色值（及窗口客户区坐标和RGB分量）
def UI_Zoom():
    s = TURING.UI_Zoom()
    return s

#在屏幕上按住鼠标左键框选区域（及宽高）
def UI_Area():
    s = TURING.UI_Area()
    return s

#在屏幕中间弹出提示对话框
def UI_MsgBox(Content, Title = "我的眼睛--图灵识别", iStyle = 1, Timeout = 0):
    s = TURING.UI_MsgBox(Content, Title, iStyle, Timeout)
    return s[0]

#在屏幕中间弹出可输入内容对话框
def UI_InputBox(Content, Title = "我的眼睛--图灵识别", Default = "", Timeout = 0):
    s = TURING.UI_InputBox(Content, Title, Default, Timeout)
    return s[0]




#屏幕_打印图像
def Screen_PrintImage(x = 0, y = 0):
    TURING.Screen_PrintImage(x, y)
    return

#屏幕_打印文字（字体样式和精度，默认："0|0"(格式：模式<0正常，1粗体，2斜体，4下划线，8删除线。其他依次叠加数字>|精度<0抗锯齿，1清晰>)）
def Screen_PrintText(text, x = 0, y = 0, FBcolor = "0000FF|000000", FontNameSize = "宋体|9", Model = "0|0"):
    TURING.Screen_PrintText(text, x, y, FBcolor, FontNameSize, Model)
    return

#屏幕_强制刷新
def Screen_Refresh():
    TURING.Screen_Refresh()
    return



#算法_与众不同
def Different():
    s = TURING.Different()
    return s

#算法_统计差平方
def EvalVariance():
    n = TURING.EvalVariance()
    return n

#算法_取直线上所有坐标
def GetLineAllPos(x1, y1, x2, y2):
    s = TURING.GetLineAllPos(x1, y1, x2, y2)
    return s[0]

#算法_获取所有端点坐标 (X,Y|X,Y|…)
def GetAllPoints(value):
    s = TURING.GetAllPoints(value)
    return s[0].split("|")

#算法_抽取端点之间的线段 (X,Y-X,Y-X,Y…)【自动寻路】
def GetOneLine(x1, y1, x2, y2):
    s = TURING.GetOneLine(x1, y1, x2, y2)
    return s[0].split("-")

#算法_抽取所有端点之间的线段 (X,Y-X,Y-X,Y…|X,Y-X,Y-X,Y…|…)  0任意线，1直线
def GetAllLines(value = 0, Num = 0):
    s = TURING.GetAllLines(value, Num)
    return s[0].split("|")

#算法_两线交叉坐标（体验版）
def TwoLinesCrossPos(sx1, sy1, sx2, sy2, ex1, ey1, ex2, ey2):
    s = TURING.TwoLinesCrossPos(sx1, sy1, sx2, sy2, ex1, ey1, ex2, ey2)
    return s[0]

#算法_统计每种颜色数量[返回每个颜色数量，从大到小排序的三种格式：BBGGRR,100|H.S.V,59|RRGGBB,76]
def GetColorPoints(value = "BGR"):
    n = TURING.GetColorPoints(value)
    return n[0]

#算法_统计颜色点数量
def CountColorNum(value):
    n = TURING.CountColorNum(value)
    return n[0]

#算法_获取指定范围内所有颜色的均值（支持图中图） 
def GetAveRGB(left, top, right, bottom):
    s = TURING.GetAveRGB(left, top, right, bottom)
    return s[0]

#获取内部图像的有效区域范围 （格式：左,上,右,下）
def GetValidArea():
    s = TURING.GetValidArea()
    return s[0]



#编码_RGB转HSV[H,S,V]
def RGBtoHSV(iColor):
    s = TURING.RGBtoHSV(iColor)
    return s[0].split(",")

#编码_HSV转RGB
def HSVtoRGB(Hue, Saturation, Value):
    s = TURING.HSVtoRGB(Hue, Saturation, Value)
    return s[0]

#编码_HBGR互转RGB
def BGRvsRGB(sColor):
    s = TURING.BGRvsRGB(sColor)
    return s[0]

#编码_二进制转十六进制字符串
def BINtoHEX(BINString):
    s = TURING.BINtoHEX(BINString)
    return s[0]

#编码_十六进制转二进制字符串
def HEXtoBIN(HEXString):
    s = TURING.HEXtoBIN(HEXString)
    return s[0]

#编码_十进制转二进制字符串
def DECtoBIN(DECNum):
    s = TURING.DECtoBIN(DECNum)
    return s[0]

#编码_图片Base64编码  对图片进行Base64编码（支持bmp/png/jpg/gif等），IsHead默认False，True为含包头（格式：“data:image/<后缀名>;base64,”）
def Image_Base64Encode(FilePath, IsHead = False):
    s = TURING.Image_Base64Encode(FilePath, IsHead)
    return s[0]

#编码_字符串MD5加密   Code编码，默认3（格式：0:ANSI，1:ANSI-UTF8，2:GB2312，3:GB2312-UTF8）
def Pass_MD5String(Text, Code = 3):
    s = TURING.Pass_MD5String(Text, Code)
    return s[0]

#编码_简单加密（10位秘钥）    明文内容 ,"123,4,56,78,90,1,234,56,78,90" 不超过255
def Pass_Encode(TextString, Password = "123,4,56,78,90,1,234,56,78,90"):
    s = TURING.Pass_Encode(TextString, Password)
    return s[0]

#编码_简单解密（10位秘钥）    密文内容 ,"123,4,56,78,90,1,234,56,78,90" 不超过255
def Pass_Uncode(TextString, Password = "123,4,56,78,90,1,234,56,78,90"):
    s = TURING.Pass_Uncode(TextString, Password)
    return s[0]



#系统_精准的计算时间差
def GetTime():
    n = TURING.GetTime()
    return n

#系统_清理内存
def Memory_Clear():
    TURING.Memory_Clear()
    return

#系统_总共的物理内存|可用的物理内存|已用的内存比率
def Memory_GetInfo():
    s = TURING.Memory_GetInfo()
    return s

#系统_获取硬盘型号
def GetHDSN():
    s = TURING.GetHDSN()
    return s

#系统_命令提示符(运行命令行)
def Run(Command):
    s = TURING.Run(Command)
    return s[0]

#系统_运行VBS脚本命令内容(脚本命令内容/或者vbs脚本文件.tls)
def RunVBScript(sText,AA=None,BB=None,CC=None,DD=None,EE=None,FF=None,GG=None,HH=None,II=None,JJ=None,KK=None,LL=None,MM=None,NN=None,OO=None,PP=None):
    if AA == None:
        s = TURING.RunVBScript(sText)
    elif BB == None:
        s = TURING.RunVBScript(sText,AA)
    elif CC == None:
        s = TURING.RunVBScript(sText,AA,BB)
    elif DD == None:
        s = TURING.RunVBScript(sText,AA,BB,CC)
    elif EE == None:
        s = TURING.RunVBScript(sText,AA,BB,CC,DD)
    elif FF == None:
        s = TURING.RunVBScript(sText,AA,BB,CC,DD,EE)
    elif GG == None:
        s = TURING.RunVBScript(sText,AA,BB,CC,DD,EE,FF)
    elif HH == None:
        s = TURING.RunVBScript(sText,AA,BB,CC,DD,EE,FF,GG)
    elif II == None:
        s = TURING.RunVBScript(sText,AA,BB,CC,DD,EE,FF,GG,HH)
    elif JJ == None:
        s = TURING.RunVBScript(sText,AA,BB,CC,DD,EE,FF,GG,HH,II)
    elif KK == None:
        s = TURING.RunVBScript(sText,AA,BB,CC,DD,EE,FF,GG,HH,II,JJ)
    elif LL == None:
        s = TURING.RunVBScript(sText,AA,BB,CC,DD,EE,FF,GG,HH,II,JJ,KK)
    elif MM == None:
        s = TURING.RunVBScript(sText,AA,BB,CC,DD,EE,FF,GG,HH,II,JJ,KK,LL)
    elif NN == None:
        s = TURING.RunVBScript(sText,AA,BB,CC,DD,EE,FF,GG,HH,II,JJ,KK,LL,MM)
    elif OO == None:
        s = TURING.RunVBScript(sText,AA,BB,CC,DD,EE,FF,GG,HH,II,JJ,KK,LL,MM,NN)
    elif PP == None:
        s = TURING.RunVBScript(sText,AA,BB,CC,DD,EE,FF,GG,HH,II,JJ,KK,LL,MM,NN,OO)
    else:
        s = TURING.RunVBScript(sText,AA,BB,CC,DD,EE,FF,GG,HH,II,JJ,KK,LL,MM,NN,OO,PP)
    return s



#关联ADB调试桥
def Adb_Link(AdbPath, DevicesId = ""):
    TURING.Adb_Link(AdbPath, DevicesId)
    return 

#查看设备名称
def Adb_Devices(Serial = 0):
    s = TURING.Adb_Devices(Serial)
    return s[0]

#获取设备屏幕像素
def Adb_Screencap(left = 0, top = 0, right = 0, bottom = 0, Model = 0):
    TURING.Adb_Screencap(left, top, right, bottom, Model)
    return 

#短暂点击
def Adb_Tap(x, y):
    TURING.Adb_Tap(x, y)
    return 

#滑动屏幕
def Adb_Swipe(x1, y1, x2, y2):
    TURING.Adb_Swipe(x1, y1, x2, y2)
    return 

#响应按键
def Adb_KeyEvent(Key):
    TURING.Adb_KeyEvent(Key)
    return 

#输入内容（仅支持英文、标点符号和数字）
def Adb_InputText(Text):
    TURING.Adb_InputText(Text)
    return 



#插件路径
def Path():
    s = TURING.Path()
    return s

#版本号
def Version():
    v = TURING.Version()
    return v

