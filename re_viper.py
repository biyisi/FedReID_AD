import os
import shutil

PATH0 = "./data_preprocess/data/viper/cam_0/"
PATH1 = "./data_preprocess/data/viper/cam_1/"
FILEPATH0 = "./data_preprocess/data/viper/cam_A"
FILEPATH1 = "./data_preprocess/data/viper/cam_B"


def readName0():
    filePath = FILEPATH0
    name = os.listdir(filePath)
    return name

def readName1():
    filePath = FILEPATH1
    name = os.listdir(filePath)
    return name

if __name__ == "__main__":
    # name0 = readName0()
    # print(name0)
    # cnt = 0
    # first_name = 0
    # second_name = 0
    # for i in name0:
    #     print(os.curdir)
    #     print(FILEPATH0 + '/' + i)
    #     print(PATH0)
    #     shutil.copyfile(FILEPATH0 + '/' + i, PATH0 + str(first_name).zfill(5) + '_' + str(second_name).zfill(5) + ".bmp")
    #     first_name = first_name + 1
    #     print(i)

    name1 = readName1()
    print(name1)
    cnt = 0
    first_name = 0
    second_name = 0
    for i in name1:
        print(FILEPATH1 + '/' + i)
        print(PATH1)
        shutil.copyfile(FILEPATH1 + '/' + i, PATH1 + str(first_name).zfill(5) + '_' + str(second_name).zfill(5) + ".bmp")
        first_name = first_name + 1
        print(i)











        # if (cnt % 4 == 0 or cnt % 4 == 1):
        #     # shutil.copyfile(FILEPATH+'/'+i, PATH0+i)
        #     sec = 0 if second_name % 2 == 0 else 1
        #     shutil.copyfile(FILEPATH + '/' + i, PATH0 + str(first_name).zfill(6) + '_' + str(sec).zfill(6) + ".png")
        # else:
        #     # shutil.copyfile(FILEPATH+'/'+i, PATH1+i)
        #     sec = 0 if second_name % 2 == 0 else 1
        #     shutil.copyfile(FILEPATH + '/' + i, PATH1 + str(first_name).zfill(6) + '_' + str(sec).zfill(6) + ".png")
        # # os.rename(PATH+'/'+i, PATH+'/'+"11111"+"_"+"0000"+str(cnt)+".png")
        # second_name = second_name + 1
        # cnt = cnt + 1
        # if cnt % 4 == 0:
        #     first_name = first_name + 1
        # print(i)
