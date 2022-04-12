class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,data):
        node= Node(data, self.head)
        self.head=node
    
        
    def insert_at_ending(self,data):
        if(self.head is None):
            self.head=Node(data,None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
            
        itr.next=Node(data,None)
        
    def insert_values(self,data_list):
        self.head=None
        for item in data_list:
            self.insert_at_ending(item)
            
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
            
        return count
    
    def remove_at_index(self,index):
        if(index<0 or index>=self.get_length()):
            raise Exception("Invalid index")
        
        if index==0:
            self.head=self.head.next
            return
        
        count=0
        itr=self.head
        while itr:
            if(count==index-1):
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
                
    def insert_at(self, index, data):
        if(index<0 or index>=self.get_length()):
            raise Exception("Invalid index")
        
        if(index==0):
            self.insert_at_beginning(data)
            return
        
        count=0
        itr=self.head
        while itr:
            if(count==index-1):
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
        
    def print(self):
        if(self.head is None):
            print("Linked List is empty")
            return
        
        itr=self.head
        linked_list_string=''
        while itr:
            linked_list_string+=str(itr.data) + '-->'
            itr=itr.next
        print(linked_list_string)
        
if __name__ == '__main__':
    # Test
    linked_list=LinkedList()
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_beginning(89)
    linked_list.insert_at_ending(79)
    
    linked_list.print()
    print(linked_list.get_length())
    
        

        