import pytest

from morse import decode


@pytest.mark.parametrize(
    'morse_msg, decoded_msg',
    [
        ('.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----',
         '1234567890'),
        ('.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. --',
         'ABCDEFGHIJKLM'),
        ('-. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..',
         'NOPQRSTUVWXYZ'),
        ('.-.-.- ..--.. -..-. -....- -.--. -.--.-',
         '.?/-()')
    ]
)
def test_1_(morse_msg, decoded_msg):
    assert decode(morse_msg) == decoded_msg


@pytest.mark.parametrize(
    'msg, exception',
    [
        ('......', KeyError),
        ('A', KeyError),
        ('-- .- .. -....- ------', KeyError)
    ]
)
def test_2_exceptions(msg, exception):
    with pytest.raises(exception):
        decode(msg)


@pytest.mark.parametrize(
    'morse_msg, decoded_msg',
    [
        ('', ''),
        ('...   ...', 'SS'),
    ]
)
def test_3_empty_and_space(morse_msg, decoded_msg):
    assert decode(morse_msg) == decoded_msg


if __name__ == '__main__':
    pytest.main(['issue-02_parametrize/test_parametrize_morse.py', '-v'])
