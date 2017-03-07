L = [5, 10, 12, 50, 60, 100, 500, 4]

#Heap shortcuts
def left(i): return i*2+1
def right(i): return i*2+2
def parent(i): return (i-1)/2
def root(i): return i==0
def leaf(L, i): return right(i) >= len(L) and left(i) >= len(L)
def one_child(L, i): return right(i) == len(L)

def up_heapify(L, i):
    #if i is root, heap property holds
    if root(i): return
    #Check parent. If partent smaller, swap, call recursive. If larger, return
    if L[i] > L[parent(i)]:
       (L[parent(i)], L[i]) = (L[i], L[parent(i)])
       up_heapify(i)
       return
   
up_heapify(L, 7)