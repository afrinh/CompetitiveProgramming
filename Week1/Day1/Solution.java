import java.util.*;
public class Solution 
{
    public static int highestProductOf3(int[] arr) 
    {
        Arrays.sort(arr);
        int x=1,y=1;
        if (arr[0]<0  && arr[1]<0)
        {
            x = arr[0]*arr[1];
        }
        int n = arr.length;
        x *= arr[n-1];
        y = arr[n-1]*arr[n-2]*arr[n-3];
        return Math.max(x,y);
    }

    public static void main(String[] args) {
    System.out.println(highestProduct3(new int[] {1, 2, 3, 4}));
    System.out.println(highestProduct3(new int[] {6, 1, 3, 5, 7, 8, 2}));
    System.out.println(highestProduct3(new int[] {-5, 4, 8, 2, 3}));
    System.out.println(highestProduct3(new int[] {-10, 1, 3, 2, -10}));
    System.out.println(highestProduct3(new int[] {-5, -1, -3, -2}));
}
}


    