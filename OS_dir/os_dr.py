import os

for root,dirs,files in os.walk('.',topdown=False):
    # print(root,dirs,files)
    for file in files:
        folders = root.split('\\')
        print(folders)
        print(os.path.join(root,file))
        print("#"*30)
