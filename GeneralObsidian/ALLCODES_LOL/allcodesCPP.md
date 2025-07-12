# exp1010.c


```cpp

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILENAME_LENGTH MAX_PATH
#define SOURCE_DIR "D:"
#define DEST_DIR "."



void deleteingfiles(const char *sourceDir){
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];

    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);


    do {
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }
        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            deleteingfiles(sourcePath);
        } 
        else {
            char *extension = strrchr(findFileData.cFileName, '.');
            if (extension != NULL && _stricmp(extension, ".pdf") == 0){
                printf("%s\n",sourcePath);
                DeleteFileA(sourcePath);
            }
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);


}


void copyFilesWithoutStructures_extension(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);


    // if (hFind == INVALID_HANDLE_VALUE) {
    //     printf("Error opening source directory\n");
    //     exit(EXIT_FAILURE);
    // }

    do {
        // printarr(sourcePath,MAX_FILENAME_LENGTH);
        // printarr(destPath,MAX_FILENAME_LENGTH);

        printf("%s\n",sourcePath);
        // printf("%s",destPath)
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            // CreateDirectoryA(destPath, NULL);
            copyFilesWithoutStructures_extension(sourcePath, destDir);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
            // CopyFileA(sourcePath, destPath, FALSE);

            char *extension = strrchr(findFileData.cFileName, '.');
            if (extension != NULL && (_stricmp(extension, ".jpeg") == 0 || _stricmp(extension, ".jpg") == 0 || _stricmp(extension, ".png") == 0 || _stricmp(extension, ".pdf") == 0)){
                CopyFileA(sourcePath,destPath,FALSE);
            }
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}


void copyAllFilesWithoutStructures(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);


    // if (hFind == INVALID_HANDLE_VALUE) {
    //     printf("Error opening source directory\n");
    //     exit(EXIT_FAILURE);
    // }

    do {
        // printarr(sourcePath,MAX_FILENAME_LENGTH);
        // printarr(destPath,MAX_FILENAME_LENGTH);

        printf("%s\n",sourcePath);
        // printf("%s",destPath)
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            // CreateDirectoryA(destPath, NULL);
            copyAllFilesWithoutStructures(sourcePath, destDir);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
            // CopyFileA(sourcePath, destPath, FALSE);
            CopyFileA(sourcePath,destPath,FALSE);
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}


void copyPDFFilesRecursive(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Error opening source directory\n");
        exit(EXIT_FAILURE);
    }

    do {
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            CreateDirectoryA(destPath, NULL);
            copyPDFFilesRecursive(sourcePath, destPath);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
            char *extension = strrchr(findFileData.cFileName, '.');
            if (extension != NULL && _stricmp(extension, ".pdf") == 0){
                CopyFileA(sourcePath,destPath,FALSE);
            }
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}


void copywholefolder(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Error opening source directory\n");
        exit(EXIT_FAILURE);
    }

    do {
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            CreateDirectoryA(destPath, NULL);
            copyPDFFilesRecursive(sourcePath, destPath);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
                CopyFileA(sourcePath,destPath,FALSE);
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}


int main() {
    // copyFilesWithoutStructures_extension("D:",".");
    // deleteingfiles(".");
    copyAllFilesWithoutStructures("E:",".");
    // copywholefolder("E:",".");
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# 1-13.c


```cpp

#include <stdio.h>

