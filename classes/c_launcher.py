import os
import ast

class Launcher:
    
    apps = []

    menu_key = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B',
                'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']           



    # ----------------------------------------------------------------------
    # Initialize Launcher class
    # ----------------------------------------------------------------------
    def __init__(self):
        # Read datafile
        self.readData()
        
        # Define instance variables
        self.current_page = 0
        self.launcher_exit = False
        self.menu_items = []
        self.offset_x = 0
        self.offset_y = 8
        self.page = 0
        self.per_page = 33
        self.total_pages = 0

        # Determine the number of pages in the menu
        self.setPageCount()
        
        # Fill the current page with items
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
        print(self.setColor('blue') + '                   L I N U X   L A U N C H E R   1 . 3')
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


    def readData(self):
        with open('data/programs.dat', 'r') as file:
            for line in file:
                line = line.strip()
                # Remove the outer brackets and split by comma
                inner = line[1:-1]
                # Parse individual elements
                items = []
                for item in inner.split(','):
                    item = item.strip().strip("'\"")
                    # Convert numbers
                    if item.isdigit():
                        items.append(int(item))
                    else:
                        try:
                            items.append(float(item))
                        except ValueError:
                            items.append(item)
                self.apps.append(items)
        
        
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
        for i, app in enumerate(self.apps, start = (self.per_page * self.current_page)):
        
            # clone the menu item from the apps array
            if i < len(self.apps):
                self.menu_items.append(self.apps[i])

            # Check if pointer exceeds the items for the current page
            if i == (self.current_page * self.per_page + self.per_page - 1):
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



    # ----------------------------------------------------------------------
    # Determine the needed amount of pages
    # ----------------------------------------------------------------------
    def setPageCount(self):
        pages = (len(self.apps)+1) / 33
        if pages > int(pages):
            pages = int(pages) + 1

        self.total_pages = int(pages - 1)
