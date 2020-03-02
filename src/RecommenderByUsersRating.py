#Recommender by User Rating
from EDA import EDA
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class Recommender_By_Users_Rating:
    def __init__(self):
        self.pivoted_rating_table = pd.read_csv('../Data/smaller_rating_table_25000.csv', index_col=0)
        self.asin_description = pd.read_csv('../Data/asin_description.csv', index_col=0)
        self.asin_values = self.asin_description['asin'].unique().tolist()[:25000]
        pass


    def replace_asin(self, x):
        return simple_videogames[simple_videogames['asin']==x]['description'].value[0]

    def pearson(self, s1, s2):
        s1_c = s1-s1.mean()
        s2_c = s2-s2.mean()
        return np.sum(s1_c * s2_c)/np.sqrt(np.sum(s1_c**2)*np.sum(s2_c**2))

    #===GET_RECS=====
    #===Gets num top recommendations based on asin_id
    #TODO: add cosine similarity
    def get_recs(self, asin_id, similarity_type='pearson', show_correlation=False):
        recommendations = []
        #Pearson Similarity
        if similarity_type=='pearson':
            similarity_calculator = self.pearson

        #Cosine Similarity
        elif similarity_type=='cosine similarity':
            similarity_calculator = cosine_similarity

        for asin in self.pivoted_rating_table.columns:
            if asin == asin_id:
                continue

            # cor = similarity_calculator(self.pivoted_rating_table[asin_id], self.pivoted_rating_table[asin])
            cor = self.pearson(self.pivoted_rating_table[asin_id], self.pivoted_rating_table[asin])


            #checks if the correlation is nan; if so, then continue
            if np.isnan(cor):
                continue
            else:
                if show_correlation:
                    recommendations.append((asin, cor))
                else:
                    recommendations.append(asin)

        recommendations.sort(key=lambda tup: tup[1], reverse=True)
        recommendations = recommendatsion[:11]

        recommendation_list = self.asin_description[self.asin_description['asin'].isin(recommendations)]['description'].tolist()
        shortened_recommendation_description = []
        separator = ' '
        for i in recommendation_list:
            shortened_recommendation_description.append(separator.join(shortened_recommendation_description.split()[:10]))
        return shortened_recommendation_description

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
            return self.get_recs(user_input)
