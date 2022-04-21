#Selection sort using basic min()

def selectionSort(l):
    l1 = []
    for i in range(len(l)):
        j = min(l)
        index = l.index(j)
        #print("min is:",j,"at index:",index)
        l.pop(index)
        l1.append(j)
    print(l1)

if __name__ == "__main__":
  l = [1,7,2,6,0,9,6]
  selectionSort(l)
