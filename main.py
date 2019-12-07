import PySimpleGUI as sg
import random
import numpy as np
import itertools


BAR_SPACING, EDGE_OFFSET = 11, 3


'''doesnt work so far'''
def selection_sort(arr):
    for i in range(len(arr)):

    # Find the minimum element in remaining
    # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                yield arr
    # Swap the found minimum element with
    # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    yield arr

'''insertion sort'''
def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
            yield arr
        # Break and do the final swap
        arr[pos] = cursor
    yield arr

'''bubble sort'''
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
            yield arr

'''merge sort '''
def merge_sort(arr):

    unit = 1
    while unit <= len(arr):
        h = 0
        for h in range(0, len(arr), unit * 2):
            l, r = h, min(len(arr), h + 2 * unit)
            mid = h + unit

            p, q = l, mid
            yield arr
            while p < mid and q < r:

                if arr[p] <= arr[q]:
                    p += 1


                else:
                    tmp = arr[q]
                    arr[p + 1: q + 1] = arr[p:q]
                    arr[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1
                    yield arr
        unit *= 2
        yield arr



''' odd-even sort '''
def odd_even_sort(arr, n):
    # Initially array is unsorted
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # yield arr
                isSorted = 0
                yield arr

        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # yield arr
                isSorted = 0
                yield arr
        yield arr
    # return


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
        # yield arr

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
        # yield arr

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, largest)

''' heapsort '''
def heapsort(arr):
    n = len(arr)
    # yield arr

    # Build a maxheap.
    for i in range(n, -1, -1):
        # yield arr
        yield heapify(arr, n, i)
        yield arr
    # yield arr

    # One by one extract elements
    for i in range(n-1, 0, -1):
        # yield arr
        arr[i], arr[0] = arr[0], arr[i]   # swap
        # yield arr
        yield heapify(arr, i, 0)
        yield arr
    # yield arr

''' binary insertion sort '''
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        pos = binary_search(arr, temp, 0, i) + 1


        for k in range(i, pos, -1):
            arr[k] = arr[k - 1]
            yield arr

        arr[pos] = temp
        yield arr
    yield arr

def binary_search(arr, key, start, end):
    if end - start <= 1:
        if key < arr[start]:
            return start - 1
        else:
            return start

    mid = (start + end)//2
    if arr[mid] < key:
        return binary_search(arr, key, mid, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid)
    else:
        return mid

def bucket_sort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])

    for i in range(length):
        insertionsorthelp(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]

    return result

