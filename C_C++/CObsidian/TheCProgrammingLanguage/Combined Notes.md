
# SubArr function written by me and response of chtgpt

```c
int *subArr(int arr[],int size,int subArr[]){

    for(int i = 0; i < size; i++){
        for(int j = 0; j <= i;j++){
            int *arr = malloc((i-j+2)*sizeof(int));
            for(int k = j ,h = 0; k <= i; k++,h++){
                *(arr+h) = arr[k];
            }
            subArr[j] = arr;
        }
    }
    return subArr;
}
```
