#Recommender
from ColdStart import Cold_Start

if __name__ == '__main__':
    cold_start = Cold_Start()

    while(True):
        print('Please Enter a Number From the Following: ')
        print('1. Recommendations based on asin rating')
        print('2. Recommendations based on asin description')
        print('3. Enter your own description')
        print('(q to quit)')
        user_input = str(input('Enter choice of number: '))

        if user_input == '1':
            #do first recommender
            pass

        elif user_input == '2':
            pass

        elif user_input == '3':
            cold_start_selection = cold_start.input_recommender()
            for idx, val in enumerate(cold_start_selection):
                print(str(idx+1)+": "+val)
            print('Hope you enjoy the selection!')
            print('')

        elif user_input == 'q' or 'Q':
            print('Thank you for using my recommender. Have a Great Day! Bye!')
            break

        else:
            print('============================')
            print('NOT A VALID INPUT!')
            print('============================')
