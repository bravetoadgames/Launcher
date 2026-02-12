"""
Zo dan
"""
import os

class Launcher:
    """
    -------------------------------------------------
    
    -------------------------------------------------
    """

    header_height = 9
    launcher_exit = False
    page = 0
    current_page = 0
    
    apps = [
                ['BpyTop sysmon', 'bpytop', 0],
                ['MOC mediaplayer', 'mocp', 0],
                ['Pico-8', '~/pico.sh', 1],
                ['Atari 800XL', 'atari800', 1],
                ['Commodore 64', 'flatpak run net.sf.VICE', 1],
                ['Commodore Amiga', 'flatpak run com.blitterstudio.amiberry', 1],
                ['Openshot video', 'openshot-qt', 1],
                ['OBS video recording','obs', 1],
                ['LibreOffice Writer', 'lowriter', 1],
                ['LibreOffice Calc', 'localc', 1],
                ['GcStar database', 'gcstar', 1],
                ['VirtualBox', 'virtualbox', 1],
                ['KeePass', 'keepass2', 1],
                ['VM setup', '~/Ctools/vm.sh', 0],
                ['Poker TH', 'pokerth', 1],
                ['GitKraken', 'gitkraken', 1],
                ['Spotify', 'spotify', 1],
                ['Shortwave radio', 'shortwave', 1],
                ['Dosbox', 'dosbox', 1],
                ['Greed', 'greed', 0],
                ['Sudoku', 'sudoku', 0],
                ['Krita','krita', 1],
                ['Disk analyzer', 'baobab', 1],
                ['Blender', 'blender', 1],
                ['DCSS', '~/dcss.sh', 1],
                ['VCV Rack 2', '~/rack.sh', 1],
                ['Soulseek', '~/soulseek.sh', 1],
                ['Chrome', 'google-chrome', 1],
                ['MagicaVoxel', '~/magicavoxel.sh', 1],
                ['Altirra', '~/altirra.sh', 1],
                ['Audacity', 'audacity', 1],
                ['Brave', 'brave-browser', 1],
                ['Firefox', 'firefox', 1],
                ['Spyder', 'spyder', 1],
                ['VLC player', 'vlc', 1]
           ]

    menu_key = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B',
                'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']           

    menu_item = []



    def __init__(self):
        """
        -------------------------------------------------
        Initialize Launcher class
        -------------------------------------------------
        """
        self.apps.sort()
        self.current_page = 0
        self.set_current_page()
        
        self.assign_menu_keys()
        
        # Determine the number of pages in the menu
        pages = len(self.apps) / 33
        if pages > int(pages):
            pages = int(pages) + 1
        
        self.pages = int(pages - 1)
        



    def set_current_page(self):
        """
        -------------------------------------------------
        Adopt the menu items for the current active page
        -------------------------------------------------
        Returns
        -------
        None.

        """
        # Clean up the menu item array for current page
        self.menu_item = []
        
        for i, app in enumerate(self.apps, start = self.current_page * 32):
            
            # clone the menu item from the apps array
            self.menu_item.append(app)
            
            # Check if pointer exceeds the items for the current page
            if i >= (len(self.apps) + ((self.current_page * 32) + 32)):
                break
            
        # Debug data
        print('elements processed: ' + str(i))
        print(self.menu_item)
        #exit()



    def assign_menu_keys(self):
        """
        -------------------------------------------------
        Assign menu keys to current page
        -------------------------------------------------
        Returns
        -------
        None.

        """
        for i, app in enumerate(self.apps):
            self.apps[i].append(self.menu_key[i])



    def print_menu(self):
        """
        -------------------------------------------------
        
        -------------------------------------------------
        Returns
        -------
        None.

        """
        x = 0
        y = self.header_height

        os.system('clear')
        self.print_title()

        for i, app in enumerate(self.apps):
            menu_line = self.set_color('green')
            menu_line += app[3]
            menu_line += ' - ' + app[0]
            menu_line += self.set_color('reset')
            self.print_pos(x, y, menu_line)

            y = y + 1

            if y > self.header_height + 10:
                y = self.header_height
                if x == 0:
                    x = 27
                elif x == 27:
                    x = 54

        self.print_pos(0, 20, self.print_line())
        print(self.set_color('red') + 'Q - Quit' + self.set_color('reset'))
        if self.pages > 0:
            self.print_pos(20, 21, 'Previous page [,] - Next page [.] ')
            self.print_pos(67, 21, 'Page ' + str(self.current_page + 1) + ' of ' + str(self.pages + 1))
        self.print_pos(0, 22, self.print_line())



    def print_line(self):
        """
        -------------------------------------------------
        Print a dashed line
        -------------------------------------------------
        """
        return '═' * 79



    def launch(self, input_value):
        """
        -------------------------------------------------
        
        -------------------------------------------------
        Parameters
        ----------
        input_value : Key pressed by user

        Returns
        -------
        None.

        """
        for i, app in enumerate(self.apps):
            if app[3] == input_value:
                os.system('clear')
                if app[2] == 1:
                    os.system('nohup ' + app[1] + ' > /dev/null 2>&1 &')
                else:
                    os.system(app[1])
                break



    def user_input(self):
        """
        -------------------------------------------------
        Wait for user input and launch if input was given
        -------------------------------------------------
        """
        i = input('>> ')
        i = i.upper()

        if i != "":
            if i == "Q":
                os.system('clear')
                self.launcher_exit = True
            else:
                self.launch(i)



    def print_title(self):
        """
        -------------------------------------------------
        Display a title text
        -------------------------------------------------
        """
        print(self.print_line())
        print(self.set_color('blue') + '      ██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗██████╗ ')
        print('      ██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔══██╗')
        print('      ██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██████╔╝')
        print('      ██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██╔══██╗')
        print('      ███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║')
        print('      ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝' + self.set_color('reset'))
        print(self.print_line())



    # ---------------------------------------------------
    # Return a colorcode to print
    # ---------------------------------------------------
    def set_color(self, cl):
        """
        -------------------------------------------------
        Set color
        -------------------------------------------------
        """

        escape_color = ""
        if cl == 'grey':
            escape_color = '\033[90m'
        if cl == 'red':
            escape_color = '\033[91m'
        if cl == 'green':
            escape_color = '\033[92m'
        if cl == 'yellow':
            escape_color = '\033[93m'
        if cl == 'blue':
            escape_color = '\033[94m'
        if cl == 'purple':
            escape_color = '\033[95m'
        if cl == 'cyan':
            escape_color = '\033[96m'
        if cl == 'white':
            escape_color = '\033[97m'
        if cl == 'reset':
            escape_color = '\033[0m'
        if cl == 'bold':
            escape_color = '\033[1m'
        if cl == 'underline':
            escape_color = '\033[4m'

        return escape_color



    # ---------------------------------------------------
    # Print on an X / Y position on-screen
    # ---------------------------------------------------
    def print_pos(self, x, y, text):
        """
        -------------------------------------------------
        Positional print
        -------------------------------------------------
        """
        print(f"\033[{y};{x}H{text}")
