import os
import shutil
import pandas as pd

# Create a new folder, learned from week 3 session. (Kalaitzidi, 2024)
# Kalaitzidi, I. (2024) create-classification-dataset. Available at: https://git.arts.ac.uk/tbroad/AI-4-Media-23-24/blob/main/Week-3-CNNs-and-image-classification/create-classification-dataset.ipynb (Accessed: 07 March 2024). 

my_dataset_path = r'H:\Msc Ai\Term2\AI-4-Media-23-24\AI4M-miniproject\data_folder'
# Create new folder
# os.mkdir(my_dataset_path)

source_directory = r'H:\Msc Ai\Term2\AI-4-Media-23-24\AI4M-miniproject\cubicasa5k\high_quality_architectural'

i = 1226 
# Files from "high_quality" counts 1226 

# Make a series of folder names
folder_names = os.listdir(source_directory)

for folder_name in folder_names:

    target_directory = os.path.join(source_directory, folder_name)

    # Make a series of file names
    file_names = os.listdir(target_directory)


# name discriminator, inspired from Inroduction to Data Science Week 7 session
# "df['PC'] = df['platforms'].str.contains('PC').astype(int)""  (McCallum, 2024)
# McCallum, L. (2024) Build software better, together, Week 7 - Random Forests and Feature Engineering. Available at: https://git.arts.ac.uk/lmccallum/Intro-to-ds-23-24/blob/master/intro-to-ds-week-7.ipynb (Accessed: 07 March 2024).

    for file_name in file_names:
        file_name_df = pd.Series([file_name])       
        if file_name_df.str.contains("scaled").item():

    # I used ".astype()"", and the Terminal told me to use "a.empty" or "a.bool()", "a.item()", then I tried ".bool()"
    # Terminal said "h:\Msc Ai\Term2\AI-4-Media-23-24\AI4M-miniproject\test-arrangement.py:19: FutureWarning: Series.bool is now deprecated and will be removed in future version of pandas"
    # So I searched, and change it to ".item()"
    # https://pandas.pydata.org/docs/reference/api/pandas.Series.bool.html

            target_directory = os.path.join(my_dataset_path, f"{i}.png")
            shutil.move(os.path.join(source_directory, folder_name, file_name), target_directory)
            i = i + 1
