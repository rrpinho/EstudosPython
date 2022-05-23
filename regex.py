import re

a = re.match('Py', 'Python')
print(a)
print(a.group())

print(re.match('[pP]y', "python"))
print(re.match('[a-zA-Z]y', 'Python'))
print(re.findall('[a-zA-Z]y', 'Python jython'))
print(re.findall('[a-zA-Z] [a-zA-Z]', 'Python jython'))
print(re.findall('[a-zA-Z] [a-zA-Z]+', 'Python jython'))
print(re.findall('[a-zA-Z] [a-zA-Z]{1,3}', 'Python jython'))
print(re.findall('\w+', 'Python jython'))

print(re.search(r'teste[a-z]{2}$', 'testes'))

end = 'www.site.com/clientes/1'
print(re.search(r'clientes/\d+$', end))
print(re.split(r'clientes/(?P<id>\d+)', end))
print(re.split(r'(clientes)/(?P<id>\d+)', end))