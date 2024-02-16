def print_title():
    print('\033[94m')
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("█░████░▄▄▀█░▄▄▀█░▄▄▄█▀▄▄▀█░██░")
    print("█░▄▄░█░▀▀░█░██░█░█▄▀█░▀▀░█░▀▀░")
    print("█▄██▄█▄██▄█▄██▄█▄▄▄▄█░████▀▀▀▄")
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print('\033[0m')


def print_game_over():
    print('\033[94m')
    print(" ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .           ▌ ▐·▄▄▄ .▄▄▄   ")
    print("▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·    ▪     ▪█·█▌▀▄.▀·▀▄ █· ")
    print("▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄     ▄█▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄  ")
    print("▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌    ▐█▌.▐▌ ███ ▐█▄▄▌▐█•█▌ ")
    print("·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀      ▀█▄▀▪. ▀   ▀▀▀ .▀  ▀ ")
    print('\033[0m')


def print_ascii_state(lives: int, win : bool = False):

    if lives > 7 and not win:
        return
    
    print('\033[91m')
    if win:
        print('\033[92m', end="")
        print("          ██████████████████████")
        print("                           ██  █")
        print("                             ███")
        print("                               █")
        print("                               █")
        print("        @@@@@                  █")
        print("       @     @                 █")
        print("       @)   (@                 █")
        print("          @                    █")
        print("        ,@@@,                  █")
        print("       @  @  @                 █")
        print("     .@   @   @.               █")
        print("          @                    █")
        print("         @@@                   █")
        print("        @   @                  █")
        print("       @     @                 █")
        print("████████████████████████████████")


    elif lives == 7:
        print("          ██████████████████████")
        print("                           ██  █")
        print("                             ███")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("████████████████████████████████")


    elif lives == 6:
        print("          ██████████████████████")
        print("          @                ██  █")
        print("          @                  ███")
        print("          @                    █")
        print("          @                    █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("████████████████████████████████")


    elif lives == 5:
        print("          ██████████████████████")
        print("          @                ██  █")
        print("          @                  ███")
        print("        @@@@@                  █")
        print("       @     @                 █")
        print("       @)   (@                 █")
        print("          @                    █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("████████████████████████████████")


    elif lives == 4:
        print("          ██████████████████████")
        print("          @                ██  █")
        print("          @                  ███")
        print("        @@@@@                  █")
        print("       @     @                 █")
        print("       @)   (@                 █")
        print("          @                    █")
        print("        ,@@@,                  █")
        print("          @                    █")
        print("          @                    █")
        print("          @                    █")
        print("          @                    █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("████████████████████████████████")


    elif lives == 3:
        print("          ██████████████████████")
        print("          @                ██  █")
        print("          @                  ███")
        print("        @@@@@                  █")
        print("       @     @                 █")
        print("       @)   (@                 █")
        print("          @                    █")
        print("        ,@@@,                  █")
        print("       @  @                    █")
        print("     .@   @                    █")
        print("          @                    █")
        print("          @                    █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("████████████████████████████████")


    elif lives == 2:
        print("          ██████████████████████")
        print("          @                ██  █")
        print("          @                  ███")
        print("        @@@@@                  █")
        print("       @     @                 █")
        print("       @)   (@                 █")
        print("          @                    █")
        print("        ,@@@,                  █")
        print("       @  @  @                 █")
        print("     .@   @   @.               █")
        print("          @                    █")
        print("          @                    █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("                               █")
        print("████████████████████████████████")


    elif lives == 1:
        print("          ██████████████████████")
        print("          @                ██  █")
        print("          @                  ███")
        print("        @@@@@                  █")
        print("       @     @                 █")
        print("       @)   (@                 █")
        print("          @                    █")
        print("        ,@@@,                  █")
        print("       @  @  @                 █")
        print("     .@   @   @.               █")
        print("          @                    █")
        print("         @@@                   █")
        print("        @                      █")
        print("       @                       █")
        print("                               █")
        print("                               █")
        print("████████████████████████████████")


    elif lives == 0:
        print("          ██████████████████████")
        print("          @                ██  █")
        print("          @                  ███")
        print("        @@@@@                  █")
        print("       @     @                 █")
        print("       @)   (@                 █")
        print("          @                    █")
        print("        ,@@@,                  █")
        print("       @  @  @                 █")
        print("     .@   @   @.               █")
        print("          @                    █")
        print("         @@@                   █")
        print("        @   @                  █")
        print("       @     @                 █")
        print("                               █")
        print("                               █")
        print("████████████████████████████████")