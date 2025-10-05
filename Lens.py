"""this script wrote by Tara Zakizadeh for one of the optic lab experiments
in the first part:
    v is distance between image and lens(cm)
    u is distance between object and lens(cm)
in the second part:
    d is the distance between object and screen(cm)
    x is the diffrence of two positions for lens(100+) pls(cm)
"""
import math

def lens_formular():
    f_list=[]
    for i in range(2):
        v =float(input("enter the distace between image(v) and lens pls(cm):"))
        u =float(input("enter the distance between object(u) and lens pls(cm):"))
        invers_f=(1/v)+(1/u)
        f=round(1/invers_f,3)
        f_list.append(f)
    return(f_list)


def Besel_formula():
    d =float(input("enter the distance between object and screen(cm): "))
    x=float(input("enter the diffrence of two positions for lens(100+) pls(cm): "))
    f =round(((math.pow(d,2))-(math.pow(x,2)))/(4*d),3) 
    return(f)


def error_in_F():
    v =float(input("enter the distace between image(v) and lens pls(cm):"))
    u =float(input("enter the distance between object(u) and lens pls(cm):"))
    a=(math.pow(u,2))/(math.pow((u+v),2))
    c=0.1#cm
    b=(math.pow(v,2))/(math.pow((u+v),2))
    e=0.1#cm
    g=(a)*(c)
    h=(b)*(e)
    errorr=math.sqrt(math.pow(g,2)+math.pow(h,2))
    return errorr

while True:
    print('''
    menu: 
        1.first part of experiment(Lens method)
        2.seonc part of experiment(Besel's method)
        3.Estimate the error in F
    ''')
    n=int(input("enter the numver of your choice please: "))
    if n==1:
        print(lens_formular())
    elif n==2:
        print(Besel_formula())
    elif n==3:
        print(error_in_F())
    else: print("this is invalid")
    second_n=input("dou want to countinue?(y/n)")
    if second_n =="n":
        print("bye!")
        break
