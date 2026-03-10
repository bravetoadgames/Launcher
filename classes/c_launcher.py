import os

class Launcher:
    
    apps = [
                # Internet
                ['red', 'Brave', 'brave-browser', 1],
                ['red', 'Chrome', 'google-chrome', 1],
                ['red', 'FileZilla', 'filezilla', 1],
                ['red', 'Firefox', 'firefox', 1],
                ['red', 'Soulseek', '~/soulseek.sh', 1],
                ['red', 'SyncTerm', 'syncterm', 1],
                
                # Emulators
                ['green', 'Altirra', '~/altirra.sh', 1],
                ['green', 'Atari 800XL', 'atari800', 1],
                ['green', 'Commodore 64', 'flatpak run net.sf.VICE', 1],
                ['green', 'Commodore Amiga', 'flatpak run com.blitterstudio.amiberry', 1],
                ['green', 'Dosbox', 'dosbox', 1],

                # Programming
                ['blue', 'GitKraken', 'gitkraken', 1],
                ['blue', 'Godot engine', '~/godot.sh', 1],
                ['blue', 'Pico-8', '~/pico.sh', 1],
                ['blue','Planify', 'flatpak run io.github.alainm23.planify', 1],
                ['blue', 'Spyder', 'spyder', 1],
                ['blue', 'Unity hub', 'unityhub', 1],

                # Editing tools
                ['yellow', 'Aseprite', '~/.steam/steam/steamapps/common/Aseprite/aseprite', 1],
                ['yellow', 'Audacity', 'audacity', 1],
                ['yellow', 'Blender', 'blender', 1],
                ['yellow', 'Krita','krita', 1],
                ['yellow', 'MagicaVoxel', '~/magicavoxel.sh', 1],
                ['yellow', 'Milkytracker', 'milkytracker', 1],
                ['yellow', 'OBS video recording','obs', 1],
                ['yellow', 'Openshot video', 'openshot-qt', 1],
                ['yellow', 'VCV Rack 2', '~/rack.sh', 1],

                # Media 
                ['cyan', 'MOC mediaplayer', 'gnome-terminal -- mocp', 0],
                ['cyan', 'Shortwave radio', 'shortwave', 1],
                ['cyan', 'Spotify', 'spotify', 1],
                ['cyan', 'Strawberry', 'strawberry', 1],
                ['cyan', 'VLC player', 'vlc', 1],
                
                # Games
                ['purple', 'DCSS', '~/dcss.sh', 1],
                ['purple', 'Open TTD', 'openttd', 1],
                ['purple', 'Palapeli', 'palapeli', 1],
                ['purple', 'Poker TH', 'pokerth', 1],
                ['purple', 'RPG in a Box', '~/.steam/steam/steamapps/common/RPG\ in\ a\ Box/rpginabox', 1],
                ['purple', 'Rolling line', 'wine ~/.steam/steam/steamapps/common/Rolling\ Line/RollingLine.exe', 1],
                ['purple', 'Songs of Syx', '~/.steam/steam/steamapps/common/Songs\ of\ Syx/songsofsyx', 1],
                ['purple', 'Sophie\'s dice', '~/.steam/steam/steamapps/common/Sophies\ Dice/Sophies\ Dice.x86_64', 1],
                ['purple', 'Sudoku', 'gnome-terminal -- sudoku', 0],
                ['purple', 'Transport Fever 2', '~/tf2.sh', 1],
                ['purple', 'Ultimate Racing 2D', 'wine ~/.steam/steam/steamapps/common/Ultimate\ Racing\ 2D/Ultimate_Racing_2D.exe', 1],
                
                # Gaming portals
                ['red', 'Heroic launcher', 'flatpak run com.heroicgameslauncher.hgl', 1],
                ['red', 'Steam', 'steam', 1],
                
                # Utilities
                ['green', 'Baobab disk analyzer', 'baobab', 1],
                ['green', 'BpyTop sysmon', 'gnome-terminal -- bpytop', 0],
                ['green', 'GcStar database', 'gcstar', 1],
                ['green', 'Gnome terminal', 'gnome-terminal --working-directory=~/', 1],
                ['green', 'KeePass', 'keepass2', 1],
                ['green', 'Puddletag', 'puddletag', 1],
                ['green', 'Settings', 'gnome-control-center', 1],
                ['green', 'Terminator', 'terminator --working-directory=~/', 1],

                # Other tools
                ['blue', 'Cool retro term', 'cool-retro-term', 1],
                ['blue', 'Matrix fx', 'gnome-terminal -- cmatrix', 0],
                ['blue', 'VM setup', 'gnome-terminal -- ~/Ctools/vm.sh', 0],
                ['blue', 'VirtualBox', 'virtualbox', 1],

                # AI tools
                ['yellow', 'AI model Dee', 'gnome-terminal -- ~/./aiDee.sh', 0],
                ['yellow', 'AI model Gemma3:1b', 'gnome-terminal -- ~/./aiGemma31b.sh', 0],
                ['yellow', 'AI model Gemma3:4b', 'gnome-terminal -- ~/./aiGemma34b.sh', 0],
                ['yellow', 'AI model Mistral', 'gnome-terminal -- ~/./aiMistral.sh', 0],
                ['yellow', 'AI model Simone', 'gnome-terminal -- ~/./aiSimone.sh', 0],

                # Office tools
                ['cyan', 'Calculator', 'gnome-calculator', 1],
                ['cyan', 'LibreOffice Calc', 'localc', 1],
                ['cyan', 'LibreOffice Writer', 'lowriter', 1],
           ]

    menu_key = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B',
                'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']           




    # ----------------------------------------------------------------------
    # Initialize Launcher class
    # ----------------------------------------------------------------------
    def __init__(self):
        
        # Define instance variables
        self.current_page = 0
        self.launcher_exit = False
        self.menu_items = []
        self.offset_x = 0
        self.offset_y = 8
        self.page = 0
        self.per_page = 32
        self.total_pages = 0

        # Determine the number of pages in the menu
        pages = len(self.apps) / 33
        if pages > int(pages):
            pages = int(pages) + 1

        self.total_pages = int(pages - 1)
        self.setCurrentPage()
        


    # ----------------------------------------------------------------------
    # Print a dashed line
    # ----------------------------------------------------------------------
    def showLine(self):
        return '═' * 79



    # ----------------------------------------------------------------------
    # Print all menu items on screen
    # ----------------------------------------------------------------------
    def showMenu(self):
        x = self.offset_x
        y = self.offset_y

        os.system('clear')
        self.showTitle()

        for i, item in enumerate(self.menu_items):
            menu_line = self.setColor('white')
            menu_line += item[4]
            menu_line += ' - ' + self.setColor(item[0]) + item[1]
            menu_line += self.setColor('reset')
            self.showPositionalPrint(x, y, menu_line)

            y = y + 1

            if y > self.offset_y + 10:
                y = self.offset_y
                if x == 0:
                    x = 27
                elif x == 27:
                    x = 54

        self.showPositionalPrint(0, 20, self.showLine())
        print(self.setColor('red') + 'Q - Quit' + self.setColor('reset'))
        
        if self.total_pages > 0:
            self.showPositionalPrint(20, 21, 'Previous page [,] - Next page [.] ')
            self.showPositionalPrint(67, 21, 'Page ' + str(self.current_page + 1) + ' of ' + str(self.total_pages + 1))

        self.showPositionalPrint(0, 22, self.showLine())



    # ----------------------------------------------------------------------
    # Positional print
    # ----------------------------------------------------------------------
    def showPositionalPrint(self, x, y, text):
        print(f"\033[{y};{x}H{text}")



    # ----------------------------------------------------------------------
    # Display a title text
    # ----------------------------------------------------------------------
    def showTitle(self):
        print(self.showLine())
        print('                   -----------------------------------')
        print(self.setColor('blue') + '                   L I N U X   L A U N C H E R   1 . 2')
        print('                   -----------------------------------' + self.setColor('reset'))
        print(self.showLine())



    # ----------------------------------------------------------------------
    # Wait for user input and launch if input was given
    # ----------------------------------------------------------------------
    def getUserInput(self):
        i = input('>> ')
        i = i.upper()

        if i != "":
            if i == "Q":
                os.system('clear')
                self.launcher_exit = True
            elif i == ".":
                self.current_page += 1
                if self.current_page > self.total_pages:
                    self.current_page = 0
                self.setCurrentPage()
            elif i == ",":
                self.current_page -= 1
                if self.current_page < 0:
                    self.current_page = self.total_pages
                self.setCurrentPage()
            else:
                self.setApplication(i)



    # ----------------------------------------------------------------------
    # Launch a selected program
    # ----------------------------------------------------------------------
    def setApplication(self, input_value):
        for i, item in enumerate(self.menu_items):
            if item[4] == input_value:
                os.system('clear')
                if item[3] == 1:
                    os.system('nohup ' + item[2] + ' > /dev/null 2>&1 &')
                else:
                    os.system(item[2])
                break



    def setColor(self, cl):
        """
        -------------------------------------------------
        Return a colorcode to print
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



    # ----------------------------------------------------------------------
    # Adopt the menu items for the current active page
    # ----------------------------------------------------------------------
    def setCurrentPage(self):
        # Clean up the menu item array for current page
        self.menu_items.clear()

        # Build menu_items array from apps array, starting from offset
        for i, app in enumerate(self.apps, start = self.current_page + (self.per_page * self.current_page)):

            # clone the menu item from the apps array
            if i < len(self.apps):
                self.menu_items.append(self.apps[i])
            
            # Check if pointer exceeds the items for the current page
            if i >= (self.current_page * self.per_page + self.per_page):
                break

        self.setMenuKeys()


    # ----------------------------------------------------------------------
    # Assign menu keys to current page
    # ----------------------------------------------------------------------
    def setMenuKeys(self):
        for i, item in enumerate(self.menu_items):
            if i < len(self.menu_key):
                if len(self.menu_items[i]) <= 4:
                    self.menu_items[i].append(self.menu_key[i])
                else:
                    self.menu_items[i][4] = self.menu_key[i]




