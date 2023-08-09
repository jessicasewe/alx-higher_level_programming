#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @List: linked list to check
 *
 * Return: 1 if the list has a cyckle, 0 if it doesnt
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return 1;
	}
	return 0;
}
