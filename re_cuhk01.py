import os
import shutil

PATH0 = "./data_preprocess/data/cuhk01/cam_0/"
PATH1 = "./data_preprocess/data/cuhk01/cam_1/"
FILEPATH = "./data_preprocess/data/cuhk01/campus"


def readname():
    filePath = "./data_preprocess/data/cuhk01/campus"
    name = os.listdir(filePath)
    return name


if __name__ == "__main__":
    name = readname()
    print(name)
    cnt = 0
    first_name = 0
    second_name = 0
    for i in name:
        # print(os.curdir)
        print(FILEPATH + '/' + i)
        print(PATH0)
        if (cnt % 4 == 0 or cnt % 4 == 1):
            # shutil.copyfile(FILEPATH+'/'+i, PATH0+i)
            sec = 0 if second_name % 2 == 0 else 1
            shutil.copyfile(FILEPATH + '/' + i, PATH0 + str(first_name).zfill(5) + '_' + str(sec).zfill(5) + ".png")
        else:
            # shutil.copyfile(FILEPATH+'/'+i, PATH1+i)
            sec = 0 if second_name % 2 == 0 else 1
            shutil.copyfile(FILEPATH + '/' + i, PATH1 + str(first_name).zfill(5) + '_' + str(sec).zfill(5) + ".png")
        # os.rename(PATH+'/'+i, PATH+'/'+"11111"+"_"+"0000"+str(cnt)+".png")
        second_name = second_name + 1
        cnt = cnt + 1
        if cnt % 4 == 0:
            first_name = first_name + 1
        print(i)
