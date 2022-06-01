#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to a singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp_head = NULL;
	listint_t *current = list;
	
	while (current)
	{
		temp_head = list;
		current = current->next;
		while (current != temp_head)
		{
			if (!current)
				return (0);
			else if (current->next == temp_head)
				return (1);
			temp_head = temp_head->next;
		}
	}
	return (0);
}
