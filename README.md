# TicTacToe using Socket Server
This is a project for the class : 18CSC302J - Computer Networks by Dr. S.Babu

## Overview

This is a simple game of tic-tac-toe developed in Python. It allows two players to play with one another on different command lines through networking. The server starts the game by *first* running `server.py`, waiting for the client to connect by *then* running `client.py`. Once their connected, the game itself starts.

The server starts as "X" and goes first, and the client is "O." The players choose the square they would like to use with coordinates; both "A1" and "1A" would be accepted, for example. The game proceeds, with the players taking turns, until one wins or the game is a draw. The host, then the client, is asked whether they'd like a rematch. If both agree, the game starts anew. 

Example of a turn:

```
       Your turn!

       A   B   C

   1     ║   ║ X
      ═══╬═══╬═══
   2     ║ O ║
      ═══╬═══╬═══
   3     ║   ║

Enter coordinate: 
```
## Network Communication

We used a server/client network architecture for this project using TCP (Transmission Control Protocol), and we used port 12783. The messages were sent back and forth between the server and the client thanks to the pickle module, which converts any object (in this case, a string list storing the nine squares of a tic-tac-toe grid) into a byte stream to be sent and back into an object to be read. 
## Demo
![image](https://user-images.githubusercontent.com/52796258/136496822-268fc91a-4826-4abb-9a13-9076117c3063.png)

## Development Environment

* Visual Studio Code
* Python (3.9.4) 64-bit
* Git / GitHub
* Python: Socket and Pickle modules

