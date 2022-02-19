
def subscribers(arr, day):
    time = ['12 am', '1 am', '2 am', '3 am', '4 am', '5 am', '6 am', '7 am', '8 am', '9 am', '10 am', '11 am', '12 noon', '13 pm', '14 pm', '15 pm', '16 pm', '17 pm', '18 pm', '19 pm', '20 pm', '21 pm', '22 pm', '23 pm']
    update = {}
    query = {}
    count = 0

    while True:
        update[time[count]] = arr[count]
        if count == 23:
            query[day] = sum(arr)
            for key, value in query.items():
                print('day',key,':',value,'Subscribers')
            for key, value  in update.items():
                print(key, value, 'subscribers')
            day += 1
            break

        count+=1 
    

if __name__=='__main__':
    day_one = [20, 5, 2, 4, 5, 6, 7, 2, 1, 6, 30, 70, 800, 453, 711, 432, 23, 20, 65, 43, 12, 20, 40, 56]
    day_two = [29, 71, 22, 98, 29, 30, 90, 32, 20, 54, 32, 55, 102, 7, 9, 300, 13, 100, 650, 21, 20, 32, 34, 60]
    days_data = [day_one, day_two]
    count_days = 0
    day = 1

    while count_days < len(days_data):
        subscribers(days_data[count_days], day)
        day += 1
        option = input(f"Check Next Day {day} Subscribers: ")
        if option == "yes":
            pass
        else:
            break
        count_days += 1

        


