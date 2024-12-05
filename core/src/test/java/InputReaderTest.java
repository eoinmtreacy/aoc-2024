import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.IOException;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import core.InputReader;

public class InputReaderTest {
    @Test
    public void testReadInput() throws IOException {
        char[][] result = InputReader.readInput("src/test/resources/1.txt");
        assertEquals(6, result.length); 
    }

    @Test
    public void testReadInputAsInt() throws IOException {
        int[][] result = InputReader.readInputAsInt("src/test/resources/1.txt");
        assertEquals(6, result.length); 
        for (int[] row : result) {
            for (int i : row) System.out.print(i + " ");
            System.out.println();
        }
    }

    @Test 
    public void testReadTwoChunks() throws IOException {
        ArrayList<ArrayList<int[]>> chunks = InputReader.readTwoChunks("src/test/resources/chunk.txt");
        System.out.println(chunks.get(1));
    }
}
