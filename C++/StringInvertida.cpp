#include <iostream>
#include <string>

int main() {
    std::cout << "Insira algum texto... ";
    std::string input;
    std::getline(std::cin, input);

    std::string reversed = "";
    for (int i = input.length() - 1; i >= 0; --i) {
        reversed += input[i];
    }

    std::cout << "Texto invertido: " << reversed << std::endl;

    return 0;
}
