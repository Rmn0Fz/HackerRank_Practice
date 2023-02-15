def minion_game(string):
    # your code goes here
    vowel = 'aeiou'.upper()
    string_lenght = len(string)
    kevin = sum(string_lenght-i for i in range(string_lenght) if string[i] in vowel)
    stuart = string_lenght * (string_lenght + 1) / 2 - kevin
    
    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print(f'Kevin {int(kevin)}')
    else:
        print(f'Stuart {int(stuart)}')
    

if __name__ == '__main__':
    s = input()
    minion_game(s)