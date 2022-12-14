#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - a function in C that checks
 * if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node of listint_t list
 * An empty list is considered a palindrome
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i, j, k, pali[1000];
	listint_t *current;

	if (!head)
		return (0);
	if (*head == NULL)
		return (1);

	current = *head;
	j = 0;
	while (1)
	{
		pali[j] = current->n;
		current = current->next;
		if (current == NULL)
			break;
		j++;
	}
	i = 0;
	k = j / 2;
	while (1)
	{
		if (pali[j] != pali[i])
			return (0);
		if (i == k)
			break;
		j--;
		i++;
	}
	return (1);
}
