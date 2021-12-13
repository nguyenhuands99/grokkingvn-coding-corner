'''list of cake types: tuple(<mass in kg>, <price in shilling>)
capacity: maximum for carrying
ex:
    cake_tuples = [(7,160), (3,90), (2,15)]
    capacity = 20
    Output: 555 = 6 * 90 + 1 * 15 
'''
def stealing_cakes(cakes_tuple, capacity):
    '''
    find suitable kg (by get the max price per type), if kg > capacity, get the next-best, until kg < capacity
    then sum to total price by its type price
    '''
    cake_by_price_per_kg = sorted(cakes_tuple, key=lambda t: t[1]/t[0])  # O(nlogn)
    cake = cake_by_price_per_kg.pop() # O(1)
    kg_of_type = cake[0] 
    price = cake[1]
    total_price = 0

    while True:
        if kg_of_type > capacity:
            if len(cake_by_price_per_kg) == 0:
                break
            cake = cake_by_price_per_kg.pop()  # O(1) for n times
            kg_of_type = cake[0] 
            price = cake[1]
        else:
            total_price += price
            capacity -= kg_of_type
    return total_price  # O(n)

def dp_stealing_cakes(cakes, capacity):
    ''' Using dynamic programming (bai toan balo loai 1)
    1. at weight = 1, find max_price_at_capacity1 by traversing all cake weighing 1
    2. at weight = 2, fidn max_price_at_capacity2 by traversing all cake weighing 1 or 2
        2.1 if weight == 2:
            check if its price bigger than our current max_price_at_capacity2
        2.2 if weight == 1:
            check if its price + last max_price_at_capacity1 will be bigger than current max_price_at_capacity2 (bottom-up)
    .....
    ..... (go on)
    Naturally, we will see max_price_at_capacityi+1 will depend on max_price_at_capacityi, so we will create a array to store all max_price_at_capacity values (including capacity 0, to generalize the weight condition, no need to using if)
    '''
    max_price_at_capacity = [0] * (capacity + 1)

    for i in range(1, capacity + 1):
        max_price = 0
        for weight, price in cakes:
            if weight <= i:
                max_price = max(max_price, (price + max_price_at_capacity[i - weight]))
        max_price_at_capacity[i] = max_price

    return max_price_at_capacity[capacity]  # O(k*n): where k is capacity, n is length of type of cake

if __name__ == '__main__':
#    cakes = [(7, 160), (3,90), (2,15)]
#    capacity = 20
# This case works


    capacity = 10
    cakes = [(6, 50),(3, 18), (2, 10) ]  # this case didnot work as expected
    # it should be: 70 = 1 * 50 + 2 * 10, instead of 68 = 1 * 50 + 1 * 18
    # print(stealing_cakes(cakes, capacity))

    # Actually this problem need Dynamic Programming to solve
    print(dp_stealing_cakes(cakes, capacity))
