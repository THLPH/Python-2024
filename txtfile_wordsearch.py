file = open('words.txt', 'r')
words = file.read().splitlines()
print('Number of words read:', len(words))

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0
    
    while left <= right:
        mid = (left + right) // 2
        iterations += 1
        
        if target == arr[mid]:
            print(f"Target = {target}, Found at index = {mid}, Number of iterations = {iterations}")
            return
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    print(f"Target = {target}, Found at index: -1, Number of iterations = {iterations}")
    return


target = input('Enter search key: ').lower()

while target != 'exit':
    binary_search(words, target)
    target = input('Enter search key: ').lower()
