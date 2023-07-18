cd ./astars/parser
mkdir grammar grammar/tree-sitter 

git submodule add https://github.com/tree-sitter/tree-sitter-c.git grammar/tree-sitter/tree-sitter-c
git submodule add https://github.com/tree-sitter/tree-sitter-cpp.git grammar/tree-sitter/tree-sitter-cpp
git submodule add https://github.com/tree-sitter/tree-sitter-python.git grammar/tree-sitter/tree-sitter-python

cd ../..