


import time
from datetime import timedelta



TimeList ={}

class Sorting_list:         #this is the main class for some method that we need for this project
    def __init__(self, list):   
        self.list = list   #define list 
        
        




    
    #######################################Insertion Sort #############################################
    start = time.time()
    def insertionSort(self):      ## this is the first method that sort our list by insertion sort 

      insert_list =  self.list.copy()  # make a copy form main list
      
      n = len(insert_list)

      for i in range(1, n): # travel from the second element to the end of our list 
        j = i-1

        x = insert_list[i]     #put second element to key variable and in the next line compaer with preivous element of list
        
        while insert_list[j] >x  and j>=0:
            insert_list[j+1]=insert_list[j]

            j = j- 1


        insert_list[j+1]=x 
      
     
      #return 
      return insert_list
    end = time.time()
    InsertionTime = (end-start)  
    TimeList.setdefault("Insertion time is",InsertionTime)
    
    #####################################end of insertion sort#########################################






    #########################################Selection Sort#####################################
    start = time.time()
    def SelectionSort(self):  #this method retrun a sorted list by selection sort
      select_list = self.list.copy()
      n = len(select_list)

    
      for i in range(n):
        key = i
        

        for j in range(i+1, n):
          if select_list[key] > select_list[j]:
               key = j

        if i!=key:

            select_list[i] , select_list[key]  = select_list[key], select_list[i]

      return select_list
    end = time.time()
    SelectTime = (end-start)  
    TimeList.setdefault('SelectTime is:',SelectTime)
    #####################################end of Selection sort#########################################







    ########################################Quick Sort#######################################
    start = time.time() 
    def Quicksort(self,Quick_list):  #SO because this method is a recurasive method (بازگشتی )we need to get Quick_lsit fro an argument 
      
    
          if len(Quick_list) == 1 or len(Quick_list) == 0:
              return Quick_list
          else:
              pivot = Quick_list[0]                      #we put first element in pivot 
              i = 0
              for j in range(len(Quick_list)-1):         #in this program we convert list to two list and do this again for other list and at the end we append two lists
                  if Quick_list[j+1] < pivot:

                      Quick_list[j+1],Quick_list[i+1] = Quick_list[i+1], Quick_list[j+1]

                      i = i+1






              Quick_list[0],Quick_list[i] = Quick_list[i],Quick_list[0]                  #swapping coprative element


              first= self.Quicksort(Quick_list[:i])

              second= self.Quicksort(Quick_list[i+1:])


              first.append(Quick_list[i])   # append to the first element

              return first+second
    end = time.time()
    QuickTime = (end-start)  
    TimeList.setdefault("Quick time",QuickTime)
    #######################################end of Quick Sort###################################







    ########################################insertion sort#########################################
    start = time.time() 
    def mergsort(self,merg_list ):           #I defined two method  Mergsot is for   deviding list to the small parts  
        merg_list_size = len(merg_list)


        split = int(merg_list_size/2)       #convert the list to the two lists by center and dovode 2
        left = merg_list[0:split]

        right = merg_list[split:]


        if merg_list_size > 1:
            return self.merge(self.mergsort(left),self.mergsort(right) )   # divide to teh smallest lists
        else:
            return merg_list

    def merge(self,x,y):        # and the scound method is merg  for comparing elements and put these to the best place

        if len(x) == 0:
             return y

        if len(y) == 0:
             return x


        i = j=0

        
        if x[i] <= y[j]:
            return [x[i]]+self.merge(x[1:], y)
        else:
            return [y[j]] +self.merge(x, y[1:])
            
    end = time.time()
    MergTime = (end-start)  
    TimeList.setdefault('MergTime is :', MergTime)
    #####################################end of Merg sort#########################################








    ##################################### Heap sort###############################################
    start = time.time()   
    def move(self,heap_list,n,i):      # in these two method we get list and sort by binary tree and with move method and heapsort methodwe move biggest elements to the top level(maxheap)
        left = 2*i+1 
        right = 2*i+2
        
        if left<n and heap_list[left]> heap_list[i]:
            max = left
        else:
            max = i
            
        if right <n and heap_list[right]>heap_list[max]:
            max = right
            
        if max != i:
            heap_list[i] ,heap_list[max] =heap_list[max] ,heap_list[i]    #swapping elements with max 
            self.move(heap_list, n, max)
    

    def heap_sort(self,heap_list):
        n = len(heap_list)
        
        for i in range(int(n),-1,-1 ):
            self.move(heap_list,n,i)
            
        for i in range(n-1,0,-1):
            heap_list[0] ,heap_list[i] = heap_list[i], heap_list[0]
            self.move(heap_list, i, 0)      #  we call move for getting heap and elelments for moveing first
    
        return heap_list
    end = time.time()
    HeapTime = (end-start)  
    TimeList.setdefault('HeapTime is :', HeapTime)    
    #####################################end of Heap sort#########################################
    




    #################################### Heap sort#################################################
    start = time.time()
    def Shell_Sort(self,shell_list):
        a= len(shell_list)

        efraz = int(a/2)           # in this code we put the center element to the efraz 
        while efraz > 0:
            for i in range(efraz,a):   #then we travel from cneter element to the end
                key =shell_list[i]     #put elements to key for compare
                j =i
              
                while j >=efraz and shell_list[j-efraz] > key:
                      # we compare efraz's and perivous elements
                    shell_list[j] =shell_list[j-efraz]


                    j -= efraz

                shell_list[j]=key

            efraz = int(efraz/2)  # then we change efraz to the small efraz

            return shell_list
    end = time.time()
    ShellTime = (end -start)  
    TimeList.setdefault("Shell Time is:",ShellTime)   
    #####################################end of Shell sort#########################################

