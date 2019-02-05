############################################################
# CIS 391/521: Homework 1
############################################################

student_name = "Solution"

# This is where your grade report will be sent.
student_email = "Type your preferred email address here." 

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = "Solution."

python_concepts_question_2 = "Solution."

python_concepts_question_3 = "Solution."

############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]

def concatenate(seqs):
    return [element for seq in seqs for element in seq]

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]

def all_but_last(seq):
    return seq[:-1]

def every_other(seq):
    return seq[::2]

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    for i in range(len(seq) + 1):
        yield seq[:i]

def suffixes(seq):
    for i in range(len(seq) + 1):
        yield seq[i:]

def slices(seq):
    for i in range(len(seq)):
        for j in range(i + 1, len(seq) + 1):
            yield seq[i:j]

############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    return " ".join(word.lower() for word in text.split())

def no_vowels(text):
    return "".join(char for char in text if char not in "aeiouAEIOU")

def digits_to_words(text):
    digit_names = {
        "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
        "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
    }
    return " ".join(digit_names[char] for char in text if char in digit_names)

def to_mixed_case(name):
    words = [word for word in name.split("_") if word]
    return (words[0].lower() + "".join(word.capitalize() for word in words[1:])
            if words else "")

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        self.polynomial = tuple(polynomial)

    def get_polynomial(self):
        return self.polynomial

    def __neg__(self):
        return Polynomial((-coeff, power) for coeff, power in self.polynomial)

    def __add__(self, other):
        return Polynomial(self.polynomial + other.polynomial)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Polynomial((coeff1 * coeff2, power1 + power2)
                          for coeff1, power1 in self.polynomial
                          for coeff2, power2 in other.polynomial)

    def __call__(self, x):
        return sum(coeff * (x ** power) for coeff, power in self.polynomial)

    def simplify(self):
        coeffs = {}
        for coeff, power in self.polynomial:
            coeffs[power] = coeffs.get(power, 0) + coeff
        self.polynomial = tuple(sorted(
            ((coeff, power) for power, coeff in coeffs.items() if coeff != 0),
            key=lambda (coeff, power): power, reverse=True)) or ((0, 0),)

    def __repr__(self):
        return "Polynomial({polynomial})".format(polynomial=self.polynomial)

    def __str__(self):
        connectives = {(True, True): "-", (True, False): "",
            (False, True): " - ", (False, False): " + "}
        term_strings = []
        for i, (coeff, power) in enumerate(self.polynomial):
            coeff_format = "{coeff}" if abs(coeff) != 1 or power == 0 else ""
            var_format = "x" if power != 0 else ""
            power_format = "^{power}" if power != 0 and power != 1 else ""
            term_format = coeff_format + var_format + power_format
            term_string = term_format.format(coeff=abs(coeff), power=power)
            term_strings.append(connectives[i == 0, coeff < 0] + term_string)
        return "".join(term_strings)

############################################################
# Section 7: Feedback
############################################################

feedback_question_1 = "Solution."

feedback_question_2 = "Solution."

feedback_question_3 = "Solution."
