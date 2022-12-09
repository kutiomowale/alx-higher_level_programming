#include "lists.h"
/**
 * check_cycle - a function in C that checks
 * if a singly linked list has a cycle in it
 * It does this by using two pointers
 * one traverses the list one node at a time
 * the other two nodes at a time
 * Therefore the list has a cycle when the pointers meet at the same node
 * When either of the pointers point to or get to a null pointer,
 * it means the list has no cycle
 * @list: - pointer to list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *one_step, *two_step;

	if (list == NULL)
		return (0);
	one_step = two_step = list;
	while (one_step && two_step)
	{
		if (one_step->next == NULL)
			break;
		one_step = one_step->next;
		if (two_step->next == NULL)
			break;
		two_step = two_step->next->next;
		if (one_step == two_step)
			return (1);
	}
	return (0);
}
