import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.IOException;

import org.junit.jupiter.api.Test;

import core.InputReader;

public class InputReaderTest {
    @Test
    public void testReadInput() throws IOException {
        char[][] result = InputReader.readInput("src/test/resources/1.txt");
        assertEquals(7, result.length); 
    }	 
}
