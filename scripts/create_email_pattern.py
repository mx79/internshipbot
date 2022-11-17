import pandas as pd
from urllib.parse import urlparse

with open('../email/mail.csv', 'a') as f:
    sites = list(pd.read_csv('../web/sites.csv')['sites'])
    for site in sites:
        if site[:4] == "http":
            site = urlparse(site).netloc
            if site[:4] == "www.":
                site = site[4:]
        elif site[:4] == "www.":
            site = site[4:]
        for elem in ['info', 'hello', 'contact']:
            f.write('\n{0}@{1}'.format(elem, site))
