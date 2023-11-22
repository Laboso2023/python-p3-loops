# looping_test.py

def test_print_digits(capsys):
    print_digits()
    captured = capsys.readouterr()

    expected_output = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"
    assert captured.out == expected_output, f"Expected: {expected_output}, Got: {captured.out}"

    # Check if all digits 1-10 are present
    remaining_digits = set(map(str, range(1, 11))) - set(captured.out.strip().split('\n'))
    assert remaining_digits == set(), f"You didn't print all digits 1-10, missing {', '.join(remaining_digits)}"

# Additional function to print digits
def print_digits():
    for i in range(1, 11):
        print(i)
