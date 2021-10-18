

def overwrite_list_elements():
    arr = [0, 1, 1, 1, 1, 0, 0, 0]
    insert = [2, 2, 2, 2]
    insert_pointer = 1
    result = [
        *arr[:insert_pointer],
        *insert,
        *arr[insert_pointer+len(insert):]
    ]
    assert len(arr) == len(result), 'Improper insert operation'
    print(result)


if __name__ == '__main__':
    overwrite_list_elements()
