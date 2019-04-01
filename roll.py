import re
import dice

def Roll(eq):
    removed_whitespace_eq = eq.replace(' ', '')
    output = {
        'result': 0,
        'equation': eq,
        'dice breakdown': eq
    }

    pattern = r'\d+d\d+!?[^h|l|+|-]'
    for match in re.findall(pattern, removed_whitespace_eq):
        #print(match)
        if match[-1:] == '!':
            isExploding = True
        else:
            isExploding = False

        count = int(match.split('d')[0])
        sides = int(match.split('d')[1].replace('!',''))

        match_die = dice.Die(sides, isExploding, False)
        
        match_roll = match_die.RollN(count)
        output['equation'] = output['equation'].replace(match, str(match_roll['result']), 1)
        output['dice breakdown'] = output['dice breakdown'].replace(match, str(match_roll['dice']), 1)
    
    chooser = r'\d+d\d+h\d+'
    for keep in re.findall(chooser, removed_whitespace_eq):
        #print(keep)
        count = int(keep.split('d')[0])
        sides = int(keep.split('d')[1].split('h')[0])
        k = int(keep.split('h')[1])

        keep_die = dice.Die(sides, False, False)

        keep_roll = keep_die.RollN(count)
        kept = sorted(keep_roll['dice'])[-k:]
        dropped = sorted(keep_roll['dice'])[0:count-k]
        #print('dropped: {}'.format(dropped))
        #print('kept: {}'.format(kept))
        
        output['equation'] = output['equation'].replace(keep, str(sum([sum(i) for i in kept])), 1)
        output['dice breakdown'] = output['dice breakdown'].replace(keep, str(kept), 1)
        
        output['result'] = sum([sum(i) for i in kept])
        #print(output['result'])

    dropper = r'\d+d\d+l\d+'
    for drop in re.findall(dropper, removed_whitespace_eq):
        count = int(drop.split('d')[0])
        sides = int(drop.split('d')[1].split('l')[0])
        r = int(drop.split('l')[1])

        reject_die = dice.Die(sides, False, False)

        reject_roll = reject_die.RollN(count)
        kept = sorted(reject_roll['dice'])[0:r]
        dropped = sorted(reject_roll['dice'])[r-count:]
        #print('dropped: {}'.format(dropped))
        #print('kept: {}'.format(kept))

        output['equation'] = output['equation'].replace(drop, str(sum([sum(i) for i in kept])), 1)
        output['dice breakdown'] = output['dice breakdown'].replace(drop, str(kept), 1)

        output['result'] = sum([sum(i) for i in kept])
        #print(output['result'])

    try:
        #print('start try block')
        #print('before: {} --- {}'.format(output['result'], output['equation']))
        output['result'] = eval(output['equation'])
        #print('after: {} --- {}'.format(output['result'], output['equation']))
    except:
        print('')
    return output

i = input()
while i != '':
    r = Roll(i)
    print('Result: {}'.format(r['result']))
    print('Dice: {}'.format(r['dice breakdown']))
    i = input()