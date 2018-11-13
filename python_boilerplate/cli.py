def main() -> None:
    import sys
    from .core import add
    if len(sys.argv) == 3:
        x, y = map(int, sys.argv[1:])
        print(add(x, y))
    else:
        print('please specify 2 arguments', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
