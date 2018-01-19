from cx_Freeze import setup, Executable

setup(
    name = 'BiblioEdit',
    version = '1.0',
    description = 'BiblioEdit',
    executables = [Executable('Main3.py')]
)
