# -*- coding: utf-8 -*-
import csv
import hashlib
import pandas as pd
import os.path as path
import random
import sys

#print(sys.argv[1:])

DIR = path.abspath(path.dirname(__file__))

FILES = {
    'clothing.csv': ('Blouses', 'Shirts', 'Tanks', 'Cardigans', 'Pants', 'Capris', '"Gingham" Shorts',),
    'accessories.csv': ('Watches', 'Wallets', 'Purses', 'Satchels',),
    'household_cleaners.csv': ('Kitchen Cleaner', 'Bathroom Cleaner',),
}



def write_file(writer, length, categories):
    writer.writerow(['email_hash', 'category'])
    for i in range(0, length):
        writer.writerow([
            hashlib.sha256('tech+test{}@pmg.com'.format(i).encode('utf-8')).hexdigest(),
            random.choice(categories),
        ])


def main():
    lst_dfs = []
   
    for fn, categories in FILES.items():
       
        
      
       
        #print(path.join(DIR, 'fixtures', fn), fn)
        
        with open(path.join(DIR, 'fixtures', fn), 'w', encoding='utf-8') as fh:
            write_file(
                csv.writer(fh, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL),
                random.randint(100, 1000),
                categories
            )
    output_file = sys.argv[-1]
    if len(sys.argv) < 3:
        print("inavlid arguments")
    else:
        files = sys.argv[1:-1]
        # print(len(files))
        # print(DIR,files)
        if len(files) > 1:
            for fl in files:
               
                df = pd.read_csv(path.join(DIR, fl),sep=",")
                #print(fl.split("/")[2].split(".")[0])
                #if "/" in fl and len( fl.split("/")) ==2:
                df['filename'] = fl.split("/")[2]
                lst_dfs.append(df)
                
            combined_dfs = pd.concat((lst_dfs))
            
            combined_dfs.to_csv(path.join(DIR, 'fixtures', output_file), index=False)
        else:
            
            fl = files[0]
            
            df = pd.read_csv(path.join(DIR, fl),sep=",")
            
            df['filename'] = fl.split("/")[2]
            df.to_csv(path.join(DIR, 'fixtures', output_file), index=False)
        print("files combined successfully")
if __name__ == '__main__':
    main()