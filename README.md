# Astars

> AST analysis and manipulation tools for diverse languages.

The analysis of repositories and of code submitted to online review systems is one of the practical tasks in language processing for programming languages and necessary processing for research.
In such cases, it is not uncommon to use ASTs (Abstract Syntax Trees).
However, in order to use ASTs, it is necessary to understand the structure of ASTs, which differ from language to language, and to write code to perform parsing based on them.
Also, libraries for analysis using ASTs are different for each language, so it is necessary to create libraries for each language.
In addition, manipulating tree structures to perform various analyses of ASTs is generally a cumbersome task, which can complicate the analysis code.


To solve these problems, this project provides a library for easy analysis and manipulation of ASTs.
Internally, ASTs are generated using [tree-sitter](https://tree-sitter.github.io/tree-sitter/) and analyzed based on them.
Therefore, for languages that are supported by tree-sitter, ASTs can be generated using it.


## Installation
The package is tested under Python 3. It can be installed via:
```
pip install astars
```

## Usage

Parsing a code snippet and printing the AST:

```python
>>> from astars import AParser
>>> 
>>> parser = AParser(lang="python")
>>> tree = parser.parse(
...     '''print("Hello world!")'''
...     )
>>> print(tree)
module
└── expression_statement
    └── call
        ├── identifier
        └── argument_list
            ├── (
            ├── string
            │   ├── string_start
            │   ├── string_content
            │   └── string_end
            └── )
```

Manipulating the AST:

```python
>>> from astars import AParser, APruner
>>> 
>>> parser = AParser(lang="python")
>>> tree = parser.parse(
...     '''print(1+2/4)
...     ''')
>>> 
>>> res = APruner.sequencialBackwardPrune(tree=tree)
>>> for east in res:
...     print(east[0].recover())
... 
print(1+2/4

print(1+2/

print(1+2

print(1+

print(1+

print(1

print(

print(

print

print


```