int main() {
    int c;

    while ((c = getchar()) != EOF) {
        int i = 0;
        int lengths[100] = {0}; // Move the array outside the loop
        if (c == '\t' || c == ' ') {
            i += 1;
        } 
        else {
            lengths[i]++;
        }

        // Print the histogram after each input character
        for (int j = 0; j <= i; j++) {
            for (int k = 0; k < lengths[j]; k++) {
                printf("*");
            }
            printf("\n");
        }
    }

    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# binarysearch.c


```cpp

#include <stdio.h>

int binarySearch(int arr[], int low, int high, int target) {
    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == target) {
            return mid;  // Target found at index mid
        } else if (arr[mid] < target) {
            low = mid + 1;  // Target is in the right half
        } else {
            high = mid - 1;  // Target is in the left half
        }
    }

    return -1;  // Target not found
}

int main(){
    int arr[]={72, 20, 45, 96, 82, 62, 93, 49, 88, 11, 66, 31, 51, 27, 46, 18, 0, 41, 53, 6, 86, 69, 34, 75, 14, 77, 95, 2, 38, 56};

}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# chap1-8.c


```cpp

#include <stdio.h>
int main(){

    int c,bsp,nl,tb;
    bsp=0;
    nl=0;
    tb=0;
    while(c=getchar()!=EOF){
        if ( c== "\t"){
            tb++;
        }
        if (c == "\n"){
            bsp++;
        }
        if (c == '\n'){
            nl++;
        }

    }
    printf("backspaces %d",bsp);
    printf("tabs %d",tb);
    printf("newlines %d",nl);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# del.c


```cpp

#include <windows.h>
#include <string.h>

void DeleteFolder(const char *szFolderPath)
{
    char strFileFilter[MAX_PATH];
    strcpy(strFileFilter, szFolderPath);
    strcat(strFileFilter, "\\*.*");

    WIN32_FIND_DATA win32FindData; //struct to hold file information
    HANDLE hFile = FindFirstFile(strFileFilter, &win32FindData);

    if (hFile != INVALID_HANDLE_VALUE)
    {
        do
        {
            if (win32FindData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
            {
                if (strcmp(win32FindData.cFileName, ".") != 0 && strcmp(win32FindData.cFileName, "..") != 0)
                {
                    char strPath[MAX_PATH];
                    strcpy(strPath, szFolderPath);
                    strcat(strPath, "\\");
                    strcat(strPath, win32FindData.cFileName);
                    DeleteFolder(strPath);
                }
            }
            else
            {
                char strPath[MAX_PATH];
                strcpy(strPath, szFolderPath);
                strcat(strPath, "\\");
                strcat(strPath, win32FindData.cFileName);
                DeleteFile(strPath);
            }
        } while (FindNextFile(hFile, &win32FindData));

        FindClose(hFile);
    }

    RemoveDirectory(szFolderPath);
}


int main()
{
    const char *folderPath = "."; //replace with the path of the folder you want to delete
    DeleteFolder(folderPath);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# exp100.c


```cpp

#include <stdio.h>
#include <string.h>

char* getline(FILE* ptr, char line[]) {
    // Check if the file pointer is NULL
    if (ptr == NULL) {
        return NULL;
    }

    int c, i = 0;
    // Read characters until newline or EOF
    while ((c = fgetc(ptr)) != '\n' && c != EOF) {
        *(line+i++) = c;
    }
    // Ensure proper null-termination
    *(line+i) = '\0';

    // Return NULL if nothing was read and EOF was encountered
    if (i == 0 && c == EOF) {
        return NULL;
    }

    return line;
}

int main(int argc, char *argv[]) {
    // Check if filename and mode are provided as command-line arguments
    if (argc != 3) {
        printf("Usage: %s <filename> <mode>\n", argv[0]);
        return 1;
    }

    char line[200];
    char input[200];
    FILE* fptr;

    // Open the file in the specified mode
    fptr = fopen(argv[1], argv[2]);
    if (fptr == NULL) {
        printf("Failed to open the file.\n");
        return 1;
    }

    printf("This is a simple editor where you can edit files in different modes and make files of your choices the interface may not be friendly but its amazing to use this \n");

    while (fgets(input, sizeof(input), stdin) != NULL) {
        fprintf(fptr, "%s", input);
    }

    fclose(fptr);

    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# exp101.c


```cpp

#include <stdio.h>

void split(char str[], char *words[]) {
    int word_count = 0;
    int word_start = 0;
    int in_word = 0;

    for (int i = 0; str[i] != '\0'; i++) {
        if ((str[i] == ' ' || str[i] == '\t')) {
            if (in_word) {
                str[i] = '\0'; // Null-terminate the word
                words[word_count++] = &str[word_start]; // Store the pointer to the word
                in_word = 0;
            }
        } else {
            if (!in_word) {
                word_start = i; // Start of a new word
                in_word = 1;
            }
        }
    }

    if (in_word) {
        words[word_count++] = &str[word_start]; // Store the last word
    }

    words[word_count] = NULL; // Null-terminate the array of pointers
}

int main() {
    char *ptrarr[100];
    char str[] = "Hello   Guys This is Haarit";
    
    split(str, ptrarr);

    // Printing the words
    for (int i = 0; ptrarr[i] != NULL; i++) {
        printf("Word %d: %s\n", i + 1, ptrarr[i]);
    }

    return 0;
}
 

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# exp1010.c


```cpp

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILENAME_LENGTH MAX_PATH
#define SOURCE_DIR "D:"
#define DEST_DIR "."

void copyPDFFilesRecursive_withoutstructure(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);


    // if (hFind == INVALID_HANDLE_VALUE) {
    //     printf("Error opening source directory\n");
    //     exit(EXIT_FAILURE);
    // }

    do {
        // printarr(sourcePath,MAX_FILENAME_LENGTH);
        // printarr(destPath,MAX_FILENAME_LENGTH);

        printf("%s\n",sourcePath);
        // printf("%s",destPath)
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            // CreateDirectoryA(destPath, NULL);
            copyPDFFilesRecursive_withoutstructure(sourcePath, destDir);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
            // CopyFileA(sourcePath, destPath, FALSE);

            char *extension = strrchr(findFileData.cFileName, '.');
            if (extension != NULL && _stricmp(extension, ".pdf") == 0){
                CopyFileA(sourcePath,destPath,FALSE);
            }
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}




void copyPDFFilesRecursive(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Error opening source directory\n");
        exit(EXIT_FAILURE);
    }

    do {
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            CreateDirectoryA(destPath, NULL);
            copyPDFFilesRecursive(sourcePath, destPath);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
            char *extension = strrchr(findFileData.cFileName, '.');
            if (extension != NULL && _stricmp(extension, ".pdf") == 0){
                CopyFileA(sourcePath,destPath,FALSE);
            }
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}





int main() {
    copyPDFFilesRecursive("D:", ".");
    // copyPDFFilesRecursive("C:", ".");
    // copyPDFFilesRecursive("E:",".");
    // copyPDFFilesRecursive("F:",".");
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# exp102.c


```cpp

#include <stdio.h>

int main(){

    
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# first.c


```cpp

#include <stdio.h>

int merge(int left,int right){
    
}
int* bubble(int arr[]){
    int l=sizeof(arr)/sizeof(arr[0]);
    for(int i=0;i<l;i++){
        for(int j=0;j<l-i;j++){
            if(arr[j+1]<arr[j]){
            int temp=arr[j+1];
            arr[j+1]=arr[j];
            arr[j]=temp;
            }
            else{
                break;
            }
        }

    }
    return arr;
}

int main(){

int arr1[]={1,5,3,8,9,3,7,9,4,7,1,10,15,11,36};
int arr1_sorted=bubble(arr1);
for(int i=0;i<sizeof(arr1)/sizeof(arr1[0]);i++){
    printf("%d",arr1_sorted[i]);
}

return 0;

    
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# functions.c


```cpp

#include <stdio.h>

int main() {
    char arr[100][20];
    int c;
    int i = 0;
    int j = 0;

    while ((c = getchar()) != '\n') {
        if (c != ' ' && c != '\t') {
            arr[i][j++] = c;
        } else if (j > 0) {
            arr[i++][j] = '\0';
            j = 0;
        }
    }

    // Print the strings
    for (int k = 0; k <= i; k++) {
        printf("%s\n", arr[k]);
    }

    return 0;
}




// My code little lengthy
// #include <stdio.h>



// int main(){
//     // function to get string as input and store it in an array
//     int arr[100][20];
//     int c;
//     int i=0;
//     int j=0;

//     while((c=getchar())!='\n'){
//         if (c!=' ' && c!='\t'){
//         arr[i][j]=c;
//         j++;
//         }
//         else{
//             arr[i][++j]='\0';
//             j=0;
//             i++;
//         }
//     }

//     for (int k=0;k<=i;k++){
//         for (int l=0;l<20;l++){
//             if (arr[k][l]!='\0'){
//             printf("%c",arr[k][l]);
//             }
//             else{
//                 printf("\n");
//                 break;
//             }

//         }
//     }

//     return 0;
// }



```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# game.c


```cpp

#include <stdio.h>
#include <stdlib.h>
int cash=100;
void Play(int bet){
    char C[3]={'J','Q','K'};
    printf("Shuffling........\n");
    srand(time(NULL));
    int i;
    for (i=0;i<5;i++){
        int x=rand()%3;
        int y=rand()%3;
        char temp=C[x];
        C[x]=C[y];
        C[y]=temp;
    }
    int PlayerGuess;
    printf("What is the position of Queen  -- ");
    scanf("%d",&PlayerGuess);
    if(C[PlayerGuess-1] == 'Q'){
        cash += 3*bet;
        printf("You Win! Result = %c %c %c Total Cash= %d \n",C[0],C[1],C[2],cash);
    }
    else{
        cash-=bet;
        printf("You Loose! Result =  %c %c %c  Total Cash= %d \n",C[0],C[1],C[2],cash);
    }
}
int main(){

    int bet;
    printf("Welcome to virtual Casino");
    printf("Total cash = $%d \n",cash);
    while(cash  > 0){
        printf("Whats your bet?? $");
        scanf("%d",&bet);
        if (bet == 0 || bet>cash) break;
        Play(bet);
    }

    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# kthminimum.c


```cpp

#include <stdio.h>

// Function to partition the array and return the index of the pivot element
int partition(int *arr, int low, int high) {
    int pivot = arr[low];  // Choose the first element as the pivot
        int i = low + 1;        // Index of the smaller element
        int j = high;
        // Linearized partition function
    while (i <= j) {
        while (i <= j && arr[i] < pivot) {
            i++;
        }

        while (i <= j && arr[j] > pivot) {
            j--;
        }

        if (i <= j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }
    return i-1;
}

// Function to perform quickselect
int quickselect(int *arr, int low, int high, int k) {
    if (low <= high) {
        int pivotIndex = partition(arr, low, high);

        // If the pivot is at the k-1 position, we found the k-th smallest element
        if (pivotIndex == k - 1) {
            return arr[pivotIndex];
        } else if (pivotIndex > k - 1) {
            // Look in the left subarray
            return quickselect(arr, low, pivotIndex - 1, k);
        } else {
            // Look in the right subarray
            return quickselect(arr, pivotIndex + 1, high, k);
        }
    }

    return -1;  // Error case (k out of bounds or array is empty)
}

int main() {
    int arr[] = {4, 8, 11, 2, 17, 4, 7, 6, 13, 1};
    int len = sizeof(arr) / sizeof(arr[0]);
    int k = 3; // Find the 3rd smallest element

    int result = quickselect(arr, 0, len - 1, k);

    if (result != -1) {
        printf("The %dth smallest element is: %d", k, result);
    } else {
        printf("Error: k is out of bounds or array is empty.");
    }

    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# pointer.c


```cpp

#include <stdio.h>
int main(){
    int *ip;
    int c=10;
    ip=&c;
    printf("%p",ip);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# readfile1.c


```cpp

// C Program to illustrate file opening
#include <stdio.h>
// #include <stdlib.h>

char* getline(FILE* ptr, char line[]) {
    // Check if the file pointer is NULL
    if (ptr == NULL) {
        return NULL;
    }

    int c, i = 0;
    // Read characters until newline or EOF
    while ((c = fgetc(ptr)) != '\n' && c != EOF) {
        *(line+i++) = c;
    }
    // Ensure proper null-termination
    // line[i++] = '\n';
    *(line+i) = '\0';

    // Return NULL if nothing was read and EOF was encountered
    if (i == 0 && c == EOF) {
        return NULL;
    }

    return line;
}


int main()
{
    char line[200];
	FILE* fptr;
	fptr = fopen("game.exe", "r");
	if (fptr == NULL) {
		printf("The file is not opened. The program will "
			"now exit.");
	}

    char *result;
    int i;
    while ((result = getline(fptr,line))!=NULL){
        i=0;
        while(*(result+i)!='\0'){
            putchar(*(result+i));
            i++;
        }
        putchar('\n');
    }

	return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# revertword.c


```cpp

#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 100

int main() {
    char input[MAX_LENGTH];

    printf("Enter a line of text: ");
    
    // Using fgets to read a line from stdin
    fgets(input, MAX_LENGTH, stdin);

    // Removing the newline character at the end, if present
    if (input[strlen(input) - 1] == '\n') {
        input[strlen(input) - 1] = '\0';
    }

    printf("You entered: %s\n", input);

    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# sortinng.c


```cpp

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void printarr(int *arr,int len){
    int i=0;
    while(i<len){
        printf("%d ",arr[i]);
        i++;
    }
    printf("\n");
}


void bubble(int *arr,int len){
    // int len=sizeof(arr)/sizeof(arr[0]);
    for (int i=0;i<len-1;i++){
        for (int j=1+i;j<len;j++)
        if (arr[j]<arr[i]){
            int temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
            // break;
        }
    }
}

void insertion(int *arr,int len){
    for (int i=0;i<len;i++){
        for (int j=i;j>0;j--){
            if (arr[j]<arr[j-1]){
                int temp=arr[j];
                arr[j]=arr[j-1];
                arr[j-1]=temp;
            }
            else break;
        }
    }
}


int *mergetwoarr(int arr1[],int arr2[],int len1,int len2){
    int i=0;
    int j=0;
    int *new = malloc(len1+len2);
    while (i<len1 && j<len2){
        if (arr1[i]<arr2[j]){
            new[i+j]=arr1[i];
            i++;
        }
        else{
            new[i+j]=arr2[j];
            j++;
        }
    }
    while (i<len1){
        new[i+j]=arr1[i];
        i++;
    }
    while (j<len2){
        new[i+j]=arr2[j];
        j++;
    }

    return new;
}

int *mergesort(int *arr,int len1){
    if (len1==1){
        int *result = malloc(sizeof(int));
        result[0] = arr[0];
        return result;
    }
    int l1=(int)floor(len1/2);
    int l2=len1-l1;
    int arr1[l1];
    int arr2[l2];
    for (int i=0;i<l1;i++){
        arr1[i]=arr[i];
    }
    for (int i=0;i<l2;i++){
        arr2[i]=arr[i+l2];
    }

    return mergetwoarr(mergesort(arr1,l1),mergesort(arr2,l2),l1,l2);

}



void merge(int arr[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    // Create temporary arrays
    int L[n1], R[n2];

    // Copy data to temporary arrays L[] and R[]
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // Merge the temporary arrays back into arr[l..r]
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[], if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of R[], if there are any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        // Same as (l+r)/2, but avoids overflow for large l and r
        int m = l + (r - l) / 2;

        // Sort first and second halves
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        // Merge the sorted halves
        merge(arr, l, m, r);
    }
}

void partition(int *arr,int len,int pivotindex){
    int i=1;
    int j=len-1;
    int pivot=arr[pivotindex];
    while (i<=j){
        if (arr[i]>pivot){
            if (arr[j]<=pivot){
                int temp=arr[j];
                arr[j]=arr[i];
                arr[i]=temp;
                i++;
            }
            else{
                j--;
            }
        }
        else{
            i++;
        }
    }
    int temp=arr[pivotindex];
    arr[pivotindex]=arr[i-1];
    arr[i-1]=temp;
}

int main(){
    int arr1[]={4,2,8,15,11,9,6,10,3,18,13,20,7,4};
    int len1=sizeof(arr1)/sizeof(arr1[0]);
    // int arr2[]={6,3,9,7,5,1,10,13,19,39,20,11,14,16,17,9,6,3,14};
    // int len2=sizeof(arr2)/sizeof(arr2[0]);
    // bubble(arr1,len1);
    // bubble(arr2,len2);

    partition(arr1,len1,0);
    int i=0;
    while(i<len1){
        printf("%d ",arr1[i]);
        i++;
    }
    
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# taking.c


```cpp

// #include <iostream>
#include <stdio.h>
int main(){
    // int arr[]={1,2,3,4,5,6,7,8,9,10};
    // int arr1[]={11,22,33,44,55,66,77,88,99,00};
    // int *ptr=&arr;
    // printf("%d\n",ptr);
    // printf("%d",*ptr);
    // for (int i=0;i<20;i++){
    //     printf("%d",&arr[i]);
    //     printf("\n");
    //     printf("%d",ptr);
    //     printf("\n");
    //     ptr++;
    //     // printf("%d",arr[i]);
        // printf("\n");
        // printf("%d",&arr1[i]);
        // printf("\n");
        // printf("%d",arr1[i]);
        // printf("\n");
        // printf("\n");

    // }


    int *p=0;
    for(int i=0;i<1000;i++){
        printf("%ld\n",&p);
        p++;
    }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# tempCodeRunnerFile.c


```cpp


        // printf("%c",C[1]);
        // printf("%c",C[2]);

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# class.cpp


```cpp

#include <string>
#include <iostream>
#include <cstdio>
using namespace std;
class Patient
{
    string name;
    string res;
    int age;
    public:
    Patient(string name,int age,string res)
    {
       this->name=name;
       this->age=age;
       this->res=res;
    }
    void details()
        {
            cout<<"The name of patient is "<<this->name<<" age is "<<this->age<<" residence is "<<this->res<<endl;
        }
};   //note please this is where mistake is made
class pt:Patient
{
    
};
int main()
{
    Patient p1("haarit",17,"dhandhuka");
    p1.details();
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# exp.cpp


```cpp



```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# exp2.cpp


```cpp



```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# glitch1.cpp


```cpp

#include <iostream>
using namespace std;
#include <fstream>
int main()
{
    
    cout<<"After sometime a txt file will be generated.....\n please cooperate....\n\n\n"<<endl;
    cout<<"Please wait .... "<<endl;
    cout<<"Till then see this...\n\n\n\n"<<endl;
    int k;
    cout<<"type  anything and press enter to continue\n";
    cin>>k;
    int n=30;
    int count=1;
    for (int i=1;i<=n;i++)
    {
        for (int j=1;j<=i;j++)
        {
            cout<<count<<"  ";
            count+=1;
        }
        cout<<endl;
    }

    while (true)
    {
        fstream hrc;
        hrc.open("hrc.txt",ios::app);
        hrc<<"The Zen of Python, by Tim Peters"<<endl;
        hrc<<endl;
        hrc<<"Beautiful is better than ugly."<<endl;
        hrc<<"Explicit is better than implicit."<<endl;
        hrc<<"Simple is better than complex."<<endl;
        hrc<<"Complex is better than complicated."<<endl;
        hrc<<"Flat is better than nested."<<endl;
        hrc<<"Sparse is better than dense."<<endl;
        hrc<<"Readability counts."<<endl;
        hrc<<"Special cases aren't special enough to break the rules."<<endl;
        hrc<<"Although practicality beats purity."<<endl;
        hrc<<"Errors should never pass silently."<<endl;
        hrc<<"Unless explicitly silenced."<<endl;
        hrc<<"In the face of ambiguity, refuse the temptation to guess."<<endl;
        hrc<<"There should be one-- and preferably only one --obvious way to do it."<<endl;
        hrc<<"Although that way may not be obvious at first unless you're Dutch."<<endl;
        hrc<<"Now is better than never."<<endl;
        hrc<<"Although never is often better than *right* now."<<endl;
        hrc<<"If the implementation is hard to explain, it's a bad idea."<<endl;
        hrc<<"If the implementation is easy to explain, it may be a good idea."<<endl;
        hrc<<"Namespaces are one honking great idea -- let's do more of those!"<<endl;
        hrc.close();

    }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# tempCodeRunnerFile.cpp


```cpp

    // for(int k=i;k>=0;k--)
    // {
    //     cout<<arr[k];
    // }

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# armstrong.cpp


```cpp

#include <iostream>
#include <math.h>
using namespace std;
int main()
{   
    int n;
    n=155;
    int nn=n;
    for (int i=0;i<=n;i++)
    {   
        int sum=0;
        int ii=i;
        while (i>=0)
        {
            int LastDigit=i%10;
            sum=sum+pow(LastDigit,3);
            i=i/10;
        }
        if (sum==ii)
        {
            cout<<sum<<" is Armstrong number"<<endl;
        }
        sum=0;
        
    }
    // int sum = 0;
    // while (n>0)
    // {
    //     int lastdigit=n%10;
    //     sum =sum + pow(lastdigit,3);
    //     n=n/10;
    // }
    // cout<<sum<<endl;
    // if (sum==nn)
    // {
    //     cout<<nn<<" is Armstrong number";
    // }
    // else
    // {
    //     cout<<nn<<" is not Armstrong number";
    // }
    return 0;

}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# calculator.cpp


```cpp

#include <iostream>
using namespace std;
int main()
{
while (true)
{   long double b,c;
    cout<<"Give me 1st number"<<endl;
    cin>>b;
    cout<<"Give me 2nd number"<<endl;
    cin>>c;
    cout<<"Type 1 for addition"<<endl;
    cout<<"Type 2 for subtraction"<<endl;
    cout<<"Type 3 for multiply"<<endl;
    cout<<"Type 4 for division"<<endl;
    cout<<"Type 5 to quit"<<endl;
    cout<<"Enter number accordingly"<<endl;
    int a;
    cin>>a;
    switch(a)
    {
        case 1:
            cout<<"Your answer is "<<b+c<<endl;
            break;
        case 2:
            cout<<"Your answer is "<<b-c<<endl;
            break;
        case 3:
            cout<<"Your answer is "<<b*c<<endl;
            break;
        case 4:
            cout<<"Your answer is "<<b/c<<endl;
            break;
    }
    if (a==5)
    {   
        cout<<"Thank you for using our software....";
        break;
    }
    
}
return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# combi.cpp


```cpp

#include <iostream>
using namespace std;
int fac(int n)
{
    int k=1;
    for (int i=1;i<=n;i++)
    {
        k=k*i;
    }
    return k;
}
 int main()
 {
    // cout<<fac(10);
    int n,r;
    cin>>n>>r;
    int t=(fac(r)*fac(n-r));
    int k=fac(n)/t;
    cout<<k;
 }

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# fibbonacii.cpp


```cpp

#include <iostream>
using namespace std;
void  fib(int n)
{

    int t1=0;
    int t2=1;
    for (int i=1;i<=n;i++)
    {
         cout<<t1<<",";
        int t3=t1+t2;
        t1=t2;
        t2=t3;
    }
    // if (n==0)
    // {
    //     return 0;
    // }
    // else if (n==1)
    // {
    //     return 1;
    // }
    // else
    // {
    //     return fib(n-1)+fib(n-2);
    // }
}
int main()
{
    int n;
    cin>>n;
    fib(n);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# prime.cpp


```cpp

#include <iostream>
#include <cmath>//math library pow()
using namespace std;
void prime(int n)
{
    for(int i=0;i<n;i++){
        for(int div=2;div<i+1;div++){
        if(div==(i)){
            cout<<i<<endl;
        }
        if(i%div==0){
            break;
        }
        }    
    }
}
int main()
{   
int b;
cout<<"Enter the number"<<endl;
cin>>b;
prime(b);
cout<<"IT WORKS";
int a;
cin>>a;
return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# reversenum.cpp


```cpp

#include <iostream>
#include <math.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int reverse = 0;
    while (n>0)
    {
        int lastdigit=n%10;
        reverse=reverse*10+lastdigit;
        n=n/10;
    }
    cout<<reverse;
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# exp.cpp


```cpp

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
int main()
{
    Solution.findMedianSortedArrays()
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# arraysort.cpp


```cpp

#include <bits/stdc++.h>
#include <climits>
using namespace std;
void selection(int arr[],int n)
{
    for(int i=0;i<n-1;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(arr[j]<arr[i])
            {
                int temp=arr[j];
                arr[j]=arr[i];
                arr[i]=temp;
            }
        }
    }
    for (int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
void bubble(int arr[],int n)
{
    //make using single loop structure see soluttion in 8.3.2
    for (int i=0;i<n-1;i++)
    {
        for (int j=i+1;j<n;j++)
        {
        if (arr[i]>arr[j])
        {
        int temp=arr[j];
        arr[j]=arr[i];
        arr[i]=temp;
        }
        }
    }
    for (int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
void insertion(int arr[],int n)
{
    for (int i=0;i<n;i++)
    {
        int current=arr[i];
        int j=i-1;
        while (arr[j]>current && j>=0)
        {
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=current;
    }
    for (int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
}
int main()
{
    // int n;
    // cin>>n;
    // int arr[n];
    // for (int i=0;i<n;i++)
    // {
    //     int k;
    //     cin>>k;
    //     arr[i]=k;
    // }
    int arr[]={2,34,51,76,32,89,58,41,31,56,83,95,62,64,53};
    int n=sizeof(arr)/sizeof(arr[0]);
    selection(arr,n);
    bubble(arr,n);
    insertion(arr,n);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# array_challenge.cpp


```cpp

#include <bits\stdc++.h>
using namespace std;
int maxinarray(int arr[],int n)
{
    int temp=arr[0];
    for (int i=0;i<=n;i++)
    {
        if (arr[i]>temp)
        {
            temp=arr[i];
        }
        else
        {
            temp=temp;   
        }
        // cout<<temp<<endl;
    }
    return temp;
}
int sumofsubarray(int arr[],int n)
{
    int sum=0;
    for (int j=0;j<=n;j++)
    {
        int i=0;
        while (i<=j)
        {
            sum=sum+arr[i];
            // cout<<sum<<endl;
            i++;
        }
    }
    return sum;
}
void arithsub(int arr[],int n)
{
    int ans=2;
    int pd=arr[1]-arr[0];
    int j=2;
    int cur=2;
    while (j<n)
    {
        if (pd==arr[j]-arr[j-1])
        {
            cur++;
        }
        else
        {
            pd=arr[j]-arr[j-1];
            cur=2;
        }
        ans = max(cur,ans);
        j++;
    }
    cout<<ans;

}
int main()
{
    int arr2[]={23,54,92,90,88,86,84,82,80,78,67,85,43,62,31,23,64,13,14,15,16,17,18,19};
    int ar[]={1,2,0,7,2};
    int arr[]={1,23,43,62,84,76,52,98,12,64,98,154,126,73,54,101};
    int k=sizeof(arr)/sizeof(arr[0]);
    int k1=sizeof(ar)/sizeof(ar[0]);
    int k2=sizeof(arr2)/sizeof(arr2[0]);
    //index is upto k-1 so do not type k
    // cout<<maxinarray(arr,k)<<endl;
    // cout<<sumofsubarray(ar,k1)<<endl;
    arithsub(arr2,k2);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# Q1 arr.cpp


```cpp

#include "bits/stdc++.h"
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for (int i=0;i<n;i++)
    {
        int k;
        cin>>k;
        arr[i]=k;
    }
    int lol=0;
    for (int j=0;j<n;j++)
    {
        for (int i=j+1;i<n;i++)
        {
            if (arr[j]==arr[i])
            {
                cout<<j+1;
                lol=1;
                break;
            }
        }
        if (lol==1)
        {
            lol=1;
            break;
        }
    }
    // const int N=1e5;
    // int idx[N];
    // for (int i=0;i<N;i++)
    // {
    //     idx[i]=-1;
    // }
    // int minidx=INT_MAX;
    // for (int i=0;i<n;i++)
    // {
    //     if (idx[arr[i]] != -1)
    //     {
    //         minidx=min(minidx,idx[arr[i]]);
    //     }
    //     else
    //     {
    //         idx[arr[i]]=arr[i];
    //     }
    // }
    // if (minidx==INT_MAX)
    // {
    //     cout<<-1;
    // }
    // else
    // {
    //     cout<<minidx;
    // }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# binarytodecimal.cpp


```cpp

#include <iostream>
#include <string>
using namespace std;
int p(int a,int b)
{
    int h=1;
    for (int j=1;j<=b;j++)
    {
        h=a*h;
    }
    return h;
    
}


//see lec 6.3 for alternate and efficient solution




void btod(string str)
{
    int num =0;
    int len=str.length();
    for (int i=0;i<len;i++)
    {
        int n=str[(len-1)-i]-'0';//to convert char to int 
        //numbers in ascii starts from 48 and 48th is 0
        //so we minus the position of 0 from number
        //(int)char will give the ascii code of the character
        int add=p(2,i);
        num=num+n*add;
    }
    cout<<num;

}
int main()
{
    cout<<"Enter the binary number..."<<endl;
    string str;
    cin>>str;
    btod(str);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# decimaltobinary.cpp


```cpp

#include <iostream>
using namespace std;
long long int p(long long int a,long long int b)
{
    long long int var=1;
    for (long long int i=1;i<=b;i++)
    {
        var=var*a;
    }
    return var;
}
long long int dtob(long long int n)
{
    long long int nn=n;
    long long int var2=0;
    if(n%2==0)
    {
        var2=10*var2+1;
        n=n/2;
         while (n>0)
        {
            long long int lastdigit=n%2;
            var2=10*var2+lastdigit;
            n=n/2;

        }
    }
    else
    {
        while (n>0)
        {
            long long int lastdigit=n%2;
            var2=10*var2+lastdigit;
            n=n/2;

        }
    }
    // cout<<var2<<endl;
    long long int var3=0;
    while (var2>0)
    {
        long long int lastdigit2=var2%10;
        var3=10*var3+lastdigit2;
        var2=var2/10;
    }
        if (nn%2==0)
    {
        return var3-1;
    }
    else
    {
        return var3;
    }
}
main()
{
    // int k;
    // cin>>k;
    // for (int i;i<=k;i++)
    // {
    //    cout<<i<<"----->"<<dtob(i)<<endl;
    // }
    // cout<<dtob(100000);
    // cout<<p(2,k);
    // printf("%dll",);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# decimaltohexadecimal.cpp


```cpp

#include <iostream>
#include <string>
#include <cmath>
//programme to convert decimal into hexadecimal
using namespace std;
void dtohex(int n)
{
    int i=0;
    string hex[50000];
    while (n>0)
    {
        string l;
        int last=n%16;
        switch (last)
        {
            case 0:
                l=to_string(last);
                hex[i]=l;
                break;
            case 1:
                l=to_string(last);
                hex[i]=l;
                break;
            case 2:
                l=to_string(last);
                hex[i]=l;
                break;
            case 3:
                l=to_string(last);
                hex[i]=l;
                break;
            case 4:
                l=to_string(last);
                hex[i]=l;
                break;
            case 5:
                l=to_string(last);
                hex[i]=l;
                break;
            case 6:
                l=to_string(last);
                hex[i]=l;
                break;
            case 7:
                l=to_string(last);
                hex[i]=l;
                break;
            case 8:
                l=to_string(last);
                hex[i]=l;
                break;
            case 9:
                l=to_string(last);
                hex[i]=l;
                break;
            case 10:
                to_string(last);
                hex[i]='A';
                break;
            case 11:
                to_string(last);
                hex[i]='B';
                break;
            case 12:
                to_string(last);
                hex[i]='C';
                break;
            case 13:
                to_string(last);
                hex[i]='D';
                break;
            case 14:
                to_string(last);
                hex[i]='E';
                break;
            case 15:
                to_string(last);
                hex[i]='F';
                break;
            default:
                break;
        }
        n=n/16;
        i++;
    }
    i=i-1;
    for(int j=i;j>=0;j--)
    {
        cout<<hex[j];
    }
    cout<<endl;
}
int main()
{
    int n;
    cin>>n;
    dtohex(n);
    // for (int i=0;i<=n;i++)
    // {
    //     cout<<"Hexadecimal of "<<i<<"is ";
    //     dtohex(i);
    // }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# decimaltooctal.cpp


```cpp

#include <iostream>
#include <climits>
using namespace std;
long long int p(long long int a,long long int b)
{
    long long int var=1;
    for (long long int i=1;i<=b;i++)
    {
        var=var*a;
    }
    return var;
}
long long int decimaltooctal(long long int n)
{
    long long int nn=n;
    long long int var2=0;
    if(n%8==0)
    {
        var2=10*var2+1;
        n=n/8;
         while (n>0)
        {
            long long int lastdigit=n%8;
            var2=10*var2+lastdigit;
            n=n/8;

        }
    }
    else
    {
        while (n>0)
        {
            long long int lastdigit=n%8;
            var2=10*var2+lastdigit;
            n=n/8;

        }
    }
    // cout<<var2<<endl;
    long long int var3=0;
    while (var2>0)
    {
        long long int lastdigit2=var2%10;
        var3=10*var3+lastdigit2;
        var2=var2/10;
    }
        if (nn%8==0)
    {
        return var3-1;
    }
    else
    {
        return var3;
    }
}
int main()
{
    int k;
    cin>>k;
    for (int i=0;i<=k;i++)
    {
        cout<<i<<"----->"<<decimaltooctal(i)<<endl;
    }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# dtobadvanced.cpp


```cpp

#include <iostream>
using namespace std;

void dtob(int n)
{
    long long int k=100000;
    long long int arr[k]; // Assuming 32-bit integers, you can adjust the size accordingly
                    //this is where the problem is. think what an  empty array can do
    int i = 0;
    while (n > 0)
    {
        int last = n % 2;
        arr[i] = last;
        n = n / 2;
        i++;
    }
    for (int j=i-1;j>=0;j--)
    {
        cout<<arr[j];
    }
    cout << endl;
}

int main()
{
    dtob(999999999);
    // for (int i=0;i<=100000;i++)
    // {
    //     cout<<"Binary of "<<i<<"is ";
    //     dtob(i);
    // }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# hexadecimaltodecimal.cpp


```cpp

#include <iostream>
#include <string>
using namespace std;
int p(int a,int b)
{
    int h=1;
    for (int j=1;j<=b;j++)
    {
        h=a*h;
    }
    return h;
    
}
void hextodec(string str)
{
    int num=0;
    int len = str.length();
    for (int i=0;i<len;i++)
    {
        int n=str[(len-1)-i]-'0';
        if (-1<n && n<10)
        {
            int add=p(16,i);
            num=num+n*add;
        }
        else if (n==49||n==17)
        {
            // cout<<n<<endl;
            int add=p(16,i);
            num=num+10*add;
        }
        else if (n==50||n==18)
        {
            int add=p(16,i);
            num=num+11*add;
        }
        else if (n==51||n==19)
        {
            int add=p(16,i);
            num=num+12*add;
        }
        else if (n==52||n==20)
        {
            int add=p(16,i);
            num=num+13*add;
        }
        else if (n==53||n==21)
        {
            int add=p(16,i);
            num=num+14*add;
        }
        else if (n==54||n==22)
        {
            int add=p(16,i);
            num=num+15*add;
        }
        else
        {
            cout<<"Not a valid Input";
            break;
        }
    }
    cout<<num;
}
int main()
{
    cout<<"Enter the Hexadecimal number.."<<endl;
    string str;
    cin>>str;
    hextodec(str);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# octaltodecimal.cpp


```cpp

#include <iostream>
#include <string>
using namespace std;
int p(int a,int b)
{
    int h=1;
    for (int j=1;j<=b;j++)
    {
        h=a*h;
    }
    return h;
    
}
void btod(string str)
{
    int num =0;
    int len=str.length();
    for (int i=0;i<len;i++)
    {
        int n=str[(len-1)-i]-'0';//to convert char to int 
        //numbers in ascii starts from 48 and 48th is 0
        //so we minus the position of 0 from number
        //(int)char will give the ascii code of the character
        int add=p(8,i);
        num=num+n*add;
    }
    cout<<num;

}
int main()
{
    cout<<"Enter the octal number..."<<endl;
    string str;
    cin>>str;
    btod(str);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# pattern1.cpp


```cpp

#include <iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for (int i=n;i>=1;i--)
    {
        for (int j=1;j<=i;j++)
        {
            cout<<j<<" ";
        }
        cout<<endl;
    }
    for (int i=n;i>=1;i--)
    {
        for (int j=1;j<=i;j++)
        {
            cout<<i<<" ";
        }
        cout<<endl;
    }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# pattern10.cpp


```cpp

#include <iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for (int i=1;i<=3;i++)
    {
        for (int j=1;j<=n;j++)
        {
            if((i+j)%4==0 || (i==2 && j%4==0))
            {
                cout<<"*";
            }
            else
            {
                cout<<" ";
            }
        }
        cout<<endl;
    }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# pattern2.cpp


```cpp

#include <iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for (int i=1;i<=n;i++)
    {
        for(int j=1;j<=i;j++)
        {
            cout<<" ";
        }
        for(int j=1;j<=n;j++)
        {
            cout<<" *";
        }
        cout<<endl;
    }
    for (int i=1;i<=n;i++)
    {
        for(int j=n-i;j>=1;j--)
        {
            cout<<" ";
        }
        for(int j=1;j<=n;j++)
        {
            cout<<" *";
        }
        cout<<endl;
    }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# pattern3.cpp


```cpp

#include <iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    //solution
    for (int i;i<=n;i++)
    {
        for(int j=1;j<=i;j++)
        {
            if ((i+j)%2==0)
            {
                cout<<" 1";
            }
            else
            {
                cout<<" 0";
            }
        }
        cout<<endl;
    }






//lenghty code my solution
    // for (int i=1;i<=n;i++)
    // {
    //     if (i%2==0)
    //     {
    //         for (int j=1;j<=i;j++)
    //         {
    //             if(j%2!=0)
    //             {
    //                 cout<<0<<" ";
    //             }
    //             else
    //             {
    //                 cout<<1<<" ";
    //             }
    //         }
    //     }
    //     else
    //     {
    //         for (int j=1;j<=i;j++)
    //         {
    //             if(j%2!=0)
    //             {
    //                 cout<<1<<" ";
    //             }
    //             else
    //             {
    //                 cout<<0<<" ";
    //             }
    //         }
    //     }
    // cout<<endl;
    // }









//unexpected pattern
    // for (int i=1;i<=n;i++)
    // {
    //     for (int j=1;j<=i;j++)
    //     {
    //         if (j%2==0)
    //         {
    //             cout<<0<<" ";
    //         }
    //         else
    //         {
    //             cout<<1<<" ";
    //         }
    //     }
    //     cout<<endl;
    // }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# pattern4.cpp


```cpp

#include <iostream>
using namespace std;
int main()
{
    cout<<"Enter the number of rows"<<endl;
    int n;
    cin>>n;
    for (int i=1;i<=n;i++)
    {
        for (int j=1;j<=i;j++)
        {
            cout<<"*";
        }
        int space=2*n-2*i;
        for (int j=1;j<=space;j++)
        {
            cout<<" ";
        }
        for (int j=1;j<=i;j++)
        {
            cout<<"*";
        }
        cout<<endl;
    }
    for (int i=n;i>=1;i--)
    {
        for (int j=1;j<=i;j++)
        {
            cout<<"*";
        }
        int space=2*n-2*i;
        for (int j=1;j<=space;j++)
        {
            cout<<" ";
        }
        for (int j=1;j<=i;j++)
        {
            cout<<"*";
        }
        cout<<endl;
    }
}/*hello world*/

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# pattern5.cpp


```cpp

#include <iostream>
using namespace std;
int main()
{   int n;
    cin>>n;
    int count=1;
    for (int i=1;i<=n;i++)
    {
        for (int j=1;j<=i;j++)
        {
            cout<<count<<"  ";
            count+=1;
        }
        cout<<endl;
    }
    int a;
    cin>>a;
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# pattern6.cpp


```cpp

#include <iostream>
using namespace std;
//in c++ you cannot give space between the name of the file
int main()
{   
    int rows;
    int cols;
    cin>>rows>>cols;


    // for (int i=0;i<rows+1;i++)
    // {  
    //     if (i==0)
    //     {

    //         for (int j=0;j<cols+1;j++)
    //         {
    //         cout<<"*";
    //         }
    //         cout<<endl;
    //     }
    //     if (0<i<rows)
    //     {
    //         cout<<"*";
    //         for (int k=0;k<(cols-1);k++)
    //         {
    //             cout<<" ";
    //         }
    //         cout<<"*"<<endl;
    //     }
    //     if(i==rows)
    //     {
    //         for (int l=0;l<cols+1;l++)
    //         {
    //             cout<<"*";
    //         }
    //         cout<<endl; 
    //     }
    // }

    //solution
    for (int i=1;i<=rows;i++)
    {
        for (int j=1;j<=cols;j++)
        {
            if(i==1 || j==1 || i==rows || j==cols)
            {
                cout<<"*";
            }
            else
            {
                cout<<" ";
            }
        }
        cout<<endl;
    }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# pattern7.cpp


```cpp

#include <iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for (int i=1;i<=n;i++)
    {
        for (int j=n-i;j>=1;j--)
        {
            cout<<" ";
        }
        for(int j=1;j<=i;j++)
        {
            cout<<j<<" ";
        }
        cout<<endl;
    }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# pattern8.cpp


```cpp

#include <iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for (int i=1;i<=n;i++)
    {
        for(int j=n-i;j>=1;j--)
        {
            cout<<" ";
        }
        for (int k=i;k>1;k--)
        {
            cout<<k;
        }
        for (int l=1;l<=i;l++)
        {
            cout<<l;
        }
        cout<<endl;
    }
    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# pattern9.cpp


```cpp

#include <iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for (int i=1;i<=n;i++)
    {
        for (int j=n-i;j>=1;j--)
        {
            cout<<" ";
        }
        for (int k=1;k<=2*i-1;k++)
        {
            cout<<"*";
        }
        //longer logic
        // for (int k=1;k<i;k++)
        // {
        //     cout<<"*";
        // }
        // for (int l=1;l<=i;l++)
        // {
        //     cout<<"*";
        // }
        cout<<endl;
    }
    for (int i=n;i>=1;i--)
    {
        for (int j=n-i;j>=1;j--)
        {
            cout<<" ";
        }
        for (int k=1;k<=2*i-1;k++)
        {
            cout<<"*";
        }
        // for (int k=1;k<i;k++)
        // {
        //     cout<<"*";
        // }
        // for (int l=1;l<=i;l++)
        // {
        //     cout<<"*";
        // }
        cout<<endl;
    }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# tempCodeRunnerFile.cpp


```cpp

    int count=1;
    for (int i=1;i<=n;i++)
    {
        for (int j=1;j<=i;j++)
        {
            cout<<count<<"  ";
            count+=1;
        }
        cout<<endl;
    }

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# justchill.c


```cpp

#include <stdio.h>
int main(){

    int arr[]={6,3,8,5,9,2,1,0,5};
    int i=0;
    while (i<(sizeof(arr)/sizeof(arr[0]))){
        int j=i;
        while (j >= 1)
        {
            if (arr[j]<arr[j-1]){
                int temp=arr[j];
                arr[j]=arr[j-1];
                arr[j-1]=temp;
            }
            j=j-1;
        }
        i++;
    }
    
    for(int i = 0; i < (sizeof(arr)/sizeof(arr[0])); i++) {
            printf("%d ", arr[i]);
            printf("\n");
    }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# greenlet.cpp


```cpp

/* -*- indent-tabs-mode: nil; tab-width: 4; -*- */
/* Format with:
 *  clang-format -i --style=file src/greenlet/greenlet.c
 *
 *
 * Fix missing braces with:
 *   clang-tidy src/greenlet/greenlet.c -fix -checks="readability-braces-around-statements"
*/
#include <cstdlib>
#include <string>
#include <algorithm>
#include <exception>


#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h" // PyMemberDef

#include "greenlet_internal.hpp"
// Code after this point can assume access to things declared in stdint.h,
// including the fixed-width types. This goes for the platform-specific switch functions
// as well.
#include "greenlet_refs.hpp"
#include "greenlet_slp_switch.hpp"
#include "greenlet_thread_state.hpp"
#include "greenlet_thread_support.hpp"
#include "greenlet_greenlet.hpp"

#include "TGreenletGlobals.cpp"
#include "TThreadStateDestroy.cpp"
#include "TGreenlet.cpp"
#include "TMainGreenlet.cpp"
#include "TUserGreenlet.cpp"
#include "TBrokenGreenlet.cpp"
#include "TExceptionState.cpp"
#include "TPythonState.cpp"
#include "TStackState.cpp"


using greenlet::LockGuard;
using greenlet::LockInitError;
using greenlet::PyErrOccurred;
using greenlet::Require;

using greenlet::g_handle_exit;
using greenlet::single_result;

using greenlet::Greenlet;
using greenlet::UserGreenlet;
using greenlet::MainGreenlet;
using greenlet::BrokenGreenlet;
using greenlet::ThreadState;
using greenlet::PythonState;



// ******* Implementation of things from included files
template<typename T, greenlet::refs::TypeChecker TC>
greenlet::refs::_BorrowedGreenlet<T, TC>& greenlet::refs::_BorrowedGreenlet<T, TC>::operator=(const greenlet::refs::BorrowedObject& other)
{
    this->_set_raw_pointer(static_cast<PyObject*>(other));
    return *this;
}

template <typename T, greenlet::refs::TypeChecker TC>
inline greenlet::refs::_BorrowedGreenlet<T, TC>::operator Greenlet*() const noexcept
{
    if (!this->p) {
        return nullptr;
    }
    return reinterpret_cast<PyGreenlet*>(this->p)->pimpl;
}

template<typename T, greenlet::refs::TypeChecker TC>
greenlet::refs::_BorrowedGreenlet<T, TC>::_BorrowedGreenlet(const BorrowedObject& p)
    : BorrowedReference<T, TC>(nullptr)
{

    this->_set_raw_pointer(p.borrow());
}

template <typename T, greenlet::refs::TypeChecker TC>
inline greenlet::refs::_OwnedGreenlet<T, TC>::operator Greenlet*() const noexcept
{
    if (!this->p) {
        return nullptr;
    }
    return reinterpret_cast<PyGreenlet*>(this->p)->pimpl;
}



#ifdef __clang__
#    pragma clang diagnostic push
#    pragma clang diagnostic ignored "-Wmissing-field-initializers"
#    pragma clang diagnostic ignored "-Wwritable-strings"
#elif defined(__GNUC__)
#    pragma GCC diagnostic push
//  warning: ISO C++ forbids converting a string constant to ‘char*’
// (The python APIs aren't const correct and accept writable char*)
#    pragma GCC diagnostic ignored "-Wwrite-strings"
#endif


/***********************************************************

A PyGreenlet is a range of C stack addresses that must be
saved and restored in such a way that the full range of the
stack contains valid data when we switch to it.

Stack layout for a greenlet:

               |     ^^^       |
               |  older data   |
               |               |
  stack_stop . |_______________|
        .      |               |
        .      | greenlet data |
        .      |   in stack    |
        .    * |_______________| . .  _____________  stack_copy + stack_saved
        .      |               |     |             |
        .      |     data      |     |greenlet data|
        .      |   unrelated   |     |    saved    |
        .      |      to       |     |   in heap   |
 stack_start . |     this      | . . |_____________| stack_copy
               |   greenlet    |
               |               |
               |  newer data   |
               |     vvv       |


Note that a greenlet's stack data is typically partly at its correct
place in the stack, and partly saved away in the heap, but always in
the above configuration: two blocks, the more recent one in the heap
and the older one still in the stack (either block may be empty).

Greenlets are chained: each points to the previous greenlet, which is
the one that owns the data currently in the C stack above my
stack_stop.  The currently running greenlet is the first element of
this chain.  The main (initial) greenlet is the last one.  Greenlets
whose stack is entirely in the heap can be skipped from the chain.

The chain is not related to execution order, but only to the order
in which bits of C stack happen to belong to greenlets at a particular
point in time.

The main greenlet doesn't have a stack_stop: it is responsible for the
complete rest of the C stack, and we don't know where it begins.  We
use (char*) -1, the largest possible address.

States:
  stack_stop == NULL && stack_start == NULL:  did not start yet
  stack_stop != NULL && stack_start == NULL:  already finished
  stack_stop != NULL && stack_start != NULL:  active

The running greenlet's stack_start is undefined but not NULL.

 ***********************************************************/

static PyGreenlet*
green_create_main(ThreadState* state)
{
    PyGreenlet* gmain;

    /* create the main greenlet for this thread */
    gmain = (PyGreenlet*)PyType_GenericAlloc(&PyGreenlet_Type, 0);
    if (gmain == NULL) {
        Py_FatalError("green_create_main failed to alloc");
        return NULL;
    }
    new MainGreenlet(gmain, state);

    assert(Py_REFCNT(gmain) == 1);
    return gmain;
}



/***********************************************************/

/* Some functions must not be inlined:
   * slp_restore_state, when inlined into slp_switch might cause
     it to restore stack over its own local variables
   * slp_save_state, when inlined would add its own local
     variables to the saved stack, wasting space
   * slp_switch, cannot be inlined for obvious reasons
   * g_initialstub, when inlined would receive a pointer into its
     own stack frame, leading to incomplete stack save/restore

g_initialstub is a member function and declared virtual so that the
compiler always calls it through a vtable.

slp_save_state and slp_restore_state are also member functions. They
are called from trampoline functions that themselves are declared as
not eligible for inlining.
*/

extern "C" {
static int GREENLET_NOINLINE(slp_save_state_trampoline)(char* stackref)
{
    return switching_thread_state->slp_save_state(stackref);
}
static void GREENLET_NOINLINE(slp_restore_state_trampoline)()
{
    switching_thread_state->slp_restore_state();
}
}


/***********************************************************/

static PyGreenlet*
green_new(PyTypeObject* type, PyObject* UNUSED(args), PyObject* UNUSED(kwds))
{
    PyGreenlet* o =
        (PyGreenlet*)PyBaseObject_Type.tp_new(type, mod_globs->empty_tuple, mod_globs->empty_dict);
    if (o) {
        new UserGreenlet(o, GET_THREAD_STATE().state().borrow_current());
        assert(Py_REFCNT(o) == 1);
    }
    return o;
}

static PyGreenlet*
green_unswitchable_new(PyTypeObject* type, PyObject* UNUSED(args), PyObject* UNUSED(kwds))
{
    PyGreenlet* o =
        (PyGreenlet*)PyBaseObject_Type.tp_new(type, mod_globs->empty_tuple, mod_globs->empty_dict);
    if (o) {
        new BrokenGreenlet(o, GET_THREAD_STATE().state().borrow_current());
        assert(Py_REFCNT(o) == 1);
    }
    return o;
}

static int
green_setrun(BorrowedGreenlet self, BorrowedObject nrun, void* c);
static int
green_setparent(BorrowedGreenlet self, BorrowedObject nparent, void* c);

static int
green_init(BorrowedGreenlet self, BorrowedObject args, BorrowedObject kwargs)
{
    PyArgParseParam run;
    PyArgParseParam nparent;
    static const char* const kwlist[] = {
        "run",
        "parent",
        NULL
    };

    // recall: The O specifier does NOT increase the reference count.
    if (!PyArg_ParseTupleAndKeywords(
             args, kwargs, "|OO:green", (char**)kwlist, &run, &nparent)) {
        return -1;
    }

    if (run) {
        if (green_setrun(self, run, NULL)) {
            return -1;
        }
    }
    if (nparent && !nparent.is_None()) {
        return green_setparent(self, nparent, NULL);
    }
    return 0;
}



static int
green_traverse(PyGreenlet* self, visitproc visit, void* arg)
{
    // We must only visit referenced objects, i.e. only objects
    // Py_INCREF'ed by this greenlet (directly or indirectly):
    //
    // - stack_prev is not visited: holds previous stack pointer, but it's not
    //    referenced
    // - frames are not visited as we don't strongly reference them;
    //    alive greenlets are not garbage collected
    //    anyway. This can be a problem, however, if this greenlet is
    //    never allowed to finish, and is referenced from the frame: we
    //    have an uncollectible cycle in that case. Note that the
    //    frame object itself is also frequently not even tracked by the GC
    //    starting with Python 3.7 (frames are allocated by the
    //    interpreter untracked, and only become tracked when their
    //    evaluation is finished if they have a refcount > 1). All of
    //    this is to say that we should probably strongly reference
    //    the frame object. Doing so, while always allowing GC on a
    //    greenlet, solves several leaks for us.

    Py_VISIT(self->dict);
    if (!self->pimpl) {
        // Hmm. I have seen this at interpreter shutdown time,
        // I think. That's very odd because this doesn't go away until
        // we're ``green_dealloc()``, at which point we shouldn't be
        // traversed anymore.
        return 0;
    }

    return self->pimpl->tp_traverse(visit, arg);
}

static int
green_is_gc(BorrowedGreenlet self)
{
    int result = 0;
    /* Main greenlet can be garbage collected since it can only
       become unreachable if the underlying thread exited.
       Active greenlets --- including those that are suspended ---
       cannot be garbage collected, however.
    */
    if (self->main() || !self->active()) {
        result = 1;
    }
    // The main greenlet pointer will eventually go away after the thread dies.
    if (self->was_running_in_dead_thread()) {
        // Our thread is dead! We can never run again. Might as well
        // GC us. Note that if a tuple containing only us and other
        // immutable objects had been scanned before this, when we
        // would have returned 0, the tuple will take itself out of GC
        // tracking and never be investigated again. So that could
        // result in both us and the tuple leaking due to an
        // unreachable/uncollectible reference. The same goes for
        // dictionaries.
        //
        // It's not a great idea to be changing our GC state on the
        // fly.
        result = 1;
    }
    return result;
}


static int
green_clear(PyGreenlet* self)
{
    /* Greenlet is only cleared if it is about to be collected.
       Since active greenlets are not garbage collectable, we can
       be sure that, even if they are deallocated during clear,
       nothing they reference is in unreachable or finalizers,
       so even if it switches we are relatively safe. */
    // XXX: Are we responsible for clearing weakrefs here?
    Py_CLEAR(self->dict);
    return self->pimpl->tp_clear();
}

/**
 * Returns 0 on failure (the object was resurrected) or 1 on success.
 **/
static int
_green_dealloc_kill_started_non_main_greenlet(BorrowedGreenlet self)
{
    /* Hacks hacks hacks copied from instance_dealloc() */
    /* Temporarily resurrect the greenlet. */
    assert(self.REFCNT() == 0);
    Py_SET_REFCNT(self.borrow(), 1);
    /* Save the current exception, if any. */
    PyErrPieces saved_err;
    try {
        // BY THE TIME WE GET HERE, the state may actually be going
        // away
        // if we're shutting down the interpreter and freeing thread
        // entries,
        // this could result in freeing greenlets that were leaked. So
        // we can't try to read the state.
        self->deallocing_greenlet_in_thread(
              self->thread_state()
              ? static_cast<ThreadState*>(GET_THREAD_STATE())
              : nullptr);
    }
    catch (const PyErrOccurred&) {
        PyErr_WriteUnraisable(self.borrow_o());
        /* XXX what else should we do? */
    }
    /* Check for no resurrection must be done while we keep
     * our internal reference, otherwise PyFile_WriteObject
     * causes recursion if using Py_INCREF/Py_DECREF
     */
    if (self.REFCNT() == 1 && self->active()) {
        /* Not resurrected, but still not dead!
           XXX what else should we do? we complain. */
        PyObject* f = PySys_GetObject("stderr");
        Py_INCREF(self.borrow_o()); /* leak! */
        if (f != NULL) {
            PyFile_WriteString("GreenletExit did not kill ", f);
            PyFile_WriteObject(self.borrow_o(), f, 0);
            PyFile_WriteString("\n", f);
        }
    }
    /* Restore the saved exception. */
    saved_err.PyErrRestore();
    /* Undo the temporary resurrection; can't use DECREF here,
     * it would cause a recursive call.
     */
    assert(self.REFCNT() > 0);

    Py_ssize_t refcnt = self.REFCNT() - 1;
    Py_SET_REFCNT(self.borrow_o(), refcnt);
    if (refcnt != 0) {
        /* Resurrected! */
        _Py_NewReference(self.borrow_o());
        Py_SET_REFCNT(self.borrow_o(), refcnt);
        /* Better to use tp_finalizer slot (PEP 442)
         * and call ``PyObject_CallFinalizerFromDealloc``,
         * but that's only supported in Python 3.4+; see
         * Modules/_io/iobase.c for an example.
         *
         * The following approach is copied from iobase.c in CPython 2.7.
         * (along with much of this function in general). Here's their
         * comment:
         *
         * When called from a heap type's dealloc, the type will be
         * decref'ed on return (see e.g. subtype_dealloc in typeobject.c). */
        if (PyType_HasFeature(self.TYPE(), Py_TPFLAGS_HEAPTYPE)) {
            Py_INCREF(self.TYPE());
        }

        PyObject_GC_Track((PyObject*)self);

        _Py_DEC_REFTOTAL;
#ifdef COUNT_ALLOCS
        --Py_TYPE(self)->tp_frees;
        --Py_TYPE(self)->tp_allocs;
#endif /* COUNT_ALLOCS */
        return 0;
    }
    return 1;
}


static void
green_dealloc(PyGreenlet* self)
{
    PyObject_GC_UnTrack(self);
    BorrowedGreenlet me(self);
    if (me->active()
        && me->started()
        && !me->main()) {
        if (!_green_dealloc_kill_started_non_main_greenlet(me)) {
            return;
        }
    }

    if (self->weakreflist != NULL) {
        PyObject_ClearWeakRefs((PyObject*)self);
    }
    Py_CLEAR(self->dict);

    if (self->pimpl) {
        // In case deleting this, which frees some memory,
        // somehow winds up calling back into us. That's usually a
        //bug in our code.
        Greenlet* p = self->pimpl;
        self->pimpl = nullptr;
        delete p;
    }
    // and finally we're done. self is now invalid.
    Py_TYPE(self)->tp_free((PyObject*)self);
}



static OwnedObject
throw_greenlet(BorrowedGreenlet self, PyErrPieces& err_pieces)
{
    PyObject* result = nullptr;
    err_pieces.PyErrRestore();
    assert(PyErr_Occurred());
    if (self->started() && !self->active()) {
        /* dead greenlet: turn GreenletExit into a regular return */
        result = g_handle_exit(OwnedObject()).relinquish_ownership();
    }
    self->args() <<= result;

    return single_result(self->g_switch());
}



PyDoc_STRVAR(
    green_switch_doc,
    "switch(*args, **kwargs)\n"
    "\n"
    "Switch execution to this greenlet.\n"
    "\n"
    "If this greenlet has never been run, then this greenlet\n"
    "will be switched to using the body of ``self.run(*args, **kwargs)``.\n"
    "\n"
    "If the greenlet is active (has been run, but was switch()'ed\n"
    "out before leaving its run function), then this greenlet will\n"
    "be resumed and the return value to its switch call will be\n"
    "None if no arguments are given, the given argument if one\n"
    "argument is given, or the args tuple and keyword args dict if\n"
    "multiple arguments are given.\n"
    "\n"
    "If the greenlet is dead, or is the current greenlet then this\n"
    "function will simply return the arguments using the same rules as\n"
    "above.\n");

static PyObject*
green_switch(PyGreenlet* self, PyObject* args, PyObject* kwargs)
{
    using greenlet::SwitchingArgs;
    SwitchingArgs switch_args(OwnedObject::owning(args), OwnedObject::owning(kwargs));
    self->pimpl->may_switch_away();
    self->pimpl->args() <<= switch_args;

    // If we're switching out of a greenlet, and that switch is the
    // last thing the greenlet does, the greenlet ought to be able to
    // go ahead and die at that point. Currently, someone else must
    // manually switch back to the greenlet so that we "fall off the
    // end" and can perform cleanup. You'd think we'd be able to
    // figure out that this is happening using the frame's ``f_lasti``
    // member, which is supposed to be an index into
    // ``frame->f_code->co_code``, the bytecode string. However, in
    // recent interpreters, ``f_lasti`` tends not to be updated thanks
    // to things like the PREDICT() macros in ceval.c. So it doesn't
    // really work to do that in many cases. For example, the Python
    // code:
    //     def run():
    //         greenlet.getcurrent().parent.switch()
    // produces bytecode of len 16, with the actual call to switch()
    // being at index 10 (in Python 3.10). However, the reported
    // ``f_lasti`` we actually see is...5! (Which happens to be the
    // second byte of the CALL_METHOD op for ``getcurrent()``).

    try {
        //OwnedObject result = single_result(self->pimpl->g_switch());
        OwnedObject result(single_result(self->pimpl->g_switch()));
#ifndef NDEBUG
        // Note that the current greenlet isn't necessarily self. If self
        // finished, we went to one of its parents.
        assert(!self->pimpl->args());

        const BorrowedGreenlet& current = GET_THREAD_STATE().state().borrow_current();
        // It's possible it's never been switched to.
        assert(!current->args());
#endif
        PyObject* p = result.relinquish_ownership();

        if (!p && !PyErr_Occurred()) {
            // This shouldn't be happening anymore, so the asserts
            // are there for debug builds. Non-debug builds
            // crash "gracefully" in this case, although there is an
            // argument to be made for killing the process in all
            // cases --- for this to be the case, our switches
            // probably nested in an incorrect way, so the state is
            // suspicious. Nothing should be corrupt though, just
            // confused at the Python level. Letting this propagate is
            // probably good enough.
            assert(p || PyErr_Occurred());
            throw PyErrOccurred(
                mod_globs->PyExc_GreenletError,
                "Greenlet.switch() returned NULL without an exception set."
            );
        }
        return p;
    }
    catch(const PyErrOccurred&) {
        return nullptr;
    }
}

PyDoc_STRVAR(
    green_throw_doc,
    "Switches execution to this greenlet, but immediately raises the\n"
    "given exception in this greenlet.  If no argument is provided, the "
    "exception\n"
    "defaults to `greenlet.GreenletExit`.  The normal exception\n"
    "propagation rules apply, as described for `switch`.  Note that calling "
    "this\n"
    "method is almost equivalent to the following::\n"
    "\n"
    "    def raiser():\n"
    "        raise typ, val, tb\n"
    "    g_raiser = greenlet(raiser, parent=g)\n"
    "    g_raiser.switch()\n"
    "\n"
    "except that this trick does not work for the\n"
    "`greenlet.GreenletExit` exception, which would not propagate\n"
    "from ``g_raiser`` to ``g``.\n");

static PyObject*
green_throw(PyGreenlet* self, PyObject* args)
{
    PyArgParseParam typ(mod_globs->PyExc_GreenletExit);
    PyArgParseParam val;
    PyArgParseParam tb;

    if (!PyArg_ParseTuple(args, "|OOO:throw", &typ, &val, &tb)) {
        return nullptr;
    }

    assert(typ.borrow() || val.borrow());

    self->pimpl->may_switch_away();
    try {
        // Both normalizing the error and the actual throw_greenlet
        // could throw PyErrOccurred.
        PyErrPieces err_pieces(typ.borrow(), val.borrow(), tb.borrow());

        return throw_greenlet(self, err_pieces).relinquish_ownership();
    }
    catch (const PyErrOccurred&) {
        return nullptr;
    }
}

static int
green_bool(PyGreenlet* self)
{
    return self->pimpl->active();
}

/**
 * CAUTION: Allocates memory, may run GC and arbitrary Python code.
 */
static PyObject*
green_getdict(PyGreenlet* self, void* UNUSED(context))
{
    if (self->dict == NULL) {
        self->dict = PyDict_New();
        if (self->dict == NULL) {
            return NULL;
        }
    }
    Py_INCREF(self->dict);
    return self->dict;
}

static int
green_setdict(PyGreenlet* self, PyObject* val, void* UNUSED(context))
{
    PyObject* tmp;

    if (val == NULL) {
        PyErr_SetString(PyExc_TypeError, "__dict__ may not be deleted");
        return -1;
    }
    if (!PyDict_Check(val)) {
        PyErr_SetString(PyExc_TypeError, "__dict__ must be a dictionary");
        return -1;
    }
    tmp = self->dict;
    Py_INCREF(val);
    self->dict = val;
    Py_XDECREF(tmp);
    return 0;
}

static bool
_green_not_dead(BorrowedGreenlet self)
{
    // XXX: Where else should we do this?
    // Probably on entry to most Python-facing functions?
    if (self->was_running_in_dead_thread()) {
        self->deactivate_and_free();
        return false;
    }
    return self->active() || !self->started();
}


static PyObject*
green_getdead(BorrowedGreenlet self, void* UNUSED(context))
{
    if (_green_not_dead(self)) {
        Py_RETURN_FALSE;
    }
    else {
        Py_RETURN_TRUE;
    }
}

static PyObject*
green_get_stack_saved(PyGreenlet* self, void* UNUSED(context))
{
    return PyLong_FromSsize_t(self->pimpl->stack_saved());
}


static PyObject*
green_getrun(BorrowedGreenlet self, void* UNUSED(context))
{
    try {
        OwnedObject result(self->run());
        return result.relinquish_ownership();
    }
    catch(const PyErrOccurred&) {
        return nullptr;
    }
}





static int
green_setrun(BorrowedGreenlet self, BorrowedObject nrun, void* UNUSED(context))
{
    try {
        self->run(nrun);
        return 0;
    }
    catch(const PyErrOccurred&) {
        return -1;
    }
}

static PyObject*
green_getparent(BorrowedGreenlet self, void* UNUSED(context))
{
    return self->parent().acquire_or_None();
}



static int
green_setparent(BorrowedGreenlet self, BorrowedObject nparent, void* UNUSED(context))
{
    try {
        self->parent(nparent);
    }
    catch(const PyErrOccurred&) {
        return -1;
    }
    return 0;
}


static PyObject*
green_getcontext(const PyGreenlet* self, void* UNUSED(context))
{
    const Greenlet *const g = self->pimpl;
    try {
        OwnedObject result(g->context());
        return result.relinquish_ownership();
    }
    catch(const PyErrOccurred&) {
        return nullptr;
    }
}

static int
green_setcontext(BorrowedGreenlet self, PyObject* nctx, void* UNUSED(context))
{
    try {
        self->context(nctx);
        return 0;
    }
    catch(const PyErrOccurred&) {
        return -1;
    }
}


static PyObject*
green_getframe(BorrowedGreenlet self, void* UNUSED(context))
{
    const PythonState::OwnedFrame& top_frame = self->top_frame();
    return top_frame.acquire_or_None();
}


static PyObject*
green_getstate(PyGreenlet* self)
{
    PyErr_Format(PyExc_TypeError,
                 "cannot serialize '%s' object",
                 Py_TYPE(self)->tp_name);
    return nullptr;
}

static PyObject*
green_repr(BorrowedGreenlet self)
{
    /*
      Return a string like
      <greenlet.greenlet at 0xdeadbeef [current][active started]|dead main>

      The handling of greenlets across threads is not super good.
      We mostly use the internal definitions of these terms, but they
      generally should make sense to users as well.
     */
    PyObject* result;
    int never_started = !self->started() && !self->active();

    const char* const tp_name = Py_TYPE(self)->tp_name;

    if (_green_not_dead(self)) {
        /* XXX: The otid= is almost useless because you can't correlate it to
         any thread identifier exposed to Python. We could use
         PyThreadState_GET()->thread_id, but we'd need to save that in the
         greenlet, or save the whole PyThreadState object itself.

         As it stands, its only useful for identifying greenlets from the same thread.
        */
        const char* state_in_thread;
        if (self->was_running_in_dead_thread()) {
            // The thread it was running in is dead!
            // This can happen, especially at interpreter shut down.
            // It complicates debugging output because it may be
            // impossible to access the current thread state at that
            // time. Thus, don't access the current thread state.
            state_in_thread = " (thread exited)";
        }
        else {
            state_in_thread = GET_THREAD_STATE().state().is_current(self)
                ? " current"
                : (self->started() ? " suspended" : "");
        }
        result = PyUnicode_FromFormat(
            "<%s object at %p (otid=%p)%s%s%s%s>",
            tp_name,
            self.borrow_o(),
            self->thread_state(),
            state_in_thread,
            self->active() ? " active" : "",
            never_started ? " pending" : " started",
            self->main() ? " main" : ""
        );
    }
    else {
        result = PyUnicode_FromFormat(
            "<%s object at %p (otid=%p) %sdead>",
            tp_name,
            self.borrow_o(),
            self->thread_state(),
            self->was_running_in_dead_thread()
            ? "(thread exited) "
            : ""
            );
    }

    return result;
}

/*****************************************************************************
 * C interface
 *
 * These are exported using the CObject API
 */
extern "C" {
static PyGreenlet*
PyGreenlet_GetCurrent(void)
{
    return GET_THREAD_STATE().state().get_current().relinquish_ownership();
}

static int
PyGreenlet_SetParent(PyGreenlet* g, PyGreenlet* nparent)
{
    return green_setparent((PyGreenlet*)g, (PyObject*)nparent, NULL);
}

static PyGreenlet*
PyGreenlet_New(PyObject* run, PyGreenlet* parent)
{
    using greenlet::refs::NewDictReference;
    // In the past, we didn't use green_new and green_init, but that
    // was a maintenance issue because we duplicated code. This way is
    // much safer, but slightly slower. If that's a problem, we could
    // refactor green_init to separate argument parsing from initialization.
    OwnedGreenlet g = OwnedGreenlet::consuming(green_new(&PyGreenlet_Type, nullptr, nullptr));
    if (!g) {
        return NULL;
    }

    try {
        NewDictReference kwargs;
        if (run) {
            kwargs.SetItem(mod_globs->str_run, run);
        }
        if (parent) {
            kwargs.SetItem("parent", (PyObject*)parent);
        }

        Require(green_init(g, mod_globs->empty_tuple, kwargs));
    }
    catch (const PyErrOccurred&) {
        return nullptr;
    }

    return g.relinquish_ownership();
}

static PyObject*
PyGreenlet_Switch(PyGreenlet* self, PyObject* args, PyObject* kwargs)
{
    if (!PyGreenlet_Check(self)) {
        PyErr_BadArgument();
        return NULL;
    }

    if (args == NULL) {
        args = mod_globs->empty_tuple;
    }

    if (kwargs == NULL || !PyDict_Check(kwargs)) {
        kwargs = NULL;
    }

    return green_switch(self, args, kwargs);
}

static PyObject*
PyGreenlet_Throw(PyGreenlet* self, PyObject* typ, PyObject* val, PyObject* tb)
{
    if (!PyGreenlet_Check(self)) {
        PyErr_BadArgument();
        return nullptr;
    }
    try {
        PyErrPieces err_pieces(typ, val, tb);
        return throw_greenlet(self, err_pieces).relinquish_ownership();
    }
    catch (const PyErrOccurred&) {
        return nullptr;
    }
}

static int
Extern_PyGreenlet_MAIN(PyGreenlet* self)
{
    if (!PyGreenlet_Check(self)) {
        PyErr_BadArgument();
        return -1;
    }
    return self->pimpl->main();
}

static int
Extern_PyGreenlet_ACTIVE(PyGreenlet* self)
{
    if (!PyGreenlet_Check(self)) {
        PyErr_BadArgument();
        return -1;
    }
    return self->pimpl->active();
}

static int
Extern_PyGreenlet_STARTED(PyGreenlet* self)
{
    if (!PyGreenlet_Check(self)) {
        PyErr_BadArgument();
        return -1;
    }
    return self->pimpl->started();
}

static PyGreenlet*
Extern_PyGreenlet_GET_PARENT(PyGreenlet* self)
{
    if (!PyGreenlet_Check(self)) {
        PyErr_BadArgument();
        return NULL;
    }
    // This can return NULL even if there is no exception
    return self->pimpl->parent().acquire();
}
} // extern C.

/** End C API ****************************************************************/

static PyMethodDef green_methods[] = {
    {"switch",
     reinterpret_cast<PyCFunction>(green_switch),
     METH_VARARGS | METH_KEYWORDS,
     green_switch_doc},
    {"throw", (PyCFunction)green_throw, METH_VARARGS, green_throw_doc},
    {"__getstate__", (PyCFunction)green_getstate, METH_NOARGS, NULL},
    {NULL, NULL} /* sentinel */
};

static PyGetSetDef green_getsets[] = {
    /* name, getter, setter, doc, context pointer */
    {"__dict__", (getter)green_getdict, (setter)green_setdict, /*XXX*/ NULL},
    {"run", (getter)green_getrun, (setter)green_setrun, /*XXX*/ NULL},
    {"parent", (getter)green_getparent, (setter)green_setparent, /*XXX*/ NULL},
    {"gr_frame", (getter)green_getframe, NULL, /*XXX*/ NULL},
    {"gr_context",
     (getter)green_getcontext,
     (setter)green_setcontext,
     /*XXX*/ NULL},
    {"dead", (getter)green_getdead, NULL, /*XXX*/ NULL},
    {"_stack_saved", (getter)green_get_stack_saved, NULL, /*XXX*/ NULL},
    {NULL}
};

static PyMemberDef green_members[] = {
    {NULL}
};

static PyNumberMethods green_as_number = {
    NULL, /* nb_add */
    NULL, /* nb_subtract */
    NULL, /* nb_multiply */
    NULL,                /* nb_remainder */
    NULL,                /* nb_divmod */
    NULL,                /* nb_power */
    NULL,                /* nb_negative */
    NULL,                /* nb_positive */
    NULL,                /* nb_absolute */
    (inquiry)green_bool, /* nb_bool */
};


PyTypeObject PyGreenlet_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "greenlet.greenlet", /* tp_name */
    sizeof(PyGreenlet),  /* tp_basicsize */
    0,                   /* tp_itemsize */
    /* methods */
    (destructor)green_dealloc, /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_compare */
    (reprfunc)green_repr,      /* tp_repr */
    &green_as_number,          /* tp_as _number*/
    0,                         /* tp_as _sequence*/
    0,                         /* tp_as _mapping*/
    0,                         /* tp_hash */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer*/
    G_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /* tp_flags */
    "greenlet(run=None, parent=None) -> greenlet\n\n"
    "Creates a new greenlet object (without running it).\n\n"
    " - *run* -- The callable to invoke.\n"
    " - *parent* -- The parent greenlet. The default is the current "
    "greenlet.",                        /* tp_doc */
    (traverseproc)green_traverse, /* tp_traverse */
    (inquiry)green_clear,         /* tp_clear */
    0,                                  /* tp_richcompare */
    offsetof(PyGreenlet, weakreflist),  /* tp_weaklistoffset */
    0,                                  /* tp_iter */
    0,                                  /* tp_iternext */
    green_methods,                      /* tp_methods */
    green_members,                      /* tp_members */
    green_getsets,                      /* tp_getset */
    0,                                  /* tp_base */
    0,                                  /* tp_dict */
    0,                                  /* tp_descr_get */
    0,                                  /* tp_descr_set */
    offsetof(PyGreenlet, dict),         /* tp_dictoffset */
    (initproc)green_init,               /* tp_init */
    PyType_GenericAlloc,                  /* tp_alloc */
    (newfunc)green_new,                          /* tp_new */
    PyObject_GC_Del,                   /* tp_free */
    (inquiry)green_is_gc,         /* tp_is_gc */
};



static PyObject*
green_unswitchable_getforce(PyGreenlet* self, void* UNUSED(context))
{
    BrokenGreenlet* broken = dynamic_cast<BrokenGreenlet*>(self->pimpl);
    return PyBool_FromLong(broken->_force_switch_error);
}

static int
green_unswitchable_setforce(PyGreenlet* self, BorrowedObject nforce, void* UNUSED(context))
{
    if (!nforce) {
        PyErr_SetString(
            PyExc_AttributeError,
            "Cannot delete force_switch_error"
        );
        return -1;
    }
    BrokenGreenlet* broken = dynamic_cast<BrokenGreenlet*>(self->pimpl);
    int is_true = PyObject_IsTrue(nforce);
    if (is_true == -1) {
        return -1;
    }
    broken->_force_switch_error = is_true;
    return 0;
}

static PyObject*
green_unswitchable_getforceslp(PyGreenlet* self, void* UNUSED(context))
{
    BrokenGreenlet* broken = dynamic_cast<BrokenGreenlet*>(self->pimpl);
    return PyBool_FromLong(broken->_force_slp_switch_error);
}

static int
green_unswitchable_setforceslp(PyGreenlet* self, BorrowedObject nforce, void* UNUSED(context))
{
    if (!nforce) {
        PyErr_SetString(
            PyExc_AttributeError,
            "Cannot delete force_slp_switch_error"
        );
        return -1;
    }
    BrokenGreenlet* broken = dynamic_cast<BrokenGreenlet*>(self->pimpl);
    int is_true = PyObject_IsTrue(nforce);
    if (is_true == -1) {
        return -1;
    }
    broken->_force_slp_switch_error = is_true;
    return 0;
}

static PyGetSetDef green_unswitchable_getsets[] = {
    /* name, getter, setter, doc, context pointer */
    {"force_switch_error",
     (getter)green_unswitchable_getforce,
     (setter)green_unswitchable_setforce,
     /*XXX*/ NULL},
    {"force_slp_switch_error",
     (getter)green_unswitchable_getforceslp,
     (setter)green_unswitchable_setforceslp,
     /*XXX*/ NULL},

    {NULL}
};

PyTypeObject PyGreenletUnswitchable_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "greenlet._greenlet.UnswitchableGreenlet",
    0,  /* tp_basicsize */
    0,                   /* tp_itemsize */
    /* methods */
    (destructor)green_dealloc, /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_compare */
    0,      /* tp_repr */
    0,          /* tp_as _number*/
    0,                         /* tp_as _sequence*/
    0,                         /* tp_as _mapping*/
    0,                         /* tp_hash */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer*/
    G_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /* tp_flags */
    "Undocumented internal class",                        /* tp_doc */
    (traverseproc)green_traverse, /* tp_traverse */
    (inquiry)green_clear,         /* tp_clear */
    0,                                  /* tp_richcompare */
    0,  /* tp_weaklistoffset */
    0,                                  /* tp_iter */
    0,                                  /* tp_iternext */
    0,                      /* tp_methods */
    0,                      /* tp_members */
    green_unswitchable_getsets,                      /* tp_getset */
    &PyGreenlet_Type,                                  /* tp_base */
    0,                                  /* tp_dict */
    0,                                  /* tp_descr_get */
    0,                                  /* tp_descr_set */
    0,         /* tp_dictoffset */
    (initproc)green_init,               /* tp_init */
    PyType_GenericAlloc,                  /* tp_alloc */
    (newfunc)green_unswitchable_new,                          /* tp_new */
    PyObject_GC_Del,                   /* tp_free */
    (inquiry)green_is_gc,         /* tp_is_gc */
};


PyDoc_STRVAR(mod_getcurrent_doc,
             "getcurrent() -> greenlet\n"
             "\n"
             "Returns the current greenlet (i.e. the one which called this "
             "function).\n");

static PyObject*
mod_getcurrent(PyObject* UNUSED(module))
{
    return GET_THREAD_STATE().state().get_current().relinquish_ownership_o();
}

PyDoc_STRVAR(mod_settrace_doc,
             "settrace(callback) -> object\n"
             "\n"
             "Sets a new tracing function and returns the previous one.\n");
static PyObject*
mod_settrace(PyObject* UNUSED(module), PyObject* args)
{
    PyArgParseParam tracefunc;
    if (!PyArg_ParseTuple(args, "O", &tracefunc)) {
        return NULL;
    }
    ThreadState& state = GET_THREAD_STATE();
    OwnedObject previous = state.get_tracefunc();
    if (!previous) {
        previous = Py_None;
    }

    state.set_tracefunc(tracefunc);

    return previous.relinquish_ownership();
}

PyDoc_STRVAR(mod_gettrace_doc,
             "gettrace() -> object\n"
             "\n"
             "Returns the currently set tracing function, or None.\n");

static PyObject*
mod_gettrace(PyObject* UNUSED(module))
{
    OwnedObject tracefunc = GET_THREAD_STATE().state().get_tracefunc();
    if (!tracefunc) {
        tracefunc = Py_None;
    }
    return tracefunc.relinquish_ownership();
}

PyDoc_STRVAR(mod_set_thread_local_doc,
             "set_thread_local(key, value) -> None\n"
             "\n"
             "Set a value in the current thread-local dictionary. Debbuging only.\n");

static PyObject*
mod_set_thread_local(PyObject* UNUSED(module), PyObject* args)
{
    PyArgParseParam key;
    PyArgParseParam value;
    PyObject* result = NULL;

    if (PyArg_UnpackTuple(args, "set_thread_local", 2, 2, &key, &value)) {
        if(PyDict_SetItem(
                          PyThreadState_GetDict(), // borrow
                          key,
                          value) == 0 ) {
            // success
            Py_INCREF(Py_None);
            result = Py_None;
        }
    }
    return result;
}

PyDoc_STRVAR(mod_get_pending_cleanup_count_doc,
             "get_pending_cleanup_count() -> Integer\n"
             "\n"
             "Get the number of greenlet cleanup operations pending. Testing only.\n");


static PyObject*
mod_get_pending_cleanup_count(PyObject* UNUSED(module))
{
    LockGuard cleanup_lock(*mod_globs->thread_states_to_destroy_lock);
    return PyLong_FromSize_t(mod_globs->thread_states_to_destroy.size());
}

PyDoc_STRVAR(mod_get_total_main_greenlets_doc,
             "get_total_main_greenlets() -> Integer\n"
             "\n"
             "Quickly return the number of main greenlets that exist. Testing only.\n");

static PyObject*
mod_get_total_main_greenlets(PyObject* UNUSED(module))
{
    return PyLong_FromSize_t(G_TOTAL_MAIN_GREENLETS);
}

PyDoc_STRVAR(mod_get_clocks_used_doing_optional_cleanup_doc,
             "get_clocks_used_doing_optional_cleanup() -> Integer\n"
             "\n"
             "Get the number of clock ticks the program has used doing optional "
             "greenlet cleanup.\n"
             "Beginning in greenlet 2.0, greenlet tries to find and dispose of greenlets\n"
             "that leaked after a thread exited. This requires invoking Python's garbage collector,\n"
             "which may have a performance cost proportional to the number of live objects.\n"
             "This function returns the amount of processor time\n"
             "greenlet has used to do this. In programs that run with very large amounts of live\n"
             "objects, this metric can be used to decide whether the cost of doing this cleanup\n"
             "is worth the memory leak being corrected. If not, you can disable the cleanup\n"
             "using ``enable_optional_cleanup(False)``.\n"
             "The units are arbitrary and can only be compared to themselves (similarly to ``time.clock()``);\n"
             "for example, to see how it scales with your heap. You can attempt to convert them into seconds\n"
             "by dividing by the value of CLOCKS_PER_SEC."
             "If cleanup has been disabled, returns None."
             "\n"
             "This is an implementation specific, provisional API. It may be changed or removed\n"
             "in the future.\n"
             ".. versionadded:: 2.0"
             );
static PyObject*
mod_get_clocks_used_doing_optional_cleanup(PyObject* UNUSED(module))
{
    std::clock_t& clocks = ThreadState::clocks_used_doing_gc();

    if (clocks == std::clock_t(-1)) {
        Py_RETURN_NONE;
    }
    // This might not actually work on some implementations; clock_t
    // is an opaque type.
    return PyLong_FromSsize_t(clocks);
}

PyDoc_STRVAR(mod_enable_optional_cleanup_doc,
             "mod_enable_optional_cleanup(bool) -> None\n"
             "\n"
             "Enable or disable optional cleanup operations.\n"
             "See ``get_clocks_used_doing_optional_cleanup()`` for details.\n"
             );
static PyObject*
mod_enable_optional_cleanup(PyObject* UNUSED(module), PyObject* flag)
{
    int is_true = PyObject_IsTrue(flag);
    if (is_true == -1) {
        return nullptr;
    }

    std::clock_t& clocks = ThreadState::clocks_used_doing_gc();
    if (is_true) {
        // If we already have a value, we don't want to lose it.
        if (clocks == std::clock_t(-1)) {
            clocks = 0;
        }
    }
    else {
        clocks = std::clock_t(-1);
    }
    Py_RETURN_NONE;
}

PyDoc_STRVAR(mod_get_tstate_trash_delete_nesting_doc,
             "get_tstate_trash_delete_nesting() -> Integer\n"
             "\n"
             "Return the 'trash can' nesting level. Testing only.\n");
static PyObject*
mod_get_tstate_trash_delete_nesting(PyObject* UNUSED(module))
{
    PyThreadState* tstate = PyThreadState_GET();

#if GREENLET_PY312
    return PyLong_FromLong(tstate->trash.delete_nesting);
#else
    return PyLong_FromLong(tstate->trash_delete_nesting);
#endif
}

static PyMethodDef GreenMethods[] = {
    {"getcurrent",
     (PyCFunction)mod_getcurrent,
     METH_NOARGS,
     mod_getcurrent_doc},
    {"settrace", (PyCFunction)mod_settrace, METH_VARARGS, mod_settrace_doc},
    {"gettrace", (PyCFunction)mod_gettrace, METH_NOARGS, mod_gettrace_doc},
    {"set_thread_local", (PyCFunction)mod_set_thread_local, METH_VARARGS, mod_set_thread_local_doc},
    {"get_pending_cleanup_count", (PyCFunction)mod_get_pending_cleanup_count, METH_NOARGS, mod_get_pending_cleanup_count_doc},
    {"get_total_main_greenlets", (PyCFunction)mod_get_total_main_greenlets, METH_NOARGS, mod_get_total_main_greenlets_doc},
    {"get_clocks_used_doing_optional_cleanup", (PyCFunction)mod_get_clocks_used_doing_optional_cleanup, METH_NOARGS, mod_get_clocks_used_doing_optional_cleanup_doc},
    {"enable_optional_cleanup", (PyCFunction)mod_enable_optional_cleanup, METH_O, mod_enable_optional_cleanup_doc},
    {"get_tstate_trash_delete_nesting", (PyCFunction)mod_get_tstate_trash_delete_nesting, METH_NOARGS, mod_get_tstate_trash_delete_nesting_doc},
    {NULL, NULL} /* Sentinel */
};

static const char* const copy_on_greentype[] = {
    "getcurrent",
    "error",
    "GreenletExit",
    "settrace",
    "gettrace",
    NULL
};

static struct PyModuleDef greenlet_module_def = {
    PyModuleDef_HEAD_INIT,
    "greenlet._greenlet",
    NULL,
    -1,
    GreenMethods,
};



static PyObject*
greenlet_internal_mod_init() noexcept
{
    static void* _PyGreenlet_API[PyGreenlet_API_pointers];

    try {
        CreatedModule m(greenlet_module_def);

        Require(PyType_Ready(&PyGreenlet_Type));
        Require(PyType_Ready(&PyGreenletUnswitchable_Type));

        mod_globs = new greenlet::GreenletGlobals;
        ThreadState::init();

        m.PyAddObject("greenlet", PyGreenlet_Type);
        m.PyAddObject("UnswitchableGreenlet", PyGreenletUnswitchable_Type);
        m.PyAddObject("error", mod_globs->PyExc_GreenletError);
        m.PyAddObject("GreenletExit", mod_globs->PyExc_GreenletExit);

        m.PyAddObject("GREENLET_USE_GC", 1);
        m.PyAddObject("GREENLET_USE_TRACING", 1);
        m.PyAddObject("GREENLET_USE_CONTEXT_VARS", 1L);
        m.PyAddObject("GREENLET_USE_STANDARD_THREADING", 1L);

        OwnedObject clocks_per_sec = OwnedObject::consuming(PyLong_FromSsize_t(CLOCKS_PER_SEC));
        m.PyAddObject("CLOCKS_PER_SEC", clocks_per_sec);

        /* also publish module-level data as attributes of the greentype. */
        // XXX: This is weird, and enables a strange pattern of
        // confusing the class greenlet with the module greenlet; with
        // the exception of (possibly) ``getcurrent()``, this
        // shouldn't be encouraged so don't add new items here.
        for (const char* const* p = copy_on_greentype; *p; p++) {
            OwnedObject o = m.PyRequireAttr(*p);
            PyDict_SetItemString(PyGreenlet_Type.tp_dict, *p, o.borrow());
        }

        /*
         * Expose C API
         */

        /* types */
        _PyGreenlet_API[PyGreenlet_Type_NUM] = (void*)&PyGreenlet_Type;

        /* exceptions */
        _PyGreenlet_API[PyExc_GreenletError_NUM] = (void*)mod_globs->PyExc_GreenletError;
        _PyGreenlet_API[PyExc_GreenletExit_NUM] = (void*)mod_globs->PyExc_GreenletExit;

        /* methods */
        _PyGreenlet_API[PyGreenlet_New_NUM] = (void*)PyGreenlet_New;
        _PyGreenlet_API[PyGreenlet_GetCurrent_NUM] = (void*)PyGreenlet_GetCurrent;
        _PyGreenlet_API[PyGreenlet_Throw_NUM] = (void*)PyGreenlet_Throw;
        _PyGreenlet_API[PyGreenlet_Switch_NUM] = (void*)PyGreenlet_Switch;
        _PyGreenlet_API[PyGreenlet_SetParent_NUM] = (void*)PyGreenlet_SetParent;

        /* Previously macros, but now need to be functions externally. */
        _PyGreenlet_API[PyGreenlet_MAIN_NUM] = (void*)Extern_PyGreenlet_MAIN;
        _PyGreenlet_API[PyGreenlet_STARTED_NUM] = (void*)Extern_PyGreenlet_STARTED;
        _PyGreenlet_API[PyGreenlet_ACTIVE_NUM] = (void*)Extern_PyGreenlet_ACTIVE;
        _PyGreenlet_API[PyGreenlet_GET_PARENT_NUM] = (void*)Extern_PyGreenlet_GET_PARENT;

        /* XXX: Note that our module name is ``greenlet._greenlet``, but for
           backwards compatibility with existing C code, we need the _C_API to
           be directly in greenlet.
        */
        const NewReference c_api_object(Require(
                                           PyCapsule_New(
                                               (void*)_PyGreenlet_API,
                                               "greenlet._C_API",
                                               NULL)));
        m.PyAddObject("_C_API", c_api_object);
        assert(c_api_object.REFCNT() == 2);

        // cerr << "Sizes:"
        //      << "\n\tGreenlet       : " << sizeof(Greenlet)
        //      << "\n\tUserGreenlet   : " << sizeof(UserGreenlet)
        //      << "\n\tMainGreenlet   : " << sizeof(MainGreenlet)
        //      << "\n\tExceptionState : " << sizeof(greenlet::ExceptionState)
        //      << "\n\tPythonState    : " << sizeof(greenlet::PythonState)
        //      << "\n\tStackState     : " << sizeof(greenlet::StackState)
        //      << "\n\tSwitchingArgs  : " << sizeof(greenlet::SwitchingArgs)
        //      << "\n\tOwnedObject    : " << sizeof(greenlet::refs::OwnedObject)
        //      << "\n\tBorrowedObject : " << sizeof(greenlet::refs::BorrowedObject)
        //      << "\n\tPyGreenlet     : " << sizeof(PyGreenlet)
        //      << endl;

        return m.borrow(); // But really it's the main reference.
    }
    catch (const LockInitError& e) {
        PyErr_SetString(PyExc_MemoryError, e.what());
        return NULL;
    }
    catch (const PyErrOccurred&) {
        return NULL;
    }

}

extern "C" {

PyMODINIT_FUNC
PyInit__greenlet(void)
{
    return greenlet_internal_mod_init();
}

}; // extern C

#ifdef __clang__
#    pragma clang diagnostic pop
#elif defined(__GNUC__)
#    pragma GCC diagnostic pop
#endif


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# TBrokenGreenlet.cpp


```cpp

/* -*- indent-tabs-mode: nil; tab-width: 4; -*- */
/**
 * Implementation of greenlet::UserGreenlet.
 *
 * Format with:
 *  clang-format -i --style=file src/greenlet/greenlet.c
 *
 *
 * Fix missing braces with:
 *   clang-tidy src/greenlet/greenlet.c -fix -checks="readability-braces-around-statements"
*/

#include "greenlet_greenlet.hpp"

namespace greenlet {

void* BrokenGreenlet::operator new(size_t UNUSED(count))
{
    return allocator.allocate(1);
}


void BrokenGreenlet::operator delete(void* ptr)
{
    return allocator.deallocate(static_cast<BrokenGreenlet*>(ptr),
                                1);
}

greenlet::PythonAllocator<greenlet::BrokenGreenlet> greenlet::BrokenGreenlet::allocator;

bool
BrokenGreenlet::force_slp_switch_error() const noexcept
{
    return this->_force_slp_switch_error;
}

UserGreenlet::switchstack_result_t BrokenGreenlet::g_switchstack(void)
{
  if (this->_force_switch_error) {
    return switchstack_result_t(-1);
  }
  return UserGreenlet::g_switchstack();
}

}; //namespace greenlet


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# TExceptionState.cpp


```cpp

#ifndef GREENLET_EXCEPTION_STATE_CPP
#define GREENLET_EXCEPTION_STATE_CPP

#include <Python.h>
#include "greenlet_greenlet.hpp"

namespace greenlet {


ExceptionState::ExceptionState()
{
    this->clear();
}

void ExceptionState::operator<<(const PyThreadState *const tstate) noexcept
{
    this->exc_info = tstate->exc_info;
    this->exc_state = tstate->exc_state;
}

void ExceptionState::operator>>(PyThreadState *const tstate) noexcept
{
    tstate->exc_state = this->exc_state;
    tstate->exc_info =
        this->exc_info ? this->exc_info : &tstate->exc_state;
    this->clear();
}

void ExceptionState::clear() noexcept
{
    this->exc_info = nullptr;
    this->exc_state.exc_value = nullptr;
#if !GREENLET_PY311
    this->exc_state.exc_type = nullptr;
    this->exc_state.exc_traceback = nullptr;
#endif
    this->exc_state.previous_item = nullptr;
}

int ExceptionState::tp_traverse(visitproc visit, void* arg) noexcept
{
    Py_VISIT(this->exc_state.exc_value);
#if !GREENLET_PY311
    Py_VISIT(this->exc_state.exc_type);
    Py_VISIT(this->exc_state.exc_traceback);
#endif
    return 0;
}

void ExceptionState::tp_clear() noexcept
{
    Py_CLEAR(this->exc_state.exc_value);
#if !GREENLET_PY311
    Py_CLEAR(this->exc_state.exc_type);
    Py_CLEAR(this->exc_state.exc_traceback);
#endif
}


}; // namespace greenlet

#endif // GREENLET_EXCEPTION_STATE_CPP


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# TGreenlet.cpp


```cpp

/* -*- indent-tabs-mode: nil; tab-width: 4; -*- */
/**
 * Implementation of greenlet::Greenlet.
 *
 * Format with:
 *  clang-format -i --style=file src/greenlet/greenlet.c
 *
 *
 * Fix missing braces with:
 *   clang-tidy src/greenlet/greenlet.c -fix -checks="readability-braces-around-statements"
*/

#include "greenlet_internal.hpp"
#include "greenlet_greenlet.hpp"
#include "greenlet_thread_state.hpp"

#include "TGreenletGlobals.cpp"
#include "TThreadStateDestroy.cpp"

namespace greenlet {

Greenlet::Greenlet(PyGreenlet* p)
{
    p ->pimpl = this;
}

Greenlet::~Greenlet()
{
    // XXX: Can't do this. tp_clear is a virtual function, and by the
    // time we're here, we've sliced off our child classes.
    //this->tp_clear();
}

Greenlet::Greenlet(PyGreenlet* p, const StackState& initial_stack)
    : stack_state(initial_stack)
{
    // can't use a delegating constructor because of
    // MSVC for Python 2.7
    p->pimpl = this;
}

bool
Greenlet::force_slp_switch_error() const noexcept
{
    return false;
}

void
Greenlet::release_args()
{
    this->switch_args.CLEAR();
}

/**
 * CAUTION: This will allocate memory and may trigger garbage
 * collection and arbitrary Python code.
 */
OwnedObject
Greenlet::throw_GreenletExit_during_dealloc(const ThreadState& UNUSED(current_thread_state))
{
    // If we're killed because we lost all references in the
    // middle of a switch, that's ok. Don't reset the args/kwargs,
    // we still want to pass them to the parent.
    PyErr_SetString(mod_globs->PyExc_GreenletExit,
                    "Killing the greenlet because all references have vanished.");
    // To get here it had to have run before
    return this->g_switch();
}

inline void
Greenlet::slp_restore_state() noexcept
{
#ifdef SLP_BEFORE_RESTORE_STATE
    SLP_BEFORE_RESTORE_STATE();
#endif
    this->stack_state.copy_heap_to_stack(
           this->thread_state()->borrow_current()->stack_state);
}


inline int
Greenlet::slp_save_state(char *const stackref) noexcept
{
    // XXX: This used to happen in the middle, before saving, but
    // after finding the next owner. Does that matter? This is
    // only defined for Sparc/GCC where it flushes register
    // windows to the stack (I think)
#ifdef SLP_BEFORE_SAVE_STATE
    SLP_BEFORE_SAVE_STATE();
#endif
    return this->stack_state.copy_stack_to_heap(stackref,
                                                this->thread_state()->borrow_current()->stack_state);
}

/**
 * CAUTION: This will allocate memory and may trigger garbage
 * collection and arbitrary Python code.
 */
OwnedObject
Greenlet::on_switchstack_or_initialstub_failure(
    Greenlet* target,
    const Greenlet::switchstack_result_t& err,
    const bool target_was_me,
    const bool was_initial_stub)
{
    // If we get here, either g_initialstub()
    // failed, or g_switchstack() failed. Either one of those
    // cases SHOULD leave us in the original greenlet with a valid stack.
    if (!PyErr_Occurred()) {
        PyErr_SetString(
            PyExc_SystemError,
            was_initial_stub
            ? "Failed to switch stacks into a greenlet for the first time."
            : "Failed to switch stacks into a running greenlet.");
    }
    this->release_args();

    if (target && !target_was_me) {
        target->murder_in_place();
    }

    assert(!err.the_new_current_greenlet);
    assert(!err.origin_greenlet);
    return OwnedObject();

}

OwnedGreenlet
Greenlet::g_switchstack_success() noexcept
{
    PyThreadState* tstate = PyThreadState_GET();
    // restore the saved state
    this->python_state >> tstate;
    this->exception_state >> tstate;

    // The thread state hasn't been changed yet.
    ThreadState* thread_state = this->thread_state();
    OwnedGreenlet result(thread_state->get_current());
    thread_state->set_current(this->self());
    //assert(thread_state->borrow_current().borrow() == this->_self);
    return result;
}

Greenlet::switchstack_result_t
Greenlet::g_switchstack(void)
{
    // if any of these assertions fail, it's likely because we
    // switched away and tried to switch back to us. Early stages of
    // switching are not reentrant because we re-use ``this->args()``.
    // Switching away would happen if we trigger a garbage collection
    // (by just using some Python APIs that happen to allocate Python
    // objects) and some garbage had weakref callbacks or __del__ that
    // switches (people don't write code like that by hand, but with
    // gevent it's possible without realizing it)
    assert(this->args() || PyErr_Occurred());
    { /* save state */
        if (this->thread_state()->is_current(this->self())) {
            // Hmm, nothing to do.
            // TODO: Does this bypass trace events that are
            // important?
            return switchstack_result_t(0,
                                        this, this->thread_state()->borrow_current());
        }
        BorrowedGreenlet current = this->thread_state()->borrow_current();
        PyThreadState* tstate = PyThreadState_GET();

        current->python_state << tstate;
        current->exception_state << tstate;
        this->python_state.will_switch_from(tstate);
        switching_thread_state = this;
        current->expose_frames();
    }
    assert(this->args() || PyErr_Occurred());
    // If this is the first switch into a greenlet, this will
    // return twice, once with 1 in the new greenlet, once with 0
    // in the origin.
    int err;
    if (this->force_slp_switch_error()) {
        err = -1;
    }
    else {
        err = slp_switch();
    }

    if (err < 0) { /* error */
        // Tested by
        // test_greenlet.TestBrokenGreenlets.test_failed_to_slp_switch_into_running
        //
        // It's not clear if it's worth trying to clean up and
        // continue here. Failing to switch stacks is a big deal which
        // may not be recoverable (who knows what state the stack is in).
        // Also, we've stolen references in preparation for calling
        // ``g_switchstack_success()`` and we don't have a clean
        // mechanism for backing that all out.
        Py_FatalError("greenlet: Failed low-level slp_switch(). The stack is probably corrupt.");
    }

    // No stack-based variables are valid anymore.

    // But the global is volatile so we can reload it without the
    // compiler caching it from earlier.
    Greenlet* greenlet_that_switched_in = switching_thread_state; // aka this
    switching_thread_state = nullptr;
    // except that no stack variables are valid, we would:
    // assert(this == greenlet_that_switched_in);

    // switchstack success is where we restore the exception state,
    // etc. It returns the origin greenlet because its convenient.

    OwnedGreenlet origin = greenlet_that_switched_in->g_switchstack_success();
    assert(greenlet_that_switched_in->args() || PyErr_Occurred());
    return switchstack_result_t(err, greenlet_that_switched_in, origin);
}


inline void
Greenlet::check_switch_allowed() const
{
    // TODO: Make this take a parameter of the current greenlet,
    // or current main greenlet, to make the check for
    // cross-thread switching cheaper. Surely somewhere up the
    // call stack we've already accessed the thread local variable.

    // We expect to always have a main greenlet now; accessing the thread state
    // created it. However, if we get here and cleanup has already
    // begun because we're a greenlet that was running in a
    // (now dead) thread, these invariants will not hold true. In
    // fact, accessing `this->thread_state` may not even be possible.

    // If the thread this greenlet was running in is dead,
    // we'll still have a reference to a main greenlet, but the
    // thread state pointer we have is bogus.
    // TODO: Give the objects an API to determine if they belong
    // to a dead thread.

    const BorrowedMainGreenlet main_greenlet = this->find_main_greenlet_in_lineage();

    if (!main_greenlet) {
        throw PyErrOccurred(mod_globs->PyExc_GreenletError,
                            "cannot switch to a garbage collected greenlet");
    }

    if (!main_greenlet->thread_state()) {
        throw PyErrOccurred(mod_globs->PyExc_GreenletError,
                            "cannot switch to a different thread (which happens to have exited)");
    }

    // The main greenlet we found was from the .parent lineage.
    // That may or may not have any relationship to the main
    // greenlet of the running thread. We can't actually access
    // our this->thread_state members to try to check that,
    // because it could be in the process of getting destroyed,
    // but setting the main_greenlet->thread_state member to NULL
    // may not be visible yet. So we need to check against the
    // current thread state (once the cheaper checks are out of
    // the way)
    const BorrowedMainGreenlet current_main_greenlet = GET_THREAD_STATE().state().borrow_main_greenlet();
    if (
        // lineage main greenlet is not this thread's greenlet
        current_main_greenlet != main_greenlet
        || (
            // atteched to some thread
            this->main_greenlet()
            // XXX: Same condition as above. Was this supposed to be
            // this->main_greenlet()?
            && current_main_greenlet != main_greenlet)
        // switching into a known dead thread (XXX: which, if we get here,
        // is bad, because we just accessed the thread state, which is
        // gone!)
        || (!current_main_greenlet->thread_state())) {
        // CAUTION: This may trigger memory allocations, gc, and
        // arbitrary Python code.
        throw PyErrOccurred(mod_globs->PyExc_GreenletError,
                            "cannot switch to a different thread");
    }
}

const OwnedObject
Greenlet::context() const
{
    using greenlet::PythonStateContext;
    OwnedObject result;

    if (this->is_currently_running_in_some_thread()) {
        /* Currently running greenlet: context is stored in the thread state,
           not the greenlet object. */
        if (GET_THREAD_STATE().state().is_current(this->self())) {
            result = PythonStateContext::context(PyThreadState_GET());
        }
        else {
            throw ValueError(
                            "cannot get context of a "
                            "greenlet that is running in a different thread");
        }
    }
    else {
        /* Greenlet is not running: just return context. */
        result = this->python_state.context();
    }
    if (!result) {
        result = OwnedObject::None();
    }
    return result;
}


void
Greenlet::context(BorrowedObject given)
{
    using greenlet::PythonStateContext;
    if (!given) {
        throw AttributeError("can't delete context attribute");
    }
    if (given.is_None()) {
        /* "Empty context" is stored as NULL, not None. */
        given = nullptr;
    }

    //checks type, incrs refcnt
    greenlet::refs::OwnedContext context(given);
    PyThreadState* tstate = PyThreadState_GET();

    if (this->is_currently_running_in_some_thread()) {
        if (!GET_THREAD_STATE().state().is_current(this->self())) {
            throw ValueError("cannot set context of a greenlet"
                             " that is running in a different thread");
        }

        /* Currently running greenlet: context is stored in the thread state,
           not the greenlet object. */
        OwnedObject octx = OwnedObject::consuming(PythonStateContext::context(tstate));
        PythonStateContext::context(tstate, context.relinquish_ownership());
    }
    else {
        /* Greenlet is not running: just set context. Note that the
           greenlet may be dead.*/
        this->python_state.context() = context;
    }
}

/**
 * CAUTION: May invoke arbitrary Python code.
 *
 * Figure out what the result of ``greenlet.switch(arg, kwargs)``
 * should be and transfers ownership of it to the left-hand-side.
 *
 * If switch() was just passed an arg tuple, then we'll just return that.
 * If only keyword arguments were passed, then we'll pass the keyword
 * argument dict. Otherwise, we'll create a tuple of (args, kwargs) and
 * return both.
 *
 * CAUTION: This may allocate a new tuple object, which may
 * cause the Python garbage collector to run, which in turn may
 * run arbitrary Python code that switches.
 */
OwnedObject& operator<<=(OwnedObject& lhs, greenlet::SwitchingArgs& rhs) noexcept
{
    // Because this may invoke arbitrary Python code, which could
    // result in switching back to us, we need to get the
    // arguments locally on the stack.
    assert(rhs);
    OwnedObject args = rhs.args();
    OwnedObject kwargs = rhs.kwargs();
    rhs.CLEAR();
    // We shouldn't be called twice for the same switch.
    assert(args || kwargs);
    assert(!rhs);

    if (!kwargs) {
        lhs = args;
    }
    else if (!PyDict_Size(kwargs.borrow())) {
        lhs = args;
    }
    else if (!PySequence_Length(args.borrow())) {
        lhs = kwargs;
    }
    else {
        // PyTuple_Pack allocates memory, may GC, may run arbitrary
        // Python code.
        lhs = OwnedObject::consuming(PyTuple_Pack(2, args.borrow(), kwargs.borrow()));
    }
    return lhs;
}

static OwnedObject
g_handle_exit(const OwnedObject& greenlet_result)
{
    if (!greenlet_result && mod_globs->PyExc_GreenletExit.PyExceptionMatches()) {
        /* catch and ignore GreenletExit */
        PyErrFetchParam val;
        PyErr_Fetch(PyErrFetchParam(), val, PyErrFetchParam());
        if (!val) {
            return OwnedObject::None();
        }
        return OwnedObject(val);
    }

    if (greenlet_result) {
        // package the result into a 1-tuple
        // PyTuple_Pack increments the reference of its arguments,
        // so we always need to decref the greenlet result;
        // the owner will do that.
        return OwnedObject::consuming(PyTuple_Pack(1, greenlet_result.borrow()));
    }

    return OwnedObject();
}



/**
 * May run arbitrary Python code.
 */
OwnedObject
Greenlet::g_switch_finish(const switchstack_result_t& err)
{
    assert(err.the_new_current_greenlet == this);

    ThreadState& state = *this->thread_state();
    // Because calling the trace function could do arbitrary things,
    // including switching away from this greenlet and then maybe
    // switching back, we need to capture the arguments now so that
    // they don't change.
    OwnedObject result;
    if (this->args()) {
        result <<= this->args();
    }
    else {
        assert(PyErr_Occurred());
    }
    assert(!this->args());
    try {
        // Our only caller handles the bad error case
        assert(err.status >= 0);
        assert(state.borrow_current() == this->self());
        if (OwnedObject tracefunc = state.get_tracefunc()) {
            assert(result || PyErr_Occurred());
            g_calltrace(tracefunc,
                        result ? mod_globs->event_switch : mod_globs->event_throw,
                        err.origin_greenlet,
                        this->self());
        }
        // The above could have invoked arbitrary Python code, but
        // it couldn't switch back to this object and *also*
        // throw an exception, so the args won't have changed.

        if (PyErr_Occurred()) {
            // We get here if we fell of the end of the run() function
            // raising an exception. The switch itself was
            // successful, but the function raised.
            // valgrind reports that memory allocated here can still
            // be reached after a test run.
            throw PyErrOccurred::from_current();
        }
        return result;
    }
    catch (const PyErrOccurred&) {
        /* Turn switch errors into switch throws */
        /* Turn trace errors into switch throws */
        this->release_args();
        throw;
    }
}

void
Greenlet::g_calltrace(const OwnedObject& tracefunc,
                      const greenlet::refs::ImmortalEventName& event,
                      const BorrowedGreenlet& origin,
                      const BorrowedGreenlet& target)
{
    PyErrPieces saved_exc;
    try {
        TracingGuard tracing_guard;
        // TODO: We have saved the active exception (if any) that's
        // about to be raised. In the 'throw' case, we could provide
        // the exception to the tracefunction, which seems very helpful.
        tracing_guard.CallTraceFunction(tracefunc, event, origin, target);
    }
    catch (const PyErrOccurred&) {
        // In case of exceptions trace function is removed,
        // and any existing exception is replaced with the tracing
        // exception.
        GET_THREAD_STATE().state().set_tracefunc(Py_None);
        throw;
    }

    saved_exc.PyErrRestore();
    assert(
        (event == mod_globs->event_throw && PyErr_Occurred())
        || (event == mod_globs->event_switch && !PyErr_Occurred())
    );
}

void
Greenlet::murder_in_place()
{
    if (this->active()) {
        assert(!this->is_currently_running_in_some_thread());
        this->deactivate_and_free();
    }
}

inline void
Greenlet::deactivate_and_free()
{
    if (!this->active()) {
        return;
    }
    // Throw away any saved stack.
    this->stack_state = StackState();
    assert(!this->stack_state.active());
    // Throw away any Python references.
    // We're holding a borrowed reference to the last
    // frame we executed. Since we borrowed it, the
    // normal traversal, clear, and dealloc functions
    // ignore it, meaning it leaks. (The thread state
    // object can't find it to clear it when that's
    // deallocated either, because by definition if we
    // got an object on this list, it wasn't
    // running and the thread state doesn't have
    // this frame.)
    // So here, we *do* clear it.
    this->python_state.tp_clear(true);
}

bool
Greenlet::belongs_to_thread(const ThreadState* thread_state) const
{
    if (!this->thread_state() // not running anywhere, or thread
                              // exited
        || !thread_state) { // same, or there is no thread state.
        return false;
    }
    return true;
}


void
Greenlet::deallocing_greenlet_in_thread(const ThreadState* current_thread_state)
{
    /* Cannot raise an exception to kill the greenlet if
       it is not running in the same thread! */
    if (this->belongs_to_thread(current_thread_state)) {
        assert(current_thread_state);
        // To get here it had to have run before
        /* Send the greenlet a GreenletExit exception. */

        // We don't care about the return value, only whether an
        // exception happened.
        this->throw_GreenletExit_during_dealloc(*current_thread_state);
        return;
    }

    // Not the same thread! Temporarily save the greenlet
    // into its thread's deleteme list, *if* it exists.
    // If that thread has already exited, and processed its pending
    // cleanup, we'll never be able to clean everything up: we won't
    // be able to raise an exception.
    // That's mostly OK! Since we can't add it to a list, our refcount
    // won't increase, and we'll go ahead with the DECREFs later.
    ThreadState *const  thread_state = this->thread_state();
    if (thread_state) {
        thread_state->delete_when_thread_running(this->self());
    }
    else {
        // The thread is dead, we can't raise an exception.
        // We need to make it look non-active, though, so that dealloc
        // finishes killing it.
        this->deactivate_and_free();
    }
    return;
}


int
Greenlet::tp_traverse(visitproc visit, void* arg)
{

    int result;
    if ((result = this->exception_state.tp_traverse(visit, arg)) != 0) {
        return result;
    }
    //XXX: This is ugly. But so is handling everything having to do
    //with the top frame.
    bool visit_top_frame = this->was_running_in_dead_thread();
    // When true, the thread is dead. Our implicit weak reference to the
    // frame is now all that's left; we consider ourselves to
    // strongly own it now.
    if ((result = this->python_state.tp_traverse(visit, arg, visit_top_frame)) != 0) {
        return result;
    }
    return 0;
}

int
Greenlet::tp_clear()
{
    bool own_top_frame = this->was_running_in_dead_thread();
    this->exception_state.tp_clear();
    this->python_state.tp_clear(own_top_frame);
    return 0;
}

bool Greenlet::is_currently_running_in_some_thread() const
{
    return this->stack_state.active() && !this->python_state.top_frame();
}

#if GREENLET_PY312
void GREENLET_NOINLINE(Greenlet::expose_frames)()
{
    if (!this->python_state.top_frame()) {
        return;
    }

    _PyInterpreterFrame* last_complete_iframe = nullptr;
    _PyInterpreterFrame* iframe = this->python_state.top_frame()->f_frame;
    while (iframe) {
        // We must make a copy before looking at the iframe contents,
        // since iframe might point to a portion of the greenlet's C stack
        // that was spilled when switching greenlets.
        _PyInterpreterFrame iframe_copy;
        this->stack_state.copy_from_stack(&iframe_copy, iframe, sizeof(*iframe));
        if (!_PyFrame_IsIncomplete(&iframe_copy)) {
            // If the iframe were OWNED_BY_CSTACK then it would always be
            // incomplete. Since it's not incomplete, it's not on the C stack
            // and we can access it through the original `iframe` pointer
            // directly.  This is important since GetFrameObject might
            // lazily _create_ the frame object and we don't want the
            // interpreter to lose track of it.
            assert(iframe_copy.owner != FRAME_OWNED_BY_CSTACK);

            // We really want to just write:
            //     PyFrameObject* frame = _PyFrame_GetFrameObject(iframe);
            // but _PyFrame_GetFrameObject calls _PyFrame_MakeAndSetFrameObject
            // which is not a visible symbol in libpython. The easiest
            // way to get a public function to call it is using
            // PyFrame_GetBack, which is defined as follows:
            //     assert(frame != NULL);
            //     assert(!_PyFrame_IsIncomplete(frame->f_frame));
            //     PyFrameObject *back = frame->f_back;
            //     if (back == NULL) {
            //         _PyInterpreterFrame *prev = frame->f_frame->previous;
            //         prev = _PyFrame_GetFirstComplete(prev);
            //         if (prev) {
            //             back = _PyFrame_GetFrameObject(prev);
            //         }
            //     }
            //     return (PyFrameObject*)Py_XNewRef(back);
            if (!iframe->frame_obj) {
                PyFrameObject dummy_frame;
                _PyInterpreterFrame dummy_iframe;
                dummy_frame.f_back = nullptr;
                dummy_frame.f_frame = &dummy_iframe;
                // force the iframe to be considered complete without
                // needing to check its code object:
                dummy_iframe.owner = FRAME_OWNED_BY_GENERATOR;
                dummy_iframe.previous = iframe;
                assert(!_PyFrame_IsIncomplete(&dummy_iframe));
                // Drop the returned reference immediately; the iframe
                // continues to hold a strong reference
                Py_XDECREF(PyFrame_GetBack(&dummy_frame));
                assert(iframe->frame_obj);
            }

            // This is a complete frame, so make the last one of those we saw
            // point at it, bypassing any incomplete frames (which may have
            // been on the C stack) in between the two. We're overwriting
            // last_complete_iframe->previous and need that to be reversible,
            // so we store the original previous ptr in the frame object
            // (which we must have created on a previous iteration through
            // this loop). The frame object has a bunch of storage that is
            // only used when its iframe is OWNED_BY_FRAME_OBJECT, which only
            // occurs when the frame object outlives the frame's execution,
            // which can't have happened yet because the frame is currently
            // executing as far as the interpreter is concerned. So, we can
            // reuse it for our own purposes.
            assert(iframe->owner == FRAME_OWNED_BY_THREAD
                   || iframe->owner == FRAME_OWNED_BY_GENERATOR);
            if (last_complete_iframe) {
                assert(last_complete_iframe->frame_obj);
                memcpy(&last_complete_iframe->frame_obj->_f_frame_data[0],
                       &last_complete_iframe->previous, sizeof(void *));
                last_complete_iframe->previous = iframe;
            }
            last_complete_iframe = iframe;
        }
        // Frames that are OWNED_BY_FRAME_OBJECT are linked via the
        // frame's f_back while all others are linked via the iframe's
        // previous ptr. Since all the frames we traverse are running
        // as far as the interpreter is concerned, we don't have to
        // worry about the OWNED_BY_FRAME_OBJECT case.
        iframe = iframe_copy.previous;
    }

    // Give the outermost complete iframe a null previous pointer to
    // account for any potential incomplete/C-stack iframes between it
    // and the actual top-of-stack
    if (last_complete_iframe) {
        assert(last_complete_iframe->frame_obj);
        memcpy(&last_complete_iframe->frame_obj->_f_frame_data[0],
               &last_complete_iframe->previous, sizeof(void *));
        last_complete_iframe->previous = nullptr;
    }
}
#else
void Greenlet::expose_frames()
{

}
#endif

}; // namespace greenlet


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# TGreenletGlobals.cpp


```cpp

/* -*- indent-tabs-mode: nil; tab-width: 4; -*- */
/**
 * Implementation of GreenletGlobals.
 *
 * Format with:
 *  clang-format -i --style=file src/greenlet/greenlet.c
 *
 *
 * Fix missing braces with:
 *   clang-tidy src/greenlet/greenlet.c -fix -checks="readability-braces-around-statements"
*/
#ifndef T_GREENLET_GLOBALS
#define T_GREENLET_GLOBALS

#include "greenlet_refs.hpp"
#include "greenlet_exceptions.hpp"
#include "greenlet_thread_support.hpp"
#include "greenlet_thread_state.hpp"

namespace greenlet {

// This encapsulates what were previously module global "constants"
// established at init time.
// This is a step towards Python3 style module state that allows
// reloading.
//
// In an earlier iteration of this code, we used placement new to be
// able to allocate this object statically still, so that references
// to its members don't incur an extra pointer indirection.
// But under some scenarios, that could result in crashes at
// shutdown because apparently the destructor was getting run twice?
class GreenletGlobals
{

public:
    const greenlet::refs::ImmortalEventName event_switch;
    const greenlet::refs::ImmortalEventName event_throw;
    const greenlet::refs::ImmortalException PyExc_GreenletError;
    const greenlet::refs::ImmortalException PyExc_GreenletExit;
    const greenlet::refs::ImmortalObject empty_tuple;
    const greenlet::refs::ImmortalObject empty_dict;
    const greenlet::refs::ImmortalString str_run;
    Mutex* const thread_states_to_destroy_lock;
    greenlet::cleanup_queue_t thread_states_to_destroy;

    GreenletGlobals() :
        event_switch("switch"),
        event_throw("throw"),
        PyExc_GreenletError("greenlet.error"),
        PyExc_GreenletExit("greenlet.GreenletExit", PyExc_BaseException),
        empty_tuple(Require(PyTuple_New(0))),
        empty_dict(Require(PyDict_New())),
        str_run("run"),
        thread_states_to_destroy_lock(new Mutex())
    {}

    ~GreenletGlobals()
    {
        // This object is (currently) effectively immortal, and not
        // just because of those placement new tricks; if we try to
        // deallocate the static object we allocated, and overwrote,
        // we would be doing so at C++ teardown time, which is after
        // the final Python GIL is released, and we can't use the API
        // then.
        // (The members will still be destructed, but they also don't
        // do any deallocation.)
    }

    void queue_to_destroy(ThreadState* ts) const
    {
        // we're currently accessed through a static const object,
        // implicitly marking our members as const, so code can't just
        // call push_back (or pop_back) without casting away the
        // const.
        //
        // Do that for callers.
        greenlet::cleanup_queue_t& q = const_cast<greenlet::cleanup_queue_t&>(this->thread_states_to_destroy);
        q.push_back(ts);
    }

    ThreadState* take_next_to_destroy() const
    {
        greenlet::cleanup_queue_t& q = const_cast<greenlet::cleanup_queue_t&>(this->thread_states_to_destroy);
        ThreadState* result = q.back();
        q.pop_back();
        return result;
    }
};

}; // namespace greenlet

static const greenlet::GreenletGlobals* mod_globs;

#endif // T_GREENLET_GLOBALS


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# TMainGreenlet.cpp


```cpp

/* -*- indent-tabs-mode: nil; tab-width: 4; -*- */
/**
 * Implementation of greenlet::MainGreenlet.
 *
 * Format with:
 *  clang-format -i --style=file src/greenlet/greenlet.c
 *
 *
 * Fix missing braces with:
 *   clang-tidy src/greenlet/greenlet.c -fix -checks="readability-braces-around-statements"
*/

#include "greenlet_greenlet.hpp"
#include "greenlet_thread_state.hpp"


// Protected by the GIL. Incremented when we create a main greenlet,
// in a new thread, decremented when it is destroyed.
static Py_ssize_t G_TOTAL_MAIN_GREENLETS;

namespace greenlet {
greenlet::PythonAllocator<MainGreenlet> MainGreenlet::allocator;

void* MainGreenlet::operator new(size_t UNUSED(count))
{
    return allocator.allocate(1);
}


void MainGreenlet::operator delete(void* ptr)
{
    return allocator.deallocate(static_cast<MainGreenlet*>(ptr),
                                1);
}


MainGreenlet::MainGreenlet(PyGreenlet* p, ThreadState* state)
    : Greenlet(p, StackState::make_main()),
      _self(p),
      _thread_state(state)
{
    G_TOTAL_MAIN_GREENLETS++;
}

MainGreenlet::~MainGreenlet()
{
    G_TOTAL_MAIN_GREENLETS--;
    this->tp_clear();
}

ThreadState*
MainGreenlet::thread_state() const noexcept
{
    return this->_thread_state;
}

void
MainGreenlet::thread_state(ThreadState* t) noexcept
{
    assert(!t);
    this->_thread_state = t;
}

BorrowedGreenlet
MainGreenlet::self() const noexcept
{
    return BorrowedGreenlet(this->_self.borrow());
}


const BorrowedMainGreenlet
MainGreenlet::main_greenlet() const
{
    return this->_self;
}

BorrowedMainGreenlet
MainGreenlet::find_main_greenlet_in_lineage() const
{
    return BorrowedMainGreenlet(this->_self);
}

bool
MainGreenlet::was_running_in_dead_thread() const noexcept
{
    return !this->_thread_state;
}

OwnedObject
MainGreenlet::g_switch()
{
    try {
        this->check_switch_allowed();
    }
    catch (const PyErrOccurred&) {
        this->release_args();
        throw;
    }

    switchstack_result_t err = this->g_switchstack();
    if (err.status < 0) {
        // XXX: This code path is untested, but it is shared
        // with the UserGreenlet path that is tested.
        return this->on_switchstack_or_initialstub_failure(
            this,
            err,
            true, // target was me
            false // was initial stub
        );
    }

    return err.the_new_current_greenlet->g_switch_finish(err);
}

int
MainGreenlet::tp_traverse(visitproc visit, void* arg)
{
    if (this->_thread_state) {
        // we've already traversed main, (self), don't do it again.
        int result = this->_thread_state->tp_traverse(visit, arg, false);
        if (result) {
            return result;
        }
    }
    return Greenlet::tp_traverse(visit, arg);
}

const OwnedObject&
MainGreenlet::run() const
{
    throw AttributeError("Main greenlets do not have a run attribute.");
}

void
MainGreenlet::run(const BorrowedObject UNUSED(nrun))
{
   throw AttributeError("Main greenlets do not have a run attribute.");
}

void
MainGreenlet::parent(const BorrowedObject raw_new_parent)
{
    if (!raw_new_parent) {
        throw AttributeError("can't delete attribute");
    }
    throw AttributeError("cannot set the parent of a main greenlet");
}

const OwnedGreenlet
MainGreenlet::parent() const
{
    return OwnedGreenlet(); // null becomes None
}

}; // namespace greenlet


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# TPythonState.cpp


```cpp

#ifndef GREENLET_PYTHON_STATE_CPP
#define GREENLET_PYTHON_STATE_CPP

#include <Python.h>
#include "greenlet_greenlet.hpp"

namespace greenlet {

PythonState::PythonState()
    : _top_frame()
#if GREENLET_USE_CFRAME
    ,cframe(nullptr)
    ,use_tracing(0)
#endif
#if GREENLET_PY312
    ,py_recursion_depth(0)
    ,c_recursion_depth(0)
#else
    ,recursion_depth(0)
#endif
    ,trash_delete_nesting(0)
#if GREENLET_PY311
    ,current_frame(nullptr)
    ,datastack_chunk(nullptr)
    ,datastack_top(nullptr)
    ,datastack_limit(nullptr)
#endif
{
#if GREENLET_USE_CFRAME
    /*
      The PyThreadState->cframe pointer usually points to memory on
      the stack, alloceted in a call into PyEval_EvalFrameDefault.

      Initially, before any evaluation begins, it points to the
      initial PyThreadState object's ``root_cframe`` object, which is
      statically allocated for the lifetime of the thread.

      A greenlet can last for longer than a call to
      PyEval_EvalFrameDefault, so we can't set its ``cframe`` pointer
      to be the current ``PyThreadState->cframe``; nor could we use
      one from the greenlet parent for the same reason. Yet a further
      no: we can't allocate one scoped to the greenlet and then
      destroy it when the greenlet is deallocated, because inside the
      interpreter the _PyCFrame objects form a linked list, and that too
      can result in accessing memory beyond its dynamic lifetime (if
      the greenlet doesn't actually finish before it dies, its entry
      could still be in the list).

      Using the ``root_cframe`` is problematic, though, because its
      members are never modified by the interpreter and are set to 0,
      meaning that its ``use_tracing`` flag is never updated. We don't
      want to modify that value in the ``root_cframe`` ourself: it
      *shouldn't* matter much because we should probably never get
      back to the point where that's the only cframe on the stack;
      even if it did matter, the major consequence of an incorrect
      value for ``use_tracing`` is that if its true the interpreter
      does some extra work --- however, it's just good code hygiene.

      Our solution: before a greenlet runs, after its initial
      creation, it uses the ``root_cframe`` just to have something to
      put there. However, once the greenlet is actually switched to
      for the first time, ``g_initialstub`` (which doesn't actually
      "return" while the greenlet is running) stores a new _PyCFrame on
      its local stack, and copies the appropriate values from the
      currently running _PyCFrame; this is then made the _PyCFrame for the
      newly-minted greenlet. ``g_initialstub`` then proceeds to call
      ``glet.run()``, which results in ``PyEval_...`` adding the
      _PyCFrame to the list. Switches continue as normal. Finally, when
      the greenlet finishes, the call to ``glet.run()`` returns and
      the _PyCFrame is taken out of the linked list and the stack value
      is now unused and free to expire.

      XXX: I think we can do better. If we're deallocing in the same
      thread, can't we traverse the list and unlink our frame?
      Can we just keep a reference to the thread state in case we
      dealloc in another thread? (Is that even possible if we're still
      running and haven't returned from g_initialstub?)
    */
    this->cframe = &PyThreadState_GET()->root_cframe;
#endif
}


inline void PythonState::may_switch_away() noexcept
{
#if GREENLET_PY311
    // PyThreadState_GetFrame is probably going to have to allocate a
    // new frame object. That may trigger garbage collection. Because
    // we call this during the early phases of a switch (it doesn't
    // matter to which greenlet, as this has a global effect), if a GC
    // triggers a switch away, two things can happen, both bad:
    // - We might not get switched back to, halting forward progress.
    //   this is pathological, but possible.
    // - We might get switched back to with a different set of
    //   arguments or a throw instead of a switch. That would corrupt
    //   our state (specifically, PyErr_Occurred() and this->args()
    //   would no longer agree).
    //
    // Thus, when we call this API, we need to have GC disabled.
    // This method serves as a bottleneck we call when maybe beginning
    // a switch. In this way, it is always safe -- no risk of GC -- to
    // use ``_GetFrame()`` whenever we need to, just as it was in
    // <=3.10 (because subsequent calls will be cached and not
    // allocate memory).

    GCDisabledGuard no_gc;
    Py_XDECREF(PyThreadState_GetFrame(PyThreadState_GET()));
#endif
}

void PythonState::operator<<(const PyThreadState *const tstate) noexcept
{
    this->_context.steal(tstate->context);
#if GREENLET_USE_CFRAME
    /*
      IMPORTANT: ``cframe`` is a pointer into the STACK. Thus, because
      the call to ``slp_switch()`` changes the contents of the stack,
      you cannot read from ``ts_current->cframe`` after that call and
      necessarily get the same values you get from reading it here.
      Anything you need to restore from now to then must be saved in a
      global/threadlocal variable (because we can't use stack
      variables here either). For things that need to persist across
      the switch, use `will_switch_from`.
    */
    this->cframe = tstate->cframe;
  #if !GREENLET_PY312
    this->use_tracing = tstate->cframe->use_tracing;
  #endif
#endif // GREENLET_USE_CFRAME
#if GREENLET_PY311
  #if GREENLET_PY312
    this->py_recursion_depth = tstate->py_recursion_limit - tstate->py_recursion_remaining;
    this->c_recursion_depth = C_RECURSION_LIMIT - tstate->c_recursion_remaining;
  #else // not 312
    this->recursion_depth = tstate->recursion_limit - tstate->recursion_remaining;
  #endif // GREENLET_PY312
    this->current_frame = tstate->cframe->current_frame;
    this->datastack_chunk = tstate->datastack_chunk;
    this->datastack_top = tstate->datastack_top;
    this->datastack_limit = tstate->datastack_limit;

    PyFrameObject *frame = PyThreadState_GetFrame((PyThreadState *)tstate);
    Py_XDECREF(frame);  // PyThreadState_GetFrame gives us a new
                        // reference.
    this->_top_frame.steal(frame);
  #if GREENLET_PY312
    this->trash_delete_nesting = tstate->trash.delete_nesting;
  #else // not 312
    this->trash_delete_nesting = tstate->trash_delete_nesting;
  #endif // GREENLET_PY312
#else // Not 311
    this->recursion_depth = tstate->recursion_depth;
    this->_top_frame.steal(tstate->frame);
    this->trash_delete_nesting = tstate->trash_delete_nesting;
#endif // GREENLET_PY311
}

#if GREENLET_PY312
void GREENLET_NOINLINE(PythonState::unexpose_frames)()
{
    if (!this->top_frame()) {
        return;
    }

    // See GreenletState::expose_frames() and the comment on frames_were_exposed
    // for more information about this logic.
    _PyInterpreterFrame *iframe = this->_top_frame->f_frame;
    while (iframe != nullptr) {
        _PyInterpreterFrame *prev_exposed = iframe->previous;
        assert(iframe->frame_obj);
        memcpy(&iframe->previous, &iframe->frame_obj->_f_frame_data[0],
               sizeof(void *));
        iframe = prev_exposed;
    }
}
#else
void PythonState::unexpose_frames()
{}
#endif

void PythonState::operator>>(PyThreadState *const tstate) noexcept
{
    tstate->context = this->_context.relinquish_ownership();
    /* Incrementing this value invalidates the contextvars cache,
       which would otherwise remain valid across switches */
    tstate->context_ver++;
#if GREENLET_USE_CFRAME
    tstate->cframe = this->cframe;
    /*
      If we were tracing, we need to keep tracing.
      There should never be the possibility of hitting the
      root_cframe here. See note above about why we can't
      just copy this from ``origin->cframe->use_tracing``.
    */
  #if !GREENLET_PY312
    tstate->cframe->use_tracing = this->use_tracing;
  #endif
#endif // GREENLET_USE_CFRAME
#if GREENLET_PY311
  #if GREENLET_PY312
    tstate->py_recursion_remaining = tstate->py_recursion_limit - this->py_recursion_depth;
    tstate->c_recursion_remaining = C_RECURSION_LIMIT - this->c_recursion_depth;
    this->unexpose_frames();
  #else // \/ 3.11
    tstate->recursion_remaining = tstate->recursion_limit - this->recursion_depth;
  #endif // GREENLET_PY312
    tstate->cframe->current_frame = this->current_frame;
    tstate->datastack_chunk = this->datastack_chunk;
    tstate->datastack_top = this->datastack_top;
    tstate->datastack_limit = this->datastack_limit;
    this->_top_frame.relinquish_ownership();
  #if GREENLET_PY312
    tstate->trash.delete_nesting = this->trash_delete_nesting;
  #else // not 3.12
    tstate->trash_delete_nesting = this->trash_delete_nesting;
  #endif // GREENLET_PY312
#else // not 3.11
    tstate->frame = this->_top_frame.relinquish_ownership();
    tstate->recursion_depth = this->recursion_depth;
    tstate->trash_delete_nesting = this->trash_delete_nesting;
#endif // GREENLET_PY311
}

inline void PythonState::will_switch_from(PyThreadState *const origin_tstate) noexcept
{
#if GREENLET_USE_CFRAME && !GREENLET_PY312
    // The weird thing is, we don't actually save this for an
    // effect on the current greenlet, it's saved for an
    // effect on the target greenlet. That is, we want
    // continuity of this setting across the greenlet switch.
    this->use_tracing = origin_tstate->cframe->use_tracing;
#endif
}

void PythonState::set_initial_state(const PyThreadState* const tstate) noexcept
{
    this->_top_frame = nullptr;
#if GREENLET_PY312
    this->py_recursion_depth = tstate->py_recursion_limit - tstate->py_recursion_remaining;
    // XXX: TODO: Comment from a reviewer:
    //     Should this be ``C_RECURSION_LIMIT - tstate->c_recursion_remaining``?
    // But to me it looks more like that might not be the right
    // initialization either?
    this->c_recursion_depth = tstate->py_recursion_limit - tstate->py_recursion_remaining;
#elif GREENLET_PY311
    this->recursion_depth = tstate->recursion_limit - tstate->recursion_remaining;
#else
    this->recursion_depth = tstate->recursion_depth;
#endif
}
// TODO: Better state management about when we own the top frame.
int PythonState::tp_traverse(visitproc visit, void* arg, bool own_top_frame) noexcept
{
    Py_VISIT(this->_context.borrow());
    if (own_top_frame) {
        Py_VISIT(this->_top_frame.borrow());
    }
    return 0;
}

void PythonState::tp_clear(bool own_top_frame) noexcept
{
    PythonStateContext::tp_clear();
    // If we get here owning a frame,
    // we got dealloc'd without being finished. We may or may not be
    // in the same thread.
    if (own_top_frame) {
        this->_top_frame.CLEAR();
    }
}

#if GREENLET_USE_CFRAME
void PythonState::set_new_cframe(_PyCFrame& frame) noexcept
{
    frame = *PyThreadState_GET()->cframe;
    /* Make the target greenlet refer to the stack value. */
    this->cframe = &frame;
    /*
      And restore the link to the previous frame so this one gets
      unliked appropriately.
    */
    this->cframe->previous = &PyThreadState_GET()->root_cframe;
}
#endif

const PythonState::OwnedFrame& PythonState::top_frame() const noexcept
{
    return this->_top_frame;
}

void PythonState::did_finish(PyThreadState* tstate) noexcept
{
#if GREENLET_PY311
    // See https://github.com/gevent/gevent/issues/1924 and
    // https://github.com/python-greenlet/greenlet/issues/328. In
    // short, Python 3.11 allocates memory for frames as a sort of
    // linked list that's kept as part of PyThreadState in the
    // ``datastack_chunk`` member and friends. These are saved and
    // restored as part of switching greenlets.
    //
    // When we initially switch to a greenlet, we set those to NULL.
    // That causes the frame management code to treat this like a
    // brand new thread and start a fresh list of chunks, beginning
    // with a new "root" chunk. As we make calls in this greenlet,
    // those chunks get added, and as calls return, they get popped.
    // But the frame code (pystate.c) is careful to make sure that the
    // root chunk never gets popped.
    //
    // Thus, when a greenlet exits for the last time, there will be at
    // least a single root chunk that we must be responsible for
    // deallocating.
    //
    // The complex part is that these chunks are allocated and freed
    // using ``_PyObject_VirtualAlloc``/``Free``. Those aren't public
    // functions, and they aren't exported for linking. It so happens
    // that we know they are just thin wrappers around the Arena
    // allocator, so we can use that directly to deallocate in a
    // compatible way.
    //
    // CAUTION: Check this implementation detail on every major version.
    //
    // It might be nice to be able to do this in our destructor, but
    // can we be sure that no one else is using that memory? Plus, as
    // described below, our pointers may not even be valid anymore. As
    // a special case, there is one time that we know we can do this,
    // and that's from the destructor of the associated UserGreenlet
    // (NOT main greenlet)
    PyObjectArenaAllocator alloc;
    _PyStackChunk* chunk = nullptr;
    if (tstate) {
        // We really did finish, we can never be switched to again.
        chunk = tstate->datastack_chunk;
        // Unfortunately, we can't do much sanity checking. Our
        // this->datastack_chunk pointer is out of date (evaluation may
        // have popped down through it already) so we can't verify that
        // we deallocate it. I don't think we can even check datastack_top
        // for the same reason.

        PyObject_GetArenaAllocator(&alloc);
        tstate->datastack_chunk = nullptr;
        tstate->datastack_limit = nullptr;
        tstate->datastack_top = nullptr;

    }
    else if (this->datastack_chunk) {
        // The UserGreenlet (NOT the main greenlet!) is being deallocated. If we're
        // still holding a stack chunk, it's garbage because we know
        // we can never switch back to let cPython clean it up.
        // Because the last time we got switched away from, and we
        // haven't run since then, we know our chain is valid and can
        // be dealloced.
        chunk = this->datastack_chunk;
        PyObject_GetArenaAllocator(&alloc);
    }

    if (alloc.free && chunk) {
        // In case the arena mechanism has been torn down already.
        while (chunk) {
            _PyStackChunk *prev = chunk->previous;
            chunk->previous = nullptr;
            alloc.free(alloc.ctx, chunk, chunk->size);
            chunk = prev;
        }
    }

    this->datastack_chunk = nullptr;
    this->datastack_limit = nullptr;
    this->datastack_top = nullptr;
#endif
}


}; // namespace greenlet

#endif // GREENLET_PYTHON_STATE_CPP


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# TStackState.cpp


```cpp

#ifndef GREENLET_STACK_STATE_CPP
#define GREENLET_STACK_STATE_CPP

#include "greenlet_greenlet.hpp"

namespace greenlet {

#ifdef GREENLET_USE_STDIO
#include <iostream>
using std::cerr;
using std::endl;

std::ostream& operator<<(std::ostream& os, const StackState& s)
{
    os << "StackState(stack_start=" << (void*)s._stack_start
       << ", stack_stop=" << (void*)s.stack_stop
       << ", stack_copy=" << (void*)s.stack_copy
       << ", stack_saved=" << s._stack_saved
       << ", stack_prev=" << s.stack_prev
       << ", addr=" << &s
       << ")";
    return os;
}
#endif

StackState::StackState(void* mark, StackState& current)
    : _stack_start(nullptr),
      stack_stop((char*)mark),
      stack_copy(nullptr),
      _stack_saved(0),
      /* Skip a dying greenlet */
      stack_prev(current._stack_start
                 ? &current
                 : current.stack_prev)
{
}

StackState::StackState()
    : _stack_start(nullptr),
      stack_stop(nullptr),
      stack_copy(nullptr),
      _stack_saved(0),
      stack_prev(nullptr)
{
}

StackState::StackState(const StackState& other)
// can't use a delegating constructor because of
// MSVC for Python 2.7
    : _stack_start(nullptr),
      stack_stop(nullptr),
      stack_copy(nullptr),
      _stack_saved(0),
      stack_prev(nullptr)
{
    this->operator=(other);
}

StackState& StackState::operator=(const StackState& other)
{
    if (&other == this) {
        return *this;
    }
    if (other._stack_saved) {
        throw std::runtime_error("Refusing to steal memory.");
    }

    //If we have memory allocated, dispose of it
    this->free_stack_copy();

    this->_stack_start = other._stack_start;
    this->stack_stop = other.stack_stop;
    this->stack_copy = other.stack_copy;
    this->_stack_saved = other._stack_saved;
    this->stack_prev = other.stack_prev;
    return *this;
}

inline void StackState::free_stack_copy() noexcept
{
    PyMem_Free(this->stack_copy);
    this->stack_copy = nullptr;
    this->_stack_saved = 0;
}

inline void StackState::copy_heap_to_stack(const StackState& current) noexcept
{

    /* Restore the heap copy back into the C stack */
    if (this->_stack_saved != 0) {
        memcpy(this->_stack_start, this->stack_copy, this->_stack_saved);
        this->free_stack_copy();
    }
    StackState* owner = const_cast<StackState*>(&current);
    if (!owner->_stack_start) {
        owner = owner->stack_prev; /* greenlet is dying, skip it */
    }
    while (owner && owner->stack_stop <= this->stack_stop) {
        // cerr << "\tOwner: " << owner << endl;
        owner = owner->stack_prev; /* find greenlet with more stack */
    }
    this->stack_prev = owner;
    // cerr << "\tFinished with: " << *this << endl;
}

inline int StackState::copy_stack_to_heap_up_to(const char* const stop) noexcept
{
    /* Save more of g's stack into the heap -- at least up to 'stop'
       g->stack_stop |________|
                     |        |
                     |    __ stop       . . . . .
                     |        |    ==>  .       .
                     |________|          _______
                     |        |         |       |
                     |        |         |       |
      g->stack_start |        |         |_______| g->stack_copy
     */
    intptr_t sz1 = this->_stack_saved;
    intptr_t sz2 = stop - this->_stack_start;
    assert(this->_stack_start);
    if (sz2 > sz1) {
        char* c = (char*)PyMem_Realloc(this->stack_copy, sz2);
        if (!c) {
            PyErr_NoMemory();
            return -1;
        }
        memcpy(c + sz1, this->_stack_start + sz1, sz2 - sz1);
        this->stack_copy = c;
        this->_stack_saved = sz2;
    }
    return 0;
}

inline int StackState::copy_stack_to_heap(char* const stackref,
                                          const StackState& current) noexcept
{
    /* must free all the C stack up to target_stop */
    const char* const target_stop = this->stack_stop;

    StackState* owner = const_cast<StackState*>(&current);
    assert(owner->_stack_saved == 0); // everything is present on the stack
    if (!owner->_stack_start) {
        owner = owner->stack_prev; /* not saved if dying */
    }
    else {
        owner->_stack_start = stackref;
    }

    while (owner->stack_stop < target_stop) {
        /* ts_current is entierely within the area to free */
        if (owner->copy_stack_to_heap_up_to(owner->stack_stop)) {
            return -1; /* XXX */
        }
        owner = owner->stack_prev;
    }
    if (owner != this) {
        if (owner->copy_stack_to_heap_up_to(target_stop)) {
            return -1; /* XXX */
        }
    }
    return 0;
}

inline bool StackState::started() const noexcept
{
    return this->stack_stop != nullptr;
}

inline bool StackState::main() const noexcept
{
    return this->stack_stop == (char*)-1;
}

inline bool StackState::active() const noexcept
{
    return this->_stack_start != nullptr;
}

inline void StackState::set_active() noexcept
{
    assert(this->_stack_start == nullptr);
    this->_stack_start = (char*)1;
}

inline void StackState::set_inactive() noexcept
{
    this->_stack_start = nullptr;
    // XXX: What if we still have memory out there?
    // That case is actually triggered by
    // test_issue251_issue252_explicit_reference_not_collectable (greenlet.tests.test_leaks.TestLeaks)
    // and
    // test_issue251_issue252_need_to_collect_in_background
    // (greenlet.tests.test_leaks.TestLeaks)
    //
    // Those objects never get deallocated, so the destructor never
    // runs.
    // It *seems* safe to clean up the memory here?
    if (this->_stack_saved) {
        this->free_stack_copy();
    }
}

inline intptr_t StackState::stack_saved() const noexcept
{
    return this->_stack_saved;
}

inline char* StackState::stack_start() const noexcept
{
    return this->_stack_start;
}


inline StackState StackState::make_main() noexcept
{
    StackState s;
    s._stack_start = (char*)1;
    s.stack_stop = (char*)-1;
    return s;
}

StackState::~StackState()
{
    if (this->_stack_saved != 0) {
        this->free_stack_copy();
    }
}

void StackState::copy_from_stack(void* vdest, const void* vsrc, size_t n) const
{
    char* dest = static_cast<char*>(vdest);
    const char* src = static_cast<const char*>(vsrc);
    if (src + n <= this->_stack_start
        || src >= this->_stack_start + this->_stack_saved
        || this->_stack_saved == 0) {
        // Nothing we're copying was spilled from the stack
        memcpy(dest, src, n);
        return;
    }

    if (src < this->_stack_start) {
        // Copy the part before the saved stack.
        // We know src + n > _stack_start due to the test above.
        const size_t nbefore = this->_stack_start - src;
        memcpy(dest, src, nbefore);
        dest += nbefore;
        src += nbefore;
        n -= nbefore;
    }
    // We know src >= _stack_start after the before-copy, and
    // src < _stack_start + _stack_saved due to the first if condition
    size_t nspilled = std::min<size_t>(n, this->_stack_start + this->_stack_saved - src);
    memcpy(dest, this->stack_copy + (src - this->_stack_start), nspilled);
    dest += nspilled;
    src += nspilled;
    n -= nspilled;
    if (n > 0) {
        // Copy the part after the saved stack
        memcpy(dest, src, n);
    }
}

}; // namespace greenlet

#endif // GREENLET_STACK_STATE_CPP


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# TThreadStateDestroy.cpp


```cpp

/* -*- indent-tabs-mode: nil; tab-width: 4; -*- */
/**
 * Implementation of the ThreadState destructors.
 *
 * Format with:
 *  clang-format -i --style=file src/greenlet/greenlet.c
 *
 *
 * Fix missing braces with:
 *   clang-tidy src/greenlet/greenlet.c -fix -checks="readability-braces-around-statements"
*/
#ifndef T_THREADSTATE_DESTROY
#define T_THREADSTATE_DESTROY

#include "greenlet_greenlet.hpp"
#include "greenlet_thread_state.hpp"
#include "greenlet_thread_support.hpp"
#include "greenlet_cpython_add_pending.hpp"
#include "TGreenletGlobals.cpp"

namespace greenlet {

struct ThreadState_DestroyWithGIL
{
    ThreadState_DestroyWithGIL(ThreadState* state)
    {
        if (state && state->has_main_greenlet()) {
            DestroyWithGIL(state);
        }
    }

    static int
    DestroyWithGIL(ThreadState* state)
    {
        // Holding the GIL.
        // Passed a non-shared pointer to the actual thread state.
        // state -> main greenlet
        assert(state->has_main_greenlet());
        PyGreenlet* main(state->borrow_main_greenlet());
        // When we need to do cross-thread operations, we check this.
        // A NULL value means the thread died some time ago.
        // We do this here, rather than in a Python dealloc function
        // for the greenlet, in case there's still a reference out
        // there.
        static_cast<MainGreenlet*>(main->pimpl)->thread_state(nullptr);

        delete state; // Deleting this runs the destructor, DECREFs the main greenlet.
        return 0;
    }
};



struct ThreadState_DestroyNoGIL
{
    // ensure this is actually defined.
    static_assert(GREENLET_BROKEN_PY_ADD_PENDING == 1 || GREENLET_BROKEN_PY_ADD_PENDING == 0,
                  "GREENLET_BROKEN_PY_ADD_PENDING not defined correctly.");

#if GREENLET_BROKEN_PY_ADD_PENDING
    static int _push_pending_call(struct _pending_calls *pending,
                                  int (*func)(void *), void *arg)
    {
        int i = pending->last;
        int j = (i + 1) % NPENDINGCALLS;
        if (j == pending->first) {
            return -1; /* Queue full */
        }
        pending->calls[i].func = func;
        pending->calls[i].arg = arg;
        pending->last = j;
        return 0;
    }

    static int AddPendingCall(int (*func)(void *), void *arg)
    {
        _PyRuntimeState *runtime = &_PyRuntime;
        if (!runtime) {
            // obviously impossible
            return 0;
        }
        struct _pending_calls *pending = &runtime->ceval.pending;
        if (!pending->lock) {
            return 0;
        }
        int result = 0;
        PyThread_acquire_lock(pending->lock, WAIT_LOCK);
        if (!pending->finishing) {
            result = _push_pending_call(pending, func, arg);
        }
        PyThread_release_lock(pending->lock);
        SIGNAL_PENDING_CALLS(&runtime->ceval);
        return result;
    }
#else
    // Python < 3.8 or >= 3.9
    static int AddPendingCall(int (*func)(void*), void* arg)
    {
        return Py_AddPendingCall(func, arg);
    }
#endif

    ThreadState_DestroyNoGIL(ThreadState* state)
    {
        // We are *NOT* holding the GIL. Our thread is in the middle
        // of its death throes and the Python thread state is already
        // gone so we can't use most Python APIs. One that is safe is
        // ``Py_AddPendingCall``, unless the interpreter itself has
        // been torn down. There is a limited number of calls that can
        // be queued: 32 (NPENDINGCALLS) in CPython 3.10, so we
        // coalesce these calls using our own queue.
        if (state && state->has_main_greenlet()) {
            // mark the thread as dead ASAP.
            // this is racy! If we try to throw or switch to a
            // greenlet from this thread from some other thread before
            // we clear the state pointer, it won't realize the state
            // is dead which can crash the process.
            PyGreenlet* p = state->borrow_main_greenlet();
            assert(p->pimpl->thread_state() == state || p->pimpl->thread_state() == nullptr);
            static_cast<MainGreenlet*>(p->pimpl)->thread_state(nullptr);
        }

        // NOTE: Because we're not holding the GIL here, some other
        // Python thread could run and call ``os.fork()``, which would
        // be bad if that happenend while we are holding the cleanup
        // lock (it wouldn't function in the child process).
        // Make a best effort to try to keep the duration we hold the
        // lock short.
        // TODO: On platforms that support it, use ``pthread_atfork`` to
        // drop this lock.
        LockGuard cleanup_lock(*mod_globs->thread_states_to_destroy_lock);

        if (state && state->has_main_greenlet()) {
            // Because we don't have the GIL, this is a race condition.
            if (!PyInterpreterState_Head()) {
                // We have to leak the thread state, if the
                // interpreter has shut down when we're getting
                // deallocated, we can't run the cleanup code that
                // deleting it would imply.
                return;
            }

            mod_globs->queue_to_destroy(state);
            if (mod_globs->thread_states_to_destroy.size() == 1) {
                // We added the first item to the queue. We need to schedule
                // the cleanup.
                int result = ThreadState_DestroyNoGIL::AddPendingCall(
                    ThreadState_DestroyNoGIL::DestroyQueueWithGIL,
                    NULL);
                if (result < 0) {
                    // Hmm, what can we do here?
                    fprintf(stderr,
                            "greenlet: WARNING: failed in call to Py_AddPendingCall; "
                            "expect a memory leak.\n");
                }
            }
        }
    }

    static int
    DestroyQueueWithGIL(void* UNUSED(arg))
    {
        // We're holding the GIL here, so no Python code should be able to
        // run to call ``os.fork()``.
        while (1) {
            ThreadState* to_destroy;
            {
                LockGuard cleanup_lock(*mod_globs->thread_states_to_destroy_lock);
                if (mod_globs->thread_states_to_destroy.empty()) {
                    break;
                }
                to_destroy = mod_globs->take_next_to_destroy();
            }
            // Drop the lock while we do the actual deletion.
            ThreadState_DestroyWithGIL::DestroyWithGIL(to_destroy);
        }
        return 0;
    }

};

}; // namespace greenlet

// The intent when GET_THREAD_STATE() is needed multiple times in a
// function is to take a reference to its return value in a local
// variable, to avoid the thread-local indirection. On some platforms
// (macOS), accessing a thread-local involves a function call (plus an
// initial function call in each function that uses a thread local);
// in contrast, static volatile variables are at some pre-computed
// offset.
typedef greenlet::ThreadStateCreator<greenlet::ThreadState_DestroyNoGIL> ThreadStateCreator;
static thread_local ThreadStateCreator g_thread_state_global;
#define GET_THREAD_STATE() g_thread_state_global

#endif //T_THREADSTATE_DESTROY


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# TUserGreenlet.cpp


```cpp

/* -*- indent-tabs-mode: nil; tab-width: 4; -*- */
/**
 * Implementation of greenlet::UserGreenlet.
 *
 * Format with:
 *  clang-format -i --style=file src/greenlet/greenlet.c
 *
 *
 * Fix missing braces with:
 *   clang-tidy src/greenlet/greenlet.c -fix -checks="readability-braces-around-statements"
*/

#include "greenlet_internal.hpp"
#include "greenlet_greenlet.hpp"
#include "greenlet_thread_state.hpp"
#include "TThreadStateDestroy.cpp"


namespace greenlet {
using greenlet::refs::BorrowedMainGreenlet;
greenlet::PythonAllocator<UserGreenlet> UserGreenlet::allocator;

void* UserGreenlet::operator new(size_t UNUSED(count))
{
    return allocator.allocate(1);
}


void UserGreenlet::operator delete(void* ptr)
{
    return allocator.deallocate(static_cast<UserGreenlet*>(ptr),
                                1);
}


UserGreenlet::UserGreenlet(PyGreenlet* p, BorrowedGreenlet the_parent)
    : Greenlet(p), _parent(the_parent)
{
    this->_self = p;
}

UserGreenlet::~UserGreenlet()
{
    // Python 3.11: If we don't clear out the raw frame datastack
    // when deleting an unfinished greenlet,
    // TestLeaks.test_untracked_memory_doesnt_increase_unfinished_thread_dealloc_in_main fails.
    this->python_state.did_finish(nullptr);
    this->tp_clear();
}

BorrowedGreenlet
UserGreenlet::self() const noexcept
{
    return this->_self;
}



const BorrowedMainGreenlet
UserGreenlet::main_greenlet() const
{
    return this->_main_greenlet;
}


BorrowedMainGreenlet
UserGreenlet::find_main_greenlet_in_lineage() const
{
    if (this->started()) {
        assert(this->_main_greenlet);
        return BorrowedMainGreenlet(this->_main_greenlet);
    }

    if (!this->_parent) {
        /* garbage collected greenlet in chain */
        // XXX: WHAT?
        return BorrowedMainGreenlet(nullptr);
    }

    return this->_parent->find_main_greenlet_in_lineage();
}


/**
 * CAUTION: This will allocate memory and may trigger garbage
 * collection and arbitrary Python code.
 */
OwnedObject
UserGreenlet::throw_GreenletExit_during_dealloc(const ThreadState& current_thread_state)
{
    /* The dying greenlet cannot be a parent of ts_current
       because the 'parent' field chain would hold a
       reference */
    UserGreenlet::ParentIsCurrentGuard with_current_parent(this, current_thread_state);

    // We don't care about the return value, only whether an
    // exception happened. Whether or not an exception happens,
    // we need to restore the parent in case the greenlet gets
    // resurrected.
    return Greenlet::throw_GreenletExit_during_dealloc(current_thread_state);
}

ThreadState*
UserGreenlet::thread_state() const noexcept
{
    // TODO: maybe make this throw, if the thread state isn't there?
    // if (!this->main_greenlet) {
    //     throw std::runtime_error("No thread state"); // TODO: Better exception
    // }
    if (!this->_main_greenlet) {
        return nullptr;
    }
    return this->_main_greenlet->thread_state();
}


bool
UserGreenlet::was_running_in_dead_thread() const noexcept
{
    return this->_main_greenlet && !this->thread_state();
}

OwnedObject
UserGreenlet::g_switch()
{
    assert(this->args() || PyErr_Occurred());

    try {
        this->check_switch_allowed();
    }
    catch (const PyErrOccurred&) {
        this->release_args();
        throw;
    }

    // Switching greenlets used to attempt to clean out ones that need
    // deleted *if* we detected a thread switch. Should it still do
    // that?
    // An issue is that if we delete a greenlet from another thread,
    // it gets queued to this thread, and ``kill_greenlet()`` switches
    // back into the greenlet

    /* find the real target by ignoring dead greenlets,
       and if necessary starting a greenlet. */
    switchstack_result_t err;
    Greenlet* target = this;
    // TODO: probably cleaner to handle the case where we do
    // switch to ourself separately from the other cases.
    // This can probably even further be simplified if we keep
    // track of the switching_state we're going for and just call
    // into g_switch() if it's not ourself. The main problem with that
    // is that we would be using more stack space.
    bool target_was_me = true;
    bool was_initial_stub = false;
    while (target) {
        if (target->active()) {
            if (!target_was_me) {
                target->args() <<= this->args();
                assert(!this->args());
            }
            err = target->g_switchstack();
            break;
        }
        if (!target->started()) {
            // We never encounter a main greenlet that's not started.
            assert(!target->main());
            UserGreenlet* real_target = static_cast<UserGreenlet*>(target);
            assert(real_target);
            void* dummymarker;
            was_initial_stub = true;
            if (!target_was_me) {
                target->args() <<= this->args();
                assert(!this->args());
            }
            try {
                // This can only throw back to us while we're
                // still in this greenlet. Once the new greenlet
                // is bootstrapped, it has its own exception state.
                err = real_target->g_initialstub(&dummymarker);
            }
            catch (const PyErrOccurred&) {
                this->release_args();
                throw;
            }
            catch (const GreenletStartedWhileInPython&) {
                // The greenlet was started sometime before this
                // greenlet actually switched to it, i.e.,
                // "concurrent" calls to switch() or throw().
                // We need to retry the switch.
                // Note that the current greenlet has been reset
                // to this one (or we wouldn't be running!)
                continue;
            }
            break;
        }

        target = target->parent();
        target_was_me = false;
    }
    // The ``this`` pointer and all other stack or register based
    // variables are invalid now, at least where things succeed
    // above.
    // But this one, probably not so much? It's not clear if it's
    // safe to throw an exception at this point.

    if (err.status < 0) {
        // If we get here, either g_initialstub()
        // failed, or g_switchstack() failed. Either one of those
        // cases SHOULD leave us in the original greenlet with a valid
        // stack.
        return this->on_switchstack_or_initialstub_failure(target, err, target_was_me, was_initial_stub);
    }

    // err.the_new_current_greenlet would be the same as ``target``,
    // if target wasn't probably corrupt.
    return err.the_new_current_greenlet->g_switch_finish(err);
}



Greenlet::switchstack_result_t
UserGreenlet::g_initialstub(void* mark)
{
    OwnedObject run;

    // We need to grab a reference to the current switch arguments
    // in case we're entered concurrently during the call to
    // GetAttr() and have to try again.
    // We'll restore them when we return in that case.
    // Scope them tightly to avoid ref leaks.
    {
        SwitchingArgs args(this->args());

        /* save exception in case getattr clears it */
        PyErrPieces saved;

        /*
          self.run is the object to call in the new greenlet.
          This could run arbitrary python code and switch greenlets!
        */
        run = this->_self.PyRequireAttr(mod_globs->str_run);
        /* restore saved exception */
        saved.PyErrRestore();


        /* recheck that it's safe to switch in case greenlet reparented anywhere above */
        this->check_switch_allowed();

        /* by the time we got here another start could happen elsewhere,
         * that means it should now be a regular switch.
         * This can happen if the Python code is a subclass that implements
         * __getattribute__ or __getattr__, or makes ``run`` a descriptor;
         * all of those can run arbitrary code that switches back into
         * this greenlet.
         */
        if (this->stack_state.started()) {
            // the successful switch cleared these out, we need to
            // restore our version. They will be copied on up to the
            // next target.
            assert(!this->args());
            this->args() <<= args;
            throw GreenletStartedWhileInPython();
        }
    }

    // Sweet, if we got here, we have the go-ahead and will switch
    // greenlets.
    // Nothing we do from here on out should allow for a thread or
    // greenlet switch: No arbitrary calls to Python, including
    // decref'ing

#if GREENLET_USE_CFRAME
    /* OK, we need it, we're about to switch greenlets, save the state. */
    /*
      See green_new(). This is a stack-allocated variable used
      while *self* is in PyObject_Call().
      We want to defer copying the state info until we're sure
      we need it and are in a stable place to do so.
    */
    _PyCFrame trace_info;

    this->python_state.set_new_cframe(trace_info);
#endif
    /* start the greenlet */
    ThreadState& thread_state = GET_THREAD_STATE().state();
    this->stack_state = StackState(mark,
                                   thread_state.borrow_current()->stack_state);
    this->python_state.set_initial_state(PyThreadState_GET());
    this->exception_state.clear();
    this->_main_greenlet = thread_state.get_main_greenlet();

    /* perform the initial switch */
    switchstack_result_t err = this->g_switchstack();
    /* returns twice!
       The 1st time with ``err == 1``: we are in the new greenlet.
       This one owns a greenlet that used to be current.
       The 2nd time with ``err <= 0``: back in the caller's
       greenlet; this happens if the child finishes or switches
       explicitly to us. Either way, the ``err`` variable is
       created twice at the same memory location, but possibly
       having different ``origin`` values. Note that it's not
       constructed for the second time until the switch actually happens.
    */
    if (err.status == 1) {
        // In the new greenlet.

        // This never returns! Calling inner_bootstrap steals
        // the contents of our run object within this stack frame, so
        // it is not valid to do anything with it.
        try {
            this->inner_bootstrap(err.origin_greenlet.relinquish_ownership(),
                                  run.relinquish_ownership());
        }
        // Getting a C++ exception here isn't good. It's probably a
        // bug in the underlying greenlet, meaning it's probably a
        // C++ extension. We're going to abort anyway, but try to
        // display some nice information *if* possible. Some obscure
        // platforms don't properly support this (old 32-bit Arm, see see
        // https://github.com/python-greenlet/greenlet/issues/385); that's not
        // great, but should usually be OK because, as mentioned above, we're
        // terminating anyway.
        //
        // The catching is tested by
        // ``test_cpp.CPPTests.test_unhandled_exception_in_greenlet_aborts``.
        //
        // PyErrOccurred can theoretically be thrown by
        // inner_bootstrap() -> g_switch_finish(), but that should
        // never make it back to here. It is a std::exception and
        // would be caught if it is.
        catch (const std::exception& e) {
            std::string base = "greenlet: Unhandled C++ exception: ";
            base += e.what();
            Py_FatalError(base.c_str());
        }
        catch (...) {
            // Some compilers/runtimes use exceptions internally.
            // It appears that GCC on Linux with libstdc++ throws an
            // exception internally at process shutdown time to unwind
            // stacks and clean up resources. Depending on exactly
            // where we are when the process exits, that could result
            // in an unknown exception getting here. If we
            // Py_FatalError() or abort() here, we interfere with
            // orderly process shutdown. Throwing the exception on up
            // is the right thing to do.
            //
            // gevent's ``examples/dns_mass_resolve.py`` demonstrates this.
#ifndef NDEBUG
            fprintf(stderr,
                    "greenlet: inner_bootstrap threw unknown exception; "
                    "is the process terminating?\n");
#endif
            throw;
        }
        Py_FatalError("greenlet: inner_bootstrap returned with no exception.\n");
    }


    // In contrast, notice that we're keeping the origin greenlet
    // around as an owned reference; we need it to call the trace
    // function for the switch back into the parent. It was only
    // captured at the time the switch actually happened, though,
    // so we haven't been keeping an extra reference around this
    // whole time.

    /* back in the parent */
    if (err.status < 0) {
        /* start failed badly, restore greenlet state */
        this->stack_state = StackState();
        this->_main_greenlet.CLEAR();
        // CAUTION: This may run arbitrary Python code.
        run.CLEAR(); // inner_bootstrap didn't run, we own the reference.
    }

    // In the success case, the spawned code (inner_bootstrap) will
    // take care of decrefing this, so we relinquish ownership so as
    // to not double-decref.

    run.relinquish_ownership();

    return err;
}


void
UserGreenlet::inner_bootstrap(PyGreenlet* origin_greenlet, PyObject* run)
{
    // The arguments here would be another great place for move.
    // As it is, we take them as a reference so that when we clear
    // them we clear what's on the stack above us. Do that NOW, and
    // without using a C++ RAII object,
    // so there's no way that exiting the parent frame can clear it,
    // or we clear it unexpectedly. This arises in the context of the
    // interpreter shutting down. See https://github.com/python-greenlet/greenlet/issues/325
    //PyObject* run = _run.relinquish_ownership();

    /* in the new greenlet */
    assert(this->thread_state()->borrow_current() == this->_self);
    // C++ exceptions cannot propagate to the parent greenlet from
    // here. (TODO: Do we need a catch(...) clause, perhaps on the
    // function itself? ALl we could do is terminate the program.)
    // NOTE: On 32-bit Windows, the call chain is extremely
    // important here in ways that are subtle, having to do with
    // the depth of the SEH list. The call to restore it MUST NOT
    // add a new SEH handler to the list, or we'll restore it to
    // the wrong thing.
    this->thread_state()->restore_exception_state();
    /* stack variables from above are no good and also will not unwind! */
    // EXCEPT: That can't be true, we access run, among others, here.

    this->stack_state.set_active(); /* running */

    // We're about to possibly run Python code again, which
    // could switch back/away to/from us, so we need to grab the
    // arguments locally.
    SwitchingArgs args;
    args <<= this->args();
    assert(!this->args());

    // XXX: We could clear this much earlier, right?
    // Or would that introduce the possibility of running Python
    // code when we don't want to?
    // CAUTION: This may run arbitrary Python code.
    this->_run_callable.CLEAR();


    // The first switch we need to manually call the trace
    // function here instead of in g_switch_finish, because we
    // never return there.
    if (OwnedObject tracefunc = this->thread_state()->get_tracefunc()) {
        OwnedGreenlet trace_origin;
        trace_origin = origin_greenlet;
        try {
            g_calltrace(tracefunc,
                        args ? mod_globs->event_switch : mod_globs->event_throw,
                        trace_origin,
                        this->_self);
        }
        catch (const PyErrOccurred&) {
            /* Turn trace errors into switch throws */
            args.CLEAR();
        }
    }

    // We no longer need the origin, it was only here for
    // tracing.
    // We may never actually exit this stack frame so we need
    // to explicitly clear it.
    // This could run Python code and switch.
    Py_CLEAR(origin_greenlet);

    OwnedObject result;
    if (!args) {
        /* pending exception */
        result = NULL;
    }
    else {
        /* call g.run(*args, **kwargs) */
        // This could result in further switches
        try {
            //result = run.PyCall(args.args(), args.kwargs());
            // CAUTION: Just invoking this, before the function even
            // runs, may cause memory allocations, which may trigger
            // GC, which may run arbitrary Python code.
            result = OwnedObject::consuming(PyObject_Call(run, args.args().borrow(), args.kwargs().borrow()));
        }
        catch (...) {
            // Unhandled C++ exception!

            // If we declare ourselves as noexcept, if we don't catch
            // this here, most platforms will just abort() the
            // process. But on 64-bit Windows with older versions of
            // the C runtime, this can actually corrupt memory and
            // just return. We see this when compiling with the
            // Windows 7.0 SDK targeting Windows Server 2008, but not
            // when using the Appveyor Visual Studio 2019 image. So
            // this currently only affects Python 2.7 on Windows 64.
            // That is, the tests pass and the runtime aborts
            // everywhere else.
            //
            // However, if we catch it and try to continue with a
            // Python error, then all Windows 64 bit platforms corrupt
            // memory. So all we can do is manually abort, hopefully
            // with a good error message. (Note that the above was
            // tested WITHOUT the `/EHr` switch being used at compile
            // time, so MSVC may have "optimized" out important
            // checking. Using that switch, we may be in a better
            // place in terms of memory corruption.) But sometimes it
            // can't be caught here at all, which is confusing but not
            // terribly surprising; so again, the G_NOEXCEPT_WIN32
            // plus "/EHr".
            //
            // Hopefully the basic C stdlib is still functional enough
            // for us to at least print an error.
            //
            // It gets more complicated than that, though, on some
            // platforms, specifically at least Linux/gcc/libstdc++. They use
            // an exception to unwind the stack when a background
            // thread exits. (See comments about noexcept.) So this
            // may not actually represent anything untoward. On those
            // platforms we allow throws of this to propagate, or
            // attempt to anyway.
# if defined(WIN32) || defined(_WIN32)
            Py_FatalError(
                "greenlet: Unhandled C++ exception from a greenlet run function. "
                "Because memory is likely corrupted, terminating process.");
            std::abort();
#else
            throw;
#endif
        }
    }
    // These lines may run arbitrary code
    args.CLEAR();
    Py_CLEAR(run);

    if (!result
        && mod_globs->PyExc_GreenletExit.PyExceptionMatches()
        && (this->args())) {
        // This can happen, for example, if our only reference
        // goes away after we switch back to the parent.
        // See test_dealloc_switch_args_not_lost
        PyErrPieces clear_error;
        result <<= this->args();
        result = single_result(result);
    }
    this->release_args();
    this->python_state.did_finish(PyThreadState_GET());

    result = g_handle_exit(result);
    assert(this->thread_state()->borrow_current() == this->_self);

    /* jump back to parent */
    this->stack_state.set_inactive(); /* dead */


    // TODO: Can we decref some things here? Release our main greenlet
    // and maybe parent?
    for (Greenlet* parent = this->_parent;
         parent;
         parent = parent->parent()) {
        // We need to somewhere consume a reference to
        // the result; in most cases we'll never have control
        // back in this stack frame again. Calling
        // green_switch actually adds another reference!
        // This would probably be clearer with a specific API
        // to hand results to the parent.
        parent->args() <<= result;
        assert(!result);
        // The parent greenlet now owns the result; in the
        // typical case we'll never get back here to assign to
        // result and thus release the reference.
        try {
            result = parent->g_switch();
        }
        catch (const PyErrOccurred&) {
            // Ignore, keep passing the error on up.
        }

        /* Return here means switch to parent failed,
         * in which case we throw *current* exception
         * to the next parent in chain.
         */
        assert(!result);
    }
    /* We ran out of parents, cannot continue */
    PyErr_WriteUnraisable(this->self().borrow_o());
    Py_FatalError("greenlet: ran out of parent greenlets while propagating exception; "
                  "cannot continue");
    std::abort();
}

void
UserGreenlet::run(const BorrowedObject nrun)
{
    if (this->started()) {
        throw AttributeError(
                        "run cannot be set "
                        "after the start of the greenlet");
    }
    this->_run_callable = nrun;
}

const OwnedGreenlet
UserGreenlet::parent() const
{
    return this->_parent;
}

void
UserGreenlet::parent(const BorrowedObject raw_new_parent)
{
    if (!raw_new_parent) {
        throw AttributeError("can't delete attribute");
    }

    BorrowedMainGreenlet main_greenlet_of_new_parent;
    BorrowedGreenlet new_parent(raw_new_parent.borrow()); // could
                                                          // throw
                                                          // TypeError!
    for (BorrowedGreenlet p = new_parent; p; p = p->parent()) {
        if (p == this->_self) {
            throw ValueError("cyclic parent chain");
        }
        main_greenlet_of_new_parent = p->main_greenlet();
    }

    if (!main_greenlet_of_new_parent) {
        throw ValueError("parent must not be garbage collected");
    }

    if (this->started()
        && this->_main_greenlet != main_greenlet_of_new_parent) {
        throw ValueError("parent cannot be on a different thread");
    }

    this->_parent = new_parent;
}

void
UserGreenlet::murder_in_place()
{
    this->_main_greenlet.CLEAR();
    Greenlet::murder_in_place();
}

bool
UserGreenlet::belongs_to_thread(const ThreadState* thread_state) const
{
    return Greenlet::belongs_to_thread(thread_state) && this->_main_greenlet == thread_state->borrow_main_greenlet();
}


int
UserGreenlet::tp_traverse(visitproc visit, void* arg)
{
    Py_VISIT(this->_parent.borrow_o());
    Py_VISIT(this->_main_greenlet.borrow_o());
    Py_VISIT(this->_run_callable.borrow_o());

    return Greenlet::tp_traverse(visit, arg);
}

int
UserGreenlet::tp_clear()
{
    Greenlet::tp_clear();
    this->_parent.CLEAR();
    this->_main_greenlet.CLEAR();
    this->_run_callable.CLEAR();
    return 0;
}

UserGreenlet::ParentIsCurrentGuard::ParentIsCurrentGuard(UserGreenlet* p,
                                                     const ThreadState& thread_state)
    : oldparent(p->_parent),
      greenlet(p)
{
    p->_parent = thread_state.get_current();
}

UserGreenlet::ParentIsCurrentGuard::~ParentIsCurrentGuard()
{
    this->greenlet->_parent = oldparent;
    oldparent.CLEAR();
}

}; //namespace greenlet


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# _test_extension.c


```cpp

/* This is a set of functions used by test_extension_interface.py to test the
 * Greenlet C API.
 */

#include "../greenlet.h"

#ifndef Py_RETURN_NONE
#    define Py_RETURN_NONE return Py_INCREF(Py_None), Py_None
#endif

#define TEST_MODULE_NAME "_test_extension"

static PyObject*
test_switch(PyObject* self, PyObject* greenlet)
{
    PyObject* result = NULL;

    if (greenlet == NULL || !PyGreenlet_Check(greenlet)) {
        PyErr_BadArgument();
        return NULL;
    }

    result = PyGreenlet_Switch((PyGreenlet*)greenlet, NULL, NULL);
    if (result == NULL) {
        if (!PyErr_Occurred()) {
            PyErr_SetString(PyExc_AssertionError,
                            "greenlet.switch() failed for some reason.");
        }
        return NULL;
    }
    Py_INCREF(result);
    return result;
}

static PyObject*
test_switch_kwargs(PyObject* self, PyObject* args, PyObject* kwargs)
{
    PyGreenlet* g = NULL;
    PyObject* result = NULL;

    PyArg_ParseTuple(args, "O!", &PyGreenlet_Type, &g);

    if (g == NULL || !PyGreenlet_Check(g)) {
        PyErr_BadArgument();
        return NULL;
    }

    result = PyGreenlet_Switch(g, NULL, kwargs);
    if (result == NULL) {
        if (!PyErr_Occurred()) {
            PyErr_SetString(PyExc_AssertionError,
                            "greenlet.switch() failed for some reason.");
        }
        return NULL;
    }
    Py_XINCREF(result);
    return result;
}

static PyObject*
test_getcurrent(PyObject* self)
{
    PyGreenlet* g = PyGreenlet_GetCurrent();
    if (g == NULL || !PyGreenlet_Check(g) || !PyGreenlet_ACTIVE(g)) {
        PyErr_SetString(PyExc_AssertionError,
                        "getcurrent() returned an invalid greenlet");
        Py_XDECREF(g);
        return NULL;
    }
    Py_DECREF(g);
    Py_RETURN_NONE;
}

static PyObject*
test_setparent(PyObject* self, PyObject* arg)
{
    PyGreenlet* current;
    PyGreenlet* greenlet = NULL;

    if (arg == NULL || !PyGreenlet_Check(arg)) {
        PyErr_BadArgument();
        return NULL;
    }
    if ((current = PyGreenlet_GetCurrent()) == NULL) {
        return NULL;
    }
    greenlet = (PyGreenlet*)arg;
    if (PyGreenlet_SetParent(greenlet, current)) {
        Py_DECREF(current);
        return NULL;
    }
    Py_DECREF(current);
    if (PyGreenlet_Switch(greenlet, NULL, NULL) == NULL) {
        return NULL;
    }
    Py_RETURN_NONE;
}

static PyObject*
test_new_greenlet(PyObject* self, PyObject* callable)
{
    PyObject* result = NULL;
    PyGreenlet* greenlet = PyGreenlet_New(callable, NULL);

    if (!greenlet) {
        return NULL;
    }

    result = PyGreenlet_Switch(greenlet, NULL, NULL);
    Py_CLEAR(greenlet);
    if (result == NULL) {
        return NULL;
    }

    Py_INCREF(result);
    return result;
}

static PyObject*
test_raise_dead_greenlet(PyObject* self)
{
    PyErr_SetString(PyExc_GreenletExit, "test GreenletExit exception.");
    return NULL;
}

static PyObject*
test_raise_greenlet_error(PyObject* self)
{
    PyErr_SetString(PyExc_GreenletError, "test greenlet.error exception");
    return NULL;
}

static PyObject*
test_throw(PyObject* self, PyGreenlet* g)
{
    const char msg[] = "take that sucka!";
    PyObject* msg_obj = Py_BuildValue("s", msg);
    PyGreenlet_Throw(g, PyExc_ValueError, msg_obj, NULL);
    Py_DECREF(msg_obj);
    if (PyErr_Occurred()) {
        return NULL;
    }
    Py_RETURN_NONE;
}

static PyObject*
test_throw_exact(PyObject* self, PyObject* args)
{
    PyGreenlet* g = NULL;
    PyObject* typ = NULL;
    PyObject* val = NULL;
    PyObject* tb = NULL;

    if (!PyArg_ParseTuple(args, "OOOO:throw", &g, &typ, &val, &tb)) {
        return NULL;
    }

    PyGreenlet_Throw(g, typ, val, tb);
    if (PyErr_Occurred()) {
        return NULL;
    }
    Py_RETURN_NONE;
}

static PyMethodDef test_methods[] = {
    {"test_switch",
     (PyCFunction)test_switch,
     METH_O,
     "Switch to the provided greenlet sending provided arguments, and \n"
     "return the results."},
    {"test_switch_kwargs",
     (PyCFunction)test_switch_kwargs,
     METH_VARARGS | METH_KEYWORDS,
     "Switch to the provided greenlet sending the provided keyword args."},
    {"test_getcurrent",
     (PyCFunction)test_getcurrent,
     METH_NOARGS,
     "Test PyGreenlet_GetCurrent()"},
    {"test_setparent",
     (PyCFunction)test_setparent,
     METH_O,
     "Se the parent of the provided greenlet and switch to it."},
    {"test_new_greenlet",
     (PyCFunction)test_new_greenlet,
     METH_O,
     "Test PyGreenlet_New()"},
    {"test_raise_dead_greenlet",
     (PyCFunction)test_raise_dead_greenlet,
     METH_NOARGS,
     "Just raise greenlet.GreenletExit"},
    {"test_raise_greenlet_error",
     (PyCFunction)test_raise_greenlet_error,
     METH_NOARGS,
     "Just raise greenlet.error"},
    {"test_throw",
     (PyCFunction)test_throw,
     METH_O,
     "Throw a ValueError at the provided greenlet"},
    {"test_throw_exact",
     (PyCFunction)test_throw_exact,
     METH_VARARGS,
     "Throw exactly the arguments given at the provided greenlet"},
    {NULL, NULL, 0, NULL}
};


#define INITERROR return NULL

static struct PyModuleDef moduledef = {PyModuleDef_HEAD_INIT,
                                       TEST_MODULE_NAME,
                                       NULL,
                                       0,
                                       test_methods,
                                       NULL,
                                       NULL,
                                       NULL,
                                       NULL};

PyMODINIT_FUNC
PyInit__test_extension(void)
{
    PyObject* module = NULL;
    module = PyModule_Create(&moduledef);

    if (module == NULL) {
        return NULL;
    }

    PyGreenlet_Import();
    return module;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# _test_extension_cpp.cpp


```cpp

/* This is a set of functions used to test C++ exceptions are not
 * broken during greenlet switches
 */

#include "../greenlet.h"
#include "../greenlet_compiler_compat.hpp"
#include <exception>
#include <stdexcept>

struct exception_t {
    int depth;
    exception_t(int depth) : depth(depth) {}
};

/* Functions are called via pointers to prevent inlining */
static void (*p_test_exception_throw_nonstd)(int depth);
static void (*p_test_exception_throw_std)();
static PyObject* (*p_test_exception_switch_recurse)(int depth, int left);

static void
test_exception_throw_nonstd(int depth)
{
    throw exception_t(depth);
}

static void
test_exception_throw_std()
{
    throw std::runtime_error("Thrown from an extension.");
}

static PyObject*
test_exception_switch_recurse(int depth, int left)
{
    if (left > 0) {
        return p_test_exception_switch_recurse(depth, left - 1);
    }

    PyObject* result = NULL;
    PyGreenlet* self = PyGreenlet_GetCurrent();
    if (self == NULL)
        return NULL;

    try {
        if (PyGreenlet_Switch(PyGreenlet_GET_PARENT(self), NULL, NULL) == NULL) {
            Py_DECREF(self);
            return NULL;
        }
        p_test_exception_throw_nonstd(depth);
        PyErr_SetString(PyExc_RuntimeError,
                        "throwing C++ exception didn't work");
    }
    catch (const exception_t& e) {
        if (e.depth != depth)
            PyErr_SetString(PyExc_AssertionError, "depth mismatch");
        else
            result = PyLong_FromLong(depth);
    }
    catch (...) {
        PyErr_SetString(PyExc_RuntimeError, "unexpected C++ exception");
    }

    Py_DECREF(self);
    return result;
}

/* test_exception_switch(int depth)
 * - recurses depth times
 * - switches to parent inside try/catch block
 * - throws an exception that (expected to be caught in the same function)
 * - verifies depth matches (exceptions shouldn't be caught in other greenlets)
 */
static PyObject*
test_exception_switch(PyObject* UNUSED(self), PyObject* args)
{
    int depth;
    if (!PyArg_ParseTuple(args, "i", &depth))
        return NULL;
    return p_test_exception_switch_recurse(depth, depth);
}


static PyObject*
py_test_exception_throw_nonstd(PyObject* self, PyObject* args)
{
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    p_test_exception_throw_nonstd(0);
    PyErr_SetString(PyExc_AssertionError, "unreachable code running after throw");
    return NULL;
}

static PyObject*
py_test_exception_throw_std(PyObject* self, PyObject* args)
{
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    p_test_exception_throw_std();
    PyErr_SetString(PyExc_AssertionError, "unreachable code running after throw");
    return NULL;
}

static PyObject*
py_test_call(PyObject* self, PyObject* arg)
{
    PyObject* noargs = PyTuple_New(0);
    PyObject* ret = PyObject_Call(arg, noargs, nullptr);
    Py_DECREF(noargs);
    return ret;
}



/* test_exception_switch_and_do_in_g2(g2func)
 * - creates new greenlet g2 to run g2func
 * - switches to g2 inside try/catch block
 * - verifies that no exception has been caught
 *
 * it is used together with test_exception_throw to verify that unhandled
 * exceptions thrown in one greenlet do not propagate to other greenlet nor
 * segfault the process.
 */
static PyObject*
test_exception_switch_and_do_in_g2(PyObject* self, PyObject* args)
{
    PyObject* g2func = NULL;
    PyObject* result = NULL;

    if (!PyArg_ParseTuple(args, "O", &g2func))
        return NULL;
    PyGreenlet* g2 = PyGreenlet_New(g2func, NULL);
    if (!g2) {
        return NULL;
    }

    try {
        result = PyGreenlet_Switch(g2, NULL, NULL);
        if (!result) {
            return NULL;
        }
    }
    catch (const exception_t& e) {
        /* if we are here the memory can be already corrupted and the program
         * might crash before below py-level exception might become printed.
         * -> print something to stderr to make it clear that we had entered
         *    this catch block.
         * See comments in inner_bootstrap()
         */
#if defined(WIN32) || defined(_WIN32)
        fprintf(stderr, "C++ exception unexpectedly caught in g1\n");
        PyErr_SetString(PyExc_AssertionError, "C++ exception unexpectedly caught in g1");
        Py_XDECREF(result);
        return NULL;
#else
        throw;
#endif
    }

    Py_XDECREF(result);
    Py_RETURN_NONE;
}

static PyMethodDef test_methods[] = {
    {"test_exception_switch",
     (PyCFunction)&test_exception_switch,
     METH_VARARGS,
     "Switches to parent twice, to test exception handling and greenlet "
     "switching."},
    {"test_exception_switch_and_do_in_g2",
     (PyCFunction)&test_exception_switch_and_do_in_g2,
     METH_VARARGS,
     "Creates new greenlet g2 to run g2func and switches to it inside try/catch "
     "block. Used together with test_exception_throw to verify that unhandled "
     "C++ exceptions thrown in a greenlet doe not corrupt memory."},
    {"test_exception_throw_nonstd",
     (PyCFunction)&py_test_exception_throw_nonstd,
     METH_VARARGS,
     "Throws non-standard C++ exception. Calling this function directly should abort the process."
    },
    {"test_exception_throw_std",
     (PyCFunction)&py_test_exception_throw_std,
     METH_VARARGS,
     "Throws standard C++ exception. Calling this function directly should abort the process."
    },
    {"test_call",
     (PyCFunction)&py_test_call,
     METH_O,
     "Call the given callable. Unlike calling it directly, this creates a "
     "new C-level stack frame, which may be helpful in testing."
    },
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef moduledef = {PyModuleDef_HEAD_INIT,
                                       "greenlet.tests._test_extension_cpp",
                                       NULL,
                                       0,
                                       test_methods,
                                       NULL,
                                       NULL,
                                       NULL,
                                       NULL};

PyMODINIT_FUNC
PyInit__test_extension_cpp(void)
{
    PyObject* module = NULL;

    module = PyModule_Create(&moduledef);

    if (module == NULL) {
        return NULL;
    }

    PyGreenlet_Import();
    if (_PyGreenlet_API == NULL) {
        return NULL;
    }

    p_test_exception_throw_nonstd = test_exception_throw_nonstd;
    p_test_exception_throw_std = test_exception_throw_std;
    p_test_exception_switch_recurse = test_exception_switch_recurse;

    return module;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# _speedups.c


```cpp

#include <Python.h>

static PyObject* markup;

static int
init_constants(void)
{
	PyObject *module;

	/* import markup type so that we can mark the return value */
	module = PyImport_ImportModule("markupsafe");
	if (!module)
		return 0;
	markup = PyObject_GetAttrString(module, "Markup");
	Py_DECREF(module);

	return 1;
}

#define GET_DELTA(inp, inp_end, delta) \
	while (inp < inp_end) { \
		switch (*inp++) { \
		case '"': \
		case '\'': \
		case '&': \
			delta += 4; \
			break; \
		case '<': \
		case '>': \
			delta += 3; \
			break; \
		} \
	}

#define DO_ESCAPE(inp, inp_end, outp) \
	{ \
		Py_ssize_t ncopy = 0; \
		while (inp < inp_end) { \
			switch (*inp) { \
			case '"': \
				memcpy(outp, inp-ncopy, sizeof(*outp)*ncopy); \
				outp += ncopy; ncopy = 0; \
				*outp++ = '&'; \
				*outp++ = '#'; \
				*outp++ = '3'; \
				*outp++ = '4'; \
				*outp++ = ';'; \
				break; \
			case '\'': \
				memcpy(outp, inp-ncopy, sizeof(*outp)*ncopy); \
				outp += ncopy; ncopy = 0; \
				*outp++ = '&'; \
				*outp++ = '#'; \
				*outp++ = '3'; \
				*outp++ = '9'; \
				*outp++ = ';'; \
				break; \
			case '&': \
				memcpy(outp, inp-ncopy, sizeof(*outp)*ncopy); \
				outp += ncopy; ncopy = 0; \
				*outp++ = '&'; \
				*outp++ = 'a'; \
				*outp++ = 'm'; \
				*outp++ = 'p'; \
				*outp++ = ';'; \
				break; \
			case '<': \
				memcpy(outp, inp-ncopy, sizeof(*outp)*ncopy); \
				outp += ncopy; ncopy = 0; \
				*outp++ = '&'; \
				*outp++ = 'l'; \
				*outp++ = 't'; \
				*outp++ = ';'; \
				break; \
			case '>': \
				memcpy(outp, inp-ncopy, sizeof(*outp)*ncopy); \
				outp += ncopy; ncopy = 0; \
				*outp++ = '&'; \
				*outp++ = 'g'; \
				*outp++ = 't'; \
				*outp++ = ';'; \
				break; \
			default: \
				ncopy++; \
			} \
			inp++; \
		} \
		memcpy(outp, inp-ncopy, sizeof(*outp)*ncopy); \
	}

static PyObject*
escape_unicode_kind1(PyUnicodeObject *in)
{
	Py_UCS1 *inp = PyUnicode_1BYTE_DATA(in);
	Py_UCS1 *inp_end = inp + PyUnicode_GET_LENGTH(in);
	Py_UCS1 *outp;
	PyObject *out;
	Py_ssize_t delta = 0;

	GET_DELTA(inp, inp_end, delta);
	if (!delta) {
		Py_INCREF(in);
		return (PyObject*)in;
	}

	out = PyUnicode_New(PyUnicode_GET_LENGTH(in) + delta,
						PyUnicode_IS_ASCII(in) ? 127 : 255);
	if (!out)
		return NULL;

	inp = PyUnicode_1BYTE_DATA(in);
	outp = PyUnicode_1BYTE_DATA(out);
	DO_ESCAPE(inp, inp_end, outp);
	return out;
}

static PyObject*
escape_unicode_kind2(PyUnicodeObject *in)
{
	Py_UCS2 *inp = PyUnicode_2BYTE_DATA(in);
	Py_UCS2 *inp_end = inp + PyUnicode_GET_LENGTH(in);
	Py_UCS2 *outp;
	PyObject *out;
	Py_ssize_t delta = 0;

	GET_DELTA(inp, inp_end, delta);
	if (!delta) {
		Py_INCREF(in);
		return (PyObject*)in;
	}

	out = PyUnicode_New(PyUnicode_GET_LENGTH(in) + delta, 65535);
	if (!out)
		return NULL;

	inp = PyUnicode_2BYTE_DATA(in);
	outp = PyUnicode_2BYTE_DATA(out);
	DO_ESCAPE(inp, inp_end, outp);
	return out;
}


static PyObject*
escape_unicode_kind4(PyUnicodeObject *in)
{
	Py_UCS4 *inp = PyUnicode_4BYTE_DATA(in);
	Py_UCS4 *inp_end = inp + PyUnicode_GET_LENGTH(in);
	Py_UCS4 *outp;
	PyObject *out;
	Py_ssize_t delta = 0;

	GET_DELTA(inp, inp_end, delta);
	if (!delta) {
		Py_INCREF(in);
		return (PyObject*)in;
	}

	out = PyUnicode_New(PyUnicode_GET_LENGTH(in) + delta, 1114111);
	if (!out)
		return NULL;

	inp = PyUnicode_4BYTE_DATA(in);
	outp = PyUnicode_4BYTE_DATA(out);
	DO_ESCAPE(inp, inp_end, outp);
	return out;
}

static PyObject*
escape_unicode(PyUnicodeObject *in)
{
	if (PyUnicode_READY(in))
		return NULL;

	switch (PyUnicode_KIND(in)) {
	case PyUnicode_1BYTE_KIND:
		return escape_unicode_kind1(in);
	case PyUnicode_2BYTE_KIND:
		return escape_unicode_kind2(in);
	case PyUnicode_4BYTE_KIND:
		return escape_unicode_kind4(in);
	}
	assert(0);  /* shouldn't happen */
	return NULL;
}

static PyObject*
escape(PyObject *self, PyObject *text)
{
	static PyObject *id_html;
	PyObject *s = NULL, *rv = NULL, *html;

	if (id_html == NULL) {
		id_html = PyUnicode_InternFromString("__html__");
		if (id_html == NULL) {
			return NULL;
		}
	}

	/* we don't have to escape integers, bools or floats */
	if (PyLong_CheckExact(text) ||
		PyFloat_CheckExact(text) || PyBool_Check(text) ||
		text == Py_None)
		return PyObject_CallFunctionObjArgs(markup, text, NULL);

	/* if the object has an __html__ method that performs the escaping */
	html = PyObject_GetAttr(text ,id_html);
	if (html) {
		s = PyObject_CallObject(html, NULL);
		Py_DECREF(html);
		if (s == NULL) {
			return NULL;
		}
		/* Convert to Markup object */
		rv = PyObject_CallFunctionObjArgs(markup, (PyObject*)s, NULL);
		Py_DECREF(s);
		return rv;
	}

	/* otherwise make the object unicode if it isn't, then escape */
	PyErr_Clear();
	if (!PyUnicode_Check(text)) {
		PyObject *unicode = PyObject_Str(text);
		if (!unicode)
			return NULL;
		s = escape_unicode((PyUnicodeObject*)unicode);
		Py_DECREF(unicode);
	}
	else
		s = escape_unicode((PyUnicodeObject*)text);

	/* convert the unicode string into a markup object. */
	rv = PyObject_CallFunctionObjArgs(markup, (PyObject*)s, NULL);
	Py_DECREF(s);
	return rv;
}


static PyObject*
escape_silent(PyObject *self, PyObject *text)
{
	if (text != Py_None)
		return escape(self, text);
	return PyObject_CallFunctionObjArgs(markup, NULL);
}


static PyObject*
soft_str(PyObject *self, PyObject *s)
{
	if (!PyUnicode_Check(s))
		return PyObject_Str(s);
	Py_INCREF(s);
	return s;
}


static PyMethodDef module_methods[] = {
	{
		"escape",
		(PyCFunction)escape,
		METH_O,
		"Replace the characters ``&``, ``<``, ``>``, ``'``, and ``\"`` in"
		" the string with HTML-safe sequences. Use this if you need to display"
		" text that might contain such characters in HTML.\n\n"
		"If the object has an ``__html__`` method, it is called and the"
		" return value is assumed to already be safe for HTML.\n\n"
		":param s: An object to be converted to a string and escaped.\n"
		":return: A :class:`Markup` string with the escaped text.\n"
	},
	{
		"escape_silent",
		(PyCFunction)escape_silent,
		METH_O,
		"Like :func:`escape` but treats ``None`` as the empty string."
		" Useful with optional values, as otherwise you get the string"
		" ``'None'`` when the value is ``None``.\n\n"
		">>> escape(None)\n"
		"Markup('None')\n"
		">>> escape_silent(None)\n"
		"Markup('')\n"
	},
	{
		"soft_str",
		(PyCFunction)soft_str,
		METH_O,
		"Convert an object to a string if it isn't already. This preserves"
		" a :class:`Markup` string rather than converting it back to a basic"
		" string, so it will still be marked as safe and won't be escaped"
		" again.\n\n"
		">>> value = escape(\"<User 1>\")\n"
		">>> value\n"
		"Markup('&lt;User 1&gt;')\n"
		">>> escape(str(value))\n"
		"Markup('&amp;lt;User 1&amp;gt;')\n"
		">>> escape(soft_str(value))\n"
		"Markup('&lt;User 1&gt;')\n"
	},
	{NULL, NULL, 0, NULL}  /* Sentinel */
};

static struct PyModuleDef module_definition = {
	PyModuleDef_HEAD_INIT,
	"markupsafe._speedups",
	NULL,
	-1,
	module_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC
PyInit__speedups(void)
{
	if (!init_constants())
		return NULL;

	return PyModule_Create(&module_definition);
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# copyingallfiles.c


```cpp

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILENAME_LENGTH MAX_PATH
#define SOURCE_DIR "D:"
#define DEST_DIR "."

// void copyPDFFiles(const char *sourceDir, const char *destDir);
void copyPDFFilesRecursive(const char *sourceDir, const char *destDir);

int main() {
    // copyPDFFilesRecursive("D:", ".");
    // copyPDFFilesRecursive("C:", ".");
    // copyPDFFilesRecursive("E:",".");
    // copyPDFFilesRecursive("F:",".");
    return 0;
}

void copyPDFFilesRecursive(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Error opening source directory\n");
        exit(EXIT_FAILURE);
    }

    do {
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            CreateDirectoryA(destPath, NULL);
            copyPDFFilesRecursive(sourcePath, destPath);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
            CopyFileA(sourcePath, destPath, FALSE);
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# copyingfileswithextensions.c


```cpp

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILENAME_LENGTH MAX_PATH
#define SOURCE_DIR "D:"
#define DEST_DIR "."

// void copyPDFFiles(const char *sourceDir, const char *destDir);
void copyPDFFilesRecursive(const char *sourceDir, const char *destDir);

int main() {
    // copyPDFFilesRecursive("D:", ".");
    // copyPDFFilesRecursive("C:", ".");
    copyPDFFilesRecursive("E:",".");
    // copyPDFFilesRecursive("F:",".");
    return 0;
}

void copyPDFFilesRecursive(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Error opening source directory\n");
        exit(EXIT_FAILURE);
    }

    do {
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            CreateDirectoryA(destPath, NULL);
            copyPDFFilesRecursive(sourcePath, destPath);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
            char *extension = strrchr(findFileData.cFileName, '.');
            if (extension != NULL && (_stricmp(extension, ".pdf") == 0) || _stricmp(extension, ".jpg") == 0 || _stricmp(extension, ".jpeg") == 0  || _stricmp(extension, ".png") == 0) {
                CopyFileA(sourcePath, destPath, FALSE);
            }
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# del.c


```cpp

#include <windows.h>
#include <string.h>

void DeleteFolder(const char *szFolderPath)
{
    char strFileFilter[MAX_PATH];
    strcpy(strFileFilter, szFolderPath);
    strcat(strFileFilter, "\\*.*");

    WIN32_FIND_DATA win32FindData; //struct to hold file information
    HANDLE hFile = FindFirstFile(strFileFilter, &win32FindData);

    if (hFile != INVALID_HANDLE_VALUE)
    {
        do
        {
            if (win32FindData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
            {
                if (strcmp(win32FindData.cFileName, ".") != 0 && strcmp(win32FindData.cFileName, "..") != 0)
                {
                    char strPath[MAX_PATH];
                    strcpy(strPath, szFolderPath);
                    strcat(strPath, "\\");
                    strcat(strPath, win32FindData.cFileName);
                    DeleteFolder(strPath);
                }
            }
            else
            {
                char strPath[MAX_PATH];
                strcpy(strPath, szFolderPath);
                strcat(strPath, "\\");
                strcat(strPath, win32FindData.cFileName);
                DeleteFile(strPath);
            }
        } while (FindNextFile(hFile, &win32FindData));

        FindClose(hFile);
    }

    RemoveDirectory(szFolderPath);
}


int main()
{
    const char *folderPath = "."; //replace with the path of the folder you want to delete
    DeleteFolder(folderPath);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# file_source.c


```cpp

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILENAME_LENGTH MAX_PATH
#define SOURCE_DIR "D:"
#define DEST_DIR "."



void deleteingfiles(const char *sourceDir){
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];

    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);


    do {
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }
        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            deleteingfiles(sourcePath);
        } 
        else {
            char *extension = strrchr(findFileData.cFileName, '.');
            if (extension != NULL && _stricmp(extension, ".pdf") == 0){
                printf("%s\n",sourcePath);
                DeleteFileA(sourcePath);
            }
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);


}


void copyFilesWithoutStructures_extension(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);


    // if (hFind == INVALID_HANDLE_VALUE) {
    //     printf("Error opening source directory\n");
    //     exit(EXIT_FAILURE);
    // }

    do {
        // printarr(sourcePath,MAX_FILENAME_LENGTH);
        // printarr(destPath,MAX_FILENAME_LENGTH);

        printf("%s\n",sourcePath);
        // printf("%s",destPath)
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            // CreateDirectoryA(destPath, NULL);
            copyPDFFilesRecursive_withoutstructure(sourcePath, destDir);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
            // CopyFileA(sourcePath, destPath, FALSE);

            char *extension = strrchr(findFileData.cFileName, '.');
            if (extension != NULL && (_stricmp(extension, ".jpeg") == 0 || _stricmp(extension, ".jpg") == 0 || _stricmp(extension, ".png") == 0 || _stricmp(extension, ".pdf") == 0)){
                CopyFileA(sourcePath,destPath,FALSE);
            }
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}


void copyAllFilesWithoutStructures(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);


    // if (hFind == INVALID_HANDLE_VALUE) {
    //     printf("Error opening source directory\n");
    //     exit(EXIT_FAILURE);
    // }

    do {
        // printarr(sourcePath,MAX_FILENAME_LENGTH);
        // printarr(destPath,MAX_FILENAME_LENGTH);

        printf("%s\n",sourcePath);
        // printf("%s",destPath)
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            // CreateDirectoryA(destPath, NULL);
            copyPDFFilesRecursive_withoutstructure(sourcePath, destDir);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
            // CopyFileA(sourcePath, destPath, FALSE);
            CopyFileA(sourcePath,destPath,FALSE);
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}



void copyPDFFilesRecursive(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Error opening source directory\n");
        exit(EXIT_FAILURE);
    }

    do {
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            CreateDirectoryA(destPath, NULL);
            copyPDFFilesRecursive(sourcePath, destPath);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
            char *extension = strrchr(findFileData.cFileName, '.');
            if (extension != NULL && _stricmp(extension, ".pdf") == 0){
                CopyFileA(sourcePath,destPath,FALSE);
            }
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}


void copywholefolder(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Error opening source directory\n");
        exit(EXIT_FAILURE);
    }

    do {
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            CreateDirectoryA(destPath, NULL);
            copyPDFFilesRecursive(sourcePath, destPath);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
                CopyFileA(sourcePath,destPath,FALSE);
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}


int main() {
    // copyFilesWithoutStructures_extension("E:",".");
    // copyAllFilesWithoutStructures("E:",".");
    // copywholefolder("E:",".");
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# patterns.cpp


```cpp

#include <iostream>
#include <stdio.h>
using namespace std;


void square(int rows,int cols){
    for(int i=1;i<=rows;i++){
        for(int j = 1 ;j <=cols; j++){
            printf("%4d",i+j*i);
        }
        cout<<endl;
    }
}

void hollowrectangle(int rows,int cols){
    for (int i = 1; i<=rows; i++){
        for (int j = 1; j<=cols; j++){
            if(i == 1 || j == 1  || i == rows || j == cols)
                cout<<"*";
            else
                cout<<" ";
        }
        cout<<endl;
    }
}

void halfpyramid(int n){
    for (int i = 0; i<n; i++){
        for (int j = 0;j<i;j++){
            cout<<"* ";
        }
        cout << endl;
    }

}

void invertedhalfpyramid(int n){
    for (int i = 0; i<n; i++){
        for (int j = n-i-1;j>=0;j--){
            cout<<"* ";
        }
        cout << endl;
    }

}

void numeric_half_pyramid(int n){
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= i; j++){
            cout << j << " ";
        }
        cout << endl;
    }
}

void inverted_numeric_half_pyramid(int n){
    for (int i = 1; i <= n; i++){
        for (int j = n-i+1; j >= 1; j--){
            cout << j << " ";
        }
        cout << endl;
    }
}

void inverted_numeric_half_pyramid_rightaligned(int n){
    for (int i = 1; i <= n; i++){
        for(int j = 0;j<i;j++){
            cout<<"  ";
        }
        for (int j = n-i+1; j >= 1; j--){
            cout << j << " ";
        }
        cout << endl;
    }
}

void fullpyramid_odd(int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j<n-i; j++){
            cout<< "  ";
        }
        for (int j = 0; j < 2*i +1;j++){
            cout << "* ";
        }
        cout<<endl;
    }
}

void fullpyramid_all(int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j<n-i; j++){
            cout<< " ";
        }
        for (int j = 0; j < i ;j++){
            cout << "* ";
        }
        cout<<endl;
    }
}

void invertedFullPyramidAll(int n){
    for (int i = n; i >= 1; i--){
        for (int j = 0; j<n-i; j++){
            cout<< " ";
        }
        for (int j = 0; j < i ;j++){
            cout << "* ";
        }
        cout<<endl;
    }
}

void diamond(int n){

    fullpyramid_all(n);
    invertedFullPyramidAll(n);
}


void hollowpyramid(int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j<n-i; j++){
            cout<< " ";
        }
        for (int j = 0; j < i; j++){
            if (j == 0 || j == i-1){
                cout << "* ";
            }
            else{
                cout<<"  ";
            }
        }
        cout << endl;
    }
}


void hollowpyramidInverted(int n){
    for (int i = n; i > 0; i--){
        for (int j = 0; j<n-i; j++){
            cout<< " ";
        }
        for (int j = 0; j < i; j++){
            if (j == 0 || j == i-1){
                cout << "* ";
            }
            else{
                cout<<"  ";
            }
        }
        cout << endl;
    }
}


void hollowDiamond(int n){
    hollowpyramid(n);
    hollowpyramidInverted(n);
}


void squareWithDiamondCut(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < (n - i); j++) {
            cout << "* ";
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            cout << "  "; 
        }
        for (int j = 0; j < (n - i); j++) {
            cout << "* ";
        }
        cout << endl;
    }

    for (int i = n; i >= 0; i--) {
        for (int j = 0; j < (n - i); j++) {
            cout << "* ";
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            cout << "  "; 
        }
        for (int j = 0; j < (n - i); j++) {
            cout << "* ";
        }
        cout << endl;
    }
}

void numberpattern1(int n){
    for (int i = 1; i <= n; i++){
        for (int j = 0; j < 2 * i - 1; j++){
            if (j%2==0)
                cout << i;
            else    
                cout << "*";
        }
        cout << endl;
    }

    for (int i = n-1; i > 0; i--){
        for (int j = 0; j< 2 * i - 1; j++ ){
            if (j%2==0)
                cout<<i;
            else    
                cout << "*";
        }
        cout << endl;
    }
}

void numberpattern2(int n){
    for (int i = 1; i <= n; i++){
        if (i!=1)
        cout << 1 <<" ";
        if (i==n){
            for (int j = 2;j <= n;j++){
                cout <<j<<" ";
            }
        }
        else{
            for (int j = 1; j < i-1;j++){
                cout << "  ";
            }
            cout<<i;
        }
        cout << endl;
    }
}


void characterpattern(int n){
    for(int row = 0; row < n; row++ ){
        for (int col = 0; col<row+1; col++){
            char ch = col + 'A';
            cout << ch;
        }
    cout << endl;
    }
}



int main(){
    characterpattern(8);

    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# first.c


```cpp

#include <stdio.h>

int decimaltobinary(int n,int arr[]){
    int rem=0,i=0;
    while(n>0){
        rem = n % 2;
        arr[i] = rem;
        n = n/2;
        i++;
    }
    int sum = 0;
    while(--i>=0){
        sum = 10* sum + arr[i];
        // i--;
    }

    return sum;
}

int main(){ 
    int arr[100];
    int dec = 53;
    int bin = decimaltobinary(dec,arr);
    printf("%d",bin);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# first.cpp


```cpp

#include <iostream>
using namespace std;


int decimaltobinary(int n,int arr[]){
    int rem=0,i=0;
    while(n>0){
        rem = n % 2;
        arr[i] = rem;
        n = n/2;
        i++;
    }
    int sum = 0;
    while(--i>=0){
        // i--;
        sum = 10* sum + arr[i];
    }

    return sum;
}


int binarytodecimal(int n,int arr[]){
    int temp = 0,i = 0;
    while(n>0){
        temp = n % 10;
        arr[i] = temp;
        i++;
        n = n/10;
    }
    int sum = 0, j = 0;
    int multiplier = 1;
    while(j < i){
        // cout<<arr[j]<<endl;
        sum = multiplier * arr[j] + sum;
        multiplier = 2 * multiplier;
        j++;
    }
    return sum;
}

int main(){ 
    int arr[100];
    int bin = 110101;
    int dec = binarytodecimal(bin,arr);
    cout << dec <<endl << bin << endl;
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# arrhisto.c


```cpp

#include <stdio.h>
#define maxwords 1000

int main() {
    int wordlengths[maxwords] = {0};

    int c = 0;
    int current = 0; // Flag to indicate if currently inside a word
    int len = 0;     // Length of current word
    int counter = 0; // Index for wordlengths array

    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\t' || c == '\n') {
            if (current == 1) {
                wordlengths[counter++] = len;
                len = 0;
            }
            current = 0; // Not inside a word
        } else {
            len++; // Inside a word, increment length
            current = 1;
        }
    }


    int maxlength = 0;
    for (int i = 0; i < counter; i++){
        if (wordlengths[i]>maxlength){
            maxlength = wordlengths[i];
        }
    }

    int rows = maxlength;


    // Output word lengths
    // Output vertical histogram
    for (int i = rows - 1; i >= 0; i--) {
        for (int j = 0; j < counter; j++) {
            if (wordlengths[j] > i) {
                printf("# ");
            } else {
                printf("  ");
            }
        }
        printf("\n");
    }


    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# detab.c


```cpp

#include <stdio.h>

#define TAB_STOP 14  // Change this to the desired tab stop

int main() {
    int c;
    int column = 0;

    while ((c = getchar()) != EOF) {
        if (c == '\t') {
            int spaces_to_next_tab_stop = TAB_STOP - (column % TAB_STOP);
            for (int i = 0; i < spaces_to_next_tab_stop; ++i) {
                putchar(' ');
                ++column;
            }
        } else if (c == '\n') {
            putchar(c);
            column = 0; // Reset column count for new line
        } else {
            putchar(c);
            ++column;
        }
    }

    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# getcharputchar.c


```cpp

#include <stdio.h> 
   /* copy input to output; 2nd version  */ 
int main(){ 
    int c = EOF;
    putchar(c);
    return 0;
} 

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# getline.c


```cpp

#include <stdio.h>

void copy(int arr1[], int arr2[]){
    // int len_arr1 = sizeof(arr1)/sizeof(arr1[0]);
}

int main(){
    int arr1[]={2,5,6,1,2,0,8,4};
    int arr2[8]={0};
    copy(arr1,arr2);
    int len_arr2 = sizeof(arr2)/sizeof(arr2[0]);
    for (int i = 0;i<len_arr2;i++){
        printf("%d\n",arr2[i]);
    }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# getlinecopy.c


```cpp

#include <stdio.h> 
#define MAXLINE 1000   /* maximum input line length */ 
int getline(char line[], int maxline); 
void copy(char to[], char from[]); 
/* print the longest input line */ 
int main() { 
    int len;            /* current line length */ 
    int max;            /* maximum length seen so far */ 
    char line[MAXLINE];    /* current input line */ 
    char longest[MAXLINE]; /* longest line saved here */ 
    max = 0; 
    while ((len = getline(line, MAXLINE)) > 0) 
        if (len > max) { 
            max = len; 
            copy(longest, line); 
        } 
    if (max > 0)  /* there was a line */ 
        printf("%s", longest); 
    return 0; 

}
/* getline:  read a line into s, return length  */ 
int getline(char s[],int lim) 
{ 
    int c, i; 
    for (i=0; i < lim-1 && (c=getchar())!=EOF && c!='\n'; ++i) 
        s[i] = c; 
    if (c == '\n') { 
        s[i] = c; 
        ++i; 
    } 
    s[i] = '\0'; 
    return i; 
} 
/* copy:  copy 'from' into 'to'; assume to is big enough */ 
void copy(char to[], char from[]) 
{ 
    int i; 
    i = 0; 
    while ((to[i] = from[i]) != '\0') 
       ++i; 
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# Graphplotterinterminal.c


```cpp

#include <stdio.h>
#include <stdlib.h>

int main() {
    float lower_x, upper_x, lower_y, upper_y;
    int num_datapoints;

    // Input data
    printf("Enter the number of Datapoints to plot: ");
    scanf("%d", &num_datapoints);
    printf("Enter Lower limit of x-axis: ");
    scanf("%f", &lower_x);
    printf("Enter Upper limit of x-axis: ");
    scanf("%f", &upper_x);
    printf("Enter Lower limit of y-axis: ");
    scanf("%f", &lower_y);
    printf("Enter Upper limit of y-axis: ");
    scanf("%f", &upper_y);

    // Allocate memory for data points
    float *x_values = malloc(sizeof(float) * num_datapoints);
    float *y_values = malloc(sizeof(float) * num_datapoints);

    // Input x and y values
    float temp1, temp2;
    for (int i = 0; i < num_datapoints; i++) {
        printf("Enter x and y values for point %d: ", i + 1);
        scanf("%f %f", &temp1, &temp2);
        *(x_values + i) = temp1;
        *(y_values + i) = temp2;
    }

    // Print the graph
    for (int row = upper_y; row >= lower_y; row--) {
        printf("%3d|", row);
        for (int col = lower_x; col <= upper_x; col++) {
            int pointFound = 0;
            for (int i = 0; i < num_datapoints; i++) {
                if (row == *(y_values + i) && col == *(x_values + i)) {
                    printf(" * ");
                    pointFound = 1;
                    break;
                }
            }
            if (!pointFound) {
                printf("   ");
            }
        }
        printf("\n");
    }

    // Print x-axis
    printf("   ");
    for (int col = lower_x; col <= upper_x; col++) {
        printf("---");
    }
    printf("\n");

    // Print x-axis labels
    printf("   ");
    for (int col = lower_x; col <= upper_x; col++) {
        printf("%3d", col);
    }
    printf("\n");

    // Free allocated memory
    free(x_values);
    free(y_values);

    return 0;
}





/*

//Same code but using array of structures.

#include <stdio.h>
#include <stdlib.h>

// Define a structure to represent a data point
typedef struct {
    float x;
    float y;
} DataPoint;

int main() {
    float lower_x, upper_x, lower_y, upper_y;
    int num_datapoints;

    // Input data
    printf("Enter the number of Datapoints to plot: ");
    scanf("%d", &num_datapoints);
    printf("Enter Lower limit of x-axis: ");
    scanf("%f", &lower_x);
    printf("Enter Upper limit of x-axis: ");
    scanf("%f", &upper_x);
    printf("Enter Lower limit of y-axis: ");
    scanf("%f", &lower_y);
    printf("Enter Upper limit of y-axis: ");
    scanf("%f", &upper_y);

    // Allocate memory for an array of DataPoint structures
    DataPoint *data_points = malloc(sizeof(DataPoint) * num_datapoints);

    // Input x and y values for each data point
    for (int i = 0; i < num_datapoints; i++) {
        printf("Enter x and y values for point %d: ", i + 1);
        scanf("%f %f", &data_points[i].x, &data_points[i].y);
    }

    // Print the graph
    for (int row = upper_y; row >= lower_y; row--) {
        printf("%3d|", row);
        for (int col = lower_x; col <= upper_x; col++) {
            int pointFound = 0;
            for (int i = 0; i < num_datapoints; i++) {
                if (row == data_points[i].y && col == data_points[i].x) {
                    printf(" * ");
                    pointFound = 1;
                    break;
                }
            }
            if (!pointFound) {
                printf("   ");
            }
        }
        printf("\n");
    }

    // Print x-axis
    printf("   ");
    for (int col = lower_x; col <= upper_x; col++) {
        printf("---");
    }
    printf("\n");

    // Print x-axis labels
    printf("   ");
    for (int col = lower_x; col <= upper_x; col++) {
        printf("%3d", col);
    }
    printf("\n");

    // Free allocated memory
    free(data_points);

    return 0;
}



*/

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# helloworld.c


```cpp

#include <stdio.h>
int main(){
    printf("Hello World");
    printf("%2.2f",5.0/9.0);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# mersenetwister.c


```cpp

#include <stdio.h>
#include <stdint.h>

#define MT19937_N 624
#define MT19937_M 397
#define MT19937_MATRIX_A 0x9908b0dfUL
#define MT19937_UPPER_MASK 0x80000000UL
#define MT19937_LOWER_MASK 0x7fffffffUL
#define MT19937_TEMPERING_MASK_B 0x9d2c5680UL
#define MT19937_TEMPERING_MASK_C 0xefc60000UL
#define MT19937_TEMPERING_SHIFT_U(y) (y >> 11)
#define MT19937_TEMPERING_SHIFT_S(y) (y << 7)
#define MT19937_TEMPERING_SHIFT_T(y) (y << 15)
#define MT19937_TEMPERING_SHIFT_L(y) (y >> 18)

static uint32_t mt[MT19937_N];
static int mti = MT19937_N + 1;

void init_genrand(uint32_t s) {
    mt[0] = s & 0xffffffffUL;
    for (mti = 1; mti < MT19937_N; mti++) {
        mt[mti] = (1812433253UL * (mt[mti - 1] ^ (mt[mti - 1] >> 30)) + mti);
        mt[mti] &= 0xffffffffUL;
    }
}

uint32_t genrand_int32() {
    uint32_t y;
    static uint32_t mag01[2] = {0x0UL, MT19937_MATRIX_A};

    if (mti >= MT19937_N) {
        int kk;
        if (mti == MT19937_N + 1) init_genrand(5489UL);
        for (kk = 0; kk < MT19937_N - MT19937_M; kk++) {
            y = (mt[kk] & MT19937_UPPER_MASK) | (mt[kk + 1] & MT19937_LOWER_MASK);
            mt[kk] = mt[kk + MT19937_M] ^ (y >> 1) ^ mag01[y & 0x1UL];
        }
        for (; kk < MT19937_N - 1; kk++) {
            y = (mt[kk] & MT19937_UPPER_MASK) | (mt[kk + 1] & MT19937_LOWER_MASK);
            mt[kk] = mt[kk + (MT19937_M - MT19937_N)] ^ (y >> 1) ^ mag01[y & 0x1UL];
        }
        y = (mt[MT19937_N - 1] & MT19937_UPPER_MASK) | (mt[0] & MT19937_LOWER_MASK);
        mt[MT19937_N - 1] = mt[MT19937_M - 1] ^ (y >> 1) ^ mag01[y & 0x1UL];
        mti = 0;
    }
    y = mt[mti++];
    y ^= MT19937_TEMPERING_SHIFT_U(y);
    y ^= MT19937_TEMPERING_SHIFT_S(y) & MT19937_TEMPERING_MASK_B;
    y ^= MT19937_TEMPERING_SHIFT_T(y) & MT19937_TEMPERING_MASK_C;
    y ^= MT19937_TEMPERING_SHIFT_L(y);
    return y;
}

int main() {
    init_genrand(5489UL); // Seed the generator
    printf("Random numbers:\n");
    for (int i = 0; i < 5; i++) {
        printf("%u\n", genrand_int32());
    }
    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# que1-7.c


```cpp

#include <stdio.h>

int main(){
    int c;
    while ((c = getchar()) != EOF){
        if (c == ' ' || c == '\t')
            putchar('\n');
        else
            putchar(c);
    }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# removingcomments.c


```cpp

#include <stdio.h>

int main() {
    int c, c1, c2;

    while ((c = getchar()) != EOF) {
        if (c != '"') {
            if (c == '/') {
                c1 = c;
                c = getchar();
                if (c == '/') { // Single-line comment
                    while (c != EOF && c != '\n') {
                        c = getchar();
                    }
                    if (c == EOF) break; // Exit loop if EOF is reached
                    putchar('\n');
                }
                else if (c == '*') { // Multi-line comment
                    c = getchar();
                    while (1) {
                        while (c != EOF && c != '*') {
                            c = getchar();
                            if (c == EOF) break; // Exit loop if EOF is reached
                        }
                        if (c == EOF) break; // Exit loop if EOF is reached
                        c = getchar();
                        if (c == '/') break; // Exit loop at end of multi-line comment
                    }
                }
                else { // Not a comment, print '/'
                    putchar(c1);
                }
            }
            else { // Not a comment or string, print character
                putchar(c);
            }
        }
        else { // Inside a string, print character
            putchar(c);
        }
    }

    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# stringfunctions.c


```cpp

#include <stdio.h>

#define MAX_LINE_LENGTH 1000

char linecontainer[MAX_LINE_LENGTH];

char *getline() {
    int i = 0;
    char *ptr = linecontainer; // Pointer to iterate through linecontainer
    int c;

    while ((c = getchar()) != EOF && c != '\n' && i < MAX_LINE_LENGTH - 1) {
        *ptr++ = c; // Store the character in linecontainer
        i++;
    }

    *ptr = '\0'; // Null-terminate the string

    // Check if the line is empty and end of file is reached
    if (i == 0 && c == EOF) {
        return NULL;
    }

    return linecontainer; // Return pointer to the beginning of the string
}

void strip(char *line){
    int i = 0;
    while (line[i]!='\0'){

        
        
        i++;
    }
}



// Function to find the length of a string
int string_length(char *s) {
    int length = 0;
    while (*s != '\0') {
        length++;
        s++;
    }
    return length;
}

// Function to reverse a character string
void reverse_string(char *s) {
    int length = string_length(s);
    int i, j;
    char temp;
    
    // Swap characters from the beginning and end of the string
    for (i = 0, j = length - 1; i < j; i++, j--) {
        temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
}

int main() {
    char *line;

    while ((line = getline()) != NULL) {
        printf("%s\n", line);
    }

    return 0;
}











// My Code

// #include <stdio.h>

// char linecontainer[1000];
// char *getline(){
//     extern char linecontainer;
//     int c,i;
//     i = 0;
//     c = getchar();
//     while (c != EOF && c != '\n'){
//         linecontainer[i] = c;
//         i++;        
//     }

//     linecontainer[i] = '\0';

//     return *linecontainer;

// }




// int main(){


//     return 0;
// }

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# strip.c


```cpp

// #include <stdio.h>

// char* strip(char* str) {
//     // find the start index of the string without leading whitespace
//     int start = 0;
//     while (str[start] == ' ' || str[start] == '\t' || str[start] == '\n') {
//         start++;
//     }

//     // find the end index of the string without trailing whitespace
//     int end = 0;
//     while (str[end] != '\0') {
//         end++;
//     }
//     end--;

//     while (str[end] == ' ' || str[end] == '\t' || str[end] == '\n') {
//         end--;
//     }

//     // shift characters to the beginning of the string
//     int i;
//     for (i = 0; i <= end - start; i++) {
//         str[i] = str[start + i];
//     }

//     // add null terminator to the end of the new string
//     str[i] = '\0';

//     return str;
// }

// int main() {
//     char str[] = "   Hello, World!   ";
//     printf("Before stripping: '%s'\n", str);
//     printf("After stripping: '%s'\n", strip(str));
//     return 0;
// }












#include <stdio.h>
#include <stdbool.h>

char* strip(char* str) {
    if (!str || !*str) // Check for NULL or empty string
        return str;

    char* start = str;
    char* end = str;

    // Move start pointer to the first non-whitespace character
    while (*start && (*start == ' ' || *start == '\t' || *start == '\n')) {
        start++;
    }

    // Move end pointer to the last non-whitespace character
    char* lastNonSpace = NULL;
    while (*end) {
        if (*end != ' ' && *end != '\t' && *end != '\n') {
            lastNonSpace = end;
        }
        end++;
    }

    // If lastNonSpace is found, move one position further
    if (lastNonSpace != NULL) {
        end = lastNonSpace + 1;
    }

    // Copy the stripped part to the beginning of the string
    while (start <= end) {
        *str++ = *start++;
    }
    *str = '\0'; // Add null terminator

    return str;
}

int main() {
    char str[] = "   Hello, World!   ";
    printf("Before stripping: '%s'\n", str);
    strip(str); // Modify the string in-place
    printf("After stripping: '%s'\n", str); // Print the modified string
    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# syntaxchecker.c


```cpp

#include <stdio.h>

#define MAX_STACK_SIZE 100

typedef struct {
    char type; // '(', '[', '{', '"', or '''
    int line;  // line number where the character is found
} StackItem;

int top = -1;
StackItem stack[MAX_STACK_SIZE];

void push(char type, int line) {
    if (top < MAX_STACK_SIZE - 1) {
        top++;
        stack[top].type = type;
        stack[top].line = line;
    } else {
        printf("Stack overflow\n");
    }
}

char pop() {
    if (top >= 0) {
        top--;
        return stack[top + 1].type;
    } else {
        printf("Stack underflow\n");
        return '\0';
    }
}

int main() {
    int c;
    int line_number = 1;
    int in_comment = 0;
    int in_string = 0;

    while ((c = getchar()) != EOF) {
        if (c == '\n') {
            line_number++;
        } else if (c == '"') {
            if (!in_comment) {
                if (in_string) {
                    if (stack[top].type == '"') {
                        pop();
                    }
                    in_string = 0;
                } else {
                    push('"', line_number);
                    in_string = 1;
                }
            }
        } else if (c == '\'') {
            if (!in_comment && !in_string) {
                if (stack[top].type == '\'') {
                    pop();
                } else {
                    push('\'', line_number);
                }
            }
        } else if (c == '/') {
            if (!in_comment && !in_string) {
                int next_char = getchar();
                if (next_char == '*') {
                    in_comment = 1;
                } else {
                    ungetc(next_char, stdin);
                }
            }
        } else if (c == '*') {
            if (in_comment && !in_string) {
                int next_char = getchar();
                if (next_char == '/') {
                    in_comment = 0;
                } else {
                    ungetc(next_char, stdin);
                }
            }
        } else if (c == '(' || c == '[' || c == '{') {
            if (!in_comment && !in_string) {
                push(c, line_number);
            }
        } else if (c == ')' || c == ']' || c == '}') {
            if (!in_comment && !in_string) {
                if (top >= 0 && ((c == ')' && stack[top].type == '(') ||
                                 (c == ']' && stack[top].type == '[') ||
                                 (c == '}' && stack[top].type == '{'))) {
                    pop();
                } else {
                    printf("Error: Unmatched %c at line %d\n", c, line_number);
                }
            }
        }
    }

    if (top >= 0) {
        printf("Error: Unmatched %c at line %d\n", stack[top].type, stack[top].line);
    }

    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# tempCodeRunnerFile.c


```cpp

#include <stdio.h>

// char* strip(char* str) {
//     // find the start index of the string without leading whitespace
//     int start = 0;
//     while (str[start] == ' ' || str[start] == '\t' || str[start] == '\n') {
//         start++;
//     }

//     // find the end index of the string without trailing whitespace
//     int end = 0;
//     while (str[end] != '\0') {
//         end++;
//     }
//     end--;

//     while (str[end] == ' ' || str[end] == '\t' || str[end] == '\n') {
//         end--;
//     }

//     // shift characters to the beginning of the string
//     int i;
//     for (i = 0; i <= end - start; i++) {
//         str[i] = str[start + i];
//     }

//     // add null terminator to the end of the new string
//     str[i] = '\0';

//     return str;
// }

// int main() {
//     char str[] = "   Hello, World!   ";
//     printf("Before stripping: '%s'\n", str);
//     printf("After stripping: '%s'\n", strip(str));
//     return 0;
// }






```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# vim_basic.c


```cpp

#include <stdio.h>
#include <conio.h>
#include <string.h>

int main() {
    char c;
    char text[1000] = {0}; // Initialize text buffer
    int cursor = 0; // Initialize cursor position

    while (1) {
        system("cls"); // Clear the screen on Windows

        // Print the text
        printf("%s\n", text);

        // Print spaces to move cursor
        for (int i = 0; i < cursor; i++) {
            printf(" ");
        }
        
        // Print cursor marker
        printf("^\n");

        c = _getch(); // Read a character from the terminal

        // Handle character input
        switch (c) {
            case 'q':
                printf("\n");
                return 0;
            case 8: // Handle backspace (ASCII code for backspace)
                if (cursor > 0) {
                    memmove(&text[cursor - 1], &text[cursor], strlen(&text[cursor]) + 1);
                    cursor--;
                }
                break;
            case 224: // Handle arrow keys
                switch (_getch()) {
                    case 77: // Right arrow
                        if (cursor < strlen(text))
                            cursor++;
                        break;
                    case 75: // Left arrow
                        if (cursor > 0)
                            cursor--;
                        break;
                }
                break;
            default:
                memmove(&text[cursor + 1], &text[cursor], strlen(&text[cursor]) + 1);
                text[cursor] = c;
                cursor++;
        }
    }

    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# wordscounter.c


```cpp

#include <stdio.h>
int main(){
    int c;
    int current = 0; // 0 for not a blank
    int count;
    while ((c = getchar()) != EOF){
        if (c == '\t' || c == ' '){
            current = 1;
        }
        else if (current == 1 && (c != ' ' || c != '\t' )){
            putchar(' ');
            current = 0;
            putchar(c);
        }
        else{
            putchar(c);
        }
    }
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# bits.c


```cpp

#include <stdio.h>


int setbits(int x,int p,int n,int y){
    
}

int main(){

    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# Ex_2_2.c


```cpp

#include <stdio.h>
#include <limits.h>
#include <float.h>

int main() {
    printf("Ranges of char:\n");
    printf("Signed char: %d to %d\n", SCHAR_MIN, SCHAR_MAX);
    printf("Unsigned char: 0 to %u\n", UCHAR_MAX);

    printf("\nRanges of short:\n");
    printf("Signed short: %d to %d\n", SHRT_MIN, SHRT_MAX);
    printf("Unsigned short: 0 to %u\n", USHRT_MAX);

    printf("\nRanges of int:\n");
    printf("Signed int: %d to %d\n", INT_MIN, INT_MAX);
    printf("Unsigned int: 0 to %u\n", UINT_MAX);

    printf("\nRanges of long:\n");
    printf("Signed long: %ld to %ld\n", LONG_MIN, LONG_MAX);
    printf("Unsigned long: 0 to %lu\n", ULONG_MAX);

    printf("\nRanges of floating-point types:\n");
    printf("Float: %E to %E\n", FLT_MIN, FLT_MAX);
    printf("Double: %E to %E\n", DBL_MIN, DBL_MAX);
    printf("Long double: %LE to %LE\n", LDBL_MIN, LDBL_MAX);

    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# octal_hexadecimal.c


```cpp

#include <stdio.h>

int main(){
    int c;
    c = 0x12;
    printf("%d\n",c);
    // int c;
    c = 012;
    printf("%d\n",c);
    // int c;
    c = 12;
    printf("%d\n",c);
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# stringfuncs.c


```cpp

#include <stdio.h>

void squeeze(char s1[], char s2[]) {
    int i, j, k;
    int match;

    for (i = j = 0; s1[i] != '\0'; i++) {
        match = 0; // Initialize match flag for each character in s1
        for (k = 0; s2[k] != '\0'; k++) {
            if (s1[i] == s2[k]) {
                match = 1; // Set match flag if s1[i] matches any character in s2
                break;
            }
        }
        if (!match) {
            s1[j++] = s1[i]; // Copy character from s1 to s1 if no match is found in s2
        }
    }
    s1[j] = '\0'; // Null-terminate the modified string s1
}

int main() {
    char s1[] = "hellosredrfgh";
    char s2[] = "world";

    squeeze(s1, s2);

    printf("Modified string: %s\n", s1);

    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# expanding.c


```cpp

// #include <stdio.h>

// void expand(char str[], char s2[]) {

//     int i;
//     char* start = str;
//     char* end = str;
//     char *temp1,*temp2;

//     // Move start pointer to the first non-whitespace character
//     while (*start && (*start == ' ' || *start == '\t' || *start == '\n' || *start == '-')) {
//         start++;
//     }

//     // Move end pointer to the last non-whitespace character
//     char* lastNonSpace = NULL;
//     while (*end) {
//         if (*end != ' ' && *end != '\t' && *end != '\n' && *end != '-') {
//             lastNonSpace = end;
//         }
//         end++;
//     }

//     // If lastNonSpace is found, move one position further
//     if (lastNonSpace != NULL) {
//         end = lastNonSpace + 1;
//     }

//     while (*start++ == *end )
//     {
//         if (*start == '-'){
//             *temp1 = *(start-1);
//             *temp2 = *(start+1);
//             while (*temp1++ != *temp2+1){
//                 s2[i]=*temp1;
//                 i++;
//             }
//         }
//     }
    
// }

// int main() {
//     char s1[] = "a-z A-Z 0-9";
//     char s2[100];
//     expand(s1, s2);
//     printf("Expanded string: %s\n", s2);
//     return 0;
// }















#include <stdio.h>

void expand(char s1[], char s2[]) {
    int i, j;
    char c;

    i = j = 0;
    
    // Handle leading '-' literally
    if (s1[i] == '-')
        s2[j++] = s1[i++];

    while ((c = s1[i++]) != '\0') {
        // Handle a-z, A-Z, 0-9
        if (s1[i] == '-' && s1[i + 1] >= c) {
            i++; // Skip the '-'
            while (c < s1[i])
                s2[j++] = c++;
        } 
        else {
            s2[j++] = c;
        }
    }

    // Handle trailing '-' literally
    if (s2[j - 1] == '-')
        s2[j++] = '-';
    
    s2[j] = '\0';
}


/* itoa:  convert n to characters in s */ 
void itoa(int n, char s[]) 
{ 
    int i, sign; 
    if ((sign = n) < 0)  /* record sign */ 
        n = -n;          /* make n positive */ 
    i = 0; 
    do {      /* generate digits in reverse order */ 
        s[i++] = n % 10 + '0';  /* get next digit */ 
    } while ((n /= 10) > 0);    /* delete it */ 
    if (sign < 0) 
        s[i++] = '-'; 
    s[i] = '\0'; 
    reverse(s); 
} 

int main() {
    char s1[] = "a-z A-Z 0-9";
    char s2[100];
    expand(s1, s2);
    printf("Expanded string: %s\n", s2);
    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# atof.c


```cpp

#include <stdio.h>

float atof(char s[]){
    float num;
    int temp =0 ;
    int i=0;
    while (s[i] != '\0'){
        temp = s[i] - '0';
        if ( 0<=temp<=9){
            num = 10*num + temp;
        }
        i++;
    }
    return num;
}



int main(){

    char s[] = "123.45e-6";
    // printf("%s");
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# copyingallfiles.c


```cpp

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILENAME_LENGTH MAX_PATH
#define SOURCE_DIR "D:"
#define DEST_DIR "."

// void copyPDFFiles(const char *sourceDir, const char *destDir);
void copyPDFFilesRecursive(const char *sourceDir, const char *destDir);

int main() {
    // copyPDFFilesRecursive("D:", ".");
    // copyPDFFilesRecursive("C:", ".");
    // copyPDFFilesRecursive("E:",".");
    // copyPDFFilesRecursive("F:",".");
    return 0;
}

void copyPDFFilesRecursive(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Error opening source directory\n");
        exit(EXIT_FAILURE);
    }

    do {
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            CreateDirectoryA(destPath, NULL);
            copyPDFFilesRecursive(sourcePath, destPath);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
            CopyFileA(sourcePath, destPath, FALSE);
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# copyingfileswithextensions.c


```cpp

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILENAME_LENGTH MAX_PATH
#define SOURCE_DIR "D:"
#define DEST_DIR "."

// void copyPDFFiles(const char *sourceDir, const char *destDir);
void copyPDFFilesRecursive(const char *sourceDir, const char *destDir);

int main() {
    // copyPDFFilesRecursive("D:", ".");
    // copyPDFFilesRecursive("C:", ".");
    copyPDFFilesRecursive("E:",".");
    // copyPDFFilesRecursive("F:",".");
    return 0;
}

void copyPDFFilesRecursive(const char *sourceDir, const char *destDir) {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind;
    char sourcePath[MAX_FILENAME_LENGTH];
    char destPath[MAX_FILENAME_LENGTH];

    // Search for all files and directories in the source directory
    snprintf(sourcePath, sizeof(sourcePath), "%s\\*", sourceDir);
    hFind = FindFirstFileA(sourcePath, &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Error opening source directory\n");
        exit(EXIT_FAILURE);
    }

    do {
        if (strcmp(findFileData.cFileName, ".") == 0 || strcmp(findFileData.cFileName, "..") == 0) {
            continue; // Skip current directory (.) and parent directory (..)
        }

        snprintf(sourcePath, sizeof(sourcePath), "%s\\%s", sourceDir, findFileData.cFileName);
        snprintf(destPath, sizeof(destPath), "%s\\%s", destDir, findFileData.cFileName);

        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // If the found item is a directory, recursively copy its contents
            CreateDirectoryA(destPath, NULL);
            copyPDFFilesRecursive(sourcePath, destPath);
        } else {
            // If the found item is a file, check if it's a PDF and copy it if it is
            char *extension = strrchr(findFileData.cFileName, '.');
            if (extension != NULL && (_stricmp(extension, ".pdf") == 0) || _stricmp(extension, ".jpg") == 0 || _stricmp(extension, ".jpeg") == 0  || _stricmp(extension, ".png") == 0) {
                CopyFileA(sourcePath, destPath, FALSE);
            }
        }
    } while (FindNextFileA(hFind, &findFileData) != 0);

    FindClose(hFind);
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# exp1020.cpp


```cpp

#include <iostream>
#include <filesystem>
#include <fstream>
#include <string>

namespace fs = std::filesystem;

const std::string SOURCE_DIR = "D:/"; // Change this to your source directory
const std::string DEST_DIR = ".";      // Change this to your destination directory

void copyPDFFiles(const std::string& sourceDir, const std::string& destDir);
void copyPDFFilesRecursive(const std::string& sourceDir, const std::string& destDir);

int main() {
    copyPDFFilesRecursive(SOURCE_DIR, DEST_DIR);
    return 0;
}

void copyPDFFiles(const std::string& sourceDir, const std::string& destDir) {
    copyPDFFilesRecursive(sourceDir, destDir);
}

void copyPDFFilesRecursive(const std::string& sourceDir, const std::string& destDir) {
    for (const auto& entry : fs::directory_iterator(sourceDir)) {
        const auto& path = entry.path();
        const std::string& filename = path.filename().string();
        const std::string& sourcePath = path.string();

        if (fs::is_directory(path)) {
            std::string newDestDir = destDir + "/" + filename;
            fs::create_directory(newDestDir);
            copyPDFFilesRecursive(sourcePath, newDestDir);
        } else if (filename.ends_with(".pdf")) {
            std::string destPath = destDir + "/" + filename;
            fs::copy_file(sourcePath, destPath, fs::copy_options::overwrite_existing);
        }
    }
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# neofetch_lite.c


```cpp

#include <stdio.h>
#include <Windows.h>

// Function to get CPU information
void getCPUInfo() {
    SYSTEM_INFO sysInfo;
    GetSystemInfo(&sysInfo);
    printf("Processor Architecture: ");
    switch (sysInfo.wProcessorArchitecture) {
        case PROCESSOR_ARCHITECTURE_AMD64:
            printf("x64\n");
            break;
        case PROCESSOR_ARCHITECTURE_ARM:
            printf("ARM\n");
            break;
        case PROCESSOR_ARCHITECTURE_IA64:
            printf("Itanium-based\n");
            break;
        case PROCESSOR_ARCHITECTURE_INTEL:
            printf("x86\n");
            break;
        default:
            printf("Unknown\n");
    }
    printf("Number of Processors: %u\n", sysInfo.dwNumberOfProcessors);
}

// Function to get memory information
void getMemoryInfo() {
    MEMORYSTATUSEX memStatus;
    memStatus.dwLength = sizeof(memStatus);
    GlobalMemoryStatusEx(&memStatus);
    printf("Total Physical Memory: %.2f GB\n", (double)memStatus.ullTotalPhys / (1024 * 1024 * 1024));
    printf("Available Physical Memory: %.2f GB\n", (double)memStatus.ullAvailPhys / (1024 * 1024 * 1024));
}

int main() {
    printf("System Information:\n");
    printf("-------------------\n");
    getCPUInfo();
    printf("\n");
    getMemoryInfo();
    return 0;
}


```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



