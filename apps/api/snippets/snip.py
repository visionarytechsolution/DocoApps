import random
import string
import math

def random_password():
        password = ''.join(random.sample(string.ascii_lowercase, 8))
        return password

def email_or_sms_it(**kwargs):
    pass

#### Paginator 

perpage = 100

def paginate(page):
        try:
            page = page
        except:
            page = 0
        start = perpage * page
        end = start + perpage

        return start, end

def page_count(r):
      total = r.count()
      pages = math.ceil(total / perpage) 

      return pages
