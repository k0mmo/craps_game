'''
Simple craps game
Python 3
Author: K0mmo
Date: Nov 25 2019
Ver: 1.0
'''

import random
import sys
import os




def Main():

    def clear(): # clear screen system that will clear the screen in windows, mac and linux consoles

        # for windows
        if os.name == 'nt':
            os.system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            os.system('clear')

    def Top():
        clear()
        while True:
            print("\n------------------------------------------------") #top part of the display that doesnt change only the dice section will change to save coding time
            print("|                     Craps                    |")
            print("------------------------------------------------")
            print("|                                              |")
            Dice()


    def Dice():
        Die1_roll = random.randint(1, 6) # pulls a random number from 1 to 6 stores it in the variable
        Die2_roll = random.randint(1, 6) # pulls a random number from 1 to 6 stores it in the variable

        if Die1_roll == 1 and Die2_roll == 1: # checks to see what the number of die 1 and die 2 is and then uses the correct display for each
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   |         |   ------------   |         |   |")
            print("|   |    *    |                  |    *    |   |")
            print("|   |         |   ------------   |         |   |")
            print("|   -----------   |Snake Eyes|   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 1 and Die2_roll == 2:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   |         |   ------------   |    *    |   |")
            print("|   |    *    |                  |         |   |")
            print("|   |         |   ------------   |    *    |   |")
            print("|   -----------   | Total: 3 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 1 and Die2_roll == 3:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   |         |   ------------   | *       |   |")
            print("|   |    *    |                  |    *    |   |")
            print("|   |         |   ------------   |       * |   |")
            print("|   -----------   | Total: 4 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 1 and Die2_roll == 4:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   |         |   ------------   | *     * |   |")
            print("|   |    *    |                  |         |   |")
            print("|   |         |   ------------   | *     * |   |")
            print("|   -----------   | Total: 5 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 1 and Die2_roll == 5:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   |         |   ------------   | *     * |   |")
            print("|   |    *    |                  |    *    |   |")
            print("|   |         |   ------------   | *     * |   |")
            print("|   -----------   | Total: 6 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 1 and Die2_roll == 6:
            print("|                 ------------                 |")
            print("|   -----------   |    WIN   |   -----------   |")
            print("|   |         |   ------------   | *     * |   |")
            print("|   |    *    |                  | *     * |   |")
            print("|   |         |   ------------   | *     * |   |")
            print("|   -----------   | Total: 7 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 2 and Die2_roll == 1:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   |    *    |   ------------   |         |   |")
            print("|   |         |                  |    *    |   |")
            print("|   |    *    |   ------------   |         |   |")
            print("|   -----------   | Total: 3 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 2 and Die2_roll == 2:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   |    *    |   ------------   |    *    |   |")
            print("|   |         |                  |         |   |")
            print("|   |    *    |   ------------   |    *    |   |")
            print("|   -----------   | Total: 4 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 2 and Die2_roll == 3:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   |    *    |   ------------   | *       |   |")
            print("|   |         |                  |    *    |   |")
            print("|   |    *    |   ------------   |       * |   |")
            print("|   -----------   | Total: 5 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 2 and Die2_roll == 4:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   |    *    |   ------------   | *     * |   |")
            print("|   |         |                  |         |   |")
            print("|   |    *    |   ------------   | *     * |   |")
            print("|   -----------   | Total: 6 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 2 and Die2_roll == 5:
            print("|                 ------------                 |")
            print("|   -----------   |    WIN   |   -----------   |")
            print("|   |    *    |   ------------   | *     * |   |")
            print("|   |         |                  |    *    |   |")
            print("|   |    *    |   ------------   | *     * |   |")
            print("|   -----------   | Total: 7 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 2 and Die2_roll == 6:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   |         |   ------------   | *     * |   |")
            print("|   |    *    |                  | *     * |   |")
            print("|   |         |   ------------   | *     * |   |")
            print("|   -----------   | Total: 8 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 3 and Die2_roll == 1:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   | *       |   ------------   |         |   |")
            print("|   |    *    |                  |    *    |   |")
            print("|   |       * |   ------------   |         |   |")
            print("|   -----------   | Total: 4 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 3 and Die2_roll == 2:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   | *       |   ------------   |    *    |   |")
            print("|   |    *    |                  |         |   |")
            print("|   |       * |   ------------   |    *    |   |")
            print("|   -----------   | Total: 5 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 3 and Die2_roll == 3:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   | *       |   ------------   | *       |   |")
            print("|   |    *    |                  |    *    |   |")
            print("|   |       * |   ------------   |       * |   |")
            print("|   -----------   | Total: 6 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 3 and Die2_roll == 4:
            print("|                 ------------                 |")
            print("|   -----------   |    WIN   |   -----------   |")
            print("|   | *       |   ------------   | *     * |   |")
            print("|   |    *    |                  |         |   |")
            print("|   |       * |   ------------   | *     * |   |")
            print("|   -----------   | Total: 7 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 3 and Die2_roll == 5:
            print("|                 ------------                 |")
            print("|   -----------   |    Lose  |   -----------   |")
            print("|   | *       |   ------------   | *     * |   |")
            print("|   |    *    |                  |    *    |   |")
            print("|   |       * |   ------------   | *     * |   |")
            print("|   -----------   | Total: 8 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 3 and Die2_roll == 6:
            print("|                 ------------                 |")
            print("|   -----------   |    WIN   |   -----------   |")
            print("|   | *       |   ------------   | *     * |   |")
            print("|   |    *    |                  | *     * |   |")
            print("|   |       * |   ------------   | *     * |   |")
            print("|   -----------   | Total: 9 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 4 and Die2_roll == 1:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   | *     * |   ------------   |         |   |")
            print("|   |         |                  |    *    |   |")
            print("|   | *     * |   ------------   |         |   |")
            print("|   -----------   | Total: 5 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 4 and Die2_roll == 2:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   | *     * |   ------------   |    *    |   |")
            print("|   |         |                  |         |   |")
            print("|   | *     * |   ------------   |    *    |   |")
            print("|   -----------   | Total: 6 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 4 and Die2_roll == 3:
            print("|                 ------------                 |")
            print("|   -----------   |    WIN   |   -----------   |")
            print("|   | *     * |   ------------   | *       |   |")
            print("|   |         |                  |    *    |   |")
            print("|   | *     * |   ------------   |       * |   |")
            print("|   -----------   | Total: 7 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 4 and Die2_roll == 4:
            print("|                 ------------                 |")
            print("|   -----------   |    Lose  |   -----------   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   |         |                  |         |   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   -----------   | Total: 8 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 4 and Die2_roll == 5:
            print("|                 ------------                 |")
            print("|   -----------   |    Lose  |   -----------   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   |         |                  |    *    |   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   -----------   | Total: 9 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 4 and Die2_roll == 6:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   |         |                  | *     * |   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   -----------   | Total: 10|   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 5 and Die2_roll == 1:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   | *     * |   ------------   |         |   |")
            print("|   |    *    |                  |    *    |   |")
            print("|   | *     * |   ------------   |         |   |")
            print("|   -----------   | Total: 6 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 5 and Die2_roll == 2:
            print("|                 ------------                 |")
            print("|   -----------   |    WIN   |   -----------   |")
            print("|   | *     * |   ------------   |    *    |   |")
            print("|   |    *    |                  |         |   |")
            print("|   | *     * |   ------------   |    *    |   |")
            print("|   -----------   | Total: 7 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 5 and Die2_roll == 3:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   | *     * |   ------------   | *       |   |")
            print("|   |    *    |                  |    *    |   |")
            print("|   | *     * |   ------------   |       * |   |")
            print("|   -----------   | Total: 8 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 5 and Die2_roll == 4:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   |    *    |                  |         |   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   -----------   | Total: 9 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 5 and Die2_roll == 5:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   |    *    |                  |    *    |   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   -----------   | Total: 10|   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 5 and Die2_roll == 6:
            print("|                 ------------                 |")
            print("|   -----------   |   WIN    |   -----------   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   |    *    |                  | *     * |   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   -----------   | Total: 11|   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 6 and Die2_roll == 1:
            print("|                 ------------                 |")
            print("|   -----------   |   WIN    |   -----------   |")
            print("|   | *     * |   ------------   |         |   |")
            print("|   | *     * |                  |    *    |   |")
            print("|   | *     * |   ------------   |         |   |")
            print("|   -----------   | Total: 7 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 6 and Die2_roll == 2:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   | *     * |   ------------   |    *    |   |")
            print("|   | *     * |                  |         |   |")
            print("|   | *     * |   ------------   |    *    |   |")
            print("|   -----------   | Total: 8 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 6 and Die2_roll == 3:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   | *     * |   ------------   | *       |   |")
            print("|   | *     * |                  |    *    |   |")
            print("|   | *     * |   ------------   |       * |   |")
            print("|   -----------   | Total: 9 |   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 6 and Die2_roll == 4:
            print("|                 ------------                 |")
            print("|   -----------   |    Lose  |   -----------   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   | *     * |                  |         |   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   -----------   | Total: 10|   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 6 and Die2_roll == 5:
            print("|                 ------------                 |")
            print("|   -----------   |    WIN   |   -----------   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   | *     * |                  |    *    |   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   -----------   | Total: 11|   -----------   |")
            print("|                 ------------                 |")
            Bottom()
        elif Die1_roll == 6 and Die2_roll == 6:
            print("|                 ------------                 |")
            print("|   -----------   |   Lose   |   -----------   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   | *     * |                  | *     * |   |")
            print("|   | *     * |   ------------   | *     * |   |")
            print("|   -----------   | Total: 12|   -----------   |")
            print("|                 ------------                 |")
            Bottom()

    def Bottom():
        print("|                                              |") # bottom section of the display doesnt change simply to save time coding
        print("------------------------------------------------")
        print("|                 Author: K0mmo                |")
        print("------------------------------------------------\n")
        print("Would you like to play again? y/n") # asks to play again
        user_input = input(">> ") # stores users choice
        if user_input == "y": # if yes send it back to the top section
            Top()
        elif user_input == "n": # if no then it exits program
            clear()
            sys.exit()
        else:
            print("invlaid choice") # prevents other text from being enetered
            Top()
    Top()

Main()
