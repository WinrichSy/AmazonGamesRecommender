#Recommender by User Rating
import os
from EDA import EDA
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class Recommender_By_Users_Rating:
    def __init__(self):
        self.asin_title = pd.read_csv('../Data/asin_title.csv', index_col=0)
        self.item_similarity = np.load('../Data/item_similarity.npy')
        self.asin_values = self.asin_title['asin'].unique()
        #instantiate eda object
        self.eda = EDA()
        pass


    def replace_asin(self, x):
        return simple_videogames[simple_videogames['asin']==x]['title'].value[0]

    # def pearson(self, s1, s2):
    #     s1_c = s1-s1.mean()
    #     s2_c = s2-s2.mean()
    #     return np.sum(s1_c * s2_c)/np.sqrt(np.sum(s1_c**2)*np.sum(s2_c**2))

    #===GET_RECS=====
    #===Gets num top recommendations based on asin_id
    def get_recs(self, asin, show_correlation=False):
        #then get the indices of it
        indices = pd.Series(self.asin_title['asin'])
        #initialize new list of things to recommend
        recommended_items = []
        #indices == 0 because it is 0 (because of temp df)
        idx = indices[indices == asin].index[0]

        #get scores based on consine similarity
        score_series = pd.Series(self.item_similarity[int(idx)]).sort_values(ascending = False)

        other_recommended =[]
        top_10_indexes = score_series.iloc[1:6].index
        for i in top_10_indexes:
            product_title_asin = list(self.asin_title.index)[i]
            recommended_items.append(self.asin_title.iloc[int(product_title_asin), 0])

        return recommended_items#, other_recommended


    #===INPUT_RECOMMENDER
    #===Asks for input from user
    def input_recommender(self):
        os.system('clear')
        print('********************************************************')
        print('[1] ASIN RECOMMENDATIONS THROUGH COLLABORATIVE FILTERING')
        print('********************************************************')
        user_input = str(input("Enter an asin (q to quit): "))
        print('')

        if user_input == 'q':
            print('Returning back to menu...')
            print('')
            return 'quit'

        if user_input not in self.asin_values:
            print('============================')
            print('     NOT A VALID INPUT!')
            print('============================')
            print('')
            self.eda.countdown('Retry another input in ',countdown_time = 3)
            return self.input_recommender()

        else:
            # print('asin: ' + user_input, self.asin_title[self.asin_title['asin']==user_input]['title'])
            print('Here are some recommendations!')
            print('------------------------------')
            return self.get_recs(user_input)
