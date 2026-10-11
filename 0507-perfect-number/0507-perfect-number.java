class Solution {
    public boolean checkPerfectNumber(int num) {
        if(num<=1){
            return false;
        }
        int ans=1;
        for(int i=2;i<=Math.sqrt(num);i++){
            if(num%i==0){
                ans+=i;
                if((num/i)!=i){
                    ans+=num/i;
                 }
            }

        }
        if(ans==num){
            return true;
        }
        else{
            return false;
        }
    }
}