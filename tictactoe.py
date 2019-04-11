# Data Science | SS2019 | Carolin Gellner | 2. Python Exercise: Exercise 2

game = []

win_player_x = 0
win_player_o = 0

def print_game_bord():
                print( '\n -----------')
                print( '| ' + game[0] + ' | ' + game[1] + ' | ' + game[2] + ' |')
                print( ' -----------')
                print( '| ' + game[3] + ' | ' + game[4] + ' | ' + game[5] + ' |')
                print( ' -----------')
                print( '| ' + game[6] + ' | ' + game[7] + ' | ' + game[8] + ' |')
                print( ' -----------\n')




play = 0


while True:
        
        play += 1

        print("----- TIC-TAC-TO Game ------")
        print("Type the number of the field you want to occupy.")
        print("Game No. " + str(play))


        round = 0
        currentplayer = 'x'

        for x in range (0, 9):
                game.append(str(x + 1))

        print_game_bord()

        while True:

                round += 1

                while True:
                       
                        while True:
                                
                                userinput = input(">>> Player " + currentplayer + " : ")

                                try:
                                        val = int(userinput)
                                        if val > 0 and val < 10:
                                                break
                                        else:
                                                print("Value must be between 1 and 9.")
                                except ValueError:
                                        print("That's not a Number!")
                                
                        if(game[int(userinput)-1] == userinput):
                                game[int(userinput)-1] = currentplayer
                                break
                        else:
                                print("The field is already occupied. Choose another field.")


                print_game_bord()

                if((game[0] == game[1] == game[2]) or 
                (game[3] == game[4] == game[5]) or 
                (game[6] == game[7] == game[8]) or 
                (game[0] == game[3] == game[6]) or
                (game[1] == game[4] == game[7]) or
                (game[2] == game[5] == game[8]) or 
                (game[0] == game[4] == game[8]) or
                (game[6] == game[4] == game[2])):
                        print("The game is over. Result: player " + currentplayer + " won.")
                        
                        if currentplayer  == 'x':
                                win_player_x += 1
                        elif currentplayer == 'o':
                                win_player_o += 1
                        break

                elif round == 9:
                        print("The game is over. Result: Nobody won")
                        break


                if currentplayer == 'x':
                        currentplayer = 'o'
                elif currentplayer == 'o':
                        currentplayer = 'x'

        
        newGame = input("Do you want to start a new game? (y/n): ")
        if newGame == 'n':
                print("**** RESULT ****")
                print("Games: " + str(play))
                print('Player x has won {} games.'.format(win_player_x))
                print('Player o has won {} games.'.format(win_player_o))
               
                if win_player_o == win_player_x:
                      print("Both players were equally good")
                elif win_player_o > win_player_x:
                        print("Player o is the winner!")
                elif win_player_x > win_player_o:
                        print("Player x is the winner!")

                break
        elif newGame == 'y':
                game.clear()

        



                

