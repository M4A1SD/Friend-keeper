class MenuService:
    def __init__(self):
        self.menu = ["I have new entry", "Im free for action", "Add new friend"]
        self.friends = ["benny", "niko", "lior"]

    def display_menu(self):
        print(self.menu)
        return input("Enter your choice:\n")

    def display_friends(self):
        print(self.friends)
        return input("enter friend name:\n")

    def get_new_information(self):
        return input("enter new information:\n") 