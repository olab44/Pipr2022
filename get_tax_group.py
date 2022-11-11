def get_tax_group(name):
    if name in tax_groupA:
        return 'A'
    elif name in tax_groupB:
        return 'B'
    elif name in tax_groupC:
        return 'C'
    elif name in tax_groupD:
        return 'D'
    else:
        return 'E'


tax_groupA = {'milk', 'bread'}
tax_groupB = {'fruits', 'vegetables'}
tax_groupC = {'water', 'juice'}
tax_groupD = {'phone', 'headphones'}

print(get_tax_group('beer'))
