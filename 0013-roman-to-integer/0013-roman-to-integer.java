class Solution {
    public int romanToInt(String s) {
        int result=0;
        Map<Character,Integer> map= Map.of(
            'I',1,'V',5,'X',10,'L',50,'C',100,'D',500,'M',1000
            );
        for(int i=0;i<s.length();i++){
            int curr=map.get(s.charAt(i));
            int next=(i<s.length()-1)?map.get(s.charAt(i+1)):0;

            if(curr<next){
                result=result-curr;
            }
            else{
                result=result+curr;
            }
        }
        return result;
}
}