def insertionsorthelp(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


def draw_bars(graph, items, bar_width, bar_spacing):       # redraws bars each time
    # type: (sg.Graph, List)->None
    for i, item in enumerate(items):
        # print(i)
        # print(item)
        graph.DrawRectangle(top_left=(i * bar_spacing + EDGE_OFFSET, item),
                            bottom_right=(i * bar_spacing + EDGE_OFFSET + bar_width, 0), fill_color='sky blue')

        # print('current number' + str(item))


def main():
    sg.change_look_and_feel('Tan')

    # num_bars = 1 + 10 #num_bars is half of x in data_size ex datasize = 1000 numbars = 90, data_size = 500 num_bars = 45
    #
    #
    # list_to_sort = [DATA_SIZE[1]//num_bars*i  for i in range(1,num_bars)]
    # random.shuffle(list_to_sort)

    # second_list = list_to_sort.copy()

    GRAPH_SIZE = (800,300)
    DATA_SIZE = (800, 350)

    graph_title1 = ''
    graph_title2 = ''
    # print(num_bars)
    # print(list_to_sort)



    # Choose which sort
    l2 = [[sg.Text('Pick a number', size=(10,1), justification='left', font=("Helvetica", 15))], [sg.Input(size=(10, 1), justification='right', key='-INPUT-')], [sg.T('Choose a sort')],
          [sg.Listbox(['Bubble Sort', 'Insertion Sort', 'Merge Sort',
           'Odd-Even Sort', 'Binary Insertion Sort', 'Heap Sort', 'Selection Sort'], select_mode='multiple', size=(60,30))],
           [sg.Radio('My first Radio!', "RADIO1", default=True),
           sg.Radio('My second radio!', "RADIO1")],
          [sg.Ok()],]
    w2 = sg.Window('Choose sort', l2)
    button, values = w2()
    w2.close()
    print(values)

    number = int(values['-INPUT-'])

    if number > 150:
        GRAPH_SIZE = (1100,300)



    print(number)

    num_bars = 1 + number #num_bars is half of x in data_size ex datasize = 1000 numbars = 90, data_size = 500 num_bars = 45
    list_to_sort = [DATA_SIZE[1]//num_bars*i  for i in range(1,num_bars)]
    random.shuffle(list_to_sort)
    second_list = list_to_sort.copy()


    bar_width = ((DATA_SIZE[1]*2)//num_bars)
    bar_spacing = bar_width + 1
    print(bar_width)



    choice1 = values[0][0]
    choice2 = values[0][1]




    # use [0][0] for now to only choose one sort
    if values[0][0] == 'Bubble Sort':
        sort_algo1 = bubble_sort(list_to_sort)
        graph_title1 = 'Bubble Sort'
    elif values[0][0] == 'Insertion Sort':
        sort_algo1 = insertion_sort(list_to_sort)
        graph_title1 = 'Insertion Sort'
    elif values[0][0] == 'Merge Sort':
        sort_algo1 = merge_sort(list_to_sort)
        graph_title1 = 'Merge Sort'
    elif values[0][0] == 'Odd-Even Sort':
        sort_algo1 = odd_even_sort(list_to_sort, len(list_to_sort))
        graph_title1 = 'Odd-Even Sort'
    elif values[0][0] == 'Heap Sort':
        sort_algo1 = heapsort(list_to_sort)
        graph_title1 = 'Heap Sort'
    elif values[0][0] == 'Binary Insertion Sort':
        sort_algo1 = binary_insertion_sort(list_to_sort)
        graph_title1 = 'Binary Insertion Sort'
    elif values[0][0] == 'Selection Sort':
        sort_algo1 = selection_sort(list_to_sort)
        graph_title1 = 'Selection Sort'

    else:
        return


    if values[0][1] == 'Bubble Sort':
        sort_algo2 = bubble_sort(second_list)
        graph_title2 = 'Bubble Sort'
    elif values[0][1] == 'Insertion Sort':
        sort_algo2 = insertion_sort(second_list)
        graph_title2 = 'Insertion Sort'
    elif values[0][1] == 'Merge Sort':
        sort_algo2 = merge_sort(second_list)
        graph_title2 = 'Merge Sort'
    elif values[0][1] == 'Odd-Even Sort':
        sort_algo2 = odd_even_sort(second_list, len(second_list))
        graph_title2 = 'Odd-Even Sort'
    elif values[0][1] == 'Heap Sort':
        sort_algo2 = heapsort(second_list)
        graph_title2 = 'Heap Sort'
    elif values[0][1] == 'Binary Insertion Sort':
        sort_algo2 = binary_insertion_sort(second_list)
        graph_title2 = 'Binary Insertion Sort'
    elif values[0][0] == 'Selection Sort':
        sort_algo1 = selection_sort(second_list)
        graph_title2 = 'Selection Sort'
    else:
        return

    start_button = sg.Button("Start", size= (5, 1))
    graph1 = sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE)
    graph2 = sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE)

    layout = [[start_button], [sg.T(graph_title1, size=(30, 1), justification='center', font=("Helvetica", 25))], [graph1],
                [sg.T(graph_title2, size=(30, 1), justification='center', font=("Helvetica", 25))], [graph2],
              [sg.T('Speed    Faster'), sg.Slider((0,80), orientation='h', default_value=25, key='-SPEED-'), sg.T('Slower')]]

    window = sg.Window('Sort Visualization', layout, finalize=True)
    draw_bars(graph1, list_to_sort, bar_width, bar_spacing)
    draw_bars(graph2, second_list, bar_width, bar_spacing)

    # insertion = insertion_sort(second_list)

    while True:
        event, values = window.read()
        if event is None:
            break
        timeout=25  # start with 25ms delay between draws
        # for partially_sorted_list in sort_algo1:
        #     # print(partially_sorted_list)
        #     event, values = window.read(timeout=timeout)
        #     if event is None:
        #         break
        #     graph1.Erase()
        #     # graph2.Erase()
        #     draw_bars(graph1, partially_sorted_list)
        #     # draw_bars(graph2, partially_sorted_list)
        #     timeout = int(values['-SPEED-'])
        # for part in insertion:
        #     event, values = window.read(timeout=timeout)
        #     graph2.Erase()
        #     draw_bars(graph2, part)
        #     timeout = int(values['-SPEED-'])

        for a, b in itertools.zip_longest(sort_algo1, sort_algo2):
            event, values = window.read(timeout=timeout)
            if a is not None:
                print('this is the first sort')
                graph1.Erase()
                draw_bars(graph1, a, bar_width, bar_spacing)
            if b is not None:
                print('this is the second sort')
                graph2.Erase()
                draw_bars(graph2, b, bar_width, bar_spacing)
            else:
                pass
            timeout = int(values['-SPEED-'])






    window.close()

main()
