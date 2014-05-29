/*
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
*/
public class Solution {
    public String addBinary(String a, String b) {
        int lenA = a.length();
        int lenB = b.length();
        if(lenA==0){
            return b;
        }
        if(lenB == 0){
            return a;
        }
        String res = "";
        boolean carry = false;
        int i = lenA-1;
        int j = lenB-1;
        while(i>=0 || j>=0){
            char c1 = i>=0?a.charAt(i):'0';
            char c2 = j>=0?b.charAt(j):'0';
            if(c1=='1'&&c2=='1'){
                res = (carry?"1":"0")+res;
                carry = true;
            }
            else if(c1=='0'&&c2=='0'){
                res = (carry?"1":"0")+res;
                carry = false;
            }
            else{
                if(carry){
                    res = "0" + res;
                }
                else{
                    res = "1" + res;
                }
            }
            i--;
            j--;
        }
        if(carry){
            res = "1" + res;
        }
        return res;
    }
}
