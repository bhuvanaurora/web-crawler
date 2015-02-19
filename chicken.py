import mechanize

def if_chicken_exists():
    b = mechanize.Browser()
    b.set_handle_robots(False)
    fd = b.open("http://www.dominos.com")
    #print fd.read()
    fd.seek(0)
    return 'chicken' in fd.read().lower()

if __name__ == '__main__':
    if if_chicken_exists():
        print 'Yes!'
    else:
        print 'No'