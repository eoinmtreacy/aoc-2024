package core; 

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
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
}