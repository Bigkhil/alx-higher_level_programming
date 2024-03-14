#include "lists.h"
/**
 * check_cycle - checks for a cycle
 * @list: pointer to a node in list'
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *temp1 = list;

	while (list != NULL)
	{
		temp1 = list;
		list = list->next;
		if (list == temp || list == temp1)
			return (1);
	}
	return (0);
}
