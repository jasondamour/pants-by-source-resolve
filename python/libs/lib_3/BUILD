python_sources(
    sources=['**/*.py', '!**/*_test.py'],
    **parametrize('app_2', interpreter_constraints=['==3.10.*'], resolve='app_2'),
)

python_tests(
    name='tests',
    sources=['**/*_test.py'],
    **parametrize('app_2', interpreter_constraints=['==3.10.*'], resolve='app_2'),
)

poetry_requirements(
    name='poetry',
    resolve=parametrize('app_2')
)
