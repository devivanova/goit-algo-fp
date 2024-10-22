class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def merge_sorted_lists(self, list2):
        p = self.head
        q = list2.head
        merged_list = LinkedList()

        while p is not None and q is not None:
            if p.data <= q.data:
                merged_list.append(p.data)
                p = p.next
            else:
                merged_list.append(q.data)
                q = q.next

        while p is not None:
            merged_list.append(p.data)
            p = p.next

        while q is not None:
            merged_list.append(q.data)
            q = q.next

        return merged_list

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next

        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.merge_sub_lists(left, right)

        return sorted_list

    def merge_sub_lists(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.merge_sub_lists(a.next, b)
        else:
            result = b
            result.next = self.merge_sub_lists(a, b.next)

        return result

    def sort(self):
        if self.head is not None:
            self.head = self.merge_sort(self.head)


llist1 = LinkedList()
llist1.append(10)
llist1.append(30)
llist1.append(20)
llist1.append(5)

print("Оригінальний список 1:")
llist1.print_list()

print("Сортування списку 1:")
llist1.sort()
llist1.print_list()

llist2 = LinkedList()
llist2.append(7)
llist2.append(15)
llist2.append(25)

print("Оригінальний список 2:")
llist2.print_list()

print("Об'єднання списків:")
merged_list = llist1.merge_sorted_lists(llist2)
merged_list.print_list()

print("Реверсування об'єднаного списку:")
merged_list.reverse()
merged_list.print_list()
