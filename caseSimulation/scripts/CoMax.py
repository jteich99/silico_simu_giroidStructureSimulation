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
    deltaTime = 0.8 / maxCo
    if deltaTime < 0.01 and deltaTime > 0.005:
        deltaTime = 0.005
    elif deltaTime < 0.025 and deltaTime > 0.01:
        deltaTime = 0.01
    elif deltaTime < 0.05 and deltaTime > 0.025:
        deltaTime = 0.025
    elif deltaTime < 0.1 and deltaTime > 0.05:
        deltaTime = 0.05
    elif deltaTime < 0.25 and deltaTime > 0.1:
        deltaTime = 0.1
    elif deltaTime < 0.5 and deltaTime > 0.25:
        deltaTime = 0.25
    elif deltaTime < 1 and deltaTime > 0.5:
        deltaTime = 0.5
    elif deltaTime < 2.5 and deltaTime > 1:
        deltaTime = 1
    elif deltaTime < 5 and deltaTime > 2.5:
        deltaTime = 2.5
    elif deltaTime < 10 and deltaTime > 5:
        deltaTime = 5
    elif deltaTime > 10:
        deltaTime = 10


    outputCoFile.writelines(
        f'maxCo={maxCo}\n' +
        f'deltaTime={ deltaTime }'
    )
        # finally:
        #     pass
        # if line.charAt(0)

