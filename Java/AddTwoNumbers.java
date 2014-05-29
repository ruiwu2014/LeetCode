/*
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

*/



/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1 == null){
        	return l2;
        }
        if(l2 == null){
        	return l1;
        }
        int carry = 0;
        ListNode res = new ListNode(0);
		ListNode current = res;
        while(l1 != null || l2 != null){
        	int sub = (l1==null?0:l1.val) + (l2==null?0:l2.val) + carry;
        	carry = 0;
        	if(sub >= 10){
        		sub -= 10;
        		carry = 1;
        	}
        	ListNode next = new ListNode(sub);
        	current.next = next;
        	current = current.next;
        	l1 = l1==null?null:l1.next;
        	l2 = l2==null?null:l2.next;
        }
        if(carry>0){
        	ListNode next = new ListNode(carry);
        	current.next = next;
        }
        return res.next;
    }
}
