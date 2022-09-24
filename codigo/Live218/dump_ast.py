"""Faz o parse de código fonte e printa a AST do python."""
from argparse import ArgumentParser
from ast import dump, parse

from astmonkey import transformers, visitors


def _dump(fname: str) -> None:
    with open(fname, 'r') as file:
        tree = parse(file.read())
        print(dump(tree, indent=2))


def _graph(fname: str) -> None:
    with open(fname, 'r') as file:
        tree = parse(file.read())
        node = transformers.ParentChildNodeTransformer().visit(tree)
        visitor = visitors.GraphNodeVisitor()
        visitor.visit(node)
        visitor.graph.write_png('graph.png')


def main() -> None:
    parser = ArgumentParser(
        description='Parse source files and print the abstract syntax tree (AST).'
    )
    parser.add_argument('-g', action='store_true', help='generate graph')
    parser.add_argument('FILE', nargs='*', help='files to parse')
    args = parser.parse_args()

    if args.g:
        for fname in args.FILE:
            _graph(fname)
    else:
        for fname in args.FILE:
            _dump(fname)


if __name__ == '__main__':
    main()
