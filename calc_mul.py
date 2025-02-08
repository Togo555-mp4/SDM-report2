#!/usr/bin/python3

import re
                
def calc(A,B):
    # 整数型であるか確認（整数でない場合は -1 を返す）
    if not isinstance(A, int) or not isinstance(B, int):
        return -1

    # 1 から 999 の範囲内か確認（範囲外なら -1 を返す）
    if not (1 <= A <= 999 and 1 <= B <= 999):
        return -1

    # 掛け算を実行して結果を返す
    return A * B
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
