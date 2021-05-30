def my_print(txt):
    print(txt)


msg_template = """ Hello {name},
we are delighted to see you in {website}.
we are happy to see you. 
"""

def format_msg(my_name='Arnob', my_website='lol.me'):
    my_msg =  msg_template.format(name=my_name, website=my_website)
    print(my_msg)
    return my_msg


def base_function(*args, **kwargs):
    print(args, kwargs)