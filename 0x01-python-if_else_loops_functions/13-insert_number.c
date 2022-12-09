#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - a function in C that inserts a number
 * into a sorted singly linked list
 *
 * @head: double pointer to head of list
 * @number: the number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *previous, *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	current = *head;
	if (number <= current->n)
	{
		new->next = current;
		current = new;
		return (new);
	}
	while (current->next != NULL)
	{
		previous = current;
		current = current->next;
		if (number <= current->n)
		{
			previous->next = new;
			new->next = current;
			return (new);
		}
	}
	current->next = new;
	return (new);
}
