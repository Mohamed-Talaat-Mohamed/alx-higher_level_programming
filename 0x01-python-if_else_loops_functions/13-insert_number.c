#include "lists.h"

/**
 * insert_node - a Function to insert node in a sorted list
 * @head: pointer to list
 * @number: input integer
 * Return: the new node address, (NULL) in fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = (*head);
	listint_t *ne_node;

	ne_node = malloc(sizeof(listint_t));
	if (ne_node == NULL)
		return (NULL);
	ne_node->n = number;
	ne_node->next = NULL;

	if (temp == NULL || ne_node->n < temp->n)
	{
		ne_node->next = temp;
		*head = ne_node;
		return (ne_node);
	}
	while (temp != NULL)
	{
		if (temp->next == NULL || ne_node->n < temp->next->n)
		{
			ne_node->next = temp->next;
			temp->next = ne_node;
			return (ne_node);
		}
		temp = temp->next;
	}
	return (NULL);
}
