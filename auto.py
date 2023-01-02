if __name__ == '__main__':
    import sys

    module = sys.argv.pop(1)
    app = __import__(module)
    print(f'module: {module}')
    print(f'argv {sys.argv}')

    app.main()
