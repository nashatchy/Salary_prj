

import glassdoor_scrapper as gs 
import pandas as pd 
path="D:/Github/Salary_prj"
df= gs.get_jobs('data scientist',10, False, path, 5)