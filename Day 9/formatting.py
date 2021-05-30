msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
""" # .format(name="Justin", website='cfe.sh')

def format_msg(my_name="Arnob", my_website="baba.marley.com"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg


