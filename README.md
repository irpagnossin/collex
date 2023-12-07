# Coleção de exercícios

Este projeto contém inúmeros exemplos de problemas e exercícios, de Física, Matemática e Estatística, com soluções. Os arquivos [eg_mechanics.pdf](./eg_mechanics.pdf) e [eg_statistics.pdf](./eg_statistics.pdf) ilustram o conteúdo dessas questões.

# Dependências
## LaTeX
Alguns dos exemplos estão escritos em LaTeX. Para compilá-los você precisará de vários pacotes. Se você usa Linux, basta instalar esses pacotes do TeXLive:
- `texlive-base`
- `texlive-latex`
- `texlive-latexrecommended`
- `texlive-fontsrecommended`
- `texlive-langportuguese`
- `texlive-pictures`
- `texlive-latexextra`
- `texlive-mathscience`

# Python
Algumas questões estão parametrizadas, permitindo a criação de várias questões diferentes a partir do mesmo enunciado. Elas estão escritas como um template Jinja para o Python. Por exemplo, a questão `physics/analytical_mechanics/analytical_mechanics_q3.tex.jinja`. Use o arquivo Python homônimo, isto é, `analytical_mechanics_q3.py`, para gerar o arquivo `.tex` correspondente:
```bash
python physics/analytical_mechanics/analytical_mechanics_q3.py
```

Para criar essas questões, crie um ambiente virtual e instale as dependências, assim:
```bash
$ python -m venv .venv
$ . .venv/bin/activate
$ pip install --upgrade pip && pip install -r requirements.txt
```

