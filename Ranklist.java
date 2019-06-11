package June11;
import java.util.HashMap;
import java.util.ArrayList;
import java.io.*;
import java.util.Collections;

public class Ranklist {
	
	
	public static void generateRankList() throws Exception {
		
		File file = new File("C:/Users/Bhumika/Desktop/bhumika/Week02Day01/ranklist.txt");

		BufferedReader br = new BufferedReader(new FileReader(file));

		String string1;
		HashMap <String, Integer> rollNumberAndMarks= new HashMap<String, Integer>();
		ArrayList <Integer> markList = new ArrayList<Integer>();
		ArrayList <String> nameList = new ArrayList<String>();
		while ((string1 = br.readLine()) != null) {
//			markList.add(Integer.parseInt(string1.substring(string1.length() - 3, string1.length() - 1)));
//			nameList.add(string1.substring(0, 5));
			rollNumberAndMarks.put(string1.substring(0, 5), Integer.parseInt(string1.substring(string1.length() - 3, string1.length() - 1)));
		}
		
		HashMap<String, Integer> sorted = rollNumberAndMarks;
		
	    sorted = rollNumberAndMarks
	            .entrySet()
	            .stream()
	            .sorted(Collections.reverseOrder(HashMap.Entry.comparingByValue()))
	            .collect(
	                toMap(HashMap.Entry::getKey, HashMap.Entry::getValue, (e1, e2) -> e2,
	                    HashMap::new));
		
		
	}

	public static void main(String[] args) {


	}

}
