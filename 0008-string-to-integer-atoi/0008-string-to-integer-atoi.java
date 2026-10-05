class Solution {

    public int myAtoi(String s) {

        int i = 0;
        int sign = 1;
        int ans = 0;

        // 1. Remove leading spaces
        while(i < s.length() && s.charAt(i) == ' ') {
            i++;
        }

        // 2. Check sign
        if(i < s.length() && s.charAt(i) == '-') {
            sign = -1;
            i++;
        }
        else if(i < s.length() && s.charAt(i) == '+') {
            i++;
        }

        // 3. Convert digits
        while(i < s.length() && 
              s.charAt(i) >= '0' && s.charAt(i) <= '9') {

            int digit = s.charAt(i) - '0';

            // 4. Check overflow
            if(ans > (Integer.MAX_VALUE - digit) / 10) {
                if(sign == 1)
                    return Integer.MAX_VALUE;
                else
                    return Integer.MIN_VALUE;
            }

            ans = ans * 10 + digit;
            i++;
        }

        return ans * sign;
    }
}