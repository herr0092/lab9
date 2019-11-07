import os
from gfxhat import lcd, backlight, fonts
import herr0092_library as f

# ============
# TASK 1
# ============
def createCsvFile( fileName, fileOutputName ):
    foutCSV = open( fileOutputName, 'w')
    finTXT  = open( fileName, 'r') 

    foutCSV.write('First Name, Count\n')

    for line in finTXT:
        newLine = line.split(' ')
        newLine = ','.join(newLine)
        foutCSV.write(newLine)

    foutCSV.close();
    finTXT.close();

# Create Boys CSV
createCsvFile('2000_BoysNames.txt','2000_BoysNames.csv')

# Create Girls CSV
createCsvFile('2000_GirlsNames.txt','2000_GirlsNames.csv')

# ============
# TASK 2
# ============
filename = input('Enter file name:')
filename = filename + '.csv'

if ( os.path.exists(filename) ):
    foutCSV = open( filename, 'r')
    for line in foutCSV:
        print( line.split(',') )
else:
    print('File do not exist')


# ============
# TASK 3
# ============
foutFont3File = open( 'font3.txt', 'r')
dictionary = {}

for line in foutFont3File:
    newLine = line.split(',')
    key   = newLine[1][0]
    value = newLine[0][2:]

    dictionary[key] = value


def getObjectFromLetter( l ):
    hexa  = dictionary[l]
    listArr = [ 
        hexa[0:2], 
        hexa[2:4], 
        hexa[4:6],
        hexa[6:8],
        hexa[8:10],
        hexa[10:12],
        hexa[12:14],
        hexa[14:16]
    ]
    
    newObject = []
    for pair in listArr:
        binary = bin( int(pair,16) )
        strBinary  = str(binary)[2:].zfill(8) # 01000110
        # print( pair , strBinary )
        listOfBinariesStrs = list(strBinary);
        listOfBinaries = [];
        for i in listOfBinariesStrs:
            listOfBinaries.append( int(i) )

        newObject.append( listOfBinaries )
        # newObject.append( list(strBinary) )

    return newObject

letter = input('Enter a letter to print: ')

if ( letter in dictionary ):
    obj = getObjectFromLetter( letter )
    # Prepare the Screen
    f.clearScreen()
    f.displayObject( obj, 40,20)
else:
    print('Letter not in dictionary')


# Just for fun, Im going to print every letter inside the dictionary
for key in dictionary:
    obj = getObjectFromLetter( key )
    f.displayObject( obj, 40,20)
    f.dormir(0.5)
    