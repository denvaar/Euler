import java.util.Vector;

public class p2 {

    public static void main(String args[]) {

        Vector<Integer> fibNumbers = new Vector();
        fibNumbers.addElement(new Integer(1));
        fibNumbers.addElement(new Integer(2));
        Integer even = 2;
        Integer next = 3;
        
        while (next <= 4000000) {
            if ((next % 2) == 0) {
                even += next;
            }
            fibNumbers.addElement(next);
            next = fibNumbers.elementAt(fibNumbers.size() - 1) + fibNumbers.elementAt(fibNumbers.size() - 2);
        }

        System.out.println(even);
        
    }

}
