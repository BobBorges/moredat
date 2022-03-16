#!/usr/bin/env python3
import shutil

def main():
    letters = 'ABCDEFGHIJKLMNOPQRST'
    numbers = ['1','2','3','4']

    for L in letters:
        for N in numbers:
            if f'{L}{N}' != 'A1':
                shutil.copy('A1_1_d.jpg', f'{L}{N}_1_d.jpg')
                shutil.copy('A1_2_t.jpg', f'{L}{N}_2_t.jpg')
                shutil.copy('A1_3_d.jpg', f'{L}{N}_3_d.jpg')
                shutil.copy('A1_4_d.jpg', f'{L}{N}_4_d.jpg')
            else:
                print('AAAAA 11111')

if __name__ == '__main__':
	main()


