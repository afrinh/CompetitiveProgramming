import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import java.lang.*;
import static org.junit.Assert.*;

public class Solution {
    static int count = 0;
    static int second_largest = 0;
    public static class BinaryTreeNode {

        public int value;
        public BinaryTreeNode left;
        public BinaryTreeNode right;

        public BinaryTreeNode(int value) {
            this.value = value;
        }

        public BinaryTreeNode insertLeft(int leftValue) {
            this.left = new BinaryTreeNode(leftValue);
            return this.left;
        }

        public BinaryTreeNode insertRight(int rightValue) {
            this.right = new BinaryTreeNode(rightValue);
            return this.right;
        }
    }

    public static int findSecondLargest(BinaryTreeNode rootNode) {
        if (rootNode == null || rootNode.left == null && rootNode.right == null)
            throw new IllegalArgumentException();
        count = 0;
        secondLargestUtil(rootNode);
        return second_largest;
    }
    static void secondLargestUtil(BinaryTreeNode node)
    {   
        if (node == null || count >= 2)
            return;
        secondLargestUtil(node.right); 
        count++;
        if (count == 2) {
            second_largest = node.value;
            return;
        }
        secondLargestUtil(node.left); 
    }

















    // tests

    @Test
    public void findSecondLargestTest() {
        final BinaryTreeNode root = new BinaryTreeNode(50);
        final BinaryTreeNode a = root.insertLeft(30);
        a.insertLeft(10);
        a.insertRight(40);
        final BinaryTreeNode b = root.insertRight(70);
        b.insertLeft(60);
        b.insertRight(80);
        final int actual = findSecondLargest(root);
        final int expected = 70;
        assertEquals(expected, actual);
    }

    @Test
    public void largestHasLeftChildTest() {
        final BinaryTreeNode root = new BinaryTreeNode(50);
        final BinaryTreeNode a = root.insertLeft(30);
        a.insertLeft(10);
        a.insertRight(40);
        root.insertRight(70).insertLeft(60);
        final int actual = findSecondLargest(root);
        final int expected = 60;
        assertEquals(expected, actual);
    }

    @Test
    public void largestHasLeftSubtreeTest() {
        final BinaryTreeNode root = new BinaryTreeNode(50);
        final BinaryTreeNode a = root.insertLeft(30);
        a.insertLeft(10);
        a.insertRight(40);
        final BinaryTreeNode b = root.insertRight(70).insertLeft(60);
        b.insertLeft(55).insertRight(58);
        b.insertRight(65);
        final int actual = findSecondLargest(root);
        final int expected = 65;
        assertEquals(expected, actual);
    }

    @Test
    public void secondLargestIsRootNodeTest() {
        final BinaryTreeNode root = new BinaryTreeNode(50);
        final BinaryTreeNode a = root.insertLeft(30);
        a.insertLeft(10);
        a.insertRight(40);
        root.insertRight(70);
        final int actual = findSecondLargest(root);
        final int expected = 50;
        assertEquals(expected, actual);
    }

    @Test
    public void descendingLinkedListTest() {
        final BinaryTreeNode root = new BinaryTreeNode(50);
        root.insertLeft(40).insertLeft(30).insertLeft(20);
        final int actual = findSecondLargest(root);
        final int expected = 40;
        assertEquals(expected, actual);
    }

    @Test
    public void ascendingLinkedListTest() {
        final BinaryTreeNode root = new BinaryTreeNode(50);
        root.insertRight(60).insertRight(70).insertRight(80);
        final int actual = findSecondLargest(root);
        final int expected = 70;
        assertEquals(expected, actual);
    }

    @Test(expected = Exception.class)
    public void exceptionWithTreeThatHasOneNodeTest() {
        final BinaryTreeNode root = new BinaryTreeNode(50);
        findSecondLargest(root);
    }

    @Test(expected = Exception.class)
    public void exceptionWithEmptyTreeTest() {
        findSecondLargest(null);
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