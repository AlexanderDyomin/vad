from vad import split_string
some = ['cyka blyat', 'hehe-heh-e blya', '1-2-3-4-5-6', '. . ? = & = ) order by -- ']
some = list(map(lambda x: x.lower(), some))
some = list(map(split_string, some))
print(some)