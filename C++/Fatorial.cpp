#include <iostream>

using namespace std;

int main() {
    int numero;

    cout << "Escreva um numero inteiro positivo: ";
    cin >> numero;

    if (numero < 0) {
        cout << "Por favor, insira um numero inteiro positivo..." << endl;
        return 1;
    }

    unsigned long long fatorial = 1;
    for (int i = 1; i <= numero; ++i) {
        fatorial *= i;
    }

    cout << "O fatorial de " << numero << " e: " << fatorial << endl;

    return 0;
}
