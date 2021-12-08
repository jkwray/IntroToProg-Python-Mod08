# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# JWray,12.05.21,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JWray,12.05.2021,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = '%.2f' % float(product_price)

    # -- Properties --
    # Product Name
    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, value):
        self.__product_name = value

    # Product Price
    @property
    def product_price(self):
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        self.__product_price = value

    # -- Methods --
    def __str__(self):
        return self.product_name + ', ' + self.product_price


# End Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JWray,12.05.2021,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :return: (list) of dictionary rows
        """

        rows = []
        file = open(file_name, "r")
        for line in file:
            product_name, product_price = line.split(",")
            p = Product(product_name.strip(), float(product_price.strip(), ))
            rows.append(p)
        file.close()
        return rows

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Adds new item to list of dictionary rows

                :param file_name: (string) with name of file:
                :param list_of_product_objects: (list) you want to write to a file:
                """
        file = open(file_name, 'w')
        for row in list_of_product_objects:
            file.write(row.product_name + ', ' + row.product_price + '\n')
        file.close()
        print('Data has been saved!')


# End Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs Input and Output tasks:

        methods:
            output_menu() -> returns string to display menu
            input_menu_choice() -> allows user to input menu choice and returns it to main script
            output_current_product_list(list_of_rows) -> takes list of objects, formats, and prints them
            input_new_product() -> allows user to input new product and price and returns
                it as an object to be appended to the current list
        changelog: (When,Who,What)
            RRoot,1.1.2030,Created Class
            JWray,12.05.2021,Modified code to complete assignment 8
        """

    @staticmethod
    def output_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) View Current List of Products
            2) Add a Product
            3) Save Data to File & Exit
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_product_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display:
        :return: nothing
        """
        print()
        print("******* The product list is: *******")
        for row in list_of_rows:
            # print(row.product_name, "%.2f" % float(row.product_price), sep=', ')
            print(str(row))
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_product():
        """ Collects user input for saving a new task item to the list

                :param none
                :return: product: (Product) object to add to the list
                """
        # get product and price from user
        name = input('Please enter product name: ')
        price = input('Please enter price: ')
        p = Product(name, price)
        return p


# End Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

try:
    # Load data from file into a list of product objects when script starts
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while(True):
        # Show user a menu of options
        IO.output_menu()

        # Get user's menu option choice
        choice_str = IO.input_menu_choice()

        if choice_str.strip() == '1':  # Show current product list
            IO.output_current_product_list(lstOfProductObjects)
            continue

        elif choice_str == '2':  # Add new product to list
            new_product = IO.input_new_product()
            lstOfProductObjects.append(new_product)
            print('New product successfully added!')

            # print current product list to show new one added
            IO.output_current_product_list(lstOfProductObjects)
            continue

        elif choice_str == '3':  # Save data and exit
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            print('Good-bye!')
            break

        else:
            print('"', choice_str, '"', 'is not a valid menu choice.')
            print()
            continue

except Exception as e:
    print(e)
    print()

# End Main Body of Script  ---------------------------------------------------- #
