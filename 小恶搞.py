import easygui as s
import sys
s.msgbox("大家欢迎来到实力至上主义的教室")
while True :

    msg=("请选择你想要吃的零食")
    title=("零食仓库")
    choices=["舔屁眼","含鸡巴","吸咪咪","含龙眼","请输入你喜欢的零食","退出"]
    choice=s.choicebox(msg,title,choices)
    if choice=="请输入你喜欢的零食":
        msg=("请输入你喜欢的零食")
        title=("心里话")
        s.enterbox(msg,title)
    if choice=="退出":
        exit(0)
    s.msgbox("你的选择是:"+str(choice),"结果")

    msg=("亲爱的，-你还要零食吗")
    title=("零食仓库")
    choices=["我还要吃","我吃饱了，不想吃了"]
    if s.ccbox(msg,title,choices):
        pass
    else:
        sys.exit(0)

