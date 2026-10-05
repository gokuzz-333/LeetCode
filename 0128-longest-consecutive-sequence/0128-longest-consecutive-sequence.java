class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set=new HashSet<>();
        for(int num:nums){
            set.add(num);
        }
        int longest=0;
        for(int value:set){
            if(set.contains(value-1)){
                continue;
            }
            int current=1;
            int next=value+1;
            while(set.contains(next)){
                current++;
                next++;
            }
            longest=Math.max(longest,current);
        }
        return longest;
    }
}