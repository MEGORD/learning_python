class Group:
    def __init__(self, year, course, university):
        self.year = year
        self.course = course
        self.university = university
        self.list = []

    def plus_s(self, student):
        self.list.append(student)

    def cross_s(self, student):
        self.list.remove(student)

    def searching(self, surname):
        flag = 0
        for element in self.list:
            if element.surname == surname:
                print(element)
                flag = 1
        if flag == 0:
            print("This student not in this group.")

    def l_list(self):
        return len(self.list)

    def __str__(self):
        n_list = []
        nr_list = ""
        for element in self.list:
            n_list = str(element)
            nr_list += n_list + '\n'
        return nr_list