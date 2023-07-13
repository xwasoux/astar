from astar import AParser, AstAnalyser, AstOperator, ACodeGenerator
from anytree import RenderTree

def main():
    code = '''
    def max(a, b):
        if a > b:
            return a
        else:
            return b
    '''

    parser = AParser()
    tree = parser.parse(text=code, lang="python")
    print(RenderTree(tree).by_attr("type"))

    analyser = AstAnalyser(tree=tree)

    subunitNodeList = analyser.subunitNodes()
    print(len(subunitNodeList))
    sample = subunitNodeList[-1]

    operator = AstOperator()
    editedTree = operator.delete(root=tree, target=sample)
    print(RenderTree(editedTree).by_attr("type"))

    generator = ACodeGenerator()
    print(generator.generate(root=tree))
    print(generator.generate(root=editedTree))

if __name__ == "__main__":
    main()
