#include <iostream>
using namespace std;

int main() {
    double salarioAtual, percentualReajuste, novoSalario;

    cout << "Escreva o salario mensal atual: ";
    cin >> salarioAtual;

    cout << "Escreva o percentual de reajuste: ";
    cin >> percentualReajuste;

    novoSalario = salarioAtual + (salarioAtual * percentualReajuste / 100.0);

    cout << "O novo salario apos o reajuste é: " << novoSalario << endl;

    return 0;
}