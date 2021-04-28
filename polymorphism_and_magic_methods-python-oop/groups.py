class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f'{self.name} {self.surname}'


class Group:

    def __init__(self, name, people):
        self.name = name
        self.people = people

    @classmethod
    def create_new_group(cls, name, people):
        return cls(name, people)

    def get_name(self):
        return self.name

    def get_people(self):
        return self.people

    def __add__(self, other):
        name = self.get_name() + other.get_name()
        people = self.get_people() + other.get_people()
        return Group.create_new_group(name, people)

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item]}"

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        list_of_members = []
        for p in self.people:
            p_p = p
            list_of_members.append(str(p_p))

        return f"Group {self.name} with members {', '.join(list_of_members)}"

# Test code
# p0 = Person('Aliko', 'Dangote')
# p1 = Person('Bill', 'Gates')
# p2 = Person('Warren', 'Buffet')
# p3 = Person('Elon', 'Musk')
# p4 = p2 + p3
#
# first_group = Group('__VIP__', [p0, p1, p2])
# second_group = Group('Special', [p3, p4])
# third_group = first_group + second_group
#
# print(len(first_group))
# print(second_group)
# print(third_group[0])
#
# for person in third_group:
#     print(person)
