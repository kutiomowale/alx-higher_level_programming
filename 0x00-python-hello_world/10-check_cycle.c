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
	listint_t *nodes[1000];
	int i, j;

	if (list == NULL)
		return (0);
	i = 0;
	while (list->next != NULL)
	{
		nodes[i] = list;
		j = 0;
		while (j <= i)
		{
			if (list->next == nodes[j])
				return (1);
			j++;
		}
		list = list->next;
		i++;
	}
	return (0);
}
