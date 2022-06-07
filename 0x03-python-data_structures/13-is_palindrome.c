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

/**
 * comp_list - compares two singly linked lists
 * @l1: pointer to a listint_t list
 * @l2: pointer to a listint_t list
 * Return: 0 if list are not equal, 1 if they are equal
 */
int comp_list(listint_t *l1, listint_t *l2)
{
	int status = 0;
	listint_t *temp = l1;
	listint_t *temp2 = l2;

	while (l1 != NULL)
	{
		if (l1->n == l2->n)
		{
			status = 1;
		}
		else
		{
			status = 0;
			break;
		}
		l1 = l1->next;
		l2 = l2->next;
	}
	while (temp->next)
		temp = temp->next;
	temp->next = temp2;
	return (status);
}

/**
 * is_palindrome - checks if a singly linked list is a
 * palindrome
 * @head: pointer to a pointer to a singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast_pointer = *head;
	listint_t *slow_pointer = *head;
	listint_t *head2 = NULL;
	listint_t *temp = NULL;

	while (1)
	{
		if (fast_pointer == NULL)
			break;
		else if (fast_pointer->next == NULL)
			break;
		temp = slow_pointer;
		fast_pointer = fast_pointer->next->next;
		slow_pointer = slow_pointer->next;
	}
	temp->next = NULL;
	head2 = reverse_list(&slow_pointer);

	return (comp_list(*head, head2));
}
