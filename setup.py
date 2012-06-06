"""
Setup elasticsearch-server.
"""
import os

from distutils.core import setup

def _collect(path):
    entries = []
    for entry in os.listdir(path):
        joined_entry = os.path.join(path, entry)
        if os.path.isfile(joined_entry):
            entries.append(os.path.join(joined_entry))
    return entries

if __name__ == '__main__':
    setup(name="Elasticsearch Server",
          version="0.19.4",
          description="Wrapper to get elastic search in a virtual env for ease of development.",
          url="http://wingu.com/",
          author="Wingu",
          author_email="eric@wingu.com",
          scripts=_collect('bin'),
          data_files=[('lib/elasticsearch', _collect('lib'))]
          )

