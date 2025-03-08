from booksconv.mp3conv import BooksManager

buff = BooksManager(text_or_file=True)
buff.convert_wordfile_to_mp3(book="Example.docx", mp3_path="test.mp3", language="en")
