public class Main {
    public static void main(String[] args) {
        int arr[] = { 1, 11, 13, 5, 4, 8};
        int length = arr.length;
        HeapSort heapSort = new HeapSort();
        heapSort.sort(arr);

        for(int i = 0; i < length; i++) {
            System.out.println(arr[i] + " ");
        }
    }
}
