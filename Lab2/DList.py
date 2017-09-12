# ----------------------------------------------------------------------
# DList.py
# Tom Green
# ----------------------------------------------------------------------

import sys

from DListNode import *


# ----------------------------------------------------------------------

class DList:
    '''implementation of subset of Python built-in list API using
    a doubly linked list'''

    # List implemented as doubly linked nodes
    # invariant:
    # self.size indicates the number of items in the list
    # if self.size == 0, self.head is None otherwise
    # self.head is a reference to the first DListNode in list
    # self.tail is a reference to the last DListNode in the list to
    #   make the append operation efficient
    # preconditions for each method are indicated by the assert test

    # ------------------------------------------------------------------

    def __init__(self, seq=None):

        '''creates an empty list'''
        
        # intialize instance variables of linked list
        self.head = None
        self.tail = None
        self.size = 0

        # If passed a sequence, place items in list 
        if seq is not None:
            for i in seq:
                self.append(i)

    # ------------------------------------------------------------------

    def __len__(self):

        '''returns number of items in the list'''

        # returns the instancec variable, size
        return self.size

    # ------------------------------------------------------------------

    def __iter__(self):

        '''forward iterator'''

        # set node to head
        node = self.head
  
        while node is not None:
            # yield the node's item
            yield node.item
            # the next node becomes node and loops back to the while statement
            node = node.next

    # ------------------------------------------------------------------

    def _find(self, position):

        '''private method that returns node that is at location position
        in the list;
        for non negative positions, 0 is first item, size-1 is last item
        for negative positions, -1 is the last item -size is the first
        item'''

        # if the head contains something
        if self.head:
            # if the position is greater than or equal to 0 and the position is smaller than the size
            if position >= 0 and position < self.size: 
                # set node as first of list
                node = self.head
                # iterate through the list based on parameter, position
                for i in range(position):
                    # next node becomes node
                    node = node.next
                return node
            # else if the position is less than 0 and the position is greater than or equal to negative-size
            elif position < 0 and position >= -self.size:
                # set self.tail as node
                node = self.tail
                # iterate through the list starting from end 
                for i in range(-position):
                    # set node as previous node
                    node = node.prev
                return node
            else:
                # if position is not given raise ValueError
                raise IndexError
        else:
            # else the position is not a valid index of the list
            raise IndexErrorr

    # ------------------------------------------------------------------

    def __getitem__(self, position):

        '''return data item at location position'''

        # utilize find method to retrieve node at position 
        node = self._find(position)
        return node.item

    # ------------------------------------------------------------------

    def __setitem__(self, position, value):

        '''set data item at location position to value'''

        # utilize find method to retrieve node at the position
        node = self._find(position)
        # set the item of that node to the value
        node.item = value

    # ------------------------------------------------------------------

    def __delitem__(self, position):

        '''delete item at location position from the list'''
        
        # utilize the delete method 
        self._delete(position)

    # ------------------------------------------------------------------

    def _delete(self, position):

        '''private method to delete item at location position from the list'''
        
        # if there is something at the head
        if self.head:
            # set the node as the found node at position
            node = self._find(position)
            # if the size of list is 1
            if self.size == 1:
                # set the head and tail as none 
                self.head = None
                self.tail = None
            # else if the node is the head    
            elif node is self.head:
                # set the next node's, after head, previous link to None
                # this removes the head
                node.next.prev = None
                # self.head becomes what was the node after head
                self.head = node.next
            elif node is self.tail:
                # set the previous node's next link of the tail to None
                # this removes the tail
                node.prev.next = None
                # the tail is now set as the node that was before the tail
                self.tail = node.prev
            else:
                # else the node is not the only item in list, or the head, or the tail
                # setting the previous node's next link to the node after found-node
                node.prev.next = node.next
                node.next.prev = node.prev
            # subtract one from the size 
            self.size -= 1
            return node.item
        else:
            # else the position is not a valid index of the list
            raise IndexError

    # ------------------------------------------------------------------

    def append(self, x):

        '''appends x onto end of the list'''

        newNode = DListNode(x, self.tail)
        if self.size == 0:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    # ------------------------------------------------------------------

    def insert(self, i, x):

        '''inserts x before position i in the list'''

        newNode = DListNode(x)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        elif i == self.size:
            self.append(x)
        elif i == 0:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        else:
            node = self._find(i)
            newNode.next = node
            newNode.prev = node.prev
            node.prev.next = newNode
            node.prev = newNode
        self.size += 1

    # ------------------------------------------------------------------

    def pop(self, i=None):

        '''returns and removes at position i from list; the default is to
        return and remove the last item'''

        if i is None:
            i = self.size - 1
        return self._delete(i)

    # ------------------------------------------------------------------

    def remove(self, x):

        '''removes the first instance of x from the list'''

        self._delete(self.index(x))

    # ------------------------------------------------------------------

    def __min__(self):

        '''return minimum element in the list'''

        if self.head:
            node = self.head
            min = node.item
            while node:
                if node.item < min:
                    min = node.item
                node = node.next
            return min
        else:
            raise ValueError

    # ------------------------------------------------------------------

    def __max__(self):

        '''return maximum element in the list'''

        if self.head:
            node = self.head
            max = node.item
            while node:
                if node.item > max:
                    max = node.item
                node = node.next
            return max
        else:
            raise ValueError

    # ------------------------------------------------------------------

    def extend(self, l):

        '''add each element of list l onto the list'''

        for i in l:
            self.append(i)

    # ------------------------------------------------------------------

    def count(self, x):

        '''return number of occurrences of x in the list'''
        node = self.head
        count = 0
        while node:
            if node.item == x:
                count += 1
            node = node.next
        return count

    # ------------------------------------------------------------------

    def index(self, x, start=0):

        '''return position of first occurence of x in the list starting
        at position start'''

        node = self._find(start)
        pos = start
        while node and node.item != x:
            node = node.next
            pos += 1
        if node == None:
            raise ValueError
        else:
            return pos

    # ------------------------------------------------------------------

    def reverse_iter(self):

        '''iterate over items in reverse'''

        node = self.tail
        while node is not None:
            yield node.item
            node = node.prev

# ----------------------------------------------------------------------
