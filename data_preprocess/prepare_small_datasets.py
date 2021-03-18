import os
import shutil
from data_preprocess.preprocess_small_datasets import preprocess_all_small_datasets

def prepare_all_small_datasets(args):

    preprocess_all_small_datasets(args)

    # for dataset in ['3dpes', 'cuhk01', 'cuhk02', 'ilids', 'prid', 'viper']:
    # for dataset in ['3dpes', 'cuhk01', 'ilids', 'prid', 'viper']:
    # for dataset in ['cuhk01', 'viper']:
    for dataset in ['AHU']:
        
        os.mkdir('data/'+dataset+'/pytorch')

        files = ['data/'+dataset+'/train.txt', 'data/'+dataset+'/val.txt']
        with open('data/'+dataset+'/train_all.txt', 'w') as outfile:
            for fname in files:
                with open(fname) as infile:
                    outfile.write(infile.read())

        for file in os.listdir('data/'+dataset):
            if file.split('.')[-1]=='txt':
                name = file.split('.')[0]

                if 'gallery' in name:
                    name = 'gallery'
                if 'probe' in name: 
                    name = 'query'

                # print("dataset =", dataset)
                data_dir = 'data/'+dataset+'/pytorch/'+name
                os.mkdir(data_dir)
                # print("before open dataset =", dataset)
                # print("before open file =", file)
                with open('data/'+dataset+'/'+file) as f:
                    for line in f:
                        # print("line =", line)
                        img,label = line.split()
                        img = img.replace('\\', '/')
                        if not os.path.exists(data_dir+'/'+label):
                            os.mkdir(data_dir+'/'+label)
                        print("img = ", img)
                        a,b,c,d = img.split('/')
                        print(data_dir+'/'+label+'/'+c+'_'+d)
                        shutil.copyfile(img, data_dir+'/'+label+'/'+c+'_'+d)







