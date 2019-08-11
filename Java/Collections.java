import java.util.*;

//Basic explanation of collections, but there are several more collections not mentioned, and many helpful methods not demonstrated.
//Check out the Java API docs.
public class Collections {

  public static void main(String[] args) {

    //Arrays. Size set at runtime and cannot be changed
    int[] array1 = {3, 9, 6}; //Setting values at creation
    for (int x : array1) {
      System.out.print(x+" "); //3 9 6
    }
    System.out.println();
    Arrays.sort(array1);
    for (int x : array1) {
      System.out.print(x+" ");  //3 6 9
    }
    System.out.println();
    int[] array2 = new int[3]; //Array of size 3, default values (0 in this case)

    int[][] array3 = new int[3][3]; //2d array. 3X3 matrix
    array3[0][0] = 1;
    System.out.println(array3[0][0]); //1

    int[] array4 = array1; //Both now refer to the same object
    System.out.println(array4.equals(array1)); //True, compares if they point to the same object
    int[] arrayCopy = new int[3];
    System.arraycopy(array1, 0, arrayCopy, 0, array1.length);  //Copies values of the array
    System.out.println(Arrays.equals(array1, arrayCopy)); //True, compares values
    System.out.println();

    //ArrayLists. Act like resizable array. Stored in memory similar to an resizing-array (sequentially).
    ArrayList<Integer> myList = new ArrayList<>();
    myList.add(27);
    myList.add(49);
    System.out.println(myList); //[27, 49]
    myList.set(0, 29);
    System.out.println(myList); //[29, 49]
    myList.remove(0);
    System.out.println(myList);  //[49]
    myList.add(68);
    System.out.println(myList.get(1)); //68
    System.out.println(myList.indexOf(68)); //1
    myList.clear(); //myList is now empty
    System.out.println();


    //LinkedLists. Act as a normal Linked List, a collection of nodes with pointers to the next one.
    List<String> myList2 = new LinkedList<>();
    myList2.add("Bob");
    myList2.add("George");
    System.out.println(myList2); //[Bob, George]
    myList2.remove(0); //Removal by index
    System.out.println(myList2);  //[George]
    myList2.add("Sam");
    System.out.println(myList2.get(1)); //Sam
    System.out.println(myList2.indexOf("Sam")); //1
    myList2.remove("Sam"); //Removal of first match
    System.out.println(myList2);  //[George]

    //HashMap. Key-Val pair. UNORDERED. Order is not guaranteed
    Map<String, Integer> myMap = new HashMap<>();
    myMap.put("One", 1);
    myMap.put("Two", 2);
    myMap.put("Three", 3);
    System.out.println(myMap); //{One=1, Two=2, Three=3}
    System.out.println(myMap.get("Two")); //2
    System.out.println();

    //Oredered Collections support iterators
    Iterator<Integer> iterator1 = myList.iterator();
    while (iterator1.hasNext()) {
      System.out.println(iterator1.next());
    }
    System.out.println();

    //Ordered Collections support for:each
    for (Integer x : myList) {
     System.out.println(x);
    }


    //Use Set to get Ordered Collection of keys
    Set<String> keys = myMap.keySet();
    Iterator<String> iterator2 = keys.iterator();
    while (iterator2.hasNext()) {
      System.out.println(myMap.get(iterator2.next()));
    }
    System.out.println();

    //Ordered Collections support for:each
    for (String x : keys) {
      System.out.println(myMap.get(x));
    }

  }
}
