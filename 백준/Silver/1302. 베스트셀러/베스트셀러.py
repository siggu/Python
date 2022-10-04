import sys
read = sys.stdin.readline

N = int(read())
books = dict()
best_seller = []

for cnt in range(N):
    book = read()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

for book, number in books.items():
    if number == max(books.values()):
        best_seller.append(book)

print(sorted(best_seller)[0])