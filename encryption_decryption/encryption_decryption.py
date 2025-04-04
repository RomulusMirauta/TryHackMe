message = 'XRPCTCRGNEI' # encrypted message
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''

for key in range(len(letters)):
   for char in message:
      if char in letters:
         num = letters.find(char)
         num = num - key
         if num < 0:
            num = num + len(letters)
            translated = translated + letters[num]
         else:
            translated = translated + char
   # print('Hacking Key %s: %s' % (key, translated))

print(f'\nThe Hacking Key is: \n\n{translated}\n')