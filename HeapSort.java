public class HeapSort {
    public void sort(int arr[]) {
        int length = arr.length;

        for(int i = length / 2 -1; i >= 0; i--) {
            heap(arr, length, i);
        }

        for(int i = length -1; i > 0; i--) {
            // setam elementul current root la sfarsit
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i]= temp;

            heap(arr, i, 0);
        }

    }

    void heap(int arr[], int length, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if(left < length && arr[left] > arr[largest]) {
            largest = left;
        }

        if(right < length && arr[right] > arr[largest]) {
            largest = right;
        }

        if(largest != i) {
            int schimbare = arr[i];
            arr[i] = arr[largest];
            arr[largest] = schimbare;

            heap(arr, length, largest);
        }
    }
}
