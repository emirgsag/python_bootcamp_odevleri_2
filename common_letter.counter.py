def count_common_letters(string_1, string_2):
    common_letters = {}
    for letter in string_1:
        for letter_2 in string_2:
            if letter == letter_2:
                common_letters[letter] = [string_1.count(letter), string_2.count(letter_2)]
    return common_letters


input_1 = input("Bir metin giriniz: ")
input_2 = input("Bir metin daha giriniz: ")

print(count_common_letters(input_1, input_2))
