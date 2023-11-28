#include <stdlib.h>
#include "lists.h"

/**
 * find_listint_loop - find loop in listed link
 * @head: pointer to head of list
 * Return: 1 if there is no cycle, 0 otherwise
 */

int *find_listint_loop(listint_t *head)
{
	listint_t *fast, *slow;

	slow = head->next;
	fast = head->next->next;
	while (fast)
	{
		if (slow == fast)
		{
			slow = head;
			while (slow != fast)
			{
				slow = slow->next;
				fast = fast->next;
			}
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
