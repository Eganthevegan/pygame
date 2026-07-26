names = ['Aarav', 'Priya', 'Dev', 'Meera', 'Kabir']

target = 'Aarav'
steps = 0
for name in names:
    steps += 1
    if name == target:
        break

print('Target  :', target)
print('Steps  :', steps, '(best case = 1)')
print('Omega  : Omega(1)')

