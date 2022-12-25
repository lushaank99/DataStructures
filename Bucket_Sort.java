
public class Bucket_Sort 
{

	public static int array[]=new int[14];
	public static void Bucket(int n)
	{
		int i, j, k;
		int buckets[]=new int[n];
	    
	    for(i = 0; i < n; ++i)
	        buckets[i] = 0;
	    
	    for(i = 0; i < n; ++i)
	        buckets[array[i]]++;
	    
	    for(i=0;i<n;i++)
	    {
	    	System.out.print(buckets[i]+"\t");
	    }
	    System.out.println();
	        
	    for(i = 0, j = 0; j < n; j++)
	    {
	    	//System.out.println("Bucket: "+"\t"+j+"\t"+buckets[j]);
	        for(k = buckets[j]; k > 0; k--)
	        {
	        	array[i] = j;
	        	i++;
	        }
	    }
	}
	public static void main(String[] args) 
	{
		array[0]=4;
		array[1]=4;
		array[2]=2;
		array[3]=1;
		array[4]=2;
		array[5]=0;
		array[6]=3;
		array[7]=2;
		array[8]=1;
		array[9]=4;
		array[10]=0;
		array[11]=2;
		array[12]=3;
		array[13]=0;
		
		print();
		Bucket(14);
		print();

	}
	public static void print()
	{
		for(int i=0;i<14;i++)
		{
			System.out.print(array[i]+"\t");
		}
		System.out.println();
	}
}
