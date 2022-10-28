def start():
  print('*********************************')
  print('***Bem vindo ao jogo da Forca!***')
  print('*********************************')

  secretWord = 'banana'
  correctLetters = ['_','_','_','_','_','_']

  loose = False
  win = False
  errors = 0

  print(correctLetters)

  while (not win  not loose):
    
    chute = input('Letter: ')
    
    if (chute in secretWord):
      position = 0
      for letra in secretWord:
        if (letra.upper() == chute.upper()):
          correctLetters[position] = letra
        position += 1
    else:
      errors += 1

    loose = errors == 6
    win = '_' not in correctLetters
    print(correctLetters)

  if(win):
    print('You Win')
  else:
    print('You Loose')
  print('Endgame')


start()