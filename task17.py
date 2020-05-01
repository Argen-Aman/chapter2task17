list1 = input('Type anything (words, numbers) to count how many times an item appears there. P.S. don\'t forget to put commas between them: ')
list1 = list1.split(', ')

def new_list (list1):
    print(list1.count(input('The item you want to count: ')))
new_list (list1)
