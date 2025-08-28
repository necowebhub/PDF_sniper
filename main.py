import PyPDF2
import pdfplumber

def remove_pages_with_text(input_pdf, output_pdf, search_text="размер 44"):
    print(f"Открываю файл: {input_pdf}")
    with open(input_pdf, "rb") as infile:
        reader = PyPDF2.PdfReader(infile)
        writer = PyPDF2.PdfWriter()

        total_pages = len(reader.pages)
        print(f"Всего страниц в файле: {total_pages}")

        # открываем pdfplumber один раз
        with pdfplumber.open(input_pdf) as pdf:
            for i in range(total_pages):
                print(f"\nПроверяю страницу {i+1}/{total_pages}...")

                page_text = pdf.pages[i].extract_text() or ""
                if search_text in page_text:
                    print(f" → Найдено '{search_text}' → страница {i+1} будет удалена")
                    continue
                else:
                    print(f" → Страница {i+1} оставлена")
                    writer.add_page(reader.pages[i])

        with open(output_pdf, "wb") as outfile:
            writer.write(outfile)

    print(f"\nГотово! Итоговый файл сохранён как: {output_pdf}")
    print(f"Оставлено страниц: {len(writer.pages)} из {total_pages}")


# пример вызова
remove_pages_with_text("input.pdf", "output.pdf", "размер 52")
