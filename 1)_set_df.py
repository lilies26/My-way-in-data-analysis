import numpy as np
import pandas as pd
nombre_columnas=['color','director_name','num_critic_for_reviews','duration','gross', 'movie_title','num_user_for_reviews',
                 'Ciudad','cotent_rating','budget','title_year','imdb_score','genre']
df=pd.read_csv('movies.csv', 
               sep='|', 
               header=None, 
               names=nombre_columnas, 
               skiprows=3,
               na_values='?', 
               thousands=',',
               index_col='movie_title')
