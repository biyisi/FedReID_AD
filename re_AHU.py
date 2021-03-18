import os
import shutil

PATH0 = "./data_preprocess/data/AHU/UAV_0/"
PATH1 = "./data_preprocess/data/AHU/UAV_1/"
# FILEPATH = "./data_preprocess/data/cuhk01/campus"
out_PATH0 = "./data_preprocess/data/AHU/cam_0/"
out_PATH1 = "./data_preprocess/data/AHU/cam_1/"


def readname():
    filePath = PATH1
    name = os.listdir(filePath)
    return name


if __name__ == "__main__":
    name = readname()
    print(name)
    for jpg_name in name:
        jpg_name_out = jpg_name[:-4]
        jpg_name_out = '0'*(5-len(jpg_name_out))+jpg_name_out+'_00000.jpg'
        shutil.copyfile(PATH1 + jpg_name, out_PATH1 + jpg_name_out)
        # print("-")

    # 00001_00000.jpg
    # 00010_00000.jpg



    # cnt = 0
    # first_name = 0
    # second_name = 0
    # for i in name:
    #     # print(os.curdir)
    #     print(FILEPATH + '/' + i)
    #     print(PATH0)
    #     if (cnt % 4 == 0 or cnt % 4 == 1):
    #         # shutil.copyfile(FILEPATH+'/'+i, PATH0+i)
    #         sec = 0 if second_name % 2 == 0 else 1
    #         shutil.copyfile(FILEPATH + '/' + i, PATH0 + str(first_name).zfill(5) + '_' + str(sec).zfill(5) + ".png")
    #     else:
    #         # shutil.copyfile(FILEPATH+'/'+i, PATH1+i)
    #         sec = 0 if second_name % 2 == 0 else 1
    #         shutil.copyfile(FILEPATH + '/' + i, PATH1 + str(first_name).zfill(5) + '_' + str(sec).zfill(5) + ".png")
    #     # os.rename(PATH+'/'+i, PATH+'/'+"11111"+"_"+"0000"+str(cnt)+".png")
    #     second_name = second_name + 1
    #     cnt = cnt + 1
    #     if cnt % 4 == 0:
    #         first_name = first_name + 1
    #     print(i)
