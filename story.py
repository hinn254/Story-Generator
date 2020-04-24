'''
The project will randomly create stories with a little bit of customizations. 
You can ask users to input a few words like name, action,
etc and then it will modify the stories using your words.
'''
import random

# function for story gen
def story_gen():

    while True:
        # benny is/was eating/running today/yesterday
        try:
            noun = input("Enter any noun: ")
            verb = input('Enter a verb: ')
            # list of sample helping verbs - can be expanded
            first = ['was','is','will be']
            # list of sample adjectives - can be expanded
            second = ['today','yesterday','tomorrow','forever','always']

            # combining everything to make a sentence
            x =  f'{noun} {random.choice(first)} {verb} {random.choice(second)}'
            print(x)
            break
        except KeyboardInterrupt:
            break
        except:
            print('Invalid Values')


story_gen()