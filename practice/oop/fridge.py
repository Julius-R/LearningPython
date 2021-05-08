class Fridge:
    def __init__(self, owner, id):
        self.owner = owner
        self.id = id
    
    items = list()
    allowed_inspectors = list()
    
    def show_fridge_details(self):
        print(f'Id: {self.id} Number of items: {self.items} Owner: {self.owner}')
    
    def add_inspector(self, inspector):
        self.allowed_inspectors.append(inspector)
        print(f'Inspector: {inspector}, has been given priveleges to view this fridge.')
    
    def remove_inspector(self, inspector):
        self.allowed_inspectors.remove(inspector)
        print(f'Inspector: {inspector}, has been removed.')
        
    def display_items(self):
        for item in self.items:
            print(item)
    
    def add_item(self, item):
        if len(self.items) == 5:
            choice = input("Fridge is full! Would you like to remove an item? y/n")
            if choice == "y":
                print("Please select item to remove")
                self.display_items()
                item_to_remove = input('Enter choice')
                self.remove_item(item_to_remove)
                self.items.append(item)
            else:
                print("Very well, item will not be added!")
        else:
            self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)