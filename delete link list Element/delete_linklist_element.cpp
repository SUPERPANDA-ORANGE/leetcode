/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


class Solution {
public:
    /*
     * @param head: a ListNode
     * @param val: An integer
     * @return: a ListNode
     */
    ListNode * removeElements(ListNode * head, int val) {
        // write your code here
        ListNode *p = head;
        if(p == NULL){
            return NULL ;
        }
        else if (p->next== NULL){
            if(p->val == val){
                return NULL;
            }
            else{
                return head;
            }
        }
        //else if(p->val == val && p->next != NULL){
            
        //}
        else{
            ListNode *p2 = p->next;
            if(p2->next==NULL&&p==head){
                if(p->val == val && p2->val != val){head= head->next;return head;}
                if(p2->val == val && p->val != val){p->next = NULL; return head;}
                if(p2->val == val && p->val == val){return NULL;}
                if(p2->val != val && p->val != val){return head;}
            }
            while(p2->next!=NULL){
                if(p2->val == val){
                    p->next = p2->next;
                    p2 = p2->next;
                }
                else {
                    p = p->next;
                    p2 = p2->next;
                }
            }
            if(p2->next == NULL){
                if(p2->val == val){
                    p->next = NULL;
                    return head;
                }
                else{return head;}
            }
        }
        
    }
};