from pybtex.database.input import bibtex

#open a bibtex file
parser = bibtex.Parser()
bibdata = parser.parse_file("homework_10_refs.bib")

#loop through the individual references
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    try:
        # change these lines to create a SQL insert
        # print b["Keywords"]
        # print b["Author"]
        # print b["Journal"]
        # print b["Volume"]
        # print b["pages"]
        # print b["Year"]
        # print b["Title"]
        print b["title"]
        print b["journal"]
        print b["year"]
        print b["volume"]
        print b["author"]
    # field may not exist for a reference
    except(KeyError):
        continue