#include "lists.h"
/**
 * check_cycle - a function in C that checks
 * if a singly linked list has a cycle in it
 * @list: - pointer to list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head;

	head = list;
	if (list == NULL)
		return (0);
	while (list->next != NULL)
	{
		if (list->next == head)
			return (1);
		list = list->next;
	}
	return (0);
}
