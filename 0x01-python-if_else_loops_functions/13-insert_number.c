#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: first element in linked list
 * @number: number to store in the new node
 * insert_after - inserts a new node at a point
 * @head: first element in linked list
 * @number: number to store in the new node
 * insert_beginning - insert at the beginning of list
 * @head: first element in linked list
 * @number: number to store in the new node
 * Return: pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *new;

	node = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (node->next != NULL)
	{
		if ((node->next)->n >= number)
		{
			new->next = node->next;
			node->next = new;
			return (new);
		}
		node = node->next;
	}
	new->next = NULL;
	node->next = new;
	return (new);
}
