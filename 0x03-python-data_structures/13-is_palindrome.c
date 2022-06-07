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
	listint_t *head2 = NULL;
	listint_t *temp = NULL;
	int i = 0, j = 0;

	while (1)
	{
		if (fast_pointer == NULL)
			break;
		else if (fast_pointer->next == NULL)
			break;
		else
		{
			temp = slow_pointer;
			fast_pointer = fast_pointer->next->next;
			slow_pointer = slow_pointer->next;
			i += 2;
			j++;
		}
	}
	temp->next = NULL;
	head2 = reverse_list(&slow_pointer);
	return (i);
}
