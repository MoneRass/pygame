from os import walk
import pygame

def import_folder(path):
    anim_ls=[]

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path+'/'+image
            current_anim = pygame.image.load(full_path).convert_alpha()
            anim_ls.append(current_anim)

    return anim_ls
