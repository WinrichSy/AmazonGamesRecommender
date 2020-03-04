import os
import time
#Recommender
from RecommenderByUsersRating import Recommender_By_Users_Rating
from RecommenderByDescription import Recommender_By_Description
# from ColdStart import Cold_Start

if __name__ == '__main__':
    recommender_by_users_rating = Recommender_By_Users_Rating()
    recommend_by_description = Recommender_By_Description()
    # cold_start = Cold_Start()

    while(True):
        os.system('clear')
        print('''
                 ===========================================
                 ****** AMAZON VIDEO GAME RECOMMENDER ******
                 ============= by Winrich Sy ===============
                                                            ''')
        print('Please Enter a Number From the Following: ')
        print('[1] - ASIN RECOMMENDATIONS THROUGH COLLABORATIVE FILTERING')
        print('[2] - ASIN RECOMMENDATIONS THROUGH CONTENT BASED')
        # print('3. Enter your own description')
        print('(q to quit)')
        print('')
        user_input = str(input('Enter choice of number: '))

        #Give User option to type in asin for recommendations based off ratings
        if user_input == '1':
            recommend_selection = recommender_by_users_rating.input_recommender()
            if recommend_selection == 'quit':
                print('')
                continue

            for idx, val in enumerate(recommend_selection):
                print(str(idx+1)+": "+val)
            print('')
            input('Enter anything to continue')

        #Give User option to type in asin for recommendations based off descriptions
        elif user_input == '2':
            recommend_selection = recommend_by_description.input_recommender()
            if recommend_selection == 'quit':
                print('')
                continue

            for idx, val in enumerate(recommend_selection):
                print(str(idx+1)+": "+val)
            print('')
            input('Enter anything to continue')

        # #Give User the option to type in own description [in testing]
        # elif user_input == '3':
        #     recommend_selection = cold_start.input_recommender()
        #     for idx, val in enumerate(recommend_selection):
        #         print(str(idx+1)+": "+val)
        #     print('Hope you enjoy the selection!')
        #     print('')

        #Give User option to quit recommneder program
        elif user_input == 'q':
            print('')
            print('Thank you for using my recommender. Have a Great Day! Bye!')
            break
            # print('For demo purposes, quitting the program is not available')
            # print('')

        else:
            print('')
            print('============================')
            print('    NOT A VALID INPUT!')
            print('============================')
            print('')
            countdown = 5
            while(countdown>0):
                print('Returning to menu...{}'.format(countdown), end='\r')
                countdown -= 1
                time.sleep(1)
