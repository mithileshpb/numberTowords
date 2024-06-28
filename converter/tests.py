from django.test import TestCase

# Create your tests here.


def convert_number_to_words_util(number, language_code='en'):
 
    language_data = {
        'en': {
            'ones': ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'],
            'teens': ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'],
            'tens': ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'],
            'thousands': ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion', 'Octillion']
        },
        'hi': {
            'ones': ['शून्य', 'एक', 'दो', 'तीन', 'चार', 'पाँच', 'छह', 'सात', 'आठ', 'नौ'],
            'teens': ['दस', 'ग्यारह', 'बारह', 'तेरह', 'चौदह', 'पंद्रह', 'सोलह', 'सत्रह', 'अठारह', 'उन्नीस'],
            'tens': ['बीस', 'इक्कीस', 'बाईस', 'तेईस', 'चौबीस', 'पच्चीस', 'छब्बीस', 'सत्ताईस', 'अट्ठाईस', 'उनतीस',
                     'तीस', 'इकतीस', 'बत्तीस', 'तैंतीस', 'चौंतीस', 'पैंतीस', 'छत्तीस', 'सैंतीस', 'अड़तीस', 'उनतालीस',
                     'चालीस', 'इकतालीस', 'बयालीस', 'तैंतालीस', 'चवालीस', 'पैंतालीस', 'छियालीस', 'सैंतालीस', 'अड़तालीस', 'उनचास',
                     'पचास', 'इक्यावन', 'बावन', 'तिरेपन', 'चौवन', 'पचपन', 'छप्पन', 'सत्तावन', 'अट्ठावन', 'उनसठ',
                     'साठ', 'इकसठ', 'बासठ', 'तिरेसठ', 'चौंसठ', 'पैंसठ', 'छियासठ', 'सड़सठ', 'अड़सठ', 'उनहत्तर',
                     'सत्तर', 'इकहत्तर', 'बहत्तर', 'तिहत्तर', 'चौहत्तर', 'पचहत्तर', 'छिहत्तर', 'सत्तहत्तर', 'अठहत्तर', 'उनासी',
                     'अस्सी', 'इक्यासी', 'बयासी', 'तिरासी', 'चौरासी', 'पचासी', 'छियासी', 'सत्तासी', 'अठासी', 'नवासी',
                     'नब्बे', 'इक्यानवे', 'बानवे', 'तिरेनवे', 'चौरानवे', 'पचानवे', 'छियानवे', 'सत्तानवे', 'अट्ठानवे', 'निन्यानवे'],
            'thousands': ['', 'हज़ार', 'लाख', 'करोड़', 'अरब', 'खरब', 'नील', 'पद्म', 'शंख', 'महाशंख']
        }
    }

    language = language_data.get(language_code, language_data['en'])

    if number == 0:
        return language['ones'][0]

    def chunk_to_words(chunk):
        words = []
        if chunk >= 100:
            words.append(language['ones'][chunk // 100])
            words.append('Hundred' if language_code == 'en' else 'सौ')
            chunk %= 100
        if 10 <= chunk < 20:
            words.append(language['teens'][chunk - 10])
            chunk = 0  # Avoid appending an extra 'zero'
        if chunk >= 20:
            words.append(language['tens'][chunk // 10 - 2] if language_code == 'en' else language['tens'][chunk - 20])
            chunk %= 10
        if chunk > 0:
            words.append(language['ones'][chunk])
        return words

    num_str = str(number)
    num_len = len(num_str)
    chunks = []

    # Split the number into chunks of 2 and 3 digits from right to left
    while num_len > 0:
        if len(chunks) == 0:
            chunk_size = 3
        else:
            chunk_size = 2
        chunk = int(num_str[max(0, num_len - chunk_size):num_len])
        chunks.append(chunk)
        num_len -= chunk_size

    words = []
    for i, chunk in enumerate(chunks):
        if chunk > 0:
            chunk_words = chunk_to_words(chunk) 
            if i > 0:
                if i < len(language['thousands']):
                    chunk_words.append(language['thousands'][i])
                else:
                    chunk_words.append(f'10^{(i-1)*2+3}')  # Just a placeholder for large scales
            words = chunk_words + words

    return ' '.join(words)

# Example test cases
print(convert_number_to_words_util(123456789876, 'hi'))  # Expected: बारह अरब चौंतीस करोड़ पचास लाख सत्तर नौ हजार आठ सौ छिहत्तर
print(convert_number_to_words_util(1234567890123456789, 'en'))  # Expected: One Quintillion Two Hundred Thirty Four Quadrillion Five Hundred Sixty Seven Trillion Eight Hundred Ninety Billion One Hundred Twenty Three Million Four Hundred Fifty Six Thousand Seven Hundred Eighty Nine



class NumberTooLargeError(Exception):
    pass

def convert_number_to_words_util(number, language_code='en'):
    if language_code == 'hi' and len(str(number)) > 15:
        raise NumberTooLargeError("संख्या 15 अंकों की सीमा से अधिक है")  # Number exceeds the 15 digit limit

    language_data = {
        'en': {
            'ones': ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'],
            'teens': ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'],
            'tens': ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'],
            'thousands': ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion', 'Octillion']
        },
        'hi': {
            'ones': ['शून्य', 'एक', 'दो', 'तीन', 'चार', 'पाँच', 'छह', 'सात', 'आठ', 'नौ'],
            'teens': ['दस', 'ग्यारह', 'बारह', 'तेरह', 'चौदह', 'पंद्रह', 'सोलह', 'सत्रह', 'अठारह', 'उन्नीस'],
            'tens': ['बीस', 'तीस', 'चालीस', 'पचास', 'साठ', 'सत्तर', 'अस्सी', 'नब्बे'],
            'compound_tens': ['इक्कीस', 'बाईस', 'तेईस', 'चौबीस', 'पच्चीस', 'छब्बीस', 'सत्ताईस', 'अट्ठाईस', 'उनतीस',
                             'इकतीस', 'बत्तीस', 'तैंतीस', 'चौंतीस', 'पैंतीस', 'छत्तीस', 'सैंतीस', 'अड़तीस', 'उनतालीस',
                             'इकतालीस', 'बयालीस', 'तैंतालीस', 'चवालीस', 'पैंतालीस', 'छियालीस', 'सैंतालीस', 'अड़तालीस', 'उनचास',
                             'इक्यावन', 'बावन', 'तिरेपन', 'चौवन', 'पचपन', 'छप्पन', 'सत्तावन', 'अट्ठावन', 'उनसठ',
                             'इकसठ', 'बासठ', 'तिरेसठ', 'चौंसठ', 'पैंसठ', 'छियासठ', 'सड़सठ', 'अड़सठ', 'उनहत्तर',
                             'इकहत्तर', 'बहत्तर', 'तिहत्तर', 'चौहत्तर', 'पचहत्तर', 'छिहत्तर', 'सत्तहत्तर', 'अठहत्तर', 'उनासी',
                             'इक्यासी', 'बयासी', 'तिरासी', 'चौरासी', 'पचासी', 'छियासी', 'सत्तासी', 'अठासी', 'नवासी',
                             'इक्यानवे', 'बानवे', 'तिरेनवे', 'चौरानवे', 'पचानवे', 'छियानवे', 'सत्तानवे', 'अट्ठानवे', 'निन्यानवे'],
            'thousands': ['', 'हज़ार', 'लाख', 'करोड़', 'अरब', 'खरब', 'नील', 'पद्म', 'शंख', 'महाशंख']
        }
    }

    language = language_data.get(language_code, language_data['en'])

    if number == 0:
        return language['ones'][0]

    def chunk_to_words(chunk):
        words = []
        if chunk >= 100:
            words.append(language['ones'][chunk // 100])
            words.append('Hundred' if language_code == 'en' else 'सौ')
            chunk %= 100
        if 10 <= chunk < 20:
            words.append(language['teens'][chunk - 10])
            chunk = 0  # Avoid appending an extra 'zero'
        if chunk >= 20:
            if language_code == 'hi' and chunk in range(21, 100):
                words.append(language['compound_tens'][chunk - 21])
                chunk = 0
            else:
                words.append(language['tens'][chunk // 10 - 2])
                chunk %= 10
        if chunk > 0:
            words.append(language['ones'][chunk])
        return words

    num_str = str(number)
    num_len = len(num_str)
    chunks = []

    # Split the number into chunks of 2 and 3 digits from right to left
    while num_len > 0:
        if len(chunks) == 0:
            chunk_size = 3
        else:
            chunk_size = 2
        chunk = int(num_str[max(0, num_len - chunk_size):num_len])
        chunks.append(chunk)
        num_len -= chunk_size

    words = []
    for i, chunk in enumerate(chunks):
        if chunk > 0:
            chunk_words = chunk_to_words(chunk)
            if i > 0:
                if i < len(language['thousands']):
                    chunk_words.append(language['thousands'][i])
                else:
                    chunk_words.append(f'10^{(i-1)*2+3}')  # Just a placeholder for large scales
            words = chunk_words + words

    return ' '.join(words)

# Example usage
# number = 12356777
# language = 'hi'
# print(convert_number_to_words_util(number, language))  # Expected output: "एक करोड़ तेईस लाख छप्पन हज़ार सात सौ सत्तासी"
