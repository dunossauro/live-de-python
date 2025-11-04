
with open('input.txt') as input_file:
    with open('output.txt', 'w') as output_file:
        output_file.write(
            input_file.read()
        )


with (
    open('input.txt') as input_file,
    open('output.txt', 'w') as output_file
):
    output_file.write(
        input_file.read()
    )
