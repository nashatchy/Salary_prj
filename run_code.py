

import glassdoor_scrapper as gs 
import pandas as pd 
path="D:/Github/Salary_prj"
df= gs.get_jobs('data scientist',1000, False, path, 10)

df.to_csv('glassdoor_scrapper_result',index=False)