import java.util.ArrayList;
import java.util.List;

class ProductOfNumbers {

    List<Integer> prodStream;
    int prod = 1;

    public ProductOfNumbers() {
       prodStream = new ArrayList<>();
    }
    
    public void add(int num) {
        if(num == 0) {
            prodStream = new ArrayList<>();
            prod = 1;
        } else {
            prod = prod * num;
            prodStream.add(prod);
        }
    }
    
    public int getProduct(int k) {
        if(k > prodStream.size()) return 0;
        if(k == prodStream.size()) return prod;
       return prod / prodStream.get(prodStream.size() - k - 1);
    }

    public static void main(String[] args) {
        ProductOfNumbers productOfNumbers = new ProductOfNumbers();
        productOfNumbers.add(3);        // [3]
        productOfNumbers.add(0);        // [3,0]
        productOfNumbers.add(2);        // [3,0,2]
        productOfNumbers.add(5);        // [3,0,2,5]
        productOfNumbers.add(4);        // [3,0,2,5,4]
        System.out.println(productOfNumbers.getProduct(2));; // return 20. The product of the last 2 numbers is 5 * 4 = 20
        System.out.println(productOfNumbers.getProduct(3));; // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
        System.out.println(productOfNumbers.getProduct(4));; // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
        productOfNumbers.add(8);        // [3,0,2,5,4,8]
        System.out.println(productOfNumbers.getProduct(2));
    }
}