s='   hello      world     '
print(s,
s.strip(),
s.lstrip(),
s.rstrip(),sep='\n')

s='string.py'
print(s,
s.startswith('str'),
s.startswith('gfg'),
s.endswith('py'),
s.endswith('js'),
'hwjefgg'.isalpha(),
'deuiehd@12333'.isalpha(),sep='\n')

print('3456789'.isalpha(),
'123456789'.isalnum(),
'fghuytrfghuihgkh'.isalnum(),
'fgdhdygvfdhjsdh1234567'.isalnum(),
'naresh'.islower(),
'sdfghjkl12345!@#$%^'.islower(),
'SDFGHJ!!!!!!@#$%12345'.isupper(),
' '.isspace(),
'hello         '.isspace(),
'Py Prg Lan'.istitle(),
'Py prg'.istitle(),
'py_prg'.isidentifier(),
'py@123'.isidentifier(),sep='\n')