print("Done!")
   



#####################################BST sort#########################################

start = time.time()
class Node(Sorting_list):
    def __init__(self, key):
        self.valed = None      #define valed for save main node of node in each level
        self.key = key           #in this part of Node class we define some variables for save elements by bstree
        self.right = None            #define Rchild and Lchild of each valed 
        self.left = None
 
    def insert(self, node):
        if self.key > node.key:            # if argument is smaller than node we put in left or if the bigger than node we put in the right of node
            if self.left is None:
                node.valed = self
                self.left = node             #putting elements in correct places
            else:
                self.left.insert(node)
        elif self.key <= node.key:           #if  bigger than node we put in the right of node
            if self.right is None:
                node.valed = self
                self.right = node          #putting elements in correct places
            else:
                self.right.insert(node)
 
    def inorder(self):                        
        if self.left is not None:
            self.left.inorder()              #travel teh child and valed 
        print(self.key, end=' ')
        if self.right is not None:
            self.right.inorder()
    
class BSTree(Sorting_list):       #we define this class for using method those are in the privous clss 
    def __init__(self):
        self.root = None
 
    def inorder(self):                # so for bst sort we need inorder to travel elements
        if self.root is not None:
            self.root.inorder()
 
    def add(self, key):           #insert elements  in the bstree
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)  # add node to the bst
 
end = time.time()
BSTTime = (end- start)  
TimeList.setdefault('BSTTime',BSTTime) 
#####################################end of BST sort#########################################

####################################end of main class##########################################
        
    
    
    
 
# in this part of code we import length of list and then get elements of our list
# test_case_length = int(input('please enter Length of your list: '))
# test_case = []
# for i in range(test_case_length):
#     a= input("please enter elements: ")
#     test_case.append(float(a))
#     print(f'your list is {test_case} ')


#template test case is:
test_case = list(range(-250,250))
test_case.reverse()

print(test_case)


# getting list to the main class    
p = Sorting_list(test_case)


#Insertion Sort
print(f'the list sorted by Insertion sort is:\n {p.insertionSort()}')
# print(TimeList,'\n\n')    


#Selection sort
print(f'the list sorted by Selection sort is: \n{p.SelectionSort()}')
# print(TimeList,'\n\n')


#Quick sort
print(f'the list sorted by Quick sort is: \n{p.Quicksort(test_case)}')
# print(TimeList,'\n\n')


#mergsort
print(f'the list sorted by Merg sort is: \n{p.mergsort(test_case)}')
# print(TimeList,'\n\n')


#heap sort
print(f'the list sorted by Heap sort is: \n{p.heap_sort(test_case)}')
# print(TimeList,'\n\n')


#sehll sort
print(f'the list sorted by shell sort is: \n{p.Shell_Sort(test_case)}')
# print(TimeList,'\n\n')


#Bst sort
se =[]
bstree = BSTree()   #for sorting by bst we need to define bstree and then create it 
for x in test_case:       
    bstree.add(x)
print(f'the list sorted by BST sort is:')
print(se.append(bstree.inorder()))
# print(TimeList,'\n\n')
 


print('\n\n')
TimeList2= {}
sort_Timelist = sorted(TimeList, key =TimeList.get)   # if we want to get time by micro seconds we should write timedelta()

for i in sort_Timelist:
    TimeList2[i] = TimeList[i]

for a, b in TimeList2.items():
    print(f"{a}: {b}" )
