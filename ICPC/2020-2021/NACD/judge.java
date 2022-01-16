import java.util.*;
import java.io.*;
import java.util.stream.IntStream;
public class judge {
    public static void main(String[] args)throws FileNotFoundException{
        //Scanner in = new Scanner(new File("in.txt"));
        Scanner in = new Scanner(System.in);
        int ans=0;        
        int num=0;
        int add1=0;
        int add2=0;
        int[] tokens = new int[3];
        String[] s;
        
        int numsRead = 0;
        while (in.hasNextLine()) {
            s = in.nextLine().split("\\s+");

            for (int i = 0; i < s.length; i++) {
                if (s[i].length() > 0 && s[i].charAt(0) != '0') {
                    try {
                        for (int j = 0; j < s[i].length(); j++) {
                            if (s[i].charAt(j) < 48 || s[i].charAt(j) > 57) {
                                System.out.println("0");
                                return;
                            }
                        }
                        int x = Integer.parseInt(s[i]);
                        tokens[numsRead] = x;
                        numsRead++;
                    }
                    catch (Exception e) {
                        System.out.println("0");
                        return;
                    }
                }
            }
        }
        if (numsRead < 3) {
            System.out.println("0");
            return;
        }

        num = tokens[0];
        add1 = tokens[1];
        add2 = tokens[2];


        if(num%2 == 0 && num > 3 && num <= Math.pow(10,9) && add2 > 0 && add1 > 0 && add1 + add2 == num){
            if(isPrime(add1) && isPrime(add2)){
                ans=1;
            }
        }
        System.out.println(ans);
    }

    public static boolean isPrime(int number) {
        if(number <= 2)
            return number == 2;
        else
            return  (number % 2) != 0
                    &&
                    IntStream.rangeClosed(3, (int) Math.sqrt(number))
                    .filter(n -> n % 2 != 0)
                    .noneMatch(n -> (number % n == 0));
    }

}