import java.util.Arrays;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PartTwo {
    public static boolean active = true;

    public static int main(char[][] input) {
        return Arrays.stream(input)
                        .map(line -> extract(line))
                        .mapToInt(line -> multiply(line))
                        .sum();
    }

    public static ArrayList<String> extract(char[] line) {

        ArrayList<String> cleaned = new ArrayList<>();

        Pattern pattern = Pattern.compile("mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don\\'t\\(\\)");
        Matcher matcher = pattern.matcher(new String(line));
        
        while(matcher.find()) {
            cleaned.add(matcher.group());
        }
        System.out.println(cleaned);

        return cleaned;
    }

    public static int multiply (ArrayList<String> strings) {
        int result = 0;
        for (String s: strings) {
            if (s.equals("don't()")) {
                active = false;
                continue;
            }

            if (s.equals("do()")) {
                active = true;
            }

            if (active && !s.equals("do()") && !s.equals("don't()")) {
                // split it on the ','
                String[] halves = s.split(",");
                // remove everything that isn't a number
                String left = halves[0].replaceAll("[^0-9]", "");
                String right = halves[1].replaceAll("[^0-9]", "");
                // multiply each number
                result += (Integer.parseInt(left) * Integer.parseInt(right));
    
            }
       }

        return result;
    }
}
