def read_expenses(path):
    skipped = 0
    result = {}

    with open(path, encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 2:
                skipped += 1
                continue
            try:
                name = parts[0].strip()
                price = int(parts[1])
            except ValueError:
                skipped += 1
                continue
            if not name or price <= 0:
                skipped += 1
                continue
            if name in result:
                result[name] += price
            else:
                result[name] = price
    return result,skipped
expenses, skipped = read_expenses("expenses.txt")
print(expenses)
print(skipped)