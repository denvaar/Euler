#include <iostream>
#include <vector>

int main(int argc, char **argv) {

    // Declare a vector to hold fib. numbers.
    std::vector<int> fibNumbers;
    std::vector<int> evens;
    fibNumbers.push_back(1);
    fibNumbers.push_back(2);
    int i = 3;
    int sum = 2;
    // Loop 4 million times.
    while (i < 4000000) {
        if ((i % 2) == 0) {
            evens.push_back(i);
            sum += i;
        }
        fibNumbers.push_back(i);
        i = (fibNumbers.end()[-2] + fibNumbers.end()[-1]);
    }

    std::cout << sum << std::endl;
    
    return 0;
}
