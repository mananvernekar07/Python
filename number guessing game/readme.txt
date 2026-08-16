# Guess the Lucky Number 🎯

A simple Python guessing game where the computer randomly selects a lucky number between **1 and 50**, and the player tries to guess it.

## Features

* Generates a random number between 1 and 50.
* Allows the player to make unlimited guesses until they find the lucky number.
* Gives hints when the guess is:

  * **A little low** 👀
  * **A little high** 👀
  * **Too low**
  * **Too high**
* Displays a congratulatory message when the correct number is guessed. 🎉

## How It Works

1. The program asks the user to type `play` to start the game.
2. A random lucky number between 1 and 50 is generated.
3. The player enters a guess.
4. The program compares the guess with the lucky number.
5. A hint is displayed based on how close the guess is.
6. The game continues until the correct number is guessed.

## Example

```text
To guess the lucky number type 'play'
play
Guess the lucky number: 25
Guess is too low!
Guess the lucky number: 32
Guess is little low👀!
Guess the lucky number: 36
36! U WON!!!🎉
```

## Requirements

* Python 3.x
* No external libraries are required. The built-in `random` module is used.

## How to Run

Save the code in a file named `lucky_number.py` and run:

```bash
python lucky_number.py
```

Then type `play` to begin the game.

## Project Purpose

This project is designed for beginners to practice Python concepts such as **random number generation, functions, loops, conditional statements, user input, and comparison operators**.
