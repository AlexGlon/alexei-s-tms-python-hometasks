import file_processing



# в вашей программе должно быть реализовано следующее
# TODO: при работе программы персонажи должны быть представлены объектами класса Character с необходимым набором аттрибутов (то есть вам необходимо перевести список словарей о персонажах в объекты класса Character: List[Dict] -> List[Character])

# пример перевода словаря в объект
character = {
    'name': 'Rick',
    'species': 'Human',
}


class Character:
    def __init__(self, name, species):
        self.name = name
        self.species = species


rick = Character(name=character['name'], species=character['species'])


# url response print
print(file_processing.list_load())


# 4*. реализуйте класс Aggregator, который аттрибутом принимает список объектов персонажей и, на основании списка всех персонажей, может вывести на экран саггрегированную информацию:
# подсказка: возможно, вам потребуется еще один класс, который запрос с клавиатуры конвертирует в объект запроса
#
# возможность получить кол-во персонажей по каждому признаку (ключу), указанному выше
# >>> show status alive
# >>> выводит на экран кол-во живых персонажей
#
# >>> show species human
# >>> выводит кол-во людей
#
# возможность вывести на экран общую аггрегацию по признаку
# >>> show status
# >>> Alive 100
# >>> unknown 37
# ...
#
# >>> show location
# >>> Citadel of Ricks 19
# >>> Earth (Replacement Dimension) 33
# ...
#
