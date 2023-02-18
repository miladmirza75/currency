def comma(number, group_size=3):
    number_str = str(number)
    groups = []
    for i in range(len(number_str), 0, -group_size):
        group = number_str[max(0, i-group_size):i]
        groups.insert(0, group)
    return ','.join(groups)
