import time

def bubb(list):
    i = len(list)
    for j in range(i-1):
        for k in range(i-j-1):
            if (list[k] > list[k+1]):
                list[k], list[k+1] = list[k+1], list[k]
    return list

def selc(list):
    i = len(list)
    for j in range(i-1):
        min = j
        for k in range(j+1, i):
            if (list[k] < list[min]):
                min = k
        list[min], list[j] = list[j], list[min]
    return list

def ins(list):
    i = len(list)
    for j in range(1, i):
        temp = list[j]
        k = j-1;
        while k >= 0 and (list[k] > temp):
            list[k+1] = list[k]
            k -= 1
        list[k+1] = temp
    return list

a = int(input("1: Bubble, 2: Selection, 3: Insertion \n"))

if a == 1:
    fra10 = open("random10k.txt", "r")
    rand10 = []
    for line in fra10:
        rand10.append(line)
    fra10.close()
    t1 = time.perf_counter()
    rand10 = bubb(rand10)
    t2 = time.perf_counter()
    ra10 = t2-t1
    print("It takes {} for random 10k".format(ra10))

    fra20 = open("random20k.txt", "r")
    rand20 = []
    for line in fra20:
        rand20.append(line)
    fra20.close()
    t1 = time.perf_counter()
    rand20 = bubb(rand20)
    t2 = time.perf_counter()
    ra20 = t2 - t1
    print("It takes {} for random 20k".format(ra20))

    fra50 = open("random50k.txt", "r")
    rand50 = []
    for line in fra50:
        rand50.append(line)
    fra50.close()
    t1 = time.perf_counter()
    rand50 = bubb(rand50)
    t2 = time.perf_counter()
    ra50 = t2 - t1
    print("It takes {} for random 50k".format(ra50))

    fra100 = open("random100k.txt", "r")
    rand100 = []
    for line in fra100:
        rand100.append(line)
    fra100.close()
    t1 = time.perf_counter()
    rand100 = bubb(rand100)
    t2 = time.perf_counter()
    ra100 = t2 - t1
    print("It takes {} for random 100k".format(ra100))
    
    fso10 = open("sorted10k.txt", "r")
    sor10 = []
    for line in fso10:
        sor10.append(line)
    fso10.close()
    t1 = time.perf_counter()
    sor10 = bubb(sor10)
    t2 = time.perf_counter()
    s10 = t2 - t1
    print("It takes {} for sorted 10k".format(s10))

    fso20 = open("sorted20k.txt", "r")
    sor20 = []
    for line in fso20:
        sor20.append(line)
    fso20.close()
    t1 = time.perf_counter()
    sor20 = bubb(sor20)
    t2 = time.perf_counter()
    s20 = t2 - t1
    print("It takes {} for sorted 20k".format(s20))

    fso50 = open("sorted50k.txt", "r")
    sor50 = []
    for line in fso50:
        sor50.append(line)
    fso50.close()
    t1 = time.perf_counter()
    sor50 = bubb(sor50)
    t2 = time.perf_counter()
    s50 = t2 - t1
    print("It takes {} for sorted 50k".format(s50))

    fso100 = open("sorted100k.txt", "r")
    sor100 = []
    for line in fso100:
        sor100.append(line)
    fso100.close()
    t1 = time.perf_counter()
    sor100 = bubb(sor100)
    t2 = time.perf_counter()
    s100 = t2 - t1
    print("It takes {} for sorted 100k".format(s100))

    fre10 = open("reverse10k.txt", "r")
    rev10 = []
    for line in fre10:
        rev10.append(line)
    fre10.close()
    t1 = time.perf_counter()
    rev10 = bubb(rev10)
    t2 = time.perf_counter()
    re10 = t2 - t1
    print("It takes {} for reverse 10k".format(re10))

    fre20 = open("reverse20k.txt", "r")
    rev20 = []
    for line in fre20:
        rev20.append(line)
    fre20.close()
    t1 = time.perf_counter()
    rev20 = bubb(rev20)
    t2 = time.perf_counter()
    re20 = t2 - t1
    print("It takes {} for reverse 20k".format(re20))

    fre50 = open("reverse50k.txt", "r")
    rev50 = []
    for line in fre50:
        rev50.append(line)
    fre50.close()
    t1 = time.perf_counter()
    rev50 = bubb(rev50)
    t2 = time.perf_counter()
    re50 = t2 - t1
    print("It takes {} for reverse 50k".format(re50))

    fre100 = open("reverse100k.txt", "r")
    rev100 = []
    for line in fre100:
        rev100.append(line)
    fre100.close()
    t1 = time.perf_counter()
    rev100 = bubb(rev100)
    t2 = time.perf_counter()
    re100 = t2 - t1
    print("It takes {} for reverse 100k".format(re100))

    fp = open("Sorting1.txt", "a")
    fp.write("Bubble Sort\n\nType\t10k\t\t20k\t\t50k\t\t100k\nRandom\t")
    fp.write(str(round(ra10, 2)))
    fp.write("\t")
    fp.write(str(round(ra20, 2)))
    fp.write("\t")
    fp.write(str(round(ra50, 2)))
    fp.write("\t")
    fp.write(str(round(ra100, 2)))
    fp.write("\n")
    
    fp.write("Sorted\t")
    fp.write(str(round(s10, 2)))
    fp.write("\t")
    fp.write(str(round(s20, 2)))
    fp.write("\t")
    fp.write(str(round(s50, 2)))
    fp.write("\t")
    fp.write(str(round(s100, 2)))
    fp.write("\n")
    
    fp.write("Reverse\t")
    fp.write(str(round(re10, 2)))
    fp.write("\t")
    fp.write(str(round(re20, 2)))
    fp.write("\t")
    fp.write(str(round(re50, 2)))
    fp.write("\t")
    fp.write(str(round(re100, 2)))
    fp.write("\n")

    fp.close()

