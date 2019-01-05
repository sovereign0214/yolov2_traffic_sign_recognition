# -*- coding: utf-8 -*-
import os

imdir_finish = 'train_images'
if not os.path.isdir(imdir_finish):
    os.mkdir(imdir_finish)

#fidget_folders = [folder for folder in os.listdir('.') if 'fidget' in folder]
imdir_need_to_rename= 'pic_wait_to_rename'
'''
記得改數字
'''
n = 5301
#for folder in fidget_folders:
for imfile in os.scandir(imdir_need_to_rename):
    file_name=imfile.path
    file_name_extension=file_name[-3:]
    if file_name_extension == 'jpg':
        os.rename(imfile.path, os.path.join(imdir_finish, '{:06}.jpg'.format(n)))
    elif(file_name_extension=='png'):
        os.rename(imfile.path, os.path.join(imdir_finish, '{:06}.png'.format(n)))
    elif(file_name_extension=='JPG'):
        os.rename(imfile.path, os.path.join(imdir_finish, '{:06}.JPG'.format(n)))
    n += 1

print("\n" + "Done.")


'''    
    os.rename(imfile.path, os.path.join(imdir, '{:06}'.format(n)))
    n += 1
'''


