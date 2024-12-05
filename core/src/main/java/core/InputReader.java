package core; 

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class InputReader {
    public static char[][] readInput(String filePath) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(filePath));
        char[][] result = new char[lines.size()][];
        for (int i = 0; i < lines.size(); i++) {
            result[i] = lines.get(i).toCharArray();
        }
        return result;
    }

    public static int[][] readInputAsInt(String filePath) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(filePath));
        int[][] result = new int[lines.size()][];
        for (int i = 0; i < lines.size(); i++) {
            String[] parts = lines.get(i).split("\\s+");
            result[i] = new int[parts.length];
            for (int j = 0; j < parts.length; j++) {
                result[i][j] = Integer.parseInt(parts[j]);
            }
        }
        return result;
    }

    public static ArrayList<ArrayList<int[]>> readTwoChunks(String filePath) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(filePath));
        ArrayList<ArrayList<int[]>> result = new ArrayList<>();

        int i = 0;
        ArrayList<int[]> rules = new ArrayList<>();
        while (!lines.get(i).equals("")) {
            System.out.println(lines.get(i));
            String[] parts = lines.get(i).split("\\|");
            int[] partsInts = new int[parts.length];
            for (int j = 0; j < parts.length; j++) {
                partsInts[j] = Integer.parseInt(parts[j]);
            }
            rules.add(partsInts);
            i++;
        }
        result.add(rules);
        i++;

        ArrayList<int[]> intLines = new ArrayList<>();
        while (i < lines.size()) {
            String[] parts = lines.get(i).split("\\,");
            int[] partsInts = new int[parts.length];
            for (int j = 0; j < parts.length; j++) {
                partsInts[j] = Integer.parseInt(parts[j]);
            }
            intLines.add(partsInts);
            i++;
        }
        result.add(intLines);

        return result;
    }
}