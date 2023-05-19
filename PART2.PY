
import re
string = " ola bom dia flor do dia meu bem jao olsebn, sexo poutas, "
print(re.search(r'meu',string)) # onde está
print(re.findall(r'd',string)) # quantidade

print(string[25:28])