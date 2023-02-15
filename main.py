ticket = 500
price = 1000
while ticket > 0:
    howmuchtic = int(input("Сколько билетов желаете купить?")) 
    if howmuchtic > ticket:
        print("Такое количество недоступно. В продаже осталось", ticket, "билетов.")
    elif howmuchtic <= ticket:
        ticket -= howmuchtic
        print("Продано", howmuchtic, "билетов. Стоимость:", howmuchtic * price, "рублей.")
        

print("Все билеты проданы!")
