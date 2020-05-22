
def find_vowels():
    """
                    My Python Script : Vowel Detector Tool
                    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    """

    vowels = "aeiouAEIOU"
    string = input("\nEnter your String:\t")
    str_enum_list = list(string)

    v_found = [element for index, element in enumerate(str_enum_list) if element in vowels]
    v_indices = [index for index, element in enumerate(str_enum_list) if element in vowels]

    if v_found:
        print("\nVowel(s) in the Input-String:\t", v_found)
        print("\nVowel_Position(s) in the Input-String:\t", v_indices)
    elif not v_found:
        print("\nNo Vowel(s) found in the Input-String !!!")


# find_vowels()
