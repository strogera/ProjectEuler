f1 = 1
f2 = 1
fn = 1

i = 1
while len(str(fn)) < 1000:
    i += 1
    fn = f1 + f2
    f1 = f2
    f2 = fn

print(i + 1)