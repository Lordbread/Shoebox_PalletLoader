from math import floor
path = "C:\Users\ZZhuan\Desktop\sku.txt"
wpath ="C:\Users\ZZhuan\Desktop\\1.txt"
po = open(wpath,"w")
fo = open(path, "r")

class HBloader():
    def __init__(self,boxlength,boxwidth,boxhight):
        self.boxwidth = float(boxwidth)
        self.boxlength = float(boxlength)
        self.boxhight = float(boxhight)

    def outer(self,Pwidth,Plength):
        Pwidth = float(Pwidth)
        Plength = float(Plength)
        if self.boxwidth!= 0 and self.boxhight!=0 and self.boxlength!=0:
            maxnumL = floor(Plength/self.boxwidth)
            restW = Pwidth - self.boxlength
            maxnumW = floor(restW/self.boxwidth)
            restL = Plength - self.boxlength
            maxnumL = maxnumL + floor(restL/self.boxwidth)
            wasteW = Pwidth - (2* self.boxlength)
            maxnumW = maxnumW + floor(wasteW/self.boxwidth)
            outernum = maxnumL + maxnumW
            return outernum
        else:
            outernum = 0
            return outernum
    def outer1(self,Pwidth,Plength):
        Pwidth = float(Pwidth)
        Plength = float(Plength)
        if self.boxwidth!= 0 and self.boxhight!=0 and self.boxlength!=0:
            maxnumW = floor(Pwidth/self.boxwidth)
            restW = Plength - self.boxlength
            maxnumL = floor(restW/self.boxwidth)
            restL = Pwidth - (2 * self.boxlength)
            maxnumL = (maxnumL*2) + floor(restL/self.boxwidth)
            outernum = maxnumL + maxnumW
            return outernum
        else:
            outernum = 0
            return outernum

    def inner(self,Pwidth,Plength):
        Pwidth = float(Pwidth)
        Plength = float(Plength)
        if self.boxwidth != 0 and self.boxhight != 0 and self.boxlength != 0:
            wasteW = Pwidth - (2 * self.boxlength)
            wasteL = Plength - (2 * self.boxlength)
            if wasteW >= self.boxwidth and wasteL >= self.boxlength and wasteW >= self.boxlength and wasteL >= self.boxwidth:
                row = floor(wasteW/self.boxwidth)
                col = floor(wasteL/self.boxlength)
                midnum = int(row * col)
            else:
                midnum = 0
            return midnum
        else:
            midnum = 0
            return  midnum

    def level(self):
        if (self.boxhight * 10) > 145:
            levelH = 145
            level = floor(levelH/self.boxhight)
            print level
        else:
            level = 10
        return level

v = fo.read().split('\n')
for line in v:
    p = line.split('\t')
    a = HBloader(p[2],p[3],p[4]).outer(100,120)
    b = HBloader(p[2],p[3],p[4]).outer(120,100)
    e = HBloader(p[2],p[3],p[4]).outer1(120,100)
    f = HBloader(p[2],p[3],p[4]).outer1(100,120)
    c = HBloader(p[2],p[3],p[4]).inner(120, 100)
    d = HBloader(p[2],p[3],p[4]).inner(100,120)
    levelnum = min(a,b,e,f) + min(c,d)
    total = levelnum * HBloader(p[2],p[3],p[4]).level()
    po.write(str(total) + "\n")