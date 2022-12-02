'''
Разнесите классы, которые использовали при решении задачи о группе студентов (задания прошлой лекции) по модулям.
Убедитесь в работоспособности прооекта.
'''
import module_a
import module_b

class TooMuch(Exception):
    def __init__(self, list):
        super().__init__()
        self.list = list
    def __str__(self):
        return "Your group is too big."

one_human = module_a.Student("Alexei", "Arcanist", "M", 18, "tolerant", 4.2)
two_human = module_a.Student("Olga", "Sebrenkova", "W", 18, "bad", 4.2)
three_human = module_a.Student("Vlodimir", "Penkov", "M", "19", "good", 3.7)

ITIP = module_b.Group(21, 2, "KHNURE")

ITIP.plus_s(one_human)
ITIP.plus_s(three_human)
ITIP.plus_s(two_human)

for i in range(1, 10):
    try:
        ITIP.plus_s(two_human)
        if ITIP.l_list() >= 10:
            raise TooMuch(list)
    except TooMuch as err:
        print("Your group is too big.")
        ITIP.cross_s(two_human)

print(ITIP)