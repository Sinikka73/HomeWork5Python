"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

with open("task2.txt", "r", encoding='utf-8') as a_obj:
    print("Количество строк в тексте: ", end="")
    print(f" sum(1 for line in a_obj))

"""
my_lst = ["Сутулится на стуле\n",
          "беспалое пальто.\n",
          "Потемки обманули,\n",
          "почудилось не то.\n"]
          
with open("task2.txt", "w", encoding='utf-8') as a_obj:
    a_obj.writelines(my_lst)

with open("task2.txt", "r", encoding='utf-8') as a_obj:
    content = a_obj.read()
    print(content)
    print(f"Количество слов в тексте: "
          f"{sum(len(x.split()) for x in content.split())}")
print()

with open("task2.txt", "r", encoding='utf-8') as a_obj:
    L = 0
    for i in a_obj:
        L += i.count("\n")
        print(f"Количество слов в {L} строке - {len(i.split())}")
    print()
    print(f"Количество строк в тексте:  {L}")
