class Chef:
    def make_chicken(self):
        print("This chef makes chicken")
    def make_salad(self):
        print("This chef makes salad")
    def make_special_dish(self):
        print("This chef makes fried chicken")

class IndianChef(Chef):
    def make_special_dish(self):
        print("This chef makes chicken tikka masala")
    def make_biryani(self):
        print("this chef makes biryani")

