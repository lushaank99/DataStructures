
public class Radix 
{
	public static int max(int a[], int n)
	{
	      int max = a[0], i;
	      for(i = 1; i < n; i++)
	      {
	            if(max < a[i])
	            max = a[i];
	      }
	      return max;
	}
	public static int a[]=new int[10];
	public static void RadixSort(int n)
	{
	      int bucket[][]=new int[10][10];
	      int bucket_cnt[]=new int[10];
	      int i, j, k, r, NOP=0, divisor=1, lar, pass;
	     
	      lar=max(a, n);
	      System.out.println("The largest element is : "+lar);
	      
	      while(lar > 0)
	      {
	            NOP++;
	            lar/=10;
	      }
	      //System.out.println("Numer of passes "+NOP);
	      /*Initialize the buckets*/
	      for(pass = 0; pass < NOP; pass++)
	      {
	            for(i = 0; i < 10; i++)
	            {
	                  bucket_cnt[i] = 0;
	            }
	            
	            for(k = 0; k < 10; k++)
	            {
	            	for(j = 0; j <10; j++)
	            	{
	            		bucket[k][j]=0;
	            	}
	            }
	            //sort the numbers according to the digit & place it into specified bucket
	            System.out.println("no\tdig\tcount");
	            for(i = 0; i < n; i++)
	            {
	                r = (a[i] / divisor) % 10;
	            	//System.out.println(a[i]+"\t"+r);
	                bucket[r][bucket_cnt[r]] = a[i];
	                bucket_cnt[r] += 1;
	                System.out.println(a[i]+"\t"+r+"\t"+bucket_cnt[r]);
	            }
	            
	            System.out.println("--------------------------------------");
	            for(k = 0; k < 10; k++)
	            {
	            	for(j = 0; j <10; j++)
	            	{
	            		System.out.print(bucket[k][j]+"\t");
	            	}
	            	System.out.println();
	            }
	            System.out.println("--------------------------------------");

	            //Collect the numbers after completed each pass
	            i = 0;
	            for(k = 0; k < 10; k++)
	            {
	            	for(j = 0; j < bucket_cnt[k]; j++)
	            	{
	            		a[i] = bucket[k][j];
	            		//System.out.println(bucket[k][j]);
	            		i++;
	            	}
	            }
	            
	            divisor *= 10;
	            System.out.println("\n Numbers after completing pass " + (pass+1));
	            for(i = 0; i < n; i++)
	            	System.out.print(a[i]+" ");
	            System.out.println("\n");
	      }
	}

	public static void main(String[] args) 
	{
		a[0]=123;
		a[1]=333;
		a[2]=456;
		a[3]=74;
		a[4]=68;
		a[5]=91;
		
		for(int i=0;i<6;i++)
		{
			System.out.print(a[i]+" ");
		}
		System.out.println();
		RadixSort(6);
	}
}
