class Solution {
    public boolean rotateString(String s, String goal) {
        if(s == null || goal == null) {
            //throw exception on A and B both being null?
            return false;
        }
        if(s.length() == 0) {
            return true;
        }
        if(s.length()!=goal.length()){
            return false;
        }
        String doubled=s+s;
        return doubled.contains(goal);
    }
}