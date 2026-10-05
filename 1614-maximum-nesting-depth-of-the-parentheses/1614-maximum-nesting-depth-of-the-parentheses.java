class Solution {
    public int maxDepth(String s) {
        int count=0;
        int longest=0;
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if(ch=='('){
                count++;
            }
            if(ch==')'){
                longest=Math.max(longest,count);
                count--;
            }
            else{
                continue;
            }
        }
        return longest;
    }
}