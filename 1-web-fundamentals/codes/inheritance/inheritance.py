class Parent:
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name: {}".format(self.last_name))
        print("Eye color: {}".format(self.eye_color))


leo_messi = Parent("Messi", "Brown")


class Children(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Children constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last name: {}".format(self.last_name))
        print("Eye color: {}".format(self.eye_color))
        print("Number of toys: {}".format(self.number_of_toys))


mateo_messi = Children("Messi", "Brown", 10)
mateo_messi.show_info()
