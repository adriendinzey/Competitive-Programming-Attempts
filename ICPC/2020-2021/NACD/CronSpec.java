import java.util.*;
import java.io.*;
public class CronSpec {
    public static void main(String[] args) throws Exception{

        boolean[] secondsOfTheDay = new boolean[24*60*60];
        int totalEvents = 0;

        //Scanner in = new Scanner(new File("in.txt"));
        Scanner in = new Scanner(System.in);

        int numsLines = stringToInt(in.nextLine())[0];
        
        for (int line = 0; line < numsLines; line++) {
            boolean[] hours = new boolean[24];
            boolean[] minutes = new boolean[60];
            boolean[] seconds = new boolean[60];

            String[] nums = in.nextLine().split(" ");

            int numHours = 0;
            String hoursStr = nums[0];
        
            String[] hourToksStr = hoursStr.split(",");
            for (int i = 0; i < hourToksStr.length; i++) {
                if (hourToksStr[i].equals("*")) {
                    numHours = 24;
                    for (int j= 0; j < 24; j++) {
                        hours[j] = true;
                    }
                }
                else if (hourToksStr[i].contains("-")) {
                    int rangeLow = Integer.parseInt(hourToksStr[i].split("-")[0]);
                    int rangeHigh = Integer.parseInt(hourToksStr[i].split("-")[1]);

                    numHours += rangeHigh - rangeLow + 1;
                    for (int j = rangeLow; j <= rangeHigh; j++) {
                        hours[j] = true;
                    }
                }
                else {
                    numHours++;
                    hours[Integer.parseInt(hourToksStr[i])] = true;
                }
            }

            int numMinutes = 0;
            String minutesStr = nums[1];
        
            String[] minuteToksStr = minutesStr.split(",");
            for (int i = 0; i < minuteToksStr.length; i++) {
                if (minuteToksStr[i].equals("*")) {
                    numMinutes = 60;
                    for (int j= 0; j < 60; j++) {
                        minutes[j] = true;
                    }
                }
                else if (minuteToksStr[i].contains("-")) {
                    int rangeLow = Integer.parseInt(minuteToksStr[i].split("-")[0]);
                    int rangeHigh = Integer.parseInt(minuteToksStr[i].split("-")[1]);

                    numMinutes += rangeHigh - rangeLow + 1;
                    for (int j = rangeLow; j <= rangeHigh; j++) {
                        minutes[j] = true;
                    }
                }
                else {
                    numMinutes++;
                    minutes[Integer.parseInt(minuteToksStr[i])] = true;
                }
            }

            int numSeconds = 0;
            String secondsStr = nums[2];
        
            String[] secondToksStr = secondsStr.split(",");
            for (int i = 0; i < secondToksStr.length; i++) {
                if (secondToksStr[i].equals("*")) {
                    numSeconds = 60;
                    for (int j= 0; j < 60; j++) {
                        seconds[j] = true;
                    }
                }
                else if (secondToksStr[i].contains("-")) {
                    int rangeLow = Integer.parseInt(secondToksStr[i].split("-")[0]);
                    int rangeHigh = Integer.parseInt(secondToksStr[i].split("-")[1]);

                    numSeconds += rangeHigh - rangeLow + 1;
                    for (int j = rangeLow; j <= rangeHigh; j++) {
                        seconds[j] = true;
                    }
                }
                else {
                    numSeconds++;
                    seconds[Integer.parseInt(secondToksStr[i])] = true;
                }
            }

            for (int hour = 0; hour < 24; hour++) {
                if (hours[hour]) {

                    for (int minute = 0; minute < 60; minute++) {
                        if (minutes[minute]) {
                            
                            for (int second = 0; second < 60; second++) {
                                if (seconds[second]) {
                                    
                                    secondsOfTheDay[hour*60*60+minute*60+second] = true;
        
                                }
                            }

                        }
                    }

                }
            }

            totalEvents += numHours*numMinutes*numSeconds;
        }

        int distinct = 0;
        for (int i = 0; i < 24*60*60; i++) {
            if (secondsOfTheDay[i]) {
                distinct++;
            }
        }

        System.out.println(distinct + " " + totalEvents);
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