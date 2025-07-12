# exp1010.c


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

#include <stdio.h>

int main(){

    
    return 0;
}

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# first.c


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c


        // printf("%c",C[1]);
        // printf("%c",C[2]);

```

****************************************************************************************************
****************************************************************************************************
****************************************************************************************************



# justchill.c


```c

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



# _test_extension.c


```c

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



# _speedups.c


```c

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


```c

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


```c

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


```c

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


```c

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



# first.c


```c

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



# arrhisto.c


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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


```c

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



# neofetch_lite.c


```c

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



