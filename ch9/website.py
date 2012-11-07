def squish(website):
    webStringy = urllib.urlopen(website)
    
    for line in webStringy:
        newline = line #this seems necessary to get line converted properly to a string.
        newline.seek(45)
        
        for achar in newline:
            if achar == '<':
                achar = '***********'
                print achar,
            else:
                print achar,

#squish('http://scintillus.com')
