# conjugaime
Uma api python que conjuga verbos


#### TODO:

- Indicativo
- Conjuntivo
- Imperativo
- Refinar a API
- Adicionar todos os verbos irregulares


## Desenvolvimento

O projeto usa Poetry para gerenciar a instalação dos pacotes e o tox como test-runner

### Rodar os testes e a cobertura
```bash
tox
```


### Ver a cobertura dos testes
```bash
tox -e cov
```

> Caso algum teste quebre os resultados não estarão disponiveis

### Para ver a cobertura no browser

```bash
firefox htmlcov/index.html
```
