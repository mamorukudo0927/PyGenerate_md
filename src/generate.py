from pathlib import Path
import os

'''Pythonでファイル出力を行う。
    ファイル名とフルパスが渡されたときはそのまま作成
    ファイル名のみ渡されたときはカレントディレクトリにファイル作成
    存在しないファイルパスの時はディレクトリ作成→ファイル作成
    @param fileName ファイル名
'''
def exportMd(fileName) :
    path = Path(fileName) 
    if fileName not in '/' :
        Path(os.path.join(os.getcwd(), fileName))
    if os.path.exists(path) :
        path.touch()
    else :
        dirPath = os.path.split(fileName)
        path = Path(dirPath[0])
        path.mkdir()
        os.chdir(path)
        path = Path(dirPath[1].split('.'))
        path.touch()

exportMd('test.md')