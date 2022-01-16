import java.util.*;
import java.io.*;
public class Friends {
    public static void main(String[] args) throws Exception{
        //Scanner in = new Scanner(new File("in.txt"));
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long[] friends = new long[n];
        for(int i=0;i<n;i++){
            friends[i]=in.nextInt();
        }        
        for(int i=0;i<n;i++){
            ArrayList<Long> l=new ArrayList<Long>();
            l.add(friends[i]);
            int j=0;
            boolean works=true;
            while(j<n&&works){
                for(int x=0;x<l.size();x++){
                    
                }
            }
        }
    }

}