elif a == 2:
    fra10 = open("data-random.txt", "r")
    rand10 = []
    for line in fra10:
        rand10.append(line)
    fra10.close()
    t1 = time.perf_counter()
    rand10 = selc(rand10)
    t2 = time.perf_counter()
    ra10 = t2 - t1
    print("It takes {} for random 10k".format(ra10))

    fra20 = open("random20k.txt", "r")
    rand20 = []
    for line in fra20:
        rand20.append(line)
    fra20.close()
    t1 = time.perf_counter()
    rand20 = selc(rand20)
    t2 = time.perf_counter()
    ra20 = t2 - t1
    print("It takes {} for random 20k".format(ra20))

    fra50 = open("random50k.txt", "r")
    rand50 = []
    for line in fra50:
        rand50.append(line)
    fra50.close()
    t1 = time.perf_counter()
    rand50 = selc(rand50)
    t2 = time.perf_counter()
    ra50 = t2 - t1
    print("It takes {} for random 50k".format(ra50))

    fra100 = open("random100k.txt", "r")
    rand100 = []
    for line in fra100:
        rand100.append(line)
    fra100.close()
    t1 = time.perf_counter()
    rand100 = selc(rand100)
    t2 = time.perf_counter()
    ra100 = t2 - t1
    print("It takes {} for random 100k".format(ra100))

    fso10 = open("data-sorted.txt", "r")
    sor10 = []
    for line in fso10:
        sor10.append(line)
    fso10.close()
    t1 = time.perf_counter()
    sor10 = selc(sor10)
    t2 = time.perf_counter()
    s10 = t2 - t1
    print("It takes {} for sorted 10k".format(s10))

    fso20 = open("sorted20k.txt", "r")
    sor20 = []
    for line in fso20:
        sor20.append(line)
    fso20.close()
    t1 = time.perf_counter()
    sor20 = selc(sor20)
    t2 = time.perf_counter()
    s20 = t2 - t1
    print("It takes {} for sorted 20k".format(s20))

    fso50 = open("sorted50k.txt", "r")
    sor50 = []
    for line in fso50:
        sor50.append(line)
    fso50.close()
    t1 = time.perf_counter()
    sor50 = selc(sor50)
    t2 = time.perf_counter()
    s50 = t2 - t1
    print("It takes {} for sorted 50k".format(s50))

    fso100 = open("sorted100k.txt", "r")
    sor100 = []
    for line in fso100:
        sor100.append(line)
    fso100.close()
    t1 = time.perf_counter()
    sor100 = selc(sor100)
    t2 = time.perf_counter()
    s100 = t2 - t1
    print("It takes {} for sorted 100k".format(s100))
    
    fre10 = open("data-reverse.txt", "r")
    rev10 = []
    for line in fre10:
        rev10.append(line)
    fre10.close()
    t1 = time.perf_counter()
    rev10 = selc(rev10)
    t2 = time.perf_counter()
    re10 = t2 - t1
    print("It takes {} for reverse 10k".format(re10))

    fre20 = open("reverse20k.txt", "r")
    rev20 = []
    for line in fre20:
        rev20.append(line)
    fre20.close()
    t1 = time.perf_counter()
    rev20 = selc(rev20)
    t2 = time.perf_counter()
    re20 = t2 - t1
    print("It takes {} for reverse 20k".format(re20))

    fre50 = open("reverse50k.txt", "r")
    rev50 = []
    for line in fre50:
        rev50.append(line)
    fre50.close()
    t1 = time.perf_counter()
    rev50 = selc(rev50)
    t2 = time.perf_counter()
    re50 = t2 - t1
    print("It takes {} for reverse 50k".format(re50))

    fre100 = open("reverse100k.txt", "r")
    rev100 = []
    for line in fre100:
        rev100.append(line)
    fre100.close()
    t1 = time.perf_counter()
    rev100 = selc(rev100)
    t2 = time.perf_counter()
    re100 = t2 - t1
    print("It takes {} for reverse 100k".format(re100))

    fp = open("Sorting2.txt", "a")
    fp.write("Selection Sort\n\nType\t10k\t\t20k\t\t50k\t\t100k\nRandom\t")
    fp.write(str(round(ra10, 2)))
    fp.write("\t")
    fp.write(str(round(ra20, 2)))
    fp.write("\t")
    fp.write(str(round(ra50, 2)))
    fp.write("\t")
    fp.write(str(round(ra100, 2)))
    fp.write("\n")
    
    fp.write("Sorted\t")
    fp.write(str(round(s10, 2)))
    fp.write("\t")
    fp.write(str(round(s20, 2)))
    fp.write("\t")
    fp.write(str(round(s50, 2)))
    fp.write("\t")
    fp.write(str(round(s100, 2)))
    fp.write("\n")
    
    fp.write("Reverse\t")
    fp.write(str(round(re10, 2)))
    fp.write("\t")
    fp.write(str(round(re20, 2)))
    fp.write("\t")
    fp.write(str(round(re50, 2)))
    fp.write("\t")
    fp.write(str(round(re100, 2)))
    fp.write("\n")

    fp.close()

