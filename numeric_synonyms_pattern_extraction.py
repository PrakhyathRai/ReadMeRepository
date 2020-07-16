""" Pattern Extraction -> Cluster - Bag of Words """
import re

def pre_process_input(string_input):
    """ Function takes string as input and returns astring with \
	synonyms replaced by root word
	Input: String
	Processing: Replacing the synonyms with the key term
	Output: Pre-processed string after relacing synonyms with key term"""
    pre_processed_text = string_input.lower()
    term_dict = {'Amount':['amount', 'cash', 'rupees', 'rs', 'cheque']}
    for i, j in term_dict.items():
        for k in j:
            if k in pre_processed_text:
                pre_processed_text = pre_processed_text.replace(k, i)
    return pre_processed_text

def fetch_amount(string_input):
    """ Functions accepts a string and extracts numerics appearing after key term\
	 and returns a list of extracted numerics
	Input: Pre-processed input string
	Processing: Regular exression findall module to extract relevant information
	Output: List of numerics extrated """
    amount_list = re.findall("[^0-9]Amount*([0-9]*[.]?[0-9]*)", string_input) \
            + re.findall("([0-9]*[.]?[0-9]*)[^0-9]*Amount", string_input)
    real_amount_list = []
    for i in amount_list:
        if i != '':
            real_amount_list.append(float(i))
    return real_amount_list

def numeric_pattern_extraction():
    """ Function to integrate modules of text extraction script
        Input: Nil
        Processing: Assembling modules to illustrate text extration by using a sample text input
        Output: Display list of numerics extracted """
    input_text = "Give him amount 2500.50 and tell give in cash 25.25 only i hav given \
	          him 255.55 cheque and he has onlu 25.5 Rs Rupees 29.99 and take 267.89 cash"
    pre_processed_string = pre_process_input(input_text)
    list_numerics = fetch_amount(pre_processed_string)
    print("List of Numerics Extractedd: ", list_numerics)

#Display List of Numerics
numeric_pattern_extraction()
