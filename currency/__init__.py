def comma(number, group_size=3):
    number_str = str(number)
    if '.' in number_str:
        int_part, frac_part = number_str.split('.')
    else:
        int_part, frac_part = number_str, None

    if int_part[0] == '-':
        sign = '-'
        int_part = int_part[1:]
    else:
        sign = ''

    if len(int_part) <= group_size:
        int_part_with_commas = int_part
    else:
        groups = []
        for i in range(len(int_part), 0, -group_size):
            group = int_part[max(0, i-group_size):i]
            groups.insert(0, group)
        int_part_with_commas = ','.join(groups)
    
    result = sign + int_part_with_commas
    
    if frac_part is not None:
        result += '.' + frac_part

    return result
