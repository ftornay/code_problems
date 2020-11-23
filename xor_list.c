/*
 An XOR linked list is a more memory efficient doubly linked list.
 Instead of each node holding next and prev fields, it holds a field named both,
 which is an XOR of the next node and the previous node.
 Implement an XOR linked list;
 it has an add(element) which adds the element to the end,
 and a get(index) which returns the node at index.
 */

#include <stdio.h>
#include <stdint.h>
#include <assert.h>

typedef struct _node {
    char *data;
    // Integer value that represents a pointer
    uintptr_t both;
} xor_node;

typedef struct _list {
    xor_node* first;
    xor_node* last;
} xor_list;

void xor_list_init(xor_list* list)
{
    list->first = list->last = NULL;
}

void add(xor_list* list, xor_node* node)
{
    if (list->first == NULL)
    {
        // Empty list
        // new node is first and last
        node->both = 0;
        list->first = list->last = node;
    }
    else
    {
        // Current last must point to new node as next
        // Xor it with last's prev value
        list->last->both ^= (uintptr_t) node;
        // new_node has current last as prev
        node->both = (uintptr_t) list->last;
        // Add new node as last
        list->last = node;
    }
}

xor_node* get(xor_list* list, int index)
{
    if(index == 0)
        return list->first;

    xor_node* current = list->first;
    uintptr_t next = list->first->both;
    for(int i = 1; i <= index; i++)
    {
        // Don't dereference NULL pointer
        if(next == 0)
            return NULL;
        // Get current node by casting uintptr_t to pointer
        current = (xor_node*) next;
        // Get next pointer by XOR_ing with the previous
        next ^= current->both;
    }
    return current;
}

int main()
{
    xor_node node0, node1, node2, *new_node;
    xor_list list;
    node0.data = "Random data";
    node1.data = "Other data";
    node2.data = "Still some more";
    xor_list_init(&list);
    add(&list, &node0);
    add(&list, &node1);
    add(&list, &node2);
    new_node = get(&list, 1);
    printf("Node1 data: %s\n", new_node->data);
    new_node = get(&list, 5);
    assert(new_node == NULL);
    return 0;
}
