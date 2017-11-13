import sys
import redcodelex, redcodeparse


def print_usage(program_name):
    print("Usage: {} <filename>".format(program_name))


def main():
    # Sanity check arguments
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print_usage(sys.argv[0])
        sys.exit(1)

    # Source code to build
    data = ''

    # Determine whether to operate on a file or stdin
    if filename == "-":
        # Operate on stdin
        pass
    else:
        data = open(filename, 'r').read()

    '''
    # Build the lexer on the program bytes
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)

    '''

    # Parser test
    result = redcodeparse.parse(data)
    print(result)


if __name__ == '__main__':
    main()
