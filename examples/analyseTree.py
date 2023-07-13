from astar import AParser, AstAnalyser
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

    allNodeList = analyser.allNodes()
    print(len(allNodeList))

    allNamedNodeList = analyser.namedNodes()
    print(len(allNamedNodeList))

    subunitNodeList = analyser.subunitNodes()
    print(len(subunitNodeList))


if __name__ == "__main__":
    main()
