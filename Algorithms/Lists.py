import time
reversed_list = []
random_list = []
sorted_list = []

reverse = open('data-reverse.txt','r+')
x = reverse.readlines()
for i in x:
    reversed_list.append(float(i))
reverse.close()


sorte = open('data-sorted.txt','r+')
y = sorte.readlines()
for i in y:
    sorted_list.append(float(i))
sorte.close()



random = open('data-random.txt','r+')
z = random.readlines()
for i in z:
    random_list.append(float(i))
random.close()


def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr            


def selection(arr):
    for i in range(len(arr)):
        min1 = i
        for j in range(i+1,len(arr)):
            if arr[min1]>arr[j]:
                arr[min1],arr[j] = arr[j],arr[min1]
    return arr



def insertion(arr):
    for i in range(len(arr)):
        j = i
        while j > 0:
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr       


choice = int(input("""1.Random Input
2.Reverse Input
3.Sorted Input\n"""))
if choice==1:
    start = time.perf_counter()
    bubble(random_list)
    end = time.perf_counter()
    
    start1 = time.perf_counter()
    selection(random_list)
    end1 = time.perf_counter()
    
    start2 = time.perf_counter()
    insertion(random_list)
    end2 = time.perf_counter()
    print("Bubble sort for random numbers:", end - start)
    print("Selection sort for random numbers:",end1-start1)

    print("Insertion sort for random numbers:", end2 - start2)

elif choice==2:
    start = time.perf_counter()
    bubble(reversed_list)
    end = time.perf_counter()
    print("Bubble sort for reverse numbers:", end - start)

    start1 = time.perf_counter()
    selection(reversed_list)
    end1 = time.perf_counter()
    print("Selection sort for reverse numbers:",end1-start1)

    start2 = time.perf_counter()
    insertion(reversed_list)
    end2 = time.perf_counter()
    print("Insertion sort for reverse numbers:", end2 - start2)


elif choice==3:
    start = time.perf_counter()
    print(bubble(sorted_list))
    end = time.perf_counter()
    
    start1 = time.perf_counter()
    print(selection(sorted_list))
    end1 = time.perf_counter()
    
    start2 = time.perf_counter()
    print(insertion(sorted_list))
    end2 = time.perf_counter()
    print("Bubble sort for sorted numbers:", end - start)
    print("Selection sort for sorted numbers:",end1-start1)

    print("Insertion sort for sorted numbers:", end2 - start2)
else:
    print("Invalid choice")
