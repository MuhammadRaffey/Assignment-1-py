s = "   Hello, World!   "
stripped_s = s.strip()
left_justified_s = stripped_s.ljust(20, '*')
right_justified_s = stripped_s.rjust(20, '*')

print(f"Original string: '{s}'")
print(f"Stripped string: '{stripped_s}'")
print(f"Left justified: '{left_justified_s}'")
print(f"Right justified: '{right_justified_s}'")
