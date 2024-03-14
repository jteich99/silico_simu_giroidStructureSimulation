import sys
latestTime = sys.argv[1]

with open('Co.sh', 'w') as outputCoFile, open(f'{latestTime}/Co', 'r') as sourceCoFile:
    sourceLines = sourceCoFile.readlines()
    maxCo = 0
    toggle = False
    for line in sourceLines:
        if line.startswith('('):
            toggle = True # para hacer que empiece a samplear una vez esta leyendo los valores del campo propiamente
        if toggle:
            try:
                Co = float(line.rstrip('/n'))
                if Co > maxCo:
                    maxCo = Co
                    # print(f'new maxCo = {maxCo}')
            except:
                pass
    # print(f'deltaTime for Co = 1 = {1/maxCo}') 
    outputCoFile.writelines(
        f'maxCo={maxCo}\n' +
        f'deltaTime={ 0.8 / maxCo}'
    )
        # finally:
        #     pass
        # if line.charAt(0)

