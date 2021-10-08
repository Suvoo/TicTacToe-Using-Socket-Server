import socket # for networking
import pickle # for sending/receiving objects 

# import the game
from tic_tac_toe import TicTacToe

HOST = '127.0.0.1'  # the server's IP address 
PORT = 12783        # the port we're connecting to 

# connect to the host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(f"\nConnected to {s.getsockname()}!")

# set up the game
player_o = TicTacToe("O")

# allow the player to suggest playing again
rematch = True

while rematch == True:
    # a header for an intense tic-tac-toe match! 
    print(f"\n\n T I C - T A C - T O E ")

    # draw the grid
    player_o.draw_grid()

    # host goes first, client receives first
    print(f"\nWaiting for other player...")
    x_symbol_list = s.recv(1024)
    x_symbol_list = pickle.loads(x_symbol_list)
    player_o.update_symbol_list(x_symbol_list)

    # the rest is in a loop; if either player has won, it exits 
    while player_o.did_win("O") == False and player_o.did_win("X") == False and player_o.is_draw() == False:
        # draw grid, ask for coordinate 
        print(f"\n       Your turn!")
        player_o.draw_grid()
        player_coord = input(f"Enter coordinate: ")
        player_o.edit_square(player_coord)

        # draw grid again
        player_o.draw_grid()

        # pickle the symbol list and send it 
        o_symbol_list = pickle.dumps(player_o.symbol_list)
        s.send(o_symbol_list)

        # if the player won with the last move or it's a draw, exit the loop 
        if player_o.did_win("O") == True or player_o.is_draw() == True:
            break

        # wait to receive the symbol list and update it
        print(f"\nWaiting for other player...")
        x_symbol_list = s.recv(1024)
        x_symbol_list = pickle.loads(x_symbol_list)
        player_o.update_symbol_list(x_symbol_list)

    # end game messages
    if player_o.did_win("O") == True:
        print(f"Congrats, you won!")
    elif player_o.is_draw() == True:
        print(f"It's a draw!")
    else:
        print(f"Sorry, the host won.")

    # host is being asked for a rematch, awaiting response 
    print(f"\nWaiting for host...")
    host_response = s.recv(1024)
    host_response = pickle.loads(host_response)
    client_response = "N"

    # if the host wants a rematch, then the client is asked 
    if host_response == "Y":
        print(f"\nThe host would like a rematch!")
        client_response = input("Rematch? (Y/N): ")
        client_response = client_response.capitalize()
        temp_client_resp = client_response

        # let the host know what the client decided 
        client_response = pickle.dumps(client_response)
        s.send(client_response)

        # if the client wants a rematch, restart the game
        if temp_client_resp == "Y":
            player_o.restart()

        # if the client said no, then no rematch 
        else:
            rematch = False

    # if the host said no, then no rematch 
    else:
        print(f"\nThe host does not want a rematch.")
        rematch = False

spacer = input(f"\nThank you for playing!\nPress enter to quit...\n")

s.close()