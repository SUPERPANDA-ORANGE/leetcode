class Solution {
public:
    /*
     * @param numbers: An array of Integer
     * @param target: target = numbers[index1] + numbers[index2]
     * @return: [index1 + 1, index2 + 1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &numbers, int target) {
        // write your code here
        for(int index = 0; index<numbers.size();index++){
            for(int i=1; i<numbers.size()-index ; i++){
                if(numbers[index]+numbers[index+i] == target){
                    vector<int> result(2);
                    result.push_back(index+1);
                    result.push_back(index+1+i);
                    return result;
                }
                else{
                    
                }
            }
        }
        
    }
};