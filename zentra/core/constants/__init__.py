LOWER_CAMELCASE_WITH_DIGITS = r"^[a-z]+(?:[A-Z][a-z]*)*\d*$"
LOWER_CAMELCASE_SINGLE_WORD = r"^[a-z]+(?:[A-Z][a-z]*)*$"
LOWERCASE_SINGLE_WORD = r"^[a-z]+\b$"
PASCALCASE_SINGLE_WORD = r"^[A-Z][a-zA-Z]*$"
PASCALCASE_WITH_DIGITS = r"^[A-Z][a-zA-Z0-9]*$"
COMPONENT_TAG_NAME_PATTERN = r"<([A-Z][a-zA-Z]*)"

PARAMETER_PREFIX = "$."

COMPONENT_FILTER_LIST = [
    "FormField",
]
