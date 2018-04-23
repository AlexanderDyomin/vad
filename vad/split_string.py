import re

def split_string(url_str):
    resulted = re.split('(\W)', url_str)
    resulted = list(filter(lambda x: x!='', resulted))
    res_string = ' '.join(resulted)
    return res_string