Trabalho Prático 1 - Sistemas Distribuídos
==========================================

Autores
-------

- Guilherme Michaelsen Chrisopher Cardoso
- João Paulo Taylor Ienczak Zanette

Objetivo
--------

Implementar os três algoritmos de exclusão mútua:
- Anel;
- Servidor/Coordenador;
- Multicast e relógios lógicos.

Linguagem:
- [ ] C;
- [ ] C++;
- [ ] Java;
- [x] Python3.

Formato de apresentação:
- [ ] Animação e GUI;
- [x] Mensagens no Console.

Dependências
------------

Dependências instaláveis com `pip install [dependências]`.

- `dataclasses`
- `carl`

Como Instalar
-------------

```bash
pip install -e muxim
```

Como executar
-------------

```bash
python -m muxim [-h]
                [--algorithm {server_based,token_ring}]
                [--n_processes N_PROCESSES]

```
