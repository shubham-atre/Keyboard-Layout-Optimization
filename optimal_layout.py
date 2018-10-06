import os,sys
import math as m
import random
import string

#Key Width equal to 1 key
keyWidth = 1.0
#Key coordinate for a 6 rows by 5 column keyboard
cord = [[(x + keyWidth/2.0,y + keyWidth/2.0) for x in range(5)] for y in range(6)]


def get_random_layout():
    # Call this function to a a randomized layout.
    # A layout is dictionary of key symbols(a to z) to it's (row, column) index
    cord_shuffle = [(x ,y) for x in range(6) for y in range(5)]
    random.shuffle(cord_shuffle)

    layout={}
    i=0
    for lt in string.ascii_lowercase:
        layout[lt]=cord_shuffle[i]
        i+=1
    # Since there are 30 slots for a 6*5 keyboard,
    # we use dummy keys to stuff remaining keys
    layout['1']=cord_shuffle[-1]
    layout['2']=cord_shuffle[-2]
    layout['3']=cord_shuffle[-3]
    layout['4']=cord_shuffle[-4]

    return layout


def makeDigramTable(data_path):
    # Make a Digram Table , which is a dictionary with key format (letter_i,letter_j) to it's Pij
    # You could safely ignore words that have only 1 character when constructing this dictionary

    fp = open(data_path)
    line = fp.readline()
    total = 0
    dict = {}
    tbl = {}

    while line:
        word_count = line.split('\t')
        word = word_count[0]
        count = int(word_count[1])
        word_len = len(word)

        for i in range(word_len - 1):
            pair = word[i] + ',' + word[i + 1]
            if pair in dict:
                dict[pair]= (dict[pair][0] + count, word[i], word[i+1])

            if pair not in dict:
                dict[pair] = (count, word[i], word[i+1])

            total = total + count

        line = fp.readline()

    fp.close()

    for k,v in dict.items():
        dict[k] =(v[0],v[1],v[2],v[0]/total)

    return dict

def FittsLaw(W,D):
    #implement the Fitt's Law based on the given arguments and constant
    a = 0.083
    b = 0.127

    mt = a + b*(m.log2(D/W + 1))
    return mt

def calculateDistance(a,b):
    x1,y1 = cord[a[0]][a[1]]
    x2,y2 = cord[b[0]][b[1]]
    return m.sqrt(pow((y2 - y1),2) +  pow((x2 - x1),2))

def computeAMT(layout, tbl):
    t = 0
    # Compute the average movement time
    for val in tbl.values():
        mt = FittsLaw(keyWidth, calculateDistance(layout[val[1]], layout[val[2]]))
        t+=mt*val[3]
    return t

def SA(num_iter, num_random_start, tbl):
    # Do the SA with num_iter iterations, you can random start by num_random_start times
    # the tbl arguments were the digram table
    r = 0
    while r < num_random_start:
        starting_state = get_random_layout()
        result = starting_state
        k=0
        cost = computeAMT(starting_state,tbl)
        if (r == 0):
            min_cost = cost
        while k<num_iter:
            key1, key2 = random.sample(list(starting_state),2)
            starting_state[key1], starting_state[key2] = starting_state[key2], starting_state[key1]
            amt = computeAMT(starting_state,tbl)
            if(cost > amt) :
                k = 0
                cost = amt
            else:
                k += 1
                starting_state[key1], starting_state[key2] = starting_state[key2], starting_state[key1]
        if(cost < min_cost):
            min_cost = cost
            result = starting_state
        r += 1
    final_result= (result,min_cost)
    #--------you should return a tuple of (optimal_layout,optimal_MT)----
    return final_result

def printLayout(layout):
    # use this function to print the layout
    keyboard= [[[] for x in range(5)] for y in range(6)]
    for k in layout:
        r=layout[k][0]
        c=layout[k][1]
        keyboard[r][c].append(k)
    for r in range(6):
        row=''
        for c in range(5):
            row+=keyboard[r][c][0]+'  '
        print(row)

if __name__ == '__main__':
    startTime = datetime.now()
    if len(sys.argv)!=4:
        print("usage: optimal_layout.py [num_SA_iteration] [num_SA_random_start] [dataset_path]")
        exit(0)
    k=int(sys.argv[1])
    rs=int(sys.argv[2])
    data_path=sys.argv[3]
    #data_path = 'words_100.txt'

    # Test Fitt's Law
    print(FittsLaw(10,10))
    print(FittsLaw(20,5))
    print(FittsLaw(10.5,1))

    #Construct Digram Table
    main_dict=makeDigramTable(data_path)
    #Run SA
    result, cost = SA(k,rs,main_dict)
    print("Optimal MT:", cost)
    printLayout(result)

