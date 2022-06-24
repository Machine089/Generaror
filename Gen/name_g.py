from random import choice

names = ["Alexandr", "Alexey", "Anatoliy", "Artem",
         "Vadim", "Victor", "Vladislav", "Grigory",
         "Denis", "Kirill", "Lev", "Leonid",
         "Maksim", "Miron", "Oleg", "Roman",
         "Semyon", "Sergey", "Stanislav", "Stepan",
         "Yuri", "Yakov", "Thomas", "Konstantin",
         "James", "John", "Sean", "Rick",
         "Robert", "Kevin", "Paul", "Pavel",
         "Jacob", "Fedor", "Ilya", "Arthur", "Bob"]

surnames = ["Parker", "Ivanov", "Palmer", "Mern",
            "Black", "White", "Rogers", "Owen",
            "Keller", "Johnson", "Jones", "Robson",
            "Roser", "Clinton", "Ma", "Ford"]


def gen_unique_names(names, surnames, how_many: int):
    answer = []
    while how_many > 0:
        combo = choice(names) + ' ' + choice(surnames)
        if combo not in answer:
            answer.append(combo)
            how_many -= 1

        return combo
