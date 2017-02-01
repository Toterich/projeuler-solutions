"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

def multipleOf3And5(n):
    #example: n=34
    #3+6+9+12+15+18+21+24+27+30+33 +5+10+15+20+25+30 -(15+30)
    #3*(1+2+3+4+5+6+7+8+9+10+11) + 5*(1+2+3+4+5+6) - 15*(1+2)
    #3*(1+2+...+(n-1)//3) + 5*(1+2+...+(n-1)//5) -15*(1+2+...+(n-1)//15)

    #calculate each biggest divider
    bigDiv15 = (n - 1) // 15 + 1
    bigDiv5 = (n - 1) // 5 + 1
    bigDiv3 = (n - 1) // 3 + 1

    #calculate partial sums (using sum of first n natural numbers)
    sum15 = bigDiv15*(bigDiv15+1)//2
    sum5 = bigDiv5*(bigDiv5+1)//2
    sum3 = bigDiv3*(bigDiv3+1)//2

    return int(3*sum3 + 5*sum5 -15*sum15)

if __name__ == '__main__':
    print(multipleOf3And5(1000))