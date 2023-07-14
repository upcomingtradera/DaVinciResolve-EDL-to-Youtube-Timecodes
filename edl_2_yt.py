import re
import sys

def edl_2_yt(filename):
    with open(filename, 'r') as f:
        content = f.read()

    lines = content.split('\n')

    chapter_titles = [re.findall(r'\|M:(.*?)\s*\|', line)[0] for line in lines if '|M:' in line]
    timecodes = [re.findall(r'\d\d:\d\d:\d\d:\d\d', line) for line in lines if re.match(r'\d\d\d\s\s\d\d\d', line)]

    if len(chapter_titles) == len(timecodes):
        for i in range(len(chapter_titles)):
            start_time = timecodes[i][0][:-3]  # Remove the frames part of the timecode
            print(f"{start_time} - {chapter_titles[i]}") 

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 convert_edl_to_youtube.py filename.edl')
        sys.exit(1)
    
    filename = sys.argv[1]
    edl_2_yt(filename)
