#include <iostream>
#include <vector>

void merge(std::vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    std::vector<int> left_half(n1);
    std::vector<int> right_half(n2);
    
    for (int i = 0; i < n1; i++) {
        left_half[i] = arr[left + i];
    }
    for (int j = 0; j < n2; j++) {
        right_half[j] = arr[mid + 1 + j];
    }
    
    int i = 0;
    int j = 0;
    int k = left;
    
    while (i < n1 && j < n2) {
        if (left_half[i] <= right_half[j]) {
            arr[k] = left_half[i];
            i++;
        } else {
            arr[k] = right_half[j];
            j++;
        }
        k++;
    }
    
    while (i < n1) {
        arr[k] = left_half[i];
        i++;
        k++;
    }
    
    while (j < n2) {
        arr[k] = right_half[j];
        j++;
        k++;
    }
}

void mergeSort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

int main() {
    std::vector<int> myArray = {5, 2, 4, 6, 1, 3, 2, 7};
    int n = myArray.size();
    
    mergeSort(myArray, 0, n - 1);
    
    for (int i = 0; i < n; i++) {
        std::cout << myArray[i] << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
