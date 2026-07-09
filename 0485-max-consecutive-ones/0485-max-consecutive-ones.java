class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int ones=0;
        int max=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==1){
                ones++;
            }
            if(nums[i]==0||i==nums.length-1){
                max=Math.max(max,ones);
                ones=0;
            }
        }
        return max;
    }
}