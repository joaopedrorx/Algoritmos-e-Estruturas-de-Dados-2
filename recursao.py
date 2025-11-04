#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ContarDigitosRecursivo 

Este script implementa a função recursiva `contar_digitos(n)` e pode ser
executado no terminal. Aceita um argumento opcional (inteiro) ou solicita
entrada interativa se nenhum argumento for informado.
"""

import sys


def contar_digitos(n: int) -> int:
    """Retorna a quantidade de dígitos do inteiro n (usa valor absoluto).

    - n: inteiro (pode ser negativo)
    - retorna: número de dígitos (>= 1)
    """
    num_abs = abs(n)
    if num_abs < 10:
        return 1
    return 1 + contar_digitos(num_abs // 10)


def parse_int(s: str) -> int:
    """Tenta converter a string em inteiro. Lança ValueError se inválido.

    Rejeita entradas não-inteiras (por ex., floats) mantendo o comportamento
    esperado do pseudocódigo original.
    """
    # int() já lança ValueError para valores inválidos ou floats com ponto
    return int(s)


def main(argv=None):
    argv = argv if argv is not None else sys.argv

    # Se houver um argumento posicional, usa-o
    if len(argv) >= 2:
        s = argv[1]
        try:
            n = parse_int(s)
        except ValueError:
            print(f'Entrada inválida: "{s}" não é um inteiro.')
            return 1
        qtd = contar_digitos(n)
        print(f'O número {n} tem {qtd} dígito(s).')
        return 0

    # Interativo: solicitar ao usuário
    try:
        s = input('Digite um número inteiro (positivo ou negativo): ').strip()
    except (EOFError, KeyboardInterrupt):
        print('\nEntrada cancelada.')
        return 1

    if s == '':
        print('Por favor, informe um número inteiro.')
        return 1

    try:
        n = parse_int(s)
    except ValueError:
        print(f'Entrada inválida: "{s}" não é um inteiro.')
        return 1

    qtd = contar_digitos(n)
    print(f'O número {n} tem {qtd} dígito(s).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
