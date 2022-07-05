# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/pytho

import re

def to_camel_case(text):
    words = re.split(r'[_\-]', text)
    return words[0] + ''.join(w.title() for w in words[1:])


assert to_camel_case('') == '', "An empty string was provided but not returned"
assert to_camel_case(
    "the_stealth_warrior") == "theStealthWarrior", f'{to_camel_case("the_stealth_warrior")} != theStealthWarrior'
assert to_camel_case(
    "The-Stealth-Warrior") == "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value"
assert to_camel_case(
    "A-B-C") == "ABC", "to_camel_case('A-B-C') did not return correct value"
