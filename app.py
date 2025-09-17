"""
Kutubxona Boshqaruv Tizimi (Library Management System)
CLI ilova - kitoblarni qo'shish, ko'rish, o'chirish, yangilash va qidirish
"""
import sys
from rich.console import Console
from rich.table import Table

console = Console()


def add_book(library: list[list[str, str, int, bool]]) -> None:
    title = input("Kitob nomi: ").strip()
    author = input("Muallif: ").strip()
    year = input("Yili: ").strip()

    if not year.isdigit():
        print("Yil notogri kiritildi!")
        return

    library.append([title, author, int(year), False])
    print("Kitob muvaffaqiyatli qoshildi!")


def show_books(library: list[list[str, str, int, bool]]) -> None:
    if not library:
        print("Kutubxona bosh...")
        return

    table = Table(title="Kutubxona kitoblari")
    table.add_column("raqami")
    table.add_column("Nom")
    table.add_column("Muallif")
    table.add_column("Yil")
    table.add_column("Holat")

    for i, book in enumerate(library, start=1):
        status = "Oqilgan" if book[3] else "Oqilmagan"
        table.add_row(str(i), book[0], book[1], str(book[2]), status)

    console.print(table) 


def delete_book(library: list[list[str, str, int, bool]]) -> None:
    show_books(library)
    index = input("Ochirish uchun indeksni kiriting: ")

    if not index.isdigit():
        print("Faqat raqam kiriting!")
        return

    index = int(index) - 1
    if 0 <= index < len(library):
        removed = library.pop(index)
        print(f"{removed[0]} o‘chirildi!")
    else:
        print("Notogri indeks!")


def main():
    library: list[list[str, str, int, bool]] = []

    while True:
        print("\n=== KUTUBXONA MENYUSI ===")
        print("1. Kitob qoshish")
        print("2. Kitoblarni korish")
        print("3. Kitobni ochirish")
        print("0. Chiqish")

        choice = input("Tanlov: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            show_books(library)
        elif choice == "3":
            delete_book(library)
        elif choice == "0":
            sys.exit()
        else:
            print("Notogri tanlov!")
main()
