def find_unique_delivery_id(delivery_ids):

    # Find the one unique ID in the list
    x = 0
    for i in delivery_ids:
        x ^= i

    return x