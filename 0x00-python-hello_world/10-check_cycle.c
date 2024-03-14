#include "lists.h"
/**
 * check_cycle - checks for a cycle
 * @list: pointer to a node in list'
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (list != NULL && temp != NULL)
	{
		list = list->next;
		temp = list->next;
		if (list == temp)
			return (1);
	}
	return (0);
}
