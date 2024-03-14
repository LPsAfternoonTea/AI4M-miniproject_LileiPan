# convert a .png image file to a .bmp image file using PIL (Uran, 2010)
# Uran, E. (2010) Converting an image file (PNG) to a bitmap file, DaniWeb. Available at: https://www.daniweb.com/programming/software-development/threads/253957/converting-an-image-file-png-to-a-bitmap-file (Accessed: 08 March 2024). 
# 


from PIL import Image
import pandas as pd
import os

my_dataset_folder = r"H:\Msc Ai\Term2\AI-4-Media-23-24\AI4M-miniproject\data_folder"

file_names = os.listdir(my_dataset_folder)

for file_name in file_names:
        
    # name discriminator, inspired from Inroduction to Data Science Week 7 session
    # "df['PC'] = df['platforms'].str.contains('PC').astype(int)""  (McCallum, 2024)
    # McCallum, L. (2024) Build software better, together, Week 7 - Random Forests and Feature Engineering. Available at: https://git.arts.ac.uk/lmccallum/Intro-to-ds-23-24/blob/master/intro-to-ds-week-7.ipynb (Accessed: 07 March 2024).

    file_name_df = pd.Series([file_name]) 
    if file_name_df.str.contains("png").item():
        
        file_in = os.path.join(my_dataset_folder, file_name)
        
        # Uran, E. (2010) Converting an image file (PNG) to a bitmap file, DaniWeb. Available at: https://www.daniweb.com/programming/software-development/threads/253957/converting-an-image-file-png-to-a-bitmap-file (Accessed: 08 March 2024). 

        img = Image.open(file_in)
        
        # programcreek (2014) Python pil.image.merge() examples, Python Examples of PIL.Image.merge. Available at: https://www.programcreek.com/python/example/66650/PIL.Image.merge#google_vignette (Accessed: 08 March 2024). 
        # Example 11, split file name. (Programcreek, 2014)

        file_out = os.path.splitext(file_name)[0] + ".bmp"
        file_out = os.path.join(my_dataset_folder, file_out)
        
        img.save(file_out)