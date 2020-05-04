from PIL import Image
import numpy as np
import openpyscad as ops
c1 = ops.Cube([10, 10, 10])
c2 = ops.Cube([10, 10, 10]).translate([10, 10, 0])
(c1 + c2).write("sample.scad")
def load_image() :
    img = Image.open("qr.PNG")
    img.load()
    data = np.array( img, dtype="int32" )
    return data
ok = load_image()
print(ok[0].size/4)
print (ok[0,0,0])
nul = np.array([0,0,0,255])
print (nul)
for i in range(int(ok[0].size/4)):
    for j in range(int(ok.size/ok[0].size/4)):
        if (ok[i,j,0]+ok[i,j,1]+ok[i,j,2] < 30):
            a = 1
                   
