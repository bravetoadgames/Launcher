"""
    Launcher
    
    By:     Arjen Schumacher
    Date:   2026-02-11
"""


from classes.c_launcher import Launcher

launcher = Launcher()

while launcher.launcher_exit is False:
    launcher.print_menu()
    launcher.user_input()
