# Hangpy 🐍

#### Video Demo:  <URL HERE>

![GitHub](https://img.shields.io/github/license/renzofbn/hangpy) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/renzofbn/hangpy)

Hangman is an engaging Python game that offers a simple yet immersive terminal interface, designed to challenge your vocabulary while providing entertainment.

The primary objective of Hangpy is to provide an enjoyable gaming experience while challenging players to guess words within a limited number of attempts.

The game is available in English and Spanish and available for Linux, Windows, MacOS, and any other platform that supports Python 3. 


![Preview Gif](https://raw.githubusercontent.com/Renzofbn/hang-py/main/preview.gif)

# Installation:

Get started by installing the game through pip:

```
pip install hangpy-cli
```

> Ensure that your $PATH includes the ~/.local/bin directory to enable your shell to locate the hangpy command seamlessly.


# Usage:

Initiate the game by entering:
```
hangpy
```

You can customize the word language or adjust the menu language by executing:
```
hangpy -c
```

Explore the top 5 scores by typing:
```
hangpy -t
```

For additional guidance, refer to the help message:
```
hangpy -h
```

# Features:
- Language Support:

    Hangpy offers both English and Spanish language support, allowing players to enjoy the game in their preferred language. Whether you want to be fluent in English or Spanish.

- Extensive Word Libraries:

    Hangpy includes a comprehensive word database comprising over 6,000 words in Spanish and 1,000 words in English. This extensive word collection ensures a diverse and challenging gaming experience, with a wide range of words for players to guess and explore.

- Enhanced Interface: 

    Hangpy features a new and improved interface, designed to provide a visually appealing and intuitive gaming environment with a colorful display.

- Score Tracking:

    Hangpy records the top 5 highest scores achieved by players, adding a competitive element to the game.

# Project Structure
> *.py files are well documented, if you want to learn more about how the game works, you could read the source files
## main.py
The main.py file serves as the entry point for the Hangpy game. With the `run()` function, it initializes the game and handles command-line arguments to customize the game's language settings and display the top scores.

## game.py
The `game.py` file is the core script of the Hangpy game. It contains the main logic and functionality required to run the game. Here's an overview of what this file includes:

- Word Selection:
    
    Hangpy randomly selects words from a predefined list, which serves as the basis for the game. These words are the ones that players attempt to guess letter by letter.

- Game Loop:
    
    The script implements a game loop that allows players to make guesses until run out of attempts or want to exit. It manages player input, validates guesses, updates the display, and tracks game progress.

- Scoring System:
    
    Hangpy records player scores and displays the top 5 scores at the end of each game. This adds a competitive element to the game, motivating players to improve their performance.

## utils.py
The `utils.py` file contains utility functions and configurations essential for the operation of Hangpy.

- CONFIG Global Variable:

    Is an instance of ConfigParser that loads the contents of the `config.ini` file upon module import. If the configuration file does not exist or is empty, the script invokes the `gen_config()` function to create a new configuration file with default settings.

    Also the config path could be found in `hangpy_config`. 

- File Initialization:

    The initialization process ensures that the game has access to necessary configurations from the config.ini file, setting up default values for game settings and player profiles if none are found.

- clear()
    
    To clear the terminal when needed :D

## translations.py
English and Spanish translations for every sentence used, under the `gm` variable.

## ascii_status
All the ascii art that the game uses, and functions to print them when needed.

## hangpy-cli Package
The hangpy-cli package facilitates the installation and execution of the Hangpy game through pip. It includes configuration files and metadata necessary for package management and distribution.


# Design Choices
## Terminal Interface
The decision to implement a terminal interface was driven by simplicity and accessibility. By using the terminal, Hangpy can run on various platforms without requiring additional dependencies or graphical libraries. This design choice ensures that users can enjoy the game without any installation hurdles or compatibility issues.

## Modular Code Structure
The project's code is organized into separate files and functions to promote modularity and maintainability. Each file encapsulates specific functionality, making it easier to understand, debug, and extend the codebase.

## User-Friendly Features
Hangpy includes features such as language customization and score tracking to enhance the user experience. Players can switch between different word languages and menu languages to cater to their preferences. Moreover, the scoring system adds a competitive element to the game, encouraging players to strive for higher scores while enjoying the game and most importantly, learning new words.



# License

Hangpy operates under the MIT License. For further details, please refer to the [LICENSE](https://github.com/renzofbn/hangpy/blob/main/LICENSE) file.
