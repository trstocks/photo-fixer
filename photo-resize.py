import os,sys
from PIL import Image

#manage files provided by client
#scale_down reduces the file size by half while keeping the aspect ratio.
def scale_down(oldPath,newPath,file):
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    img = Image.open(oldPath + '/' + file)
    width, height = img.size
    print(img.size)
    img.resize((width//2, height//2)).save(newPath + "/" + file)
#bulk scale down takes an entire folder of images and reduces their size.
def bulk_scale_down(oldPath,newPath):
    for root, dirs,files in os.walk(oldPath):
        print(files)
        for filename in files:
            if filename.split('.')[-1].lower() in ['jpg', 'gif', 'png']:
                scale_down(oldPath, newPath, filename)
#rename is #there to provide quick renaming of images in a folder which have spaces and underscores and replaces them.
#This also changes naming to lowercase for uniformity.
def rename(filePath):
    for root, dirs,files in os.walk(filePath):
        for filename in files:
            newname = filename.replace(' ', '-')
            newname = newname.replace('_', '-')
            newname = newname.lower()
            os.rename(filePath + '/' + filename, filePath + '/' + newname)
            print(newname)
if __name__ == '__main__':
        folder_of_images=sys.argv[1]
        rename(folder_of_images)
