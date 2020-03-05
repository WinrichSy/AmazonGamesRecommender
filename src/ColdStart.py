#Cold Start [Evaluating User's Own Description Input]
from EDA import EDA
import pandas as pd
import numpy as np
import os
import time
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import CountVectorizer

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
        self.choices = ['1','2','3','4','5','6','7']
        pass

    # #======RECOMMENDATIONS BY USER INPUT:
    # #======Lets user input their own description
    # def recommendations_by_user_input(self, bag_of_words, show_correlation=False):
    #     #create new df row with use of bag_of_words and append to dataframe
    #     temp = pd.DataFrame({"asin":[0], "bag_of_words":[bag_of_words]})
    #     appending_df = self.videogame_description_table.copy()
    #     appending_df = appending_df.sample(frac=1).reset_index(drop=True)
    #     temp = temp.append(appending_df, ignore_index = True)
    #     bag_of_word_list = temp['bag_of_words'][:25000]
    #
    #     #then get the indices of it
    #     indices = pd.Series(temp['asin'])
    #
    #     #initialize new list of things to recommend
    #     recommended_items = []
    #
    #     #indices == 0 because it is 0 (because of temp df)
    #     idx = indices[indices == 0].index[0]
    #
    #     #instantiate CountVectorizer
    #     count = CountVectorizer()
    #     count_matrix = count.fit_transform(bag_of_word_list)
    #
    #     vg_cosine_sim = cosine_similarity(count_matrix, count_matrix)
    #
    #     #get scores based on consine similarity
    #     score_series = pd.Series(vg_cosine_sim[idx]).sort_values(ascending = False)
    #
    #     top_10_indexes = list(score_series.iloc[1:11].index)
    #
    #     seperator = ' '
    #     for i in top_10_indexes:
    #         product_description = self.replace_asin_with_description(list(self.videogame_description_table.index)[i])
    #         if show_correlation:
    #             recommended_items.append((seperator.join(product_description.split()[:7]),score_series[i]))
    #         else:
    #             recommended_items.append(seperator.join(product_description.split()[:7]))
    #
    #     return recommended_items
    #
    # #===REPLACE ASIN WITH DESCRIPTION
    # #===Replaces asin values with their corresponding description
    # def replace_asin_with_description(self, asin):
    #     return (self.eda.remov_duplicates(self.asin_title.iloc[[asin]]['title'].item().title()))
    #
    # #===TOP 10
    # #===Retuns top 10 items from database
    # def top_10(self):
    #     #just get top 10 items. sorted by # of ratings, then avg rating
    #     #have to add # of ratings to video game column
    #     return "top_10"
    #
    # #===INPUT_RECOMMENDER
    # #===Asks for input from user
    # def input_recommender(self):
    #     input_product = input("Enter a description: ")
    #     input_product_tokenized = self.eda.personal_tokenize(self.eda.remov_duplicates(input_product.lower()))
    #
    #     if len(input_product_tokenized) == 0:
    #         print("Here are some of our most popular items!")
    #         print(self.top_10())
    #
    #     else:
    #         print('We recommend you try some of these products!')
    #         return self.recommendations_by_user_input(input_product_tokenized)

    def hard_code(self):
        print('**************************')
        print('[3] RECOMMEND BY PLATFORM')
        print('**************************')
        print('[1] PC')
        print('[2] Mac')
        print('[3] Xbox')
        print('[4] Sony')
        print('[5] Nintendo')
        print('[6] Atari')
        print('[7] Sega')
        print('=========================')
        user_input = str(input("Enter a number (q to quit): "))
        print('')

        if user_input == 'q':
            while(countdown>0):
                print('Returning to menu...{}'.format(countdown), end='\r')
                countdown -= 1
                time.sleep(1)
            return 'quit'

        if user_input not in self.choices:
            print('============================')
            print('     NOT A VALID INPUT!')
            print('============================')
            print('')
            self.eda.countdown('Retry another input in ',countdown_time = 3)
            return self.hard_code()

        else:
            #PC
            if user_input == '1':
                output = ['Mamas & Papas Soft Toy, Peanut Elephant',
                         '1UPcard Video Game Cartridge Cleaning Kit - 3 Pack with Fluid',
                         "Shiver: Vanishing Hitchhiker Collector's Edition",
                         'Thrustmaster VG Thrustmaster T500 F1 Racing Wheel - PC',
                         'SpongeBob SquarePants: Diner Dash']
            #Mac
            elif user_input == '2':
                output = ['Panzer Dragoon Zwei - Sega Saturn',
                         'Silent Hill 3 with Game Soundtrack CD',
                         'Heroes of Might and Magic III',
                         'Fighting Edition: Tekken 6 / Tag Tournament 2 / Soul Calibur V  - Playstation 3',
                         'Auawak Rapoo V300 Ergonomic APM Smart Breathing Light Built-in 32-bit 60MHz V-power3 Core Gaming Mouse for PC Laptops and Desktops - 4000DPI']

            #Xbox
            elif user_input == '3':
                output = ['[Newest 2019] Gaming Headset for Xbox One, S, PS4, PC with LED Soft Breathing Earmuffs, Adjustable Microphone, Comfortable Mute & Volume Control, 3.5mm Adapter for Laptop, PS3, Nintendo',
                         'Forza Horizon 2: VIP Membership - Xbox One Digital Code',
                         'Gam3Gear Aluminum Alloy Analog Thumbstick for Xbox ONE Green (Set of 2)',
                         'LEGO Marvel Avengers (Xbox One)',
                         'Monster Fiber Optic 450dfo Advanced Performance Audio Cable - English/French/Spanish (6.56 feet / 2 meters)']

            #Sony
            elif user_input == '4':
                output = ['Odin Sphere Leifthrasir - PlayStation 3 Standard Edition',
                         'PlayStation Vita PERSONA 4 Dancing All Night Premium Crazy Box Japan ver',
                         "Saint Seya: Soldier's Soul English/Spanish Version",
                         'X-COM: UFO Defense - PlayStation',
                         'Hard Pouch for PlayStation Vita (Pink)']

            #Nintendo
            elif user_input == '5':
                output = ['Crystalis',
                         'Hatsune Miku -Project DIVA-F 2nd[Japan Import]',
                         "Demon's Crest",
                         'Nintendo Nes Security 3 Tool Video Game Cartridge Cleaning Kit',
                         'New Nintendo 3DS Cover Plates No.063 Pokemon']

            #Atari
            elif user_input =='6':
                output = ['Dig Dug',
                         'Atari 2600 AC Power Adapter by CyCO',
                         'Warlords',
                         'Solaris',
                         'Pitfall II: Lost Caverns']

            #Sega
            elif user_input == '7':
                output = ['Controller Extension Cable for Dreamcast Controllers by Mars Devices',
                         'Snatcher',
                         'Shining The Holy Ark - Sega Saturn',
                         'Sega Saturn 6 Player Multiplayer Adapter',
                         "Wonder Boy III: The Dragon's Trap"]


            print('Here are some recommendations!')
            print('------------------------------')

            for idx, val in enumerate(output):
                print(str(idx+1)+": "+val)
            print('')
            print('Hope you enjoy the selection!')
            print('')
            input('Enter anything to continue')
            return
