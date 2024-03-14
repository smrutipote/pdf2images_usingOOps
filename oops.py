import re
import os
import pdf2image
from pdf2image import convert_from_path

class File():
    def __init__(self):
        self.file_path=r'C:\Users\D\sample.pdf'
        print('This is File Class INIT')
        
class Folder(File):
    
    def __init__(self):
        File.__init__(self)
        self.folder_name=self.file_path.split('\\')[-1].split('.')[0]
        self.path=os.getcwd()
        
    def folder_create(self):
            self.folder_path=os.path.join(self.path,self.folder_name)
            print(self.folder_path)
            if not os.path.exists(self.folder_path):
                os.mkdir(self.folder_path)
                print('folder Created')
obj1=Folder()
obj1.folder_create()

                
class ImageMake(Folder):
    
    def __init__(self):
        Folder.__init__(self)
        self.folder_path1=r'C:\Users\D\sample'
        self.pop_path=r'C:\Program Files\poppler-24.02.0\Library\bin'
        self.images=convert_from_path(self.file_path,dpi=300,poppler_path=self.pop_path)
        
    def image_name(self):
        for i,image in enumerate(self.images):
            self.file_name= os.path.join(self.folder_path1,'image_'+str(i)+'.png')
            print(self.file_name)
            image.save(self.file_name,'PNG') 
            print('Images saved')       
            
obj=ImageMake()
obj.image_name()