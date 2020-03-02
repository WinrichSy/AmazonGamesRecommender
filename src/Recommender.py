#Recommender
from ColdStart import Cold_Start
from RecommenderByDescription import Recommender_By_Description
from RecommenderByUsersRating import Recommender_By_Users_Rating

if __name__ == '__main__':
    recommender_by_users_rating = Recommender_By_Users_Rating()
    recommend_by_description = Recommender_By_Description()
    cold_start = Cold_Start()

    while(True):
        print('Please Enter a Number From the Following: ')
        print('1. Recommendations based on asin rating')
        print('2. Recommendations based on asin description')
        print('3. Enter your own description')
        print('(q to quit)')
        user_input = str(input('Enter choice of number: '))

        #Give User option to type in asin for recommendations based off ratings
        if user_input == '1':
            # recommend_selection = recommender_by_users_rating.input_recommender()
            if recommend_selection == 'quit' or recommend_selection == 'invalid':
                continue

            for idx, val in enumerate(recommend_selection):
                print(str(idx+1)+": "+val)
            print('Hope you enjoy the selection!')
            print('')

        #Give User option to type in asin for recommendations based off descriptions
        elif user_input == '2':
            recommend_selection = recommend_by_description.input_recommender()
            if recommend_selection == 'quit' or recommend_selection == 'invalid':
                continue

            for idx, val in enumerate(recommend_selection):
                print(str(idx+1)+": "+val)
            print('Hope you enjoy the selection!')
            print('')

        #Give User the option to type in own description [in testing]
        elif user_input == '3':
            recommend_selection = recommend_by_description.input_recommender()
            for idx, val in enumerate(recommend_selection):
                print(str(idx+1)+": "+val)
            print('Hope you enjoy the selection!')
            print('')

        #Give User option to quit recommneder program
        elif user_input == 'q' or 'Q':
            print('Thank you for using my recommender. Have a Great Day! Bye!')
            break

        else:
            print('============================')
            print('NOT A VALID INPUT!')
            print('============================')
