#include "lists.h"
/**
 * print_dlistint - function to print nodes of linked list
 * @h: pointer to node
 * Return: size_t
 */
size_t print_dlistint(const dlistint_t *h)
{
	int x;

	while (h != NULL)
	{
		printf(h->n);
		x++;
		h = h->next;
	}
	return (x);
}
