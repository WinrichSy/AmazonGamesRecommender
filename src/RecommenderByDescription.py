#Recommender by item description
from EDA import EDA
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class Recommender_By_Description:
    def __init__(self):
        #TODO: combine all columns into one csv.
        #   have zero nan values
        #   and cleaned
        #Load videogame description table and clean a little
        self.videogame_description_table = pd.read_csv('../Data/videogame_asin_and_bow.csv', index_col=0)
        self.videogame_description_table.fillna("", inplace=True)
        #instantiate and EDA object
        self.eda = EDA()
        #Load full videogame
        self.simple_videogames = pd.read_csv('../Data/simple_videogames.csv', index_col = 0)
        self.simple_videogames.drop(columns=['Unnamed: 0.1','rank','platform','rating'],inplace=True)
        self.simple_videogames.fillna("", inplace=True)
        #Valid asin values (change 30000 later; limited number now because cosine similarity takes too long)
        self.asin_values = self.videogame_description_table['asin'].unique().tolist()[:30000]
        self.subset = self.videogame_description_table[:30000]
        #===========================
        #Load cosine similarity matrix
        self.vg_cosine_sim = np.load('../Data/vg_cosine_sim_30000.npy')
        pass

    #=====Creating a count matrix and doing a cosine similarity
    #=====Takes a while to run! use saved pny file!
    def cosine_similarity_matrix():
        #Load videogame description table and clean a little
        self.videogame_description_table = pd.read_csv('../Data/videogame_asin_and_bow.csv', index_col=0)
        self.videogame_description_table.fillna("", inplace=True)
        self.subset = self.videogame_description_table[:30000]
        #instantiate CountVectorizer
        self.count = CountVectorizer()
        self.count_matrix = self.count.fit_transform(self.subset['bag_of_words'])
        #Calculate cosine similarity
        self.vg_cosine_sim = cosine_similarity(self.count_matrix, self.count_matrix)
        pass

    #======RECOMMENDATIONS BY USER INPUT:
    #======Lets user input their own description
    def recommendations_by_description(self, asin, show_correlation=False):
        #then get the indices of it
        indices = pd.Series(self.subset['asin'])
        #initialize new list of things to recommend
        recommended_items = []
        #indices == 0 because it is 0 (because of temp df)
        idx = indices[indices == asin].index[0]

        #get scores based on consine similarity
        score_series = pd.Series(self.vg_cosine_sim[idx]).sort_values(ascending = False)

        top_10_indexes = list(score_series.iloc[1:11].index)
        print(top_10_indexes)
        seperator = ' '
        for i in top_10_indexes:
            product_description = self.replace_asin_with_description(list(self.videogame_description_table.index)[i])
            if show_correlation:
                recommended_items.append((seperator.join(product_description.split()[:7]),score_series[i]))
            else:
                recommended_items.append(seperator.join(product_description.split()))

        return recommended_items

    #===REPLACE ASIN WITH DESCRIPTION
    #===Replaces asin values with their corresponding description
    def replace_asin_with_description(self, asin):
        return (self.eda.remov_duplicates(self.simple_videogames.iloc[[asin]]['description'].item().title()))

    # #===TOP 10
    # #===Retuns top 10 items from database
    # def top_10(self):
    #     #just get top 10 items. sorted by # of ratings, then avg rating
    #     #have to add # of ratings to video game column
    #     return "top_10"

    #===INPUT_RECOMMENDER
    #===Asks for input from user
    def input_recommender(self):
        user_input = str(input("Enter an asin (q to quit): "))
        if user_input == 'q' or user_input == 'Q':
            print('Returning back to menu...')
            print('')
            return 'quit'

        if user_input not in self.asin_values:
            print('============================')
            print('NOT A VALID INPUT!')
            print('============================')
            print('')
            return 'invalid'

        else:
            print('We recommend you try some of these products!')
            return self.recommendations_by_description(user_input)
