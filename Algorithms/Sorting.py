import time
import random

random_list = [random.uniform(1,10000) for i in range(5500)]
random_list.sort()
reversed_list = list(reversed(random_list))
sorted_list = random_list

def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
def selection(arr):
    for i in range(len(arr)):
        min1 = i
        for j in range(i+1,len(arr)):
            if arr[min1]>arr[j]:
                arr[min1],arr[j] = arr[j],arr[min1]
def insertion(arr):
    for i in range(len(arr)):
        j = i
        while j > 0:
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
choice = int(input("""1.Bubble
2.Selection
3.Insertion
4.Merge
5.Quick"""))
if choice==1:
    start = time.perf_counter()
    bubble(reversed_list)
    end = time.perf_counter()
    print("Bubble sort for reverse numbers:", end - start)

    start1 = time.perf_counter()
    bubble(random_list)
    end1 = time.perf_counter()
    print("Bubble sort for random numbers:",end1-start1)

    start2 = time.perf_counter()
    bubble(sorted_list)
    end2 = time.perf_counter()
    print("Bubble sort for sorted numbers:", end2 - start2)

elif choice==2:
    start = time.perf_counter()
    selection(reversed_list)
    end = time.perf_counter()
    print("Selection sort for reverse numbers:", end - start)

    start1 = time.perf_counter()
    selection(random_list)
    end1 = time.perf_counter()
    print("Selection sort for random numbers:",end1-start1)

    start2 = time.perf_counter()
    selection(sorted_list)
    end2 = time.perf_counter()
    print("Selection sort for sorted numbers:", end2 - start2)


elif choice==3:
    start = time.perf_counter()
    insertion(reversed_list)
    end = time.perf_counter()
    print("Insertion sort for reverse numbers:", end - start)

    start1 = time.perf_counter()
    insertion(random_list)
    end1 = time.perf_counter()
    print("Insertion sort for random numbers:",end1-start1)

    start2 = time.perf_counter()
    insertion(sorted_list)
    end2 = time.perf_counter()
    print("Insertion sort for sorted numbers:", end2 - start2)
else:
    print("Invalid choice")
