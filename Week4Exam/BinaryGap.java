import java.util.*;
public class BinaryGap
{
	static ArrayList<Integer>res = new ArrayList<>();
	public static void Binary(int n)
	{
		if(n==0)
		{
			res.add(0);
			return;
		}
		else if(n==1)
		{
			res.add(1);
			return;
		}
		else
		{
			int c=0;
			while(n!=1)
			{
				int a = n%2;
				n = n/2;
				if(a==1)
					c++;
				if(n==1)
					c++;
			}
			res.add(c);
		}
	}
	public static void main(String[] args)
	{
		int num = 6;
		for(int i=0;i<=num;i++)
			{
				Binary(i);
			}
			System.out.println(Arrays.toString(res.toArray()));
		}
	}