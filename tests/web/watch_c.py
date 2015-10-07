import os

import watch_d


# This service reports its name and file mtime, plus whatever some sub service
# uses
def run(*args, **kwargs):
    response = 'Watch C [%s]' % str(os.path.getmtime(__file__))
    result = watch_d.run(*args, **kwargs)
    if isinstance(result, basestring):
        response += '\n' + result
    return response