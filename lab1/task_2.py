# TODO Найдите количество книг, которое можно разместить на дискете
volume_Mb = 1.44 * (1024 ** 2)
count_of_pages = 100
string_page = 50
string_symbols = 25
total = count_of_pages * string_page * string_symbols
total_per_one_book = total * 4
answer = int(volume_Mb // total_per_one_book)
print("Количество книг, помещающихся на дискету:", answer)
