import java.util.*;
import java.io.*;
public class Template {
    public static void main(String[] args) throws Exception{
        //Scanner in = new Scanner(new File("in.txt"));
        Scanner in = new Scanner(System.in);
        int[] nums = stringToInt(in.nextLine());
    }
    public static int[] stringToInt(String s){
        String[] arr = s.split(" ");
        int [] intArr = new int[arr.length];
        for(int i=0;i<arr.length;i++){
            intArr[i]=Integer.parseInt(arr[i]);
        }
        return intArr;
    }

}
