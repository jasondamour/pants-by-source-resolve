from lib_3.greetings import say_hello

def test_say_hello(capsys):
    say_hello('Pants')
    captured = capsys.readouterr()
    assert captured.out == 'Hello, Pants!\nrequests version: 2.32.3\n'
