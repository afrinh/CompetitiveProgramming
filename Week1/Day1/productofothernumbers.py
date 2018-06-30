def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list) < 2:
        raise IndexError('Enter at least 2 numbers')

    product=[None]*len(int_list)
    prod=1
    for i in range(len(int_list)):
        product[i]=prod
        prod*=int_list[i]
    prod=1
    for i in range(len(int_list)-1,-1,-1):
        product[i]*=prod
        prod*=int_list[i]

    return product