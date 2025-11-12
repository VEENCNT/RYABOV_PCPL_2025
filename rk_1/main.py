from operator import itemgetter

class Libriary:
    def __init__(self, id, name, downloads, language_id):
        self.id = id
        self.name = name
        self.downloads = downloads
        self.language_id = language_id

class Language:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class LibriaryLanguage:
    def __init__(self, libriary_id, language_id):
        self.libriary_id = libriary_id
        self.language_id = language_id

languages = [
    Language(1, "Python"),
    Language(2, "C/C++"),
    Language(3, "Javascript"),
    Language(4, "Java")
]

libriaries = [
    Libriary(1, "NumPy", 16_000_000, 1),
    Libriary(2, "Pandas", 13_000_000, 1),
    Libriary(3, "SFML", 20_000, 2),
    Libriary(4, "React", 6_500_000, 3),
    Libriary(5, "Guava", 4_000_000, 4)
]   

libriaries_languages = [
    LibriaryLanguage(1, 1),
    LibriaryLanguage(1, 2),
    LibriaryLanguage(2, 1),
    LibriaryLanguage(2, 2),
    LibriaryLanguage(3, 2),
    LibriaryLanguage(4, 3),
    LibriaryLanguage(5, 4)
]

def first_task(one_to_many):
    print("Задание Г1")

    result = dict()

    for language in languages:
        language_libriaries = [libriary_name for libriary_name, _, _ in list(filter(lambda x: x[2] == language.name, one_to_many))]

        if language.name.startswith("J"):
            result[language.name] = language_libriaries

    print(result)

def second_task(one_to_many):
    print("Задание Г2")

    result = list()

    for language in languages:
        language_libriaries = list(filter(lambda x: x[2] == language.name, one_to_many))

        if len(language_libriaries) > 0:
            result.append((language.name, max(libriary_downloads for _, libriary_downloads, _ in language_libriaries)))
        else:
            result.append((language.name, 0))

    print(sorted(result, key=itemgetter(1), reverse=True))

def third_task(many_to_many):
    print("Задание Г3")

    result = sorted(many_to_many, key=itemgetter(2))

    print(result)

def main():
    one_to_many = [(libriary.name, libriary.downloads, language.name)
        for libriary in libriaries
        for language in languages
        if libriary.language_id == language.id]
    
    many_to_many_temp = [(language.name, libriary_language.language_id, libriary_language.libriary_id)
        for language in languages
        for libriary_language in libriaries_languages
        if language.id == libriary_language.language_id]
    
    many_to_many = [(libriary.name, libriary.downloads, language_name)
        for language_name, _, libriary_id in many_to_many_temp
        for libriary in libriaries if libriary.id == libriary_id]

    first_task(one_to_many)
    second_task(one_to_many)
    third_task(many_to_many)

if __name__ == "__main__":
    main()