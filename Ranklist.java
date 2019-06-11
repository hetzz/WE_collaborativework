package June11;
import java.util.HashMap;
import java.util.ArrayList;
import java.io.*;

public class Ranklist {
	
	public static void generateRankList() throws Exception {
		
		File file = new File("C:/Users/Bhumika/Desktop/bhumika/Week02Day01/ranklist.txt");

		BufferedReader br = new BufferedReader(new FileReader(file));

		String string1;
		HashMap <String, Integer> rollNumberAndMarks= new HashMap<String, Integer>();
		ArrayList <Integer> markList = new ArrayList<Integer>();
		ArrayList <String> nameList = new ArrayList<String>();
		while ((string1 = br.readLine()) != null) {
			rollNumberAndMarks.put(string1.substring(0, 5), Integer.parseInt(string1.substring(string1.length() - 3, string1.length() - 1)));
		}
	}

	public static void main(String[] args) {


	}

}
