count = int(input())

output_a = "A long time ago in a galaxy "
output_b = "far away..."

if count == 1:
    print(output_a + output_b)
if count > 1:
    count = count - 1
    far_string = 'far, ' * count
    output = output_a + far_string + output_b
    print(output)
