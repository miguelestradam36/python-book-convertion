class BooksManager:
    # Attributes
    os = __import__("os")
    success = False
    content = ''

    #Methods
    def __init__(self, text_or_file:bool):
        """
        """
        # True for files
        # False for text
        self.text_or_file = text_or_file

    def convert_wordfile_to_mp3(self, book:str, mp3_path:str, language:str)->None:
        """
        """
        try:
            from gtts import gTTS
            # The text that you want to convert to audio
            if self.text_or_file:
                import docx
                doc = docx.Document(book)
                fullText = []
                delimiter = " " # Define a delimiter
                for para in doc.paragraphs:
                    fullText.append(para.text)
                self.content = delimiter.join(fullText)
            else:
                self.content = book

            # Passing the text and language to the engine, 
            # here we have marked slow=False. Which tells 
            # the module that the converted audio should 
            # have a high speed
            myobj = gTTS(text=self.content, lang=language, slow=False)

            # Saving the converted audio in a mp3 file named
            # welcome 
            myobj.save(mp3_path)

            self.success = True

        except Exception as Error:

            print("ERROR: {}".format(Error))
            self.success = False

    def __del__(self):
        """
        """
        if self.success:
            print ("The process was a success...")
        else:
            print("It was not possible to do the conversion...")