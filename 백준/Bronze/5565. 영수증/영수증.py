price = int(input())
book_price = 0

for _ in range(9):
    book = int(input())
    book_price += book

print(price - book_price)