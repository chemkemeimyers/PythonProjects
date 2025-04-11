# Definition for singly-linked list.
class LinkedList():
    def __init__(self):
        self.head = None
    
    def append(self, data):
        newNode = ListNode(data)
        if not self.head:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
    
    def toString(self):
        current = self.head
        while current:
            print(current.val, end='-->')
            current = current.next

        
        print("None")

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #Extract the values from each linked list and reverse them
        current  = l1.head
        
        value = ""
        while current:
            value+= str(current.val)
            current = current.next
        valuell1 =  value[::-1]

        current = l2.head

        value2 = ""
        while current:
            value2+= str(current.val)
            current = current.next
        valuell2 = value2[::-1]

        #Sum the reversed values
        result = int(valuell1) + int(valuell2)

        #Reverse the result
        resultReversed = str(result)[::-1]

        #Store the result one value at a time in a linked list
        llresult = LinkedList()

        for char in resultReversed:
            llresult.append(int(char))
        
        return llresult
        

    

ll = LinkedList()
ll.append(2)
ll.append(4)
ll.append(3)
ll.toString()

ll1 = LinkedList()
ll1.append(5)
ll1.append(6)
ll1.append(4)
ll1.toString()

sol = Solution()
sol.addTwoNumbers(ll,ll1).toString()





        