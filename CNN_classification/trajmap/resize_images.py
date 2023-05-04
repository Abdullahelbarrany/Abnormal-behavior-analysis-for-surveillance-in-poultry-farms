from genericpath import isdir
import os
from PIL import Image
import pathlib

os.chdir(r'C:\Users\abdal\OneDrive\Desktop\amr gamal\New folder\he')
for category in os.listdir('.'):
  os.chdir(category)
  for file in os.listdir('.'):
    path = f'{file}'
    with Image.open(path) as img:
      img = img.resize((1920,1080))
      img.save(path)
      print(path)
  os.chdir('..')



# path = pathlib.Path('.')/ "validation"
# for folder in path.iterdir():
#   if folder.isdir():
#     counter=1
#     for file in folder.iterdir():
#       if file.is_file():
#         new_file = folder.name + str(counter) + file.suffix
#         file.rename(path/folder.name/new_file)
#         counter+=1