"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
  string1 = input('введите первую строку> ')
  string2 = input('введите вторую строку> ')

  if type(string1) != 'string' or type (string2) != 'string':
    print('0')
  elif string1 == string2:
    print('1')
  elif len(string1)>len(string2) and string2 != 'learn':
    print('2')
  elif string2 == 'learn':
    print('3')
  
    
if __name__ == "__main__":
    main()
