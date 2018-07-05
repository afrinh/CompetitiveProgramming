import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    public static boolean hasPalindromePermutation(String theString) {

        // check if any permutation of the input is a palindrome
        int M=26;
        int length=theString.length();
        int []freq=new int[M];
        // for(int i=0;i<M;i++)
        // {
        //     freq[i]=0;
        // }
        
        for (int i = 0; i < length; i++)
        freq[theString.charAt(i) - 'a']++;
 
        int odd = 0;
        for (int i = 0; i < M; i++)
          if (freq[i] % 2 == 1)
            odd++;
        
        if ((length % 2 == 1 && odd == 1 ) || (length %2 == 0 && odd == 0))
            return true;
        else
            return false;
    }


















    // tests

    @Test
    public void permutationWithOddNumberOfCharsTest() {
        final boolean result = hasPalindromePermutation("aabcbcd");
        assertTrue(result);
    }

    @Test
    public void permutationWithEvenNumberOfCharsTest() {
        final boolean result = hasPalindromePermutation("aabccbdd");
        assertTrue(result);
    }

    @Test
    public void noPermutationWithOddNumberOfChars() {
        final boolean result = hasPalindromePermutation("aabcd");
        assertFalse(result);
    }

    @Test
    public void noPermutationWithEvenNumberOfCharsTest() {
        final boolean result = hasPalindromePermutation("aabbcd");
        assertFalse(result);
    }

    @Test
    public void emptyStringTest() {
        final boolean result = hasPalindromePermutation("");
        assertTrue(result);
    }

    @Test
    public void oneCharacterStringTest() {
        final boolean result = hasPalindromePermutation("a");
        assertTrue(result);
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}