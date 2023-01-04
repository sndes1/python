# Function to calculate price of a meeting room

# defining function
def get_price(duration_minute):
    if duration_minute < 60:  # price per minute
        a = int(duration_minute * 2)  # int to print an integer and not decimal number
        if a > 22:  # validation to use cheap rate
            return 22
        else:
            return a

    elif duration_minute < 1440:  # price per hour
        a = int(duration_minute / 60) * 22 # int to print an integer and not decimal number
        if a > 60:  # validation to use cheap rate
            return 60
        else:
            return a

    elif duration_minute < 10080:  # price per day
        a = int(duration_minute / 1440) * 60  # int to print an integer and not decimal number
        if a > 105:  # validation to use cheap rate
            return 105
        else:
            return a

    else:  # price per week
        return int(duration_minute / 10080) * 105


# testing function with given test cases

print(get_price(1440))
print(get_price(2880))
print(get_price(20160))
