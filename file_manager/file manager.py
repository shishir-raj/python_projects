# list2=[1,2,3,4,5,6,7,8,9]
# list1=[i*i for i in list2]
# print(list1)

import os
files=os.listdir() #used to display files in particular folder
files.remove("file manager.py")
print(files)
def Create_If_Not_Exist(folder):
    if(not os.path.exists(folder)):
        os.makedirs(folder)

Create_If_Not_Exist('Medias')
Create_If_Not_Exist('Images')
Create_If_Not_Exist('Docs')
Create_If_Not_Exist('Others')

imgexts=['.png','.jpeg','.jpg','.gif']
images= [file for file in files if(os.path.splitext(file)[1].lower() in imgexts) ]

docexts=['.doc','.docx','.txt','.pdf','.xls']
docs=[file for file in files if(os.path.splitext(file)[1].lower() in docexts)]

mediaexts=['.mp3','.mp4','.flv']
medias=[file for file in files if(os.path.splitext(file)[1].lower() in mediaexts )]

others=[]
for file in files:
    ext=os.path.splitext(file)[1].lower()
    if(ext not in mediaexts and ext not in imgexts and ext not in docexts ):
        others.append(file)

# for media in medias:
#     os.replace(media,f'Medias/ {media}')
#
# for doc in docs:
#     os.replace(doc, f'Docs/ {doc}')
#
# for image in images:
#     os.replace(image, f'Images/ {image}')
#
# for other in others:
#     os.replace(other, f'Others/{other}')

def move(foldername,files):
    for file in files:
        os.replace(file, f'{foldername}/{file}')

move('Images',images)
move('Docs',docs)
move('Medias',medias)
move('Others',others)





