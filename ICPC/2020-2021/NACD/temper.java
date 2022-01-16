import java.util.*;
import java.io.*;
public class temper {
    public static void main(String[] args) throws Exception{
        //Scanner in = new Scanner(new File("in.txt"));
        System.out.println(prime(29));
        
        System.out.println(prime(31));
    }
    public static boolean prime(int num){
        boolean flag = false;
    for (int i = 2; i <= num / 2; ++i) {
      // condition for nonprime number
      if (num % i == 0) {
        flag = true;
        break;
      }
    }
    return !flag;
    }

}