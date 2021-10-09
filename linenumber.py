import sys, re

pattern = re.compile(r"\s+(\d+)$")

def linenumber(filename):
    outputs = []
    
    # 本文の取り出し
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                outputs.append(re.sub(pattern, '', line[:-1]))
    except FileNotFoundError:
        print("ファイルが存在しません:", filename)
        return

    # 行の追加
    text = ""
    for i, o in enumerate(outputs):
        text += o
        if i % 16 == 0:
            text += '    ' + str(i + 1)
        text += '\n'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        print("行番号を更新しました:", filename)

def main(args):
    if len(args) < 1:
        print("ファイルを指定してください")
        return
    filename = args[1:]
    for f in filename:
        linenumber(f)

if __name__ == "__main__":
    main(sys.argv)
