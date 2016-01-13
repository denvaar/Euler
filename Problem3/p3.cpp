#include <iostream>
//
//The prime factors of 13195 are 5, 7, 13 and 29.
//What is the largest prime factor of the number 600851475143 ?
//
int main(int argc, char *argv[]) {

    int i = 2;
    unsigned long long n = 600851475143;
    unsigned long long total = 1;

    while (i < n) {
        if (n % i == 0) {
            total = total * i;
            if (total >= n) break;
        }
        i++;
    }
    
    std::cout << i << std::endl;

    return 0;
}
