seg = int(input(''))

hora = seg / 3600

seg %= 3600

min = seg // 60

segF = seg % 60

print(f'{int(hora)}:{int(min)}:{int(segF)}')