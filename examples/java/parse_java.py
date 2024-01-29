import os
from astars import AParser

def main():
    with open(os.path.join(os.path.dirname(__file__), "input", "java_sample.java")) as f:
        code = f.read()

    java_parser = AParser(lang="java")
    ## If you want to build the parser to your local directory, use the following code
    # java_parser = AParser(lang="java", build_to=os.path.join(os.path.dirname(__file__)))
    tree = java_parser.parse(text=code)
    print(tree)

    return None


if __name__ == "__main__":
    main()