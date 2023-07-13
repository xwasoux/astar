from astar import AParser
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

if __name__ == "__main__":
    main()