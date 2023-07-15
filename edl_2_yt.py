import re

def convert_to_youtube_timestamps(edl_timestamps):
    return edl_timestamps[:8]

def edl_2_yt(filename):
    with open(filename, 'r') as file:
        data = file.read().replace('\r', '')

    d2 = data.replace("\n", " ")
    d3 = d2.replace("|D:1", "|D:1\n")
    marker_title_search = re.findall(r'\|M:(.*?)\s*\|', d3)
    start_time = re.findall(r'\d{2}:\d{2}:\d{2}:\d{2}', d3)
    lines = d3.split('|D:1')
    for l in lines:
        print(l)

    # chapter_starts = [re.findall(r'\d\d:\d\d:\d\d:\d\d', line) for line in lines if re.search('\d\d:\d\d:\d\d:\d\d', line)]
    chapter_starts = [convert_to_youtube_timestamps(re.findall(r'\d\d:\d\d:\d\d:\d\d', line)[0]) for line in lines if re.search('\d\d:\d\d:\d\d:\d\d', line)]
    chapter_titles = [re.findall(r'\|M:.*', line) for line in lines if '|M:' in line]

    for i, start_time in enumerate(chapter_starts):
        if i < len(chapter_titles):
            chapter_title = chapter_titles[i][0].replace("|M:","").replace("\n","").strip()
            # print(f"{start_time} - {chapter_titles[i]}")
            print(f"{start_time} - {chapter_title}")


    
if __name__ == "__main__":
    import sys
    edl_2_yt(sys.argv[1])

