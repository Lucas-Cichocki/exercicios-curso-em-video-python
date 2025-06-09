from random import randint

pc = tuple(randint(1, 100) for _ in range(5))

print('Os valores foram: ', end= '')
for i in pc:
    print(f'{i}', end= ' ')

pc = tuple(sorted(pc))

print(f'\nO maior valor sorteado e o {max(pc)}')
print(f'O menor valor sorteado foi o {min(pc)}')