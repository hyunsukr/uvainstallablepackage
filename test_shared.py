import shared as sh
sh.afunction()

sh.max_function()

sh.new_func()

print(sh.clean_string('hello world'))

print(sh.clean_string(' hello world '))


print(sh.clean_string('hello - -: -. wOr1d'))


print(sh.space_compress('word word        word2'))

multiline_string = '''
first line
second line
'''
print(sh.space_compress(multiline_string))

print(sh.space_compress(10))



