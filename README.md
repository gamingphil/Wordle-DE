# Wordle DE
This program uses genetic algrorithms to find the optimal 4 opening words for the German Wordle (https://wordle.at/).

You'll get an output like this:
| Index | Fitness | Words | Letters |
| ----------- | ----------- | ----------- | ----------- |
| [4853, 3764, 1898, 2068] | 3.0959164292497627 | ['MODUL', 'ZWACK', 'THING', 'VERBS'] | 20 |
| [1898, 2068, 4853, 3764] | 3.0959164292497627 | ['THING', 'VERBS', 'MODUL', 'ZWACK'] | 20 |
| [1898, 3764, 2068, 4853] | 3.0959164292497627 | ['THING', 'ZWACK', 'VERBS', 'MODUL'] | 20 |
| [4853, 1898, 3764, 2068] | 3.0959164292497627 | ['MODUL', 'THING', 'ZWACK', 'VERBS'] | 20 |
| [1898, 3764, 4853, 2068] | 3.0959164292497627 | ['THING', 'ZWACK', 'MODUL', 'VERBS'] | 20 |
| [1898, 3764, 2068, 4853] | 3.0959164292497627 | ['THING', 'ZWACK', 'VERBS', 'MODUL'] | 20 |
| [1898, 4853, 2068, 3764] | 3.0959164292497627 | ['THING', 'MODUL', 'VERBS', 'ZWACK'] | 20 |
| [1898, 4853, 3764, 2068] | 3.0959164292497627 | ['THING', 'MODUL', 'ZWACK', 'VERBS'] | 20 |
| [1898, 2068, 3764, 4853] | 3.0959164292497627 | ['THING', 'VERBS', 'ZWACK', 'MODUL'] | 20 |
| [1898, 3764, 2068, 4853] | 3.0959164292497627 | ['THING', 'ZWACK', 'VERBS', 'MODUL'] | 20 |
| [1898, 4853, 3764, 2068] | 3.0959164292497627 | ['THING', 'MODUL', 'ZWACK', 'VERBS'] | 20 |
| [1898, 4853, 3764, 2068] | 3.0959164292497627 | ['THING', 'MODUL', 'ZWACK', 'VERBS'] | 20 |
| [4853, 2068, 3764, 1898] | 3.0959164292497627 | ['MODUL', 'VERBS', 'ZWACK', 'THING'] | 20 |
| [4853, 3764, 1898, 2068] | 3.0959164292497627 | ['MODUL', 'ZWACK', 'THING', 'VERBS'] | 20 |
| [1898, 4516, 3764, 2068] | 2.7877492877492878 | ['THING', 'MODAL', 'ZWACK', 'VERBS'] | 19 |
| [1898, 3764, 4516, 2068] | 2.7877492877492878 | ['THING', 'ZWACK', 'MODAL', 'VERBS'] | 19 |
| [4853, 148, 3764, 1898] | 2.64957264957265 | ['MODUL', 'ASERN', 'ZWACK', 'THING'] | 18 |
| [1898, 1759, 2068, 4853] | 2.6239316239316244 | ['THING', 'SPACE', 'VERBS', 'MODUL'] | 18 |
| [1898, 4607, 4853, 2068] | 2.35707502374169 | ['THING', 'PALME', 'MODUL', 'VERBS'] | 17 |
| [1144, 4853, 3764, 2068] | 2.324786324786325 | ['JOHNS', 'MODUL', 'ZWACK', 'VERBS'] | 18 |
| [4853, 423, 1898, 2068] | 2.308641975308642 | ['MODUL', 'CHIPS', 'THING', 'VERBS'] | 17 |

The columns correspond to
1. The indexes in the list of words.
2. The assigned fitness for the solution.
3. The words of the solution.
4. The amount of letters eliminated by the solution.