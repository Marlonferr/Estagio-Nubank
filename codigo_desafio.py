def add_task(task1):
    date1 = {}
    value = input("value of task add digite add?").lower
    for i in task1:
        date1 = i["update"]
        date1 = i["add"]
        date1 = i["retrieve"]
        if "add" in value:
            add_1 = input("digite um valor")
            int(add_1)
            date1 = [add_1]
        else:
            None
def update_task(task2):
    date2 = {}
    value2 = input("value of task update?")
    for i in task2:
        date2 = i["update"]
        date2 = i["add"]
        date2 = i["retrieve"]
        if "add" in value2:
            add_2 = input("digite um valor")
            int(add_2)
            date1 = [add_2]
        else:
            None
def retrieve_task(task3):
    date3 = {}
    value3 = input("value of task update?")
    for i in task3:
        date2 = i["update"]
        date2 = i["add"]
        date2 = i["retrieve"]
        if "add" in value3:
            add_3 = input("digite um valor")
            int(add_3)
            date1 = [add_3]
        else:
            None
            
add_task()