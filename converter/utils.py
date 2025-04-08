def convert_number_to_words_util(number, language_code='en'):
    def convert_number_to_words_en(number):
        language = {
            'ones': ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'],
            'teens': ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'],
            'tens': ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'],
            'thousands': ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion', 'Octillion']
        }

        if number == 0:
            return language['ones'][0]

        def chunk_to_words(chunk):
            words = []
            if chunk >= 100:
                words.append(language['ones'][chunk // 100])
                words.append('Hundred')
                chunk %= 100
            if 10 <= chunk < 20:
                words.append(language['teens'][chunk - 10])
                chunk = 0
            if chunk >= 20:
                words.append(language['tens'][(chunk // 10) - 2])
                chunk %= 10
            if chunk > 0:
                words.append(language['ones'][chunk])
            return words

        num_str = str(number)
        num_len = len(num_str)
        chunks = []

        while num_len > 0:
            chunk_size = 3
            chunk = int(num_str[max(0, num_len - chunk_size):num_len])
            chunks.append(chunk)
            num_len -= chunk_size

        words = []
        for i, chunk in enumerate(chunks):
            if chunk > 0:
                chunk_words = chunk_to_words(chunk)
                if i > 0:
                    chunk_words.append(language['thousands'][i])
                words = chunk_words + words

        return ' '.join(words)
    def convert_number_to_words_hi(number):
        language = {
            'ones': ['शून्य', 'एक', 'दो', 'तीन', 'चार', 'पाँच', 'छह', 'सात', 'आठ', 'नौ'],
            'teens': ['दस', 'ग्यारह', 'बारह', 'तेरह', 'चौदह', 'पंद्रह', 'सोलह', 'सत्रह', 'अठारह', 'उन्नीस'],
            'tens': ['बीस', 'तीस', 'चालीस', 'पचास', 'साठ', 'सत्तर', 'अस्सी', 'नब्बे'],
            'compound_tens': ['इक्कीस', 'बाईस', 'तेईस', 'चौबीस', 'पच्चीस', 'छब्बीस', 'सत्ताईस', 'अट्ठाईस', 'उनतीस',
                             'तीस', 'इकतीस', 'बत्तीस', 'तैंतीस', 'चौंतीस', 'पैंतीस', 'छत्तीस', 'सैंतीस', 'अड़तीस', 'उनतालीस',
                             'चालीस', 'इकतालीस', 'बयालीस', 'तैंतालीस', 'चवालीस', 'पैंतालीस', 'छियालीस', 'सैंतालीस', 'अड़तालीस', 'उनचास',
                             'पचास', 'इक्यावन', 'बावन', 'तिरेपन', 'चौवन', 'पचपन', 'छप्पन', 'सत्तावन', 'अट्ठावन', 'उनसठ',
                             'साठ', 'इकसठ', 'बासठ', 'तिरेसठ', 'चौंसठ', 'पैंसठ', 'छियासठ', 'सड़सठ', 'अड़सठ', 'उनहत्तर',
                             'सत्तर', 'इकहत्तर', 'बहत्तर', 'तिहत्तर', 'चौहत्तर', 'पचहत्तर', 'छिहत्तर', 'सत्तहत्तर', 'अठहत्तर', 'उनासी',
                             'अस्सी', 'इक्यासी', 'बयासी', 'तिरासी', 'चौरासी', 'पचासी', 'छियासी', 'सत्तासी', 'अठासी', 'नवासी',
                             'नब्बे', 'इक्यानवे', 'बानवे', 'तिरेनवे', 'चौरानवे', 'पचानवे', 'छियानवे', 'सत्तानवे', 'अट्ठानवे', 'निन्यानवे'],
            'thousands': ['', 'हज़ार', 'लाख', 'करोड़', 'अरब', 'खरब', 'नील', 'पद्म', 'शंख', 'महाशंख']
        }

        if number == 0:
            return language['ones'][0]

        def chunk_to_words(chunk):
            words = []
            if chunk >= 100:
                words.append(language['ones'][chunk // 100])
                words.append('सौ')
                chunk %= 100
            if 10 <= chunk < 20:
                words.append(language['teens'][chunk - 10])
                chunk = 0
            if chunk >= 20:
                if chunk < 100:
                    words.append(language['compound_tens'][chunk - 21])
                    chunk = 0
                else:
                    words.append(language['tens'][(chunk // 10) - 2])
                    chunk %= 10
            if chunk > 0:
                words.append(language['ones'][chunk])
            return words

        num_str = str(number)
        num_len = len(num_str)
        chunks = []

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
                        chunk_words.append(f'10^{(i-1)*2+3}')
                words = chunk_words + words

        return ' '.join(words)

    if language_code == 'hi':
        return convert_number_to_words_hi(number)
    else:
        return convert_number_to_words_en(number)

# Example usage
number = 12345980
print(convert_number_to_words_util(number))  # Default to English: "Twelve Million Three Hundred Forty Five Thousand Nine Hundred Eighty"
print(convert_number_to_words_util(number, 'hi'))  # Hindi: "एक करोड़ तेईस लाख पैंतालीस हज़ार नौ सौ अस्सी"
