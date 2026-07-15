class Solution {
    public void sortColors(int[] nums) {
        int count0=0;
        int count1=0;
        int count2=0;
        for(int num:nums){
            if(num==0) count0++;
            if(num==1) count1++;
            if(num==2) count2++;
        }
        for(int i=0;i<count0;i++){
            nums[i]=0;
        }
        for(int j=count0;j<count1+count0;j++){
            nums[j]=1;
        }

        for(int k=count0+count1;k<nums.length;k++){
            nums[k]=2;
        }
        return ;
    }
}