# conta_bancaria_dio
Abordando conceitos de lógica de programação além de conceitos financeiros e de segurança, com estruturas básicas de Python  "Criando um Sistema Bancário com Python" propõe o desenvolvimento de software financeiro para atender ao desafio de código da DIO.
Este sistema propõe-se a ser uma simulação simplificada de um sistema bancário com operações básicas que um cliente pode realizar em sua conta. As funcionalidades incluem:

Saque: Permite ao cliente retirar uma quantia de dinheiro da sua conta, respeitando um limite de até 3 saques diários e um valor máximo por saque de 500 unidades monetárias. Caso as condições não sejam atendidas (por exemplo, se o valor solicitado for superior ao saldo disponível, superior ao limite por saque, ou um número inválido), o sistema exibe uma mensagem de erro apropriada.

Depósito: Permite ao cliente adicionar uma quantia de dinheiro à sua conta. O sistema verifica se o valor inserido é válido (maior que 0) antes de efetuar o depósito e atualizar o saldo. Se o valor for inválido, uma mensagem de erro é exibida.

Extrato: Exibe todas as operações de saque e depósito realizadas, além do saldo atual da conta. Isso proporciona ao cliente uma visão geral de suas transações e do estado atual de sua conta.

Sair: Encerra a sessão do cliente no sistema.

O sistema é projetado para práticas de programação básica em Python, focando em estruturas de controle como loops e condicionais, manipulação de variáveis e listas para armazenar transações. Essa simulação serve como uma introdução ao desenvolvimento de aplicações financeiras, com ênfase em funcionalidades essenciais de uma conta bancária e na importância da validação de entrada de dados e gerenciamento de estado da conta.
