# Number Guessing Game - Odd or Even Cricket Edition

## Overview
Welcome to the Number Guessing Game - Odd or Even Cricket Edition! This project brings back the nostalgia of childhood games with a digital twist. The game simulates a cricket match where players guess odd or even numbers to score runs or take wickets. Whether you're a cricket enthusiast or simply looking for some nostalgic fun, this game is for you!

## Project Structure
- **innings.py:** This module contains functions for bowling and batting, as well as determining the result of the innings.
- **user_first.py:** Handles the user's choice to bat or bowl first.
- **toss.py:** Manages the toss to decide who bats or bowls first.
- **main.py:** The main file to run the game. It imports necessary modules and starts the game.

## How to Play
1. **Run the Game:** Execute `main.py` using Python to start the game.
2. **Toss:** The game starts with a toss to decide who bats or bowls first.
3. **Toss:** If you guess odd or even correctly by entering a number, you can choose to bat or bowl first.
4. **Bat/Bowl:** 
   - If you choose to bat, enter a number from 0 to 6 to score runs. If you and the computer choose the same number, you will be out (wicket). 
   - If you choose to bowl, try to guess the same number as the computer to take its wicket.
5. **Innings Result:** After both innings are completed, the total scores are compared, and the winner is announced.

## Sample Input and Output
- Sample Input:
  - Choose odd or even: odd
  - Your guess: 3
- Sample Output:
  - Computer's number: 4
  - Total Score: 7
- choosing Ball Or Bat: 1

## Dependencies
- Python 3.x

## Author
- [Muhammed Shebeeb](https://github.com/cmshebeeb)

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository, make your changes, and submit a pull request.
