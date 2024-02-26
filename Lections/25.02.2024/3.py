import re 

text = """100  ИНФ  Информатика 213  МАТ  Математика 156  АНГ  Английский"""

print(re.findall('\s\D\D\D\s',text))
print(re.findall('\s\D{3}\s',text))  #
print(re.findall('[А-ЯЁ]{3}',text))

print(re.findall('\s[А-ЯЁ][а-яё]+',text))
print(re.findall('[а-яА-ЯёЁ]{4,}',text))  #

course_pattern = '([0-9]+)\s*([А-ЯЁ]{3})\s*([а-яА-ЯёЁ]{4,})'
print(re.findall(course_pattern, text) )