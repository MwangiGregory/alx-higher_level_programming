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
