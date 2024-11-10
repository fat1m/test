inf_volume = 1.44
pages = 100
lines_page = 50
symbols_per_line = 25

inf_volume_bytes = 1.44 * 1024 * 1024
lines = pages * lines_page
symbols = symbols_per_line * lines

book_volume = symbols * 4
result = inf_volume_bytes // book_volume
result = int(result)

print("Количество книг, помещающихся на дискету:", result)
