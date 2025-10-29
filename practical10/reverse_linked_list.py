class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    
    while current is not None:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev one step
        current = next_temp       # Move current one step
    
    return prev  # prev is the new head of the reversed list

# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    vals = []
    current = head
    while current:
        vals.append(current.val)
        current = current.next
    print(vals)

# Test case 1: odd number of nodes
head1 = create_linked_list([1, 2, 3, 4, 5])
reversed_head1 = reverseList(head1)
print("Reversed [1,2,3,4,5]:")
print_linked_list(reversed_head1)

# Test case 2: even number of nodes
head2 = create_linked_list([1, 2, 3, 4])
reversed_head2 = reverseList(head2)
print("Reversed [1,2,3,4]:")
print_linked_list(reversed_head2)
