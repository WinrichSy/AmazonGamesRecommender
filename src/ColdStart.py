#Cold Start [Evaluating User's Own Description Input]
from EDA import EDA
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class Cold_Start:
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
        self.asin_title = pd.read_csv('../Data/asin_title.csv', index_col = 0)
        pass

    #======RECOMMENDATIONS BY USER INPUT:
    #======Lets user input their own description
    def recommendations_by_user_input(self, bag_of_words, show_correlation=False):
        #create new df row with use of bag_of_words and append to dataframe
        temp = pd.DataFrame({"asin":[0], "bag_of_words":[bag_of_words]})
        appending_df = self.videogame_description_table.copy()
        appending_df = appending_df.sample(frac=1).reset_index(drop=True)
        temp = temp.append(appending_df, ignore_index = True)
        bag_of_word_list = temp['bag_of_words'][:25000]

        #then get the indices of it
        indices = pd.Series(temp['asin'])

        #initialize new list of things to recommend
        recommended_items = []

        #indices == 0 because it is 0 (because of temp df)
        idx = indices[indices == 0].index[0]

        #instantiate CountVectorizer
        count = CountVectorizer()
        count_matrix = count.fit_transform(bag_of_word_list)

        vg_cosine_sim = cosine_similarity(count_matrix, count_matrix)

        #get scores based on consine similarity
        score_series = pd.Series(vg_cosine_sim[idx]).sort_values(ascending = False)

        top_10_indexes = list(score_series.iloc[1:11].index)

        seperator = ' '
        for i in top_10_indexes:
            product_description = self.replace_asin_with_description(list(self.videogame_description_table.index)[i])
            if show_correlation:
                recommended_items.append((seperator.join(product_description.split()[:7]),score_series[i]))
            else:
                recommended_items.append(seperator.join(product_description.split()[:7]))

        return recommended_items

    #===REPLACE ASIN WITH DESCRIPTION
    #===Replaces asin values with their corresponding description
    def replace_asin_with_description(self, asin):
        return (self.eda.remov_duplicates(self.asin_title.iloc[[asin]]['title'].item().title()))

    #===TOP 10
    #===Retuns top 10 items from database
    def top_10(self):
        #just get top 10 items. sorted by # of ratings, then avg rating
        #have to add # of ratings to video game column
        return "top_10"

    #===INPUT_RECOMMENDER
    #===Asks for input from user
    def input_recommender(self):
        input_product = input("Enter a description: ")
        input_product_tokenized = self.eda.personal_tokenize(self.eda.remov_duplicates(input_product.lower()))

        if len(input_product_tokenized) == 0:
            print("Here are some of our most popular items!")
            print(self.top_10())

        else:
            print('We recommend you try some of these products!')
            return self.recommendations_by_user_input(input_product_tokenized)
