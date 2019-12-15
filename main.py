import PySimpleGUI as sg
# from numpy import random
import random
import itertools


BAR_SPACING, EDGE_OFFSET = 11, 3

SORTS = ['Bubble Sort', 'Insertion Sort', 'Merge Sort',
 'Odd-Even Sort', 'Binary Insertion Sort', 'Heap Sort',
 'Quick Sort']


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

''' quick sort '''
def quick_sort(arr, start, end):

    if start >= end:
        return

    pivot = arr[end]
    pivotIdx = start

    for i in range(start, end):
        if arr[i] < pivot:
            #swap
            if i != pivotIdx:
                arr[i], arr[pivotIdx] = arr[pivotIdx], arr[i]
            pivotIdx += 1
        yield arr
    #swap
    if end != pivotIdx:
        arr[end], arr[pivotIdx] = arr[pivotIdx], arr[end]
    yield arr

    yield from quick_sort(arr, start, pivotIdx - 1)
    yield from quick_sort(arr, pivotIdx + 1, end)

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

'''recursive merge sort'''
def merge_sort(arr, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from merge_sort(arr, start, mid)
    yield from merge_sort(arr, mid + 1, end)
    yield from merge(arr, start, mid, end)
    yield arr


def merge(arr, start, mid, end):
    merged = []
    left = start
    right = mid + 1

    while left <= mid and right <= end:
        if arr[left] < arr[right]:
            merged.append(arr[left])
            left += 1
        else:
            merged.append(arr[right])
            right += 1

    while left <= mid:
        merged.append(arr[left])
        left += 1

    while right <= end:
        merged.append(arr[right])
        right += 1

    for i, sorted_val in enumerate(merged):
        arr[start + i] = sorted_val
        yield arr


''' odd-even sort '''
def odd_even_sort(arr, n):

    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        temp = 0
        for i in range(1, n, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
                yield arr
            yield arr


        for i in range(0, n, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
                yield arr
            yield arr


''' heap_sort '''
def heap_sort(arr):
    n = len(arr)
    # yield arr

    # Build a maxheap.
    for i in range(n, -1, -1):
        yield arr
        yield heapify(arr, n, i)
        yield arr
    # yield arr

    # One by one extract elements
    for i in range(n-1, 0, -1):
        yield arr
        arr[i], arr[0] = arr[0], arr[i]   # swap
        yield arr
        yield heapify(arr, i, 0)
        yield arr
    yield arr


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2


    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l


    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r


    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap

        # Heapify the root
        heapify(arr, n, largest)


''' binary insertion sort '''
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        pos = binary_search(arr, temp, 0, i) + 1

        for k in range(i, pos, -1):
            arr[k] = arr[k - 1]
            # pos = pos - 1
            yield arr
        arr[pos] = temp
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


# draw bars
def draw_bars(graph, items, bar_width, bar_spacing):       # redraws bars each time

    for i, item in enumerate(items):

        graph.DrawRectangle(top_left=(i * bar_spacing + EDGE_OFFSET, item),
                            bottom_right=(i * bar_spacing + EDGE_OFFSET + bar_width, 0), fill_color='sky blue')




def main():

    # color theme
    sg.change_look_and_feel('Tan')


    # dictionary with sorting algorithm names as keys and their functions as values
    dict = {
            'Bubble Sort': bubble_sort, 'Insertion Sort': insertion_sort, 'Merge Sort': merge_sort,
             'Odd-Even Sort': odd_even_sort, 'Binary Insertion Sort': binary_insertion_sort, 'Heap Sort': heap_sort,
             'Quick Sort': quick_sort
        }

    # graph size
    GRAPH_SIZE = (800,300)
    DATA_SIZE = (800, 350)

    # graph titles to be renamed later
    graph_title1 = ''
    graph_title2 = ''


    # Layout for first window
    # consists of text, text input, listbox enabled for multiple selection, and group of radio buttons
    input_layout = [[sg.Text('How many elements are we sorting? (Recommended <190)', justification='left', font=("Helvetica", 15))],
        [sg.Input(size=(10, 1), justification='right', font=("Helvetica", 15), key='-INPUT-')],
            [sg.Text('Choose a sort (Please pick 2)', font=("Helvetica", 15))],
          [sg.Listbox(values=SORTS, select_mode='multiple', size=(50,20), font=("Helvetica", 15))],
           [sg.Radio('Randomly Shuffled', group_id='radio', key='-R1-', default=True, font=("Helvetica", 12)),
            sg.Radio('Reverse Sorted', group_id='radio', key='-R2-', font=("Helvetica", 12)),
           sg.Radio('Random Uneven', group_id='radio', key='-R3-', font=("Helvetica", 12))],
          [sg.Ok()],]

    # create the window
    window1 = sg.Window('Choose sort', input_layout)
    button, values = window1()
    window1.close()


    # take user input for number of elements to sort
    number_input = int(values['-INPUT-'])

    # radio button group for list shape and order
    radio_input1 = bool(values['-R1-'])
    radio_input2 = bool(values['-R2-'])
    radio_input3 = bool(values['-R3-'])

    # make the graph size bigger if number of elements to sort is large
    if number_input > 150:
        GRAPH_SIZE = (1100,300)

    print("user wrote: " + str(number_input))

    num_bars = 1 + number_input

    #initialize list of elements
    first_list = [DATA_SIZE[1]//num_bars*i  for i in range(1,num_bars)]

    # change list based on user input
    if radio_input1 == True:
        random.shuffle(first_list)
    elif radio_input2 == True:
        first_list.sort(reverse = True)
    else:
        first_list = [random.randrange(DATA_SIZE[1]//num_bars*i) for i in range(1,num_bars)]


    second_list = first_list.copy()

    # bar width
    bar_width = ((DATA_SIZE[1]*2)//num_bars)

    # spacing of bars between each other
    bar_spacing = bar_width + 1
    # print(bar_width)



    choice1 = values[0][0] # first selection in listbox
    choice2 = values[0][1] # second selection in listbox

    # match first selection
    if choice1 in dict.keys():
        if choice1 == 'Odd-Even Sort':
            sort1 = dict[choice1](first_list, len(first_list)-1)
        elif choice1 in ('Merge Sort', 'Quick Sort'):
            sort1 = dict[choice1](first_list, 0, len(first_list)-1)
        else:
            sort1 = dict[choice1](first_list)
        graph_title1 = choice1

    # match second selection
    if choice2 in dict.keys():
        if choice2 == 'Odd-Even Sort':
            sort2 = dict[choice2](second_list, len(second_list)-1)
        elif choice2 in ('Merge Sort', 'Quick Sort'):
            sort2 = dict[choice2](second_list, 0, len(second_list)-1)
        else:
            sort2 = dict[choice2](second_list)
        graph_title2 = choice2



    start_button = sg.Button("Start", size= (5, 1))
    graph1 = sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE)
    graph2 = sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE)


    # layout of sorting window
    layout = [[start_button], [sg.T('', size=(10,1))], [sg.T(graph_title1, size=(20, 1), justification='left', font=("Helvetica", 20))], [graph1], [sg.T('', size=(10,1))],
                [sg.T(graph_title2, size=(20, 1), justification='left', font=("Helvetica", 20))], [graph2],
              [sg.T('Faster'), sg.Slider((0,150), orientation='h', default_value=25, key='-SPEED-'), sg.T('Slower')]]

    window = sg.Window('All Sorts of Algorithms', layout, finalize=True)

    # draw both graphs before starting
    draw_bars(graph1, first_list, bar_width, bar_spacing)
    draw_bars(graph2, second_list, bar_width, bar_spacing)

    # when button is clicked
    while True:
        event, values = window.read()
        if event is None:
            break
        timeout=25  # start with 25ms delay between draws

        for a, b in itertools.zip_longest(sort1, sort2):
            event, values = window.read(timeout=timeout)
            if a is not None:
                # print('this is the first sort')
                graph1.Erase()
                draw_bars(graph1, a, bar_width, bar_spacing)
            if b is not None:
                # print('this is the second sort')
                graph2.Erase()
                draw_bars(graph2, b, bar_width, bar_spacing)
            else:
                pass
            timeout = int(values['-SPEED-'])


    window.close()

# comment this section out if you don't want to keep running the program
while True:
    main()
