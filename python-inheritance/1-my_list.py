#!/usr/bin/python3
'''My_list class inherits from list'''


class MyList(list):
    '''MyList Class'''

    def print_sorted(self):
        '''prints given list as sorted'''
        print(sorted(self))
