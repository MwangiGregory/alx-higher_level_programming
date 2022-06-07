#include "lists.h"
#include <stdio.h>
/**
 * reverse_list - reverse a singly linked list
 * @head: Pointer to the pointer to the head node
 * Return: pointer to the head node of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *temp1 = NULL;
	listint_t *temp2 = NULL;

	temp1 = (*head)->next;
	temp2 = (*head)->next->next;
	(*head)->next = NULL;
	temp1->next = *head;

	while (1)
	{
		*head = temp1;
		temp1 = temp2;
		if (temp1 == NULL)
			break;
		temp2 = temp1->next;
		temp1->next = *head;
	}
	return (*head);
}

int is_palindrome(listint_t **head)
{
	listint_t *fast_pointer = *head;
	listint_t *slow_pointer = *head;
	int i = 0, j = 0;

	while (1)
	{
		if (fast_pointer == NULL)
			break;
		else if (fast_pointer->next == NULL)
			break;
		else
		{
			fast_pointer = fast_pointer->next->next;
			slow_pointer = slow_pointer->next;
			i += 2;
			j++;
		}
	}
	printf("Value of jth node -> %d\n", slow_pointer->next->n);
	return (i);
}
