/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int->val;
 *     ListNode *next;
 *     ListNode(int x) :->val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * @param l1: the first list
     * @param l2: the second list
     * @return: the sum list of l1 and l2 
     */
    ListNode *addLists(ListNode *l1, ListNode *l2) {
        // write your code here
        ListNode *head_1 = l1;
        ListNode *head_2 = l2;
        if(l1 = NULL){return l2;}
        if(l2 = NULL){return l1;}
        while((head_1->next != NULL) || (head_2->next != NULL))
        {
            if(head_1->next == NULL){
                head_1->next = new ListNode(0);
            }
            if(head_2->next == NULL){
                head_2->next = new ListNode(0);
            }
            
            int temp = head_1->val + head_2->val;
            if(temp >=10){
                temp = temp%10;
                head_1->val = temp;
                head_1->next->val +=1;
            }
            else{
                head_1->val = temp;
            }
            head_1 = head_1->next;
            head_2 = head_2->next;
        }
        if((head_1->next == NULL )&& (head_2->next == NULL)){
            int temp = head_1->val + head_2->val;
            head_1->val = temp;
            if(temp>=10){
                head_1->val = (temp%10);
                head_1->next = new ListNode(1);
            }
            return l1;
        }
    }
};