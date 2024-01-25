# My Java Notes

# To-Do

- UpCasting and Downcasting Concepts with examples (https://www.youtube.com/watch?v=fJzf0Gm0G6U and https://www.youtube.com/watch?v=HpuH7n9VOYk)
- Complete String and Character Methods
- Add conversion btw int and Integer, char and Character, int[] and Integer[], char[] and Character[] (If any exists)
- Public vs Protected vs Private vs Default (https://www.geeksforgeeks.org/protected-keyword-in-java-with-examples/)
- super keyword use in inheritance with examples (super with protected or private?)
- Scan and see if anything useful or new: https://youtu.be/VE_AAUxTUCY?si=FTTgYSHG4xaKhqIo and https://youtu.be/rzA7UJ-hQn4?si=_XPw3Yo3oN1uTImk
- Time Constraint & Complexity Relationship:(https://www.youtube.com/shorts/6j8uLDZMXUg)
- Java Interview Concepts: https://www.youtube.com/watch?v=auCdqGdn2as

# Print in Java

```java
    public static final <T> void print(T t) {
        System.out.println(t);
    }
```

# size() vs length() vs length

```java
        List<Integer> list = new ArrayList<>();
        list.size(); // size of collection - Size method is invoked on an instance of list object and it operates on state of the list object

        String string = "";
        string.length(); // length of string - Not a collection, it's an immutable sequence of characters

        Integer[] array = new Integer[10];
        array.length; // length is a property of array. - Fixed length that is determined when the array is created which can't be changed
```

# String

### Split String with delimiter

```java
    public static String[] splitString(String str) {
        String[] result = str.split(",");
        return result;
    }

    public static String[] splitWithoutEmptyString(String arg1) {
        ArrayList<String> split = new ArrayList<>();
        for (String str : arg1.split("/")) {
            if (!str.equals("")) {
                split.add(str);
            }
        }
        // Convert ArrayList to String[]
        return split.toArray(new String[split.size()]);
    }
```

### Reverse String via StringBuilder

```java
    public static String reverseString(String str) {
        return new StringBuilder(str).reverse().toString();
    }
```

### Sort String Characters

```java
    // Method 1 (Short)
    public static String sortString(String s) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars); // Sorts in place
        return new String(chars);
    }

    // Method 2 (Long)
    public static String sortString(String s) {
        return new String(s.toCharArray())
                .chars()
                .sorted()
                .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append)
                .toString();
    }

    // Method 3 (Using stream)
    public static String sortString(String s) {
        return s.chars()
                .mapToObj(i -> (char) i)
                .sorted(Comparator.comparing(Character::charValue))
                .collect(Collectors.toList())
                .toString();
    }

    // Method 4 (Using stream and List)
    public static String sortString(String s) {
        List<Character> list = new ArrayList<>();
        for (Character c : s.toCharArray()) {
            list.add(c);
        }
        return list.stream()
                .sorted(Comparator.comparing(Character::charValue))
                .collect(Collectors.toList())
                .toString();
    }
```

### String Methods

#### toCharArray()

#### charAt()

#### substring()

#### toLowerCase()

#### toUpperCase()

#### compareTo() vs equals()

# Character

### Methods

#### isLetter()

#### isAlphabetic()

#### isLowerCase()

#### isUpperCase()

#### isDigit()

# Conversions

### 1. (int or Integer) & String

#### (int or Integer) to String

```java
        int num = 123;
        Integer number= 123;
        String str = String.valueOf(num);
        String string = number.toString();
```

#### String to (int or Integer)

```java
        String str = "123";
        int num = Integer.parseInt(str);
        Integer number = Integer.valueOf(str);
```

### 2. List to Array

#### List to int Array

```java
    public static int[] listToInt(List<Integer> list) {
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
```

#### List to Integer Array

```java
    public static Integer[] listToInteger(List<Integer> list) {
        return list.stream().toArray(Integer[]::new);
    }
```

### 3. Array to List

#### int Array to List

```java
    public static List<Integer> intToList(int[] arr) {
        return Arrays.stream(arr).boxed().collect(Collectors.toList());
    }
```

#### Integer Array to List

```java
    public static List<Integer> integerToList(Integer[] arr) {
        return Arrays.asList(arr);
    }
```

### 4. String[] & ArrayList

#### String[] to ArrayList

```java
    // One Liner
    public static ArrayList<String> stringArrayToArrayList(String[] array) {
        return new ArrayList<>(Arrays.asList(array));
    }

    // Vanilla
    public static ArrayList<String> stringArrayToArrayList(String[] array) {
        ArrayList<String> list = new ArrayList<>();
        for (String str : array) {
            list.add(str);
        }
        return list;
    }
```

#### ArrayList to String[]

```java
    // One Liner
    public static String[] arrayListToStringArray(ArrayList<String> list){
        return list.toArray(new String[list.size()]);
    }

    // Vanilla
    public static String[] arrayListToStringArray(ArrayList<String> list) {
        String[] array = new String[list.size()];
        for (int i = 0; i < list.size(); i++) {
            array[i] = list.get(i);
        }
        return array;
    }
```

### 5. char[] & String

#### char[] to String

```java
    public static String charArrayToString(char[] charArray) {
        String str;

        // Method 1 (Using Enhanced For Loop)
        str = "";
        for (char c : charArray) {
            str += c;
        }

        // Method 2 (Using String valueOf method)
        str = String.valueOf(charArray);

        // Method 3 (Creating new String Object)
        str = new String(charArray);

        return str;
    }
```

#### String to char[]

```java
    public static char[] stringToCharArray(String str) {
        char[] charArray = str.toCharArray();
        return charArray;
    }
```

### 6. char[] & int

#### char[] to int

```java
    public static int charArrayToInt(char[] charArray) {
        int n;
        // Method 1 (Using String valueOf method)
        n = Integer.parseInt(String.valueOf(charArray));

        // Method 2 (Creating new String Object)
        n = Integer.parseInt(new String(charArray));
        return n;
    }
```

#### int to char[]

```java
    public static char[] intToCharArray(int n) {
        char[] charArray = String.valueOf(n).toCharArray();
        return charArray;
    }
```

# Map

### Initialisation

```java
   // Method 1 (Vanilla)
   Map<String, Integer> map = new HashMap<>();
   Map<String, Integer> map = new TreeMap<>(); // sorts by key or custom comparator
   Map<String, Integer> map = new LinkedHashMap<>(); // maintains insertion order


   // Method 2 (Returns Immutable Object)
   Map<String, Integer> map = Map.of("key1", 1, "key2", 2, "key3", 3);

   // Method 3 (Returns Mutable Object)
   Map<String, Integer> map = new HashMap<>() {
       {
           put("key1", 1);
           put("key2", 2);
           put("key3", 3);
       }
   };
```

### Size

```java
        // Size of Map
        int size = map.size();
```

### Add

```java
        // Insert or Override One Element in Map
        map.put("key", "value");
```

### Remove

```java
        // Remove One Element in Map
        map.remove("key");
```

### Contains

```java
        // Check if Map contains key
        boolean flag = map.containsKey("key");

        // Check if Map contains value
        boolean flag = map.containsValue("value");
```

### Get

```java
        // Get Element in Map
        String value = map.get("key");
        String value = map.getOrDefault("key", "defaultValue");
```

### Entry

#### Iterate

```java
        HashMap<Integer, Integer> map = new LinkedHashMap<Integer, Integer>();


        // Method 1 (Vanilla Using Index)
        /*
         * NOT POSSIBLE
         */


        // Method 2 (Vanilla Enhanced For Loop)
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey() + "-" + entry.getValue());
        }


        // Method 3 (Vanilla Enhanced For Loop Function Iteration)
        public static <K, V> void printMap(Map<K, V> map) {
            for (Map.Entry<K, V> entry : map.entrySet()) {
                System.out.println(entry.getKey() + "-" + entry.getValue());
            }
        }


        // Method 4 (Using ForEach Loop)
        map.forEach((key, value) -> {
            System.out.println(key + "-" + value);
        });


        // Method 5 (Using stream)
        map.entrySet().stream().forEach(entry -> {
            System.out.println(entry.getKey() + "-" + entry.getValue());
        });
```

### Key

#### Iterate

```java
        HashMap<Integer, Integer> map = new LinkedHashMap<Integer, Integer>();


        // Method 1 (Vanilla Using Index)
        /*
         * NOT POSSIBLE
         */


        // Method 2 (Vanilla Enhanced For Loop)
        for (Integer key : map.keySet()) {
            System.out.println(key);
        }


        // Method 3 (Using ForEach Loop)
        map.keySet().forEach(key -> {
            System.out.println(key);
        });


        // Method 4 (Using stream)
        map.keySet().stream().forEach(key -> {
            System.out.println(key);
        });
```

#### Sum

```java
        HashMap<Integer, Integer> map = new LinkedHashMap<Integer, Integer>();

        // Method 1 (Vanilla Iteration)
        Integer sum = 0;
        for (Integer key : map.keySet()) {
            sum += key;
        }

        // Method 2 (Using ForEach Loop)
        /*
         * NOT POSSIBLE as variables declared outside the ForEach loop should be
         * effectively final if used inside the ForEach loop. Meaning that value can NOT
         * be changed.
         */

        // Method 3 (Using stream with keySet)
        Integer sum = map.keySet()
                .stream()
                .map(Integer::intValue)
                .reduce(0, (memory, element) -> {
                    if (element < 0)
                        return memory; // memory = memory
                    else
                        return memory + element; // memory = memory + element
                });

        // Method 4 (Using stream with entrySet)
        Integer sum = map.entrySet()
                .stream()
                .map(Map.Entry::getKey)
                .map(Integer::intValue)
                .reduce(0, (memory, element) -> {
                    if (element < 0)
                        return memory; // memory = memory
                    else
                        return memory + element; // memory = memory + element
                });
```

#### Sort

```java
        // Method 1 (Vanilla - TreeMap Oneliner)
        Map<Integer, String> map = new TreeMap<>((key1, key2) -> key1.compareTo(key2));
        Map<Integer, String> map = new TreeMap<>((key1, key2) -> key2.compareTo(key1));

        // Method 2 (Vanilla - TreeMap)
        Map<Integer, String> map = new TreeMap<>((key1, key2) -> {
            // inside this lambda expression, map is treated as effectively final
            if (key1 > key2) // (key1.compareTo(key2) > 0)
                return 1;
            else if (key1 < key2) // (key1.compareTo(key2) < 0)
                return -1;
            else // (key1.compareTo(key2) == 0)
                return 0;
        });

        // Method 3 (Using entrySet - convert and sort)
        Map<Integer, String> map = new HashMap<>();
        List<Map.Entry<Integer, String>> list = new ArrayList<>(map.entrySet());
        Collections.sort(list, (entry1, entry2) -> {
            if (entry1.getKey() > entry2.getKey())
                return 1;
            else if (entry1.getKey() < entry2.getKey())
                return -1;
            else
                return 0;
        });
        map = new LinkedHashMap<>();
        for (Map.Entry<Integer, String> entry : list) {
            map.put(entry.getKey(), entry.getValue());
        }

        // Method 4 (Using keySet)
        Map<Integer, String> map = new HashMap<>();
        List<Integer> list = new ArrayList<>(map.keySet());
        Collections.sort(list, (key1, key2) -> {
            if (key1 > key2)
                return 1;
            else if (key1 < key2)
                return -1;
            else
                return 0;
        });
        Map<Integer, String> sortedMap = new LinkedHashMap<>();
        for (Integer sortedMapKey : list) {
            sortedMap.put(sortedMapKey, map.get(sortedMapKey));
        }
        map = new LinkedHashMap<>();
        for (Map.Entry<Integer, String> entry : sortedMap.entrySet()) {
            map.put(entry.getKey(), entry.getValue());
        }
```

#### Sort (Class)

```java
    public static class InnerClass {
        private Integer amount;

        public Integer getAmount() {
            return amount;
        }

        public void setAmount(Integer amount) {
            this.amount = amount;
        }
    }

        // Method 1 (Vanilla - TreeMap Oneliner)
        Map<InnerClass, String> map = new TreeMap<>((key1, key2) -> key1.getAmount().compareTo(key2.getAmount()));
        Map<InnerClass, String> map = new TreeMap<>((key1, key2) -> key2.getAmount().compareTo(key1.getAmount()));

        // Method 1 (Vanilla - TreeMap)
        Map<InnerClass, String> map = new TreeMap<>((key1, key2) -> {
            // inside this lambda expression, map is treated as effectively final
            if (key1.getAmount() > key2.getAmount())
                return 1;
            else if (key1.getAmount() < key2.getAmount())
                return -1;
            else
                return 0;
        });

        // Method 2 (Using entrySet - convert and sort)
        Map<InnerClass, String> map = new HashMap<>();
        List<Map.Entry<InnerClass, String>> list = new ArrayList<>(map.entrySet());
        Collections.sort(list, (entry1, entry2) -> {
            if (entry1.getKey().getAmount() > entry2.getKey().getAmount())
                return 1;
            else if (entry1.getKey().getAmount() < entry2.getKey().getAmount())
                return -1;
            else
                return 0;
        });
        map = new LinkedHashMap<>();
        for (Map.Entry<InnerClass, String> entry : list) {
            map.put(entry.getKey(), entry.getValue());
        }

        // Method 3 (Using keySet - convert and sort)
        Map<InnerClass, String> map = new HashMap<>();
        List<InnerClass> list = new ArrayList<>(map.keySet());
        Collections.sort(list, (key1, key2) -> {
            if (key1.getAmount() > key2.getAmount())
                return 1;
            else if (key1.getAmount() < key2.getAmount())
                return -1;
            else
                return 0;
        });
        Map<InnerClass, String> sortedMap = new LinkedHashMap<>();
        for (InnerClass sortedMapKey : list) {
            sortedMap.put(sortedMapKey, map.get(sortedMapKey));
        }
        map = new LinkedHashMap<>();
        for (Map.Entry<InnerClass, String> entry : sortedMap.entrySet()) {
            map.put(entry.getKey(), entry.getValue());
        }
```

### Value

#### Iterate

```java
        HashMap<Integer, Integer> map = new LinkedHashMap<Integer, Integer>();

        // Method 1 (Vanilla Using Index)
        /*
         * NOT POSSIBLE
         */

        // Method 2 (Vanilla Enhanced For Loop)
        for (Integer value : map.values()) {
            System.out.println(value);
        }

        // Method 3 (Using ForEach Loop)
        map.values().forEach(value -> {
            System.out.println(value);
        });

        // Method 4 (Using stream)
        map.values().stream().forEach(value -> {
            System.out.println(value);
        });
```

#### Sum

```java
        HashMap<Integer, Integer> map = new LinkedHashMap<Integer, Integer>();

        // Method 1 (Vanilla Iteration)
        Integer sum = 0;
        for (Integer value : map.values()) {
            sum += value;
        }

        // Method 2 (Using ForEach Loop)
        /*
         * NOT POSSIBLE as variables declared outside the ForEach loop should be
         * effectively final if used inside the ForEach loop. Meaning that value can NOT
         * be changed.
         */

        // Method 3 (Using stream with keySet)
        Integer sum = map.values()
                .stream()
                .map(Integer::intValue)
                .reduce(0, (memory, element) -> {
                    if (element < 0)
                        return memory; // memory = memory
                    else
                        return memory + element; // memory = memory + element
                });

        // Method 4 (Using stream with entrySet)
        Integer sum = map.entrySet()
                .stream()
                .map(Map.Entry::getValue)
                .map(Integer::intValue)
                .reduce(0, (memory, element) -> {
                    if (element < 0)
                        return memory; // memory = memory
                    else
                        return memory + element; // memory = memory + element
                });
```

#### Sort

```java
        // Method 1 (Vanilla - TreeMap)
        /*
         * NOT POSSIBLE to maintain sorted order on new entry.
         */

        // Method 2 (Using entrySet - convert and sort)
        Map<String, Integer> map = Map.of("key1", 4, "key2", 0);
        List<Map.Entry<String, Integer>> list = new ArrayList<>(map.entrySet());
        Collections.sort(list, (entry1, entry2) -> {
            if (entry1.getValue() > entry2.getValue())
                return 1;
            else if (entry1.getValue() < entry2.getValue())
                return -1;
            else
                return 0;
        });
        map = new LinkedHashMap<>();
        for (Map.Entry<String, Integer> entry : list) {
            map.put(entry.getKey(), entry.getValue());
        }
```

#### Sort (Class)

```java
   public static class InnerClass {
       private Integer amount;


       public InnerClass(Integer amount) {
           this.amount = amount;
       }


       public Integer getAmount() {
           return amount;
       }


       public void setAmount(Integer amount) {
           this.amount = amount;
       }


       @Override
       public String toString() {
           return "(" + amount + ")";
       }
   }

       // Method 1 (Vanilla - TreeMap)
       /*
        * NOT POSSIBLE to maintain sorted order on new entry.
        */

       // Method 2 (Using entrySet - convert and sort)
       Map<String, InnerClass> map = new HashMap<>() {
           {
               put("key1", new InnerClass(4));
               put("key2", new InnerClass(0));
           }
       };
       List<Map.Entry<String, InnerClass>> list = new ArrayList<>(map.entrySet());
       Collections.sort(list, (entry1, entry2) -> {
           if (entry1.getValue().getAmount() > entry2.getValue().getAmount())
               return 1;
           else if (entry1.getValue().getAmount() < entry2.getValue().getAmount())
               return -1;
           else
               return 0;
       });
       map = new LinkedHashMap<>();
       for (Map.Entry<String, InnerClass> entry : list) {
           map.put(entry.getKey(), entry.getValue());
       }
```

# List

### Initialisation

```java
    // Method 1 (Vanilla)
    List<Integer> list = new ArrayList<>();

    // Method 2 (Returns Immutable Object - Arrays.asList())
    List<Integer> list = Arrays.asList(1, 2, 3);

    // Method 3 (Returns Immutable Object - List.of())
    List<Integer> list = List.of(1, 2, 3);

    // Method 4 (Function Returns Immutable Object - Arrays.asList())
    public static List<Integer> createList(Integer... integerValues) {
        return Arrays.asList(integerValues);
    }

    // Method 5 (Function Returns Immutable Object - List.of())
    public static List<Integer> createList(Integer... integerValues) {
        return List.of(integerValues);
    }
```

### Iterate

```java
        List<Integer> list = new ArrayList<Integer>();

        // Method 1 (Vanilla Using Index)
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }

        // Method 2 (Vanilla Enhanced For Loop)
        for (Integer element : list) {
            System.out.println(element);
        }

        // Method 3 (Using ForEach Loop)
        list.forEach(element -> {
            System.out.println(element);
        });

        // Method 4 (Using stream)
        list.stream().forEach(element -> {
            System.out.println(element);
        });
```

### Size

```java
        // Size of List
        int size = list.size();
```

### Add

```java
        // Insert One Element in List
        list.add("element");
```

### Update

```java
        // Update One Element in List
        int index = 2;
        int value = 47;
        list.set(index, value);
```

### Remove

```java
        // Remove One Element in List
        int index = 0;
        list.remove(index);
```

### Contains

```java
        // Check if List contains element
        boolean flag = list.contains("element");
```

### Get

```java
        // Get Element in List
        int index = 0;
        String element = list.get(index);
```

### Sum

```java
        List<Integer> list = new ArrayList<Integer>();

        // Method 1 (Vanilla Using Index)
        Integer sum = 0;
        for (int i = 0; i < list.size(); i++) {
            sum += list[i];
        }

        // Method 2 (Vanilla Enhanced For Loop)
        Integer sum = 0;
        for (Integer element : list) {
            sum += element;
        }

        // Method 3 (Using ForEach Loop)
        /*
         * NOT POSSIBLE as variables declared outside the ForEach loop should be
         * effectively final if used inside the ForEach loop. Meaning that value can NOT
         * be changed.
         */

        // Method 4 (Using stream)
        Integer sum = list.stream().reduce(0, (item1, item2) -> item1 + item2);

        // Method 5 (Using stream with condition)
        Integer sum = list.stream()
                .map(Integer::intValue) // maps each Integer stream value to int value
                .reduce(0, (memory, element) -> { // reduces to single value
                    if (element < 0) // condition on iterating element
                        return memory; // memory = memory
                    else
                        return memory + element; // memory = memory + element
                });
```

### Sort

```java
        List<Integer> list = new ArrayList<Integer>();

        // Method 1 (Vanilla One Liner)
        list.sort((a, b) -> a.compareTo(b)); // ascending order
        list.sort((a, b) -> b.compareTo(a)); // descending order

        // Method 2 (Vanilla - Using Custom Comparator & Lambda Expression)
        Collections.sort(list, (a, b) -> {
            if (a > b) // (a.compareTo(b) > 0)
                return 1;
            else if (a < b) // (a.compareTo(b) < 0)
                return -1;
            else // (a.compareTo(b) == 0)
                return 0;
        });

        // Method 3 (Using stream)
        list = list.stream().sorted((a, b) -> {
            if (a > b) // (a.compareTo(b) > 0)
                return 1;
            else if (a < b) // (a.compareTo(b) < 0)
                return -1;
            else // (a.compareTo(b) == 0)
                return 0;
        }).collect(Collectors.toList());

        // Method 4 (Using stream - Only increasing order)
        list = list.stream()
                .sorted(Comparator.comparing(Integer::intValue))
                .collect(Collectors.toList());

        // Method 5 (Using stream - Only decreasing order)
        list = list.stream()
                .sorted(Comparator.comparing(Integer::intValue).reversed())
                .collect(Collectors.toList());
```

### Sort (Class)

```java
    public static class InnerClass {
        private Integer amount;

        public Integer getAmount() {
            return amount;
        }

        public void setAmount(Integer amount) {
            this.amount = amount;
        }
    }

        // Method 1 (Vanilla One Liner)
        List<InnerClass> list = new ArrayList<InnerClass>();
        list.sort((a, b) -> a.getAmount().compareTo(b.getAmount())); // ascending order
        list.sort((a, b) -> b.getAmount().compareTo(a.getAmount())); // descending order

        // Method 2 (Vanilla - Using Custom Comparator & Lambda Expression)
        List<InnerClass> list = new ArrayList<InnerClass>();
        Collections.sort(list, (a, b) -> {
            if (a.getAmount() > b.getAmount())
                return 1;
            else if (a.getAmount() < b.getAmount())
                return -1;
            else
                return 0;
        });

        // Method 3 (Using stream)
        List<InnerClass> list = new ArrayList<InnerClass>();
        list = list.stream().sorted((a, b) -> {
            if (a.getAmount() > b.getAmount())
                return 1;
            else if (a.getAmount() < b.getAmount())
                return -1;
            else
                return 0;
        }).collect(Collectors.toList());

        // Method 4 (Using stream - Only increasing order)
        List<InnerClass> list = new ArrayList<InnerClass>();
        list = list.stream()
                .sorted(Comparator.comparing(InnerClass::getAmount))
                .collect(Collectors.toList());

        // Method 5 (Using stream - Only decreasing order)
        List<InnerClass> list = new ArrayList<InnerClass>();
        list = list.stream()
                .sorted(Comparator.comparing(InnerClass::getAmount).reversed())
                .collect(Collectors.toList());
```

# Set

### Initialisation

```java
   // Method 1 (Vanilla)
    Set<String> set = new HashSet<>();
    Set<String> set = new TreeSet<>(); // sorts by key or custom comparator
    Set<String> set = new LinkedHashSet<>(); // maintains insertion order

    // Method 2 (Returns Immutable Object)
    Set<String> set = Set.of("element1", "element2", "element3");
```

### Iterate

```java
        Set<String> set = new HashSet<>();

        // Method 1 (Vanilla Using Index)
        /*
         * NOT POSSIBLE
         */

        // Method 2 (Vanilla Enhanced For Loop)
        for (String element : set) {
            System.out.println(element);
        }

        // Method 3 (Vanilla Using Iterator)
        for (Iterator<String> iterator = set.iterator(); iterator.hasNext();) {
            String element = iterator.next();
            System.out.println(element);
        }
        // OR
        Iterator iterator = set.iterator();
        while (iterator.hasNext()) {
            Object object = iterator.next();
            System.out.println(object);
        }

        // Method 4 (Using ForEach Loop)
        set.forEach(element -> {
            System.out.println(element);
        });
```

### Size

```java
        // Size of Set
        int size = set.size();
```

### Add

```java
        // Insert One Element in Set
        set.add("element");
```

### Remove

```java
        // Remove One Element in Set
        set.remove("element");
```

### Contains

```java
        // Check if Set contains element
        boolean flag = set.contains("element");
```

### Get

```java
        // Get Element in Set
        /*
         * NOT POSSIBLE. Iterate to get the element or contains to check if it exists.
         */
```

### Sum

```java
        Set<Integer> set = new HashSet<>();

        // Method 1 (Vanilla Using Index)
        /*
         * NOT POSSIBLE
         */

        // Method 2 (Vanilla Enhanced For Loop)
        Integer sum = 0;
        for (String element : set) {
            sum += element;
        }

        // Method 3 (Vanilla Using Iterator)
        Integer sum = 0;
        for (Iterator<Integer> iterator = set.iterator(); iterator.hasNext();) {
            Integer element = iterator.next();
            sum += element;
        }
        // OR
        Integer sum = 0;
        Iterator iterator = set.iterator();
        while (iterator.hasNext()) {
            Object object = iterator.next();
            sum += (Integer) object;
        }

        // Method 4 (Using ForEach Loop)
        /*
         * NOT POSSIBLE as variables declared outside the ForEach loop should be
         * effectively final if used inside the ForEach loop. Meaning that value can NOT
         * be changed.
         */

        // Method 5 (Using stream)
        Integer sum = set.stream().reduce(0, (item1, item2) -> item1 + item2);

        // Method 6 (Using stream with condition)
        Integer sum = set.stream()
                .map(Integer::intValue) // maps each Integer stream value to int value
                .reduce(0, (memory, element) -> { // reduces to single value
                    if (element < 0) // condition on iterating element
                        return memory; // memory = memory
                    else
                        return memory + element; // memory = memory + element
                });
```

### Sort

```java
        // Method 1 (Vanilla - TreeSet Oneliner)
        Set<String> set = new TreeSet<>((a, b) -> a.compareTo(b)); // ascending order
        Set<String> set = new TreeSet<>((a, b) -> b.compareTo(a)); // descending order

        // Method 2 (Vanilla - TreeSet)
        Set<Integer> set = new TreeSet<>((a, b) -> {
            // inside this lambda expression, set is treated as effectively final
            if (a > b) // (a.compareTo(b) > 0)
                return 1;
            else if (a < b) // (a.compareTo(b) < 0)
                return -1;
            else // (a.compareTo(b) == 0)
                return 0;
        });
```

### Sort (Class)

```java
    public static class InnerClass {
        private Integer amount;

        public Integer getAmount() {
            return amount;
        }

        public void setAmount(Integer amount) {
            this.amount = amount;
        }
    }

        // Method 1 (Vanilla - TreeSet Oneliner)
        Set<InnerClass> set = new TreeSet<>((a, b) -> a.getAmount().compareTo(b.getAmount()));
        Set<InnerClass> set = new TreeSet<>((a, b) -> b.getAmount().compareTo(a.getAmount()));

        // Method 2 (Vanilla - TreeSet)
        Set<InnerClass> set = new TreeSet<>((a, b) -> {
            // inside this lambda expression, set is treated as effectively final
            if (a.getAmount() > b.getAmount())
                return 1;
            else if (a.getAmount() < b.getAmount())
                return -1;
            else
                return 0;
        });
```

# Stack

### Initialisation

```java
    // Method 1 (Vanilla)
    Stack<String> stack = new Stack<>();

    // Method 2 (Returns Mutable Object)
    Stack<String> stack = new Stack<String>() {
        {
            push("element1");
            push("element2");
            push("element3");
        }
    };
```

### Iterate

```java
        // Method 1 (Vanilla Using Index)
        /*
         * NOT POSSIBLE
         */

        // Method 2 (Vanilla While Loop - Top to Bottom)
        while (stack.size() != 0) {
            String element = stack.pop();
            System.out.println(element);
        }

        // Method 3 (Using Enhanced For Loop - Bottom to Top)
        for (String element : stack) {
            System.out.println(element);
        }

        // Method 4 (Using Iterator - Bottom to Top)
        for (Iterator<String> iterator = stack.iterator(); iterator.hasNext();) {
            String element = iterator.next();
            System.out.println(element);
        }
        // OR
        Iterator iterator = stack.iterator();
        while (iterator.hasNext()) {
            Object object = iterator.next();
            System.out.println(object);
        }

        // Method 5 (Using ForEach Loop - Bottom to Top)
        stack.forEach(element -> {
            System.out.println(element);
        });
```

### Size

```java
        int size = stack.size();
```

### Add

```java
        // Add element at top of Stack
        stack.push("element");
        stack.add("element");
```

### Remove

```java
        // Remove and return topmost stack element
        String element = stack.pop();
```

### Contains

```java
        // Check if Stack contains element
        boolean flag = stack.contains("element");
```

### Peek

```java
        // Only Get (Not Remove) the topmost stack element
        String element = stack.peek();
```

### Clear

```java
        // Method 1 (Vanilla)
        stack.clear();

        // Method 2 (Using new operator)
        stack = new Stack<>();
```

# Queue

### Initialisation

```java
    // Method 1 (Vanilla)
    Queue<String> queue = new LinkedList<>();

    // Method 2 (Returns Mutable Object)
    Queue<String> queue = new LinkedList<>() {
        {
            add("element1");
            add("element2");
            add("element3");
        }
    };
```

### Iterate

```java
        // Method 1 (Vanilla Using Index)
        /*
         * NOT POSSIBLE
         */

        // Method 2 (Vanilla While Loop - Front to Rear)
        while (queue.size() != 0) {
            String element = queue.remove();
            System.out.println(element);
        }

        // Method 3 (Using Enhanced For Loop - Front to Rear)
        for (String element : queue) {
            System.out.println(element);
        }

        // Method 4 (Using Iterator - Front to Rear)
        for (Iterator<String> iterator = queue.iterator(); iterator.hasNext();) {
            String element = iterator.next();
            System.out.println(element);
        }
        // OR
        Iterator iterator = queue.iterator();
        while (iterator.hasNext()) {
            Object object = iterator.next();
            System.out.println(object);
        }

        // Method 5 (Using ForEach Loop - Front to Rear)
        queue.forEach(element -> {
            System.out.println(element);
        });
```

### Size

```java
        int size = queue.size();
```

### Add

```java
        // Add element at front of the Queue
        queue.add("element");
        queue.offer("element");
```

### Remove

```java
        // Remove and return front element of queue
        String element = queue.remove();
```

### Contains

```java
        // Check if Queue contains element
        boolean flag = queue.contains("element");
```

### Peek

```java
        // Only Get (Not Remove) the front element of queue
        String element = queue.peek();
```

### Clear

```java
        // Method 1 (Vanilla)
        queue.clear();

        // Method 2 (Using new operator)
        queue = new LinkedList<>();
```

# Deque (ArrayDeque)

### Initialisation

```java
        Deque<String> deque = new ArrayDeque<>();
        // OR
        ArrayDeque<String> deque = new ArrayDeque<>();
```

### Iterate

```java
        // Method 1 (Vanilla Using Index)
        /*
         * NOT POSSIBLE
         */

        // Method 2 (Vanilla While Loop - Front to Rear)
        while (deque.size() != 0) {
            String element = deque.removeFirst(); // deque.remove(); (Queue)
            System.out.println(element);
        }

        // Method 3 (Vanilla While Loop - Rear to Front)
        while (deque.size() != 0) {
            String element = deque.removeLast(); // deque.pop(); (Stack)
            System.out.println(element);
        }

        // Method 4 (Using Enhanced For Loop - Front to Rear)
        for (String element : deque) {
            System.out.println(element);
        }

        // Method 5 (Using Iterator - Front to Rear)
        for (Iterator<String> iterator = deque.iterator(); iterator.hasNext();) {
            String element = iterator.next();
            System.out.println(element);
        }
        // OR
        Iterator iterator = deque.iterator();
        while (iterator.hasNext()) {
            Object object = iterator.next();
            System.out.println(object);
        }

        // Method 6 (Using ForEach Loop - Front to Rear)
        deque.forEach(element -> {
            System.out.println(element);
        });
```

### Size

```java
        int size = deque.size();
```

### Add

```java
        // Add element at front of the Deque
        deque.addFirst("Front");

        // Add element at rear of the Deque
        deque.addLast("Rear"); // deque.push(); (Stack)  && deque.add(); (Queue)
```

### Remove

```java
        // Remove and return element from front of the Deque
        String frontElement = deque.removeFirst(); // deque.remove(); (Queue)

        // Remove and return element from rear of the Deque
        String rearElement = deque.removeLast(); // deque.pop(); (Stack)
```

### Contains

```java
        // Check if Deque contains element
        boolean flag = deque.contains("element");
```

### Peek

```java
        // Only Get (Not Remove) the element from front of the Deque
        String frontElement = deque.peekFirst();

        // Only Get (Not Remove) the element from rear of the Deque
        String rearElement = deque.peekLast();
```

### Clear

```java
        // Method 1 (Vanilla)
        deque.clear();

        // Method 2 (Using new operator)
        deque = new ArrayDeque<>();
```

### ArrayDeque as Stack

```java
        // ArrayDeque as Stack
        ArrayDeque<String> stack = new ArrayDeque<>();
        stack.push("Hello");
        stack.push("World");
        System.out.println(stack.peekFirst()); // outputs: World
        System.out.println(stack.pop()); // outputs: World
        System.out.println(stack.pop()); // outputs: Hello
        boolean flag = stack.contains("element");
```

### ArrayDeque as Queue

```java
        // ArrayDeque as Queue
        ArrayDeque<String> queue = new ArrayDeque<>();
        queue.add("Hello");
        queue.add("World");
        System.out.println(queue.peekLast()); // outputs: Hello
        System.out.println(queue.remove()); // outputs: Hello
        System.out.println(queue.remove()); // outputs: World
        boolean flag = queue.contains("element");
```

# Priority Queue (Heap)

### Min-Heap

```java
        // Method 1 (Vanilla - Oneliner)
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b) -> a.compareTo(b));

        // Method 2 (Vanilla - Using Custom Comparator & Lambda Expression)
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b) -> {
            if (a > b) // (a.compareTo(b) > 0)
                return 1;
            else if (a < b) // (a.compareTo(b) < 0)
                return -1;
            else // (a.compareTo(b) == 0)
                return 0;
        });
```

### Max-Heap

```java
        // Method 1 (Vanilla - Oneliner)
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b.compareTo(a));

        // Method 2 (Vanilla - Using Custom Comparator & Lambda Expression)
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> {
            if (a > b) // (a.compareTo(b) > 0)
                return -1;
            else if (a < b) // (a.compareTo(b) < 0)
                return 1;
            else // (a.compareTo(b) == 0)
                return 0;
        });
```

### Min + Max Heap (Class)

```java
    public static class InnerClass {
        private Integer amount;

        public Integer getAmount() {
            return amount;
        }

        public void setAmount(Integer amount) {
            this.amount = amount;
        }
    }

        // Min-Heap
        PriorityQueue<InnerClass> minHeap = new PriorityQueue<>((a, b) -> {
            if (a.getAmount() > b.getAmount())
                return 1;
            else if (a.getAmount() < b.getAmount())
                return -1;
            else
                return 0;
        });

        // Max-Heap
        PriorityQueue<InnerClass> maxHeap = new PriorityQueue<>((a, b) -> {
            if (a.getAmount() > b.getAmount())
                return -1;
            else if (a.getAmount() < b.getAmount())
                return 1;
            else
                return 0;
        });
```

### Iterate

```java
        PriorityQueue<String> heap = new PriorityQueue<>();

        // Method 1 (Vanilla Using Index)
        /*
         * NOT POSSIBLE
         */

        // Method 2 (Vanilla While Loop - Top to Bottom)
        while (heap.size() != 0) {
            String element = heap.remove();
            System.out.println(element);
        }

        // Method 3 (Using Enhanced For Loop - Top to Bottom)
        for (String element : heap) {
            System.out.println(element);
        }

        // Method 4 (Using Iterator - Top to Bottom)
        for (Iterator<String> iterator = heap.iterator(); iterator.hasNext();) {
            String element = iterator.next();
            System.out.println(element);
        }
        // OR
        Iterator iterator = heap.iterator();
        while (iterator.hasNext()) {
            Object object = iterator.next();
            System.out.println(object);
        }

        // Method 6 (Using ForEach Loop - Top to Bottom)
        heap.forEach(element -> {
            System.out.println(element);
        });
```

### Size

```java
        int size = heap.size();
```

### Add

```java
        // Add element at top of heap
        heap.add("element");
```

### Remove

```java
        // Remove and return top element of heap
        String element = heap.remove();
```

### Contains

```java
        // Check if Heap contains element
        boolean flag = heap.contains("element");
```

### Peek

```java
        // Only Get (Not Remove) the top element of heap
        String element = heap.peek();
```

### Clear

```java
        // Method 1 (Vanilla)
        heap.clear();

        // Method 2 (Using new operator)
        heap = new PriorityQueue<>();
```

# Array

### Initialisation

```java
        // Declare and initialize int[] & Integer[] array
        int[] array = { 1, 0, 1, 1 };
        Integer[] array = { 1, 2, 4, 3 };

        // Declare and initialize int[][] & Integer[][] grid
        int[][] grid = {
                { 1, 0, 1, 1 },
                { 0, 0, 1, 0 },
                { 1, 0, 1, 1 },
                { 1, 0, 1, 0 }
        };
        Integer[][] grid = {
                { 1, 0, 1, 1 },
                { 0, 0, 1, 0 },
                { 1, 0, 1, 1 },
                { 1, 0, 1, 0 }
        };
```

### Iterate

```java
// Iterate int[] & Integer[] array (Using Enhanced For Loop)
        for (int element : array) {
            System.out.println(element);
        }
        for (Integer element : array) {
            System.out.println(element);
        }

// Iterate int[][] & Integer[][] array (Using Enhanced For Loop)
        for (int[] row : array) {
            for (int element : row) {
                System.out.println(element);
            }
        }
        for (Integer[] row : array) {
            for (Integer element : row) {
                System.out.println(element);
            }
        }
```

### Size

```java
        // Size of Array
        int size = array.length;
```

### Sort

```java
        int[] intArray = { 1, 0, 1, 1 };
        Integer[] integerArray = { 1, 2, 4, 3 };

        // Method 1 (Vanilla)
        Arrays.sort(intArray); // ascending order
        /*
         * NOT POSSIBLE for intArray one liner descending order.
         */

        Arrays.sort(integerArray, (a, b) -> a.compareTo(b)); // ascending order
        Arrays.sort(integerArray, (a, b) -> b.compareTo(a)); // descending order

        // Method 2 (Using Lambda Expression)
        Arrays.sort(integerArray, (a, b) -> {
            // inside this lambda expression, Integer[] is treated as effectively final
            if (a > b) // (a.compareTo(b) > 0)
                return 1;
            else if (a < b) // (a.compareTo(b) < 0)
                return -1;
            else // (a.compareTo(b) == 0)
                return 0;
        });
```

# @Override Object Class

### InnerClass

```java
    public static class InnerClass extends Object {
        private Integer first;
        private String second;
        private Character third;

        // Override toString() from Object class
        @Override
        public String toString() {
            return "(" + first + ", " + second + ", " + third + ")";
        }

        // Override equals() from Object class
        @Override
        public boolean equals(Object obj) {
            InnerClass that = (InnerClass) obj;
            return Objects.equals(this.first, that.first)
                    && Objects.equals(this.second, that.second)
                    && Objects.equals(this.third, that.third);
        }

        // Override hashCode() from Object class
        @Override
        public int hashCode() {
            return Objects.hash(first, second, third);
        }
    }
```

### toString()

```java
    public static class InnerClass extends Object {
        private Integer first;
        private String second;
        private Character third;

        // Override toString() from Object class
        @Override
        public String toString() {
            return "(" + first + ", " + second + ", " + third + ")";
        }
    }
```

### equals()

```java
    public static class InnerClass extends Object {
        private Integer first;
        private String second;
        private Character third;

        // Override equals() from Object class
        @Override
        public boolean equals(Object obj) {
            InnerClass that = (InnerClass) obj;
            return Objects.equals(this.first, that.first)
                    && Objects.equals(this.second, that.second)
                    && Objects.equals(this.third, that.third);
        }
    }
```

### hashCode()

```java
    public static class InnerClass extends Object {
        private Integer first;
        private String second;
        private Character third;

        // Override hashCode() from Object class
        @Override
        public int hashCode() {
            return Objects.hash(first, second, third);
        }
    }
```

# Theory Concepts

### For Each Loop Property

- Can’t have a return statement inside ForEach loop as the method that is overridden (using lambda expression) has the return type of void.
- Any global variable used inside the lambda expression must be effectively final. Meaning you can’t change any value.

### HashMap Internal Working

- Step 1: uses HashCode() to find the bucket by generating the hash
- Step 2: uses equals() check if the key exists in the bucket
- Step 3: If exists, then override/update the key-value pair.
- Step 4: If does NOT exists, then add a new node with the key-value pair details.
- Reference: https://youtu.be/CpVALR9HeTE?si=t3zZey_89Yh9o9J- and https://youtu.be/-oafFAPgLao?si=qsywpJgC79yeBthN

### Sort Order - Map, Set & Heap

- Map: sort wrt key = maintain sorted order on new entry or remove entry
- Map: sort wrt value = CANT maintain sorted order on new entry or remove entry (sort every time new entry or remove entry)
- Set: sort wrt element = maintain sorted order on new element or remove element
- Heap: priority wrt element = maintain sorted order on new element or remove element
  <br>
  <br>
- List: sort each time you add new element or remove element
- Map: sort wrt value: convert and sort every time new entry or remove entry

### InnerClass private policy

- When you declare an inner class as private, it means that the inner class is not visible to other classes outside of the outer class. The members of the inner class can still be accessed by the outer class. This is because the inner class is a member of the outer class, and the outer class has access to all of its members.
- A class doesn't have direct access to the private members of another class, even if it's an inner class. The Parent class can access the InnerChild class's members because the InnerChild class is an inner class of the Parent class. But the Parent class can't access the InnerChild class's members if it's accessed through an instance of the Parent class. This is because the Parent class is not an instance of the InnerChild class; it's a separate class that contains the InnerChild class.

```java
public class Parent {
   private class Child {
       private void childMethod() {
           System.out.println("method called");
       }
   }

   public void parentMethod() {
       Child child = new Child();
       child.childMethod(); // Accessible to child's instance
   }

   public static void main(String[] args) {
       Parent parent = new Parent();
       parent.childMethod(); // NOT Accessible to parent's instance

       parent.parentMethod(); // Allowed
   }
}
```

### TypeCasting

#### Upcasting

- \<Write>
- \<Write>

#### DownCasting

- \<Write>
- \<Write>

Reference: https://www.youtube.com/watch?v=fJzf0Gm0G6U and https://www.youtube.com/watch?v=HpuH7n9VOYk
