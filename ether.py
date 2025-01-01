def create_list(filename, item):
    with open(filename, 'a') as fa:
        fa.write(item + '\n') 

    try:
        with open(filename, 'r') as fr:
            existing_items = [line.strip() for line in fr]
            randlst.extend(existing_items)
    except FileNotFoundError:
        print('file does not exist')