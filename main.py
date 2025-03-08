from booksconv.mp3conv import BooksManager

if __name__ == '__ main __':
    buff = BooksManager(text_or_file=True)
    buff.convert_book(book="Example.docx", mp3_path="test.mp3", language="en")
    del buff