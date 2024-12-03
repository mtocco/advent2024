# https://adventofcode.com/2024/day/3

from datetime import datetime
import subprocess

def stripMeDaddy(line):
    strippedLine = line.replace('mul(','').replace(')','').split(',')
    return (int(strippedLine[0])*int(strippedLine[1]))
    
def main():
    start_time = datetime.now()
    command = ['grep', '-Eo', r'mul\([0-9]+,[0-9]+\)', 'advent2024Day3Input.txt']
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    splitLines = result.stdout.split('\n')
    total = 0
    
    for i in splitLines:
        try:
            total += stripMeDaddy(i)
        except:
            pass
        
    print(total)

    command = ['grep', '-Eo', r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)', 'advent2024Day3Input.txt']
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    splitLines = result.stdout.split('\n')
    totalPtTwo = 0
    
    mulEnabled = True
    for i in splitLines:
        
        if 'do()' in i:
            mulEnabled = True
        elif "don't()" in i:
            mulEnabled = False
        if not mulEnabled:
            continue
        if mulEnabled and 'mul' in i:
            try:
                totalPtTwo += stripMeDaddy(i)
            except:
                pass
    print(totalPtTwo)
    
main()
