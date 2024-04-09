import os
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

# Set the directory of the files that should be converted
folder_path = 'n42'

# Iterate over each file in the directory
for filename in os.listdir(folder_path):
    if filename.endswith('.n42'):  
        # Construct the full path to the file
        filepath = os.path.join(folder_path, filename)
        
        # Extract the spectroscopic data from each n42 file
        df = pd.DataFrame()
        with open(filepath) as f:
            xml = f.read()
        bs_obj = BeautifulSoup(xml, features="lxml")
        for i in range(3):
            data = bs_obj.find_all("channeldata")[i].text
            spec = pd.Series(np.fromstring(data, dtype=np.float64, sep=" "))
            df = pd.concat([df, spec], axis=1).fillna(0)
        df.columns = ['PUR', 'INDIV', 'SING']        
        
        # Save the DataFrame to a csv file with the same name as the original file
        csv_filename = os.path.splitext(filename)[0] + '.csv'
        csv_filepath = os.path.join(folder_path, csv_filename)
        df.to_csv(csv_filepath, index=False)