elif a == 3:
    fra10 = open("data-random.txt", "r")
    rand10 = []
    for line in fra10:
        rand10.append(line)
    fra10.close()
    t1 = time.perf_counter()
    rand10 = ins(rand10)
    t2 = time.perf_counter()
    ra10 = t2 - t1
    print("It takes {} for random 10k".format(ra10))

    fra20 = open("random20k.txt", "r")
    rand20 = []
    for line in fra20:
        rand20.append(line)
    fra20.close()
    t1 = time.perf_counter()
    rand20 = ins(rand20)
    t2 = time.perf_counter()
    ra20 = t2 - t1
    print("It takes {} for random 20k".format(ra20))

    fra50 = open("random50k.txt", "r")
    rand50 = []
    for line in fra50:
        rand50.append(line)
    fra50.close()
    t1 = time.perf_counter()
    rand50 = ins(rand50)
    t2 = time.perf_counter()
    ra50 = t2 - t1
    print("It takes {} for random 50k".format(ra50))

    fra100 = open("random100k.txt", "r")
    rand100 = []
    for line in fra100:
        rand100.append(line)
    fra100.close()
    t1 = time.perf_counter()
    rand100 = ins(rand100)
    t2 = time.perf_counter()
    ra100 = t2 - t1
    print("It takes {} for random 100k".format(ra100))
    
    fso10 = open("data-sorted.txt", "r")
    sor10 = []
    for line in fso10:
        sor10.append(line)
    fso10.close()
    t1 = time.perf_counter()
    sor10 = ins(sor10)
    t2 = time.perf_counter()
    s10 = t2 - t1
    print("It takes {} for sorted 10k".format(s10))

    fso20 = open("sorted20k.txt", "r")
    sor20 = []
    for line in fso20:
        sor20.append(line)
    fso20.close()
    t1 = time.perf_counter()
    sor20 = ins(sor20)
    t2 = time.perf_counter()
    s20 = t2 - t1
    print("It takes {} for sorted 20k".format(s20))

    fso50 = open("sorted50k.txt", "r")
    sor50 = []
    for line in fso50:
        sor50.append(line)
    fso50.close()
    t1 = time.perf_counter()
    sor50 = ins(sor50)
    t2 = time.perf_counter()
    s50 = t2 - t1
    print("It takes {} for sorted 50k".format(s50))

    fso100 = open("sorted100k.txt", "r")
    sor100 = []
    for line in fso100:
        sor100.append(line)
    fso100.close()
    t1 = time.perf_counter()
    sor100 = ins(sor100)
    t2 = time.perf_counter()
    s100 = t2 - t1
    print("It takes {} for sorted 100k".format(s100))

    fre10 = open("data-reverse.txt", "r")
    rev10 = []
    for line in fre10:
        rev10.append(line)
    fre10.close()
    t1 = time.perf_counter()
    rev10 = ins(rev10)
    t2 = time.perf_counter()
    re10 = t2 - t1
    print("It takes {} for reverse 10k".format(re10))

    fre20 = open("reverse20k.txt", "r")
    rev20 = []
    for line in fre20:
        rev20.append(line)
    fre20.close()
    t1 = time.perf_counter()
    rev20 = ins(rev20)
    t2 = time.perf_counter()
    re20 = t2 - t1
    print("It takes {} for reverse 20k".format(re20))

    fre50 = open("reverse50k.txt", "r")
    rev50 = []
    for line in fre50:
        rev50.append(line)
    fre50.close()
    t1 = time.perf_counter()
    rev50 = ins(rev50)
    t2 = time.perf_counter()
    re50 = t2 - t1
    print("It takes {} for reverse 50k".format(re50))

    fre100 = open("reverse100k.txt", "r")
    rev100 = []
    for line in fre100:
        rev100.append(line)
    fre100.close()
    t1 = time.perf_counter()
    rev100 = ins(rev100)
    t2 = time.perf_counter()
    re100 = t2 - t1
    print("It takes {} for reverse 100k".format(re100))

    fp = open("Sorting3.txt", "a")
    fp.write("Insertion Sort\n\nType\t10k\t\t20k\t\t50k\t\t100k\nRandom\t")
    fp.write(str(round(ra10, 2)))
    fp.write("\t")
    fp.write(str(round(ra20, 2)))
    fp.write("\t")
    fp.write(str(round(ra50, 2)))
    fp.write("\t")
    fp.write(str(round(ra100, 2)))
    fp.write("\n")
    
    fp.write("Sorted\t")
    fp.write(str(round(s10, 3)))
    fp.write("\t")
    fp.write(str(round(s20, 3)))
    fp.write("\t")
    fp.write(str(round(s50, 3)))
    fp.write("\t")
    fp.write(str(round(s100, 3)))
    fp.write("\n")

    fp.write("Reverse\t")
    fp.write(str(round(re10, 2)))
    fp.write("\t")
    fp.write(str(round(re20, 2)))
    fp.write("\t")
    fp.write(str(round(re50, 2)))
    fp.write("\t")
    fp.write(str(round(re100, 2)))
    fp.write("\n")

    fp.close()

else:
    print("\nWrong Insertion\n")