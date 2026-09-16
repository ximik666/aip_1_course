# Модули и сборка приложения
def total_cents(records):
    return sum(row["cents"] for row in records)

def main():
    print(total_cents([{"cents": 120}, {"cents": 80}]))

if __name__ == "__main__":
    main()
