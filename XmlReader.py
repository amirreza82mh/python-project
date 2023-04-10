import xml.etree.ElementTree as ET
tree = ET.parse('Automata.xml')
root = tree.getroot()

alphabet = ['','']
i = 0
finalstate = ''
state = ['','']
initialState = ''
transition =[['','',''],
              ['','',''],
              ['','','']
]

for child in root:
    if child.tag == 'Alphabets':
        for grandchild in child:
            alphabet[i] = grandchild.get('letter')
            i += 1
        i = 0
    elif child.tag == 'States':
        for grandchild in child:
            if grandchild.tag == 'FinalStates':
                for grandson in grandchild:
                    finalstate = grandson.get('name')
            elif grandchild.tag == 'state':
                state[i] = grandchild.get('name')
                i += 1
            elif grandchild.tag == 'initialState':
                initialState = grandchild.get('name')
        i = 0
    elif child.tag == 'Transitions':
        for grandchild in child:
            transition[i][0] = grandchild.get('source')
            transition[i][1] = grandchild.get('destination')
            transition[i][2] = grandchild.get('label')
            i += 1            

print('Alphabets:')
print(f'alphabet1 = {alphabet[0]}')
print(f'alphabet2 = {alphabet[1]}')
print('--------------------------------------')
print('States:')
print(f'state1 = {state[0]}')
print(f'state2 = {state[1]}')
print(f'initial State = {initialState}')
print(f'final State = {finalstate}')
print('--------------------------------------')
print('Transitions:')
print(f'from \'{transition[0][0]}\' to \'{transition[0][1]}\' with \'{transition[0][2]}\'')
print(f'from \'{transition[1][0]}\' to \'{transition[1][1]}\' with \'{transition[1][2]}\'')
print(f'from \'{transition[2][0]}\' to \'{transition[2][1]}\' with \'{transition[2][2]}\'')
print('___________________________________\n\n')

while True:
    accept = True
    CurrentState = initialState
    MyString = input('Enter String : ')
    if MyString == 'end':
        break
    for s in MyString:
        if s == alphabet[0] or s == alphabet[1]:
            accept = True
        else:
            accept = False
        if CurrentState == transition[0][0]:
            if s == transition[0][2]:
                CurrentState = transition[0][1]
            # elif s == transition[1][2]:
            #     CurrentState = transition[1][1]
        if CurrentState == transition[1][0]:
            # if s == transition[0][2]:
            #     CurrentState = transition[0][1]
            if s == transition[1][2]:
                CurrentState = transition[1][1]
        if CurrentState == transition[2][0]:
            if s == transition[2][2]:
                CurrentState = transition[2][1]
            else:
                accept = False
                continue
    if accept :
        if CurrentState == state[0]:
            print('the input string is not accepted')
        elif CurrentState == state[1]:
            print('the input string is accepted')
    else:
        print('the input string is not accepted')


