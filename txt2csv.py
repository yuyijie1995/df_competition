import pandas as pd
import os


txt_path='D:/postgraduateworking/model_ensemble/test'

txt_files_list=os.listdir(txt_path)

filename_list=[]
box_list=[]
for file in txt_files_list:
    file_path=os.path.join(txt_path,file)
    with open(file_path) as txt_file:
        results_list=txt_file.readlines()
        for one_result in results_list:
            one_result_list=one_result.split()
            filename_list.append(file.split('.')[0])
            box_list.append(one_result_list[4]+' '+one_result_list[5]+' '+one_result_list[6]+' '+one_result_list[7])


df=pd.Series(box_list,index=filename_list)
df.to_csv('result.csv')


