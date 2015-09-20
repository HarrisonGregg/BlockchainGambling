def hash_credit_card(credit_number, filename):
    f = open(filename,'r')
    table = []
    for line in f:
        table.append(line.strip('\n'))
    index = int(credit_number[-5:])
    print(table[index%len(table)])
    return table[index%len(table)]
if __name__ == '__main__':
	hash_credit_card('12309128','./account_list.txt')