import java.util.ArrayList;
import java.util.Arrays;

public class Odometer {

	public static Boolean isDistinct(String str) {
		for (int i = 0; i < str.length() - 1; i++) {
			if (str.charAt(i) == str.charAt(i + 1))
				return false;
		}
		return true;
	}

	public static int generateSmallest(int numberOfDigits) {
		String str = "";
		for (int i = 1; i <= numberOfDigits; i++)
			str += i;
		return Integer.parseInt(str);
	}

	public static int generateLargest(int numberOfDigits) {
		String str = "";
		for (int i = 9 - numberOfDigits + 1; i <= 9; i++)
			str += i;
		return Integer.parseInt(str);
	}

	public static String convertToString(int number) {
		String str = "";
		String str1 = "";
		for (int x = number; x > 0; x /= 10)
			str += x % 10;

		for (int i = str.length() - 1; i >= 0; i--)
			str1 += str.charAt(i);

		return str1;
	}

	public static String sortDigits(String str) {
		char[] c_arr = str.toCharArray();
		Arrays.sort(c_arr);
		String sortedNumber = "";
		int arr[] = new int[c_arr.length];
		for (int i = 0; i < c_arr.length; i++) {
			sortedNumber += c_arr[i];
		}
		return sortedNumber;
	}

	public static ArrayList<Integer> generateList(int numberOfDigits) {
		int smallest = generateSmallest(numberOfDigits);
		int largest = generateLargest(numberOfDigits);

		ArrayList<Integer> list = new ArrayList<Integer>();

		for (int i = smallest; i <= largest; i++) {
			String str = sortDigits(convertToString(i));
			if (isDistinct(str)) {
				int number = Integer.parseInt(str);
				if (number == i)
					list.add(number);
			}
		}
		return list;
	}

	public static int findNext(int number) {
		ArrayList<Integer> readings = generateList(3);
		int i = readings.indexOf(number);
		return readings.get(i + 1);
	}

	public static int findPrevious(int number) {
		ArrayList<Integer> readings = generateList(3);
		int i = readings.indexOf(number);
		return readings.get(i - 1);
	}

	public static int findDifference(int number1, int number2) {
		ArrayList<Integer> readings = generateList(3);
		int largestIndex = readings.indexOf(generateLargest(3));
		String str = "";
		int i = readings.indexOf(number1);
		int j = readings.indexOf(number2);
		int count = 0;
		if (i < j)
			count = j - i;
		else
			count = readings.size() - (i - j);

		return count;
	}

	public static void main(String args[]) {
		System.out.println(generateList(3));
		System.out.println(findNext(129));
		System.out.println(findPrevious(234));
		System.out.println(findDifference(689, 123));
	}
}
