"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
import math
phone_dict =   [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
def main():
  product_cnt = 0
  sell_cnt = 0
  print('что хотите сделать? \n 1) Посчитать и вывести суммарное количество продаж для каждого товара \n 2)Посчитать и вывести среднее количество продаж для каждого товара \n 3)Посчитать и вывести суммарное количество продаж всех товаров \n 4)Посчитать и вывести среднее количество продаж всех товаров')
  chose = int(input("Ваш выбор> "))
  if chose == 1:
    for product_cnt in phone_dict:
        month_counter = 0
        sum_product_sold = 0
        for sell_cnt in product_cnt['items_sold'] :
            sum_product_sold = sum_product_sold + sell_cnt
            month_counter = month_counter + 1
            if month_counter == (len(product_cnt['items_sold'])-1):
                print ('данный продукт был продан ',sum_product_sold, ' раз')
  elif chose == 2:
    for product_cnt in phone_dict:
          month_counter = 0
          sum_product_sold = 0
          for sell_cnt in product_cnt['items_sold'] :
              sum_product_sold = sum_product_sold + sell_cnt
              month_counter = month_counter + 1
              if month_counter == (len(product_cnt['items_sold'])-1):
                 sum_product_sold = sum_product_sold / month_counter
                 print ('данный продукт продавали в среднем ', math.ceil(sum_product_sold), ' раз')    
  elif chose == 3:
      month_counter = 0
      sum_product_sold = 0
      for product_cnt in phone_dict:
        for sell_cnt in product_cnt['items_sold'] :
            sum_product_sold = sum_product_sold + sell_cnt
            month_counter = month_counter + 1
            if month_counter == (3*(len(product_cnt['items_sold'])-1)):
                print ('Всего продуктов было продано ',sum_product_sold, ' раз')
  elif chose == 4:
        month_counter = 0
        sum_product_sold = 0
        for product_cnt in phone_dict:
          for sell_cnt in product_cnt['items_sold'] :
              sum_product_sold = sum_product_sold + sell_cnt
              month_counter = month_counter + 1
              if month_counter == (3*(len(product_cnt['items_sold'])-1)):
                  sum_product_sold = sum_product_sold / month_counter
                  print ('Всего продуктов было продано в среднем ',math.ceil(sum_product_sold), ' раз')

if __name__ == "__main__":
    main()
