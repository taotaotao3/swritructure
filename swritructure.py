
# -*- coding: utf-8 -*-
'''
 1:import os などあったら、半角スペースから改行までのスペルを書き出す。
 2:それ＋.でメソッドが使われているはず　os.pathのあとに『(,.," "』があれば終わり。それがメソッド名を書き出す。
 3:もし最後が.なのであればさらにメソッドが続いているはずで、そのときは2をもう一度。前のメソッド.付きでメソッド名を書き出す。
 4:2と3それぞれ書き出したら、そのメソッド内にif文がないか、メソッドがないか、出力がないかメソッドがさらにないか探す。
   4-1:もしif文があれば条件文を探す。その文の条件をみて、１つ１つの条件ごと分岐して4をその中で行う。
   
4-2:メソッドがみつけたら、4を繰り返す。
   4-3:もしprint(が見つかれば、それを書き、次の行へ改行後にclassやdef、ファイルの最後の行があるまで
'''
import os , sys , codecs
import pdb
import re
import glob
#プログラム1｜ライブラリの設定
import pathlib
import os
import pdb
import re

print('◆◆◆◆◆◆実行スタートファイル◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆')
# 引数でファイル名を記載させ、そのpyファイルの読み込み
args = sys.argv
print('引数⇒スタートファイル名:', str(args[1]))
print('◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆')

def from_file_list_export(start_file):
    # 下階層全ディレクトリ付きファイル抽出リスト
    all_directory_list = []

    #プログラム2｜mainプロシージャ

    Folderpath = os.getcwd()#対象フォルダを指定


    #プログラム3｜階層ごとのフォルダやファイルを書き出す関数
    def GetFolderFileNames(path, kaiso, all_directory_list_arg):
        # files = pathlib.Path(path).glob('*')#その階層のフォルダやファイルを取得
        files = os.listdir(path)#その階層のフォルダやファイルを取得
        all_directory_list_ch = []

        # プログラム4｜フォルダやファイルを一つずつ書き出す
        for file in files:
            output = file
            all_directory_list_ch.append(str(path) + '\\' + output)
            all_directory_list_ch.append(kaiso)
            all_directory_list_arg.append(all_directory_list_ch)
            all_directory_list_ch = []
            # プログラム5｜フォルダの場合、その下の階層のフォルダやファイルをGetFolderFileNames(プログラム6)を呼び出す
            #if not file[:3] == '.xml' or file[:3] == '.csv' or file[:3] == '.xml' or file[:3] == '.xml' or file[:3] == '.xml' or :
            if os.path.isdir(file) == True:

                print('file:',file)
                GetFolderFileNames(path + "\\" + file, kaiso+1, all_directory_list_arg)
        return all_directory_list_arg

    all_directory_list = GetFolderFileNames(Folderpath, 0, all_directory_list)#GetFolderFileNames(プログラム3)を呼び出す

    files = glob.glob("./*")
    print('◆◆◆◆◆◆現在のフォルダにあるファイル一覧◆◆◆◆◆◆◆◆◆')
    for file in files:
        print(file)

    # カレントディレクトリのファイル一覧をリストに詰める
    current_directory_files_list = os.listdir('./')


    ############################################################
    #!/usr/bin/python
    # -*- coding: utf-8 -*-
    # vim: fileencoding=utf-8

    grep_result = []
    def grep_method(search_dir, search_pattern):
        output_list = []
        DIR_NAME = search_dir
        SEARCH_WORD = search_pattern
        #FLAG_STDOUT = True
        write = sys.stdout.write
        for dirpath, dirs, files in os.walk(DIR_NAME):
            for fn in files:
                path = os.path.join(dirpath, fn)
                count = 0
                enc = 'utf-8'
                try:
                    for l in codecs.open(path, 'r', enc):
                        count = count + 1
                        if SEARCH_WORD in l:
                            output = ''
                            try:
                                output = '"' + path + '","' + str(count) + '","' + SEARCH_WORD + '","' + l.replace('"',"'").replace('\r','').replace('\n','') + '"\r\n'
                                print('output:', output)
                                output_list.append(str(path))
                                output_list.append(str(count))
                                output_list.append(SEARCH_WORD)
                                output_list.append(str(l.replace('"',"'").replace('\r','').replace('\n','')))
                                grep_result.append(output_list)
                                output_list = []       
                            except:
                                continue
                            # if FLAG_STDOUT == True:
                            #     write(output)
                            # out.write(output)
                            
                except:
                    continue
        return grep_result

    #grep_result = grep_method('./', "getTopURLStatus(")

    # ['./testfolder\\testfolder2\\testfile2.txt', '2', 'ge


    print('ここがスタートファイルのスタート')
    # start_file = str(args[1]) # Webscrape.py

    print('◆◆◆◆◆◆fromのあとにくるpyファイル名をfrom_listリストに詰める◆◆◆◆◆◆◆◆◆')
    def make_from_list(arg_file):
        f = open(arg_file, 'r', encoding='utf-8')
        datalist = f.readlines()

        # """"""で囲まれたところを削除
        datalist = re.sub(r'\"\"\"(.*?)\"\"\"','',str(datalist))

        # 改行統一
        datalist = datalist.replace('\\r\\n','\\r')
        datalist = datalist.replace('\\n','\\r')

        # #と\rで囲まれたところを全て削除
        datalist = re.sub(r'#(.*?)\\r','',datalist)

        while_flag = True
        from_list = []
        from_list_ch = []
        datalist_from_import = datalist
        while(while_flag):
            # from から import に記載ある関連pyファイル名を抜き出す
            try:
                datalist_from_import = datalist_from_import.replace('from ','fffff')
                datalist_from_import = datalist_from_import.replace(' import','iiiii')
            except:
                print('from等なし')
            try:
                datalist_from_file = (re.search(r'fffff(.*?)iiiii', datalist_from_import))[0].replace('fffff','').replace('iiiii','')
                print(datalist_from_file)
                datalist_import_file = (re.search(r'iiiii(.*?)\\r', datalist_from_import))[0].replace('fffff','').replace('iiiii','').replace('\\r','')
                print(datalist_import_file)
                from_list_ch.append(datalist_from_file)
                from_list_ch.append(datalist_import_file)
                from_list.append(from_list_ch)
                from_list_ch = []
                datalist_from_import = datalist_from_import.replace('fffff' + datalist_from_file + 'iiiii', '')
            except:
                print('ffff pyファイル名 iiiii がもうない')
                while_flag = False
                break
        f.close()
        return from_list

    from_file_list = make_from_list(start_file)

    return from_file_list

start_file = str(args[1]) # Webscrape.py
from_file_list = from_file_list_export(start_file)

# (Pdb) from_file_list
# [['createData', ' getTopURLStatus, getProfileInformation'], ['ccccccc', ' ttttttttt']]
print('◆◆◆◆◆◆一回メモに書いちゃおう◆◆◆◆◆◆◆◆◆')
file_last = open('structure.txt', 'w')
file_last.write('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■' + '\r\n')
file_last.write(str(args[1]) + '\r\n')


'''
Webscrape.py(start file)
    |
    ∟ createDate.py(from information)
    |   |
    |   checkTorihiki(import information)
    |   |
    |   getProfileInformation(import information)
    |
    ∟ ccccccc.py(from information)
        |
        ttttttttt(import information)
'''
from_file_list_next = []

file_last.write('     |' + '\r\n')
if from_file_list != []:

    for num, n in enumerate(from_file_list):

        file_last.write('    ∟' + str(from_file_list[int(num)][0]) + '.py\r\n')
        # Webscrape.py(start file)
        #     |
        #     ∟ createDate.py(from information)
        if ',' in from_file_list[int(num)][1]:

            # import が１つのみではないとき
            import_list = from_file_list[int(num)][1].split(',')
            for m in import_list:

                # import が１つにしてから
                import_method = m.strip() # 前後の空白をなくす

                if int(num) + 1 > len(from_file_list):

                    # 次のfrom ファイルがないとき
                    file_last.write('        |' + '\r\n')
                    file_last.write('        ' + str(import_method) + '()\r\n')

                else:
                    # 次のfrom ファイルがあるとき
                    file_last.write('    |   |' + '\r\n')
                    file_last.write('    |   ' + str(import_method) + '()\r\n')

                    from_file_list_next = from_file_list_export(str(from_file_list[int(num)][0]) + '.py')

                    # str(from_file_list[int(num)][0]) + '.py' のstr(import_method) + '()' の次のメソッドまでの読み込み
                    with open('./' + str(from_file_list[int(num)][0]) + '.py', encoding='utf-8', errors='ignore') as f:

                        for line_ch in f:
                            print(line_ch)
                            # もし先頭にdefがきたら次のメソッドに来ているので飛ばす
                            if (line_ch.strip())[:3] == 'def':
                                continue                          
                            for num_ffln, from_file_list_next_ch in enumerate(from_file_list_next):
                                
                                if from_file_list_next_ch[1].strip() in line_ch:
                                    method_name = from_file_list_next_ch[1].strip()
                                    # 読み込んだ該当1行にfrom内pyファイル名あり
                                    #if from_file_list_next_ch[1].strip() + '(' in line_ch:
                                    # 前に何か記載があり、指定のメソッド名のあとに半角スペースと（があり、後続に何か続くとき
                                    if re.search(rf'\b(?=\w)(.*?){method_name}(.*?)\((.*?)(?!\w)', str(line_ch)):
                                        print('Bingo！！！！！！！！！！')

                                        # さらに.カンマから(カッコまでのものがあったので抽出
                                        method_text = re.search(rf'\b(?=\w)(.*?){method_name}(.*?)\((.*?)(?!\w)', str(line_ch))

                                        print('aa')

                                        if int(num_ffln) + 1 == len(from_file_list_next):
                                            # 次のfrom ファイルがないとき
                                            file_last.write('    |    |  　|' + '\r\n')
                                            file_last.write('    |    |    ∟' + str(from_file_list_next_ch[0]) + '.py\r\n')
                                            file_last.write('    |    |    　         |' + '\r\n')
                                            file_last.write('    |    |               ' + str(method_name) + '()\r\n')
                                        else:
                                            # 次のfrom ファイルがあるとき
                                            file_last.write('    |    |  　|' + '\r\n')
                                            file_last.write('    |    |    ∟' + str(from_file_list_next_ch[0]) + '.py\r\n')
                                            file_last.write('    |    |  　|          |' + '\r\n')
                                            file_last.write('    |    |    |          ' + str(method_name) + '()\r\n')
        else:
            import_method = from_file_list[int(num)][1]
            # import が１つにしてから
            import_method = m.strip() # 前後の空白をなくす

            if int(num) + 1 > len(from_file_list):

                # 次のfrom ファイルがないとき
                file_last.write('        |' + '\r\n')
                file_last.write('        ' + str(import_method) + '()\r\n')

            else:
                # 次のfrom ファイルがあるとき
                file_last.write('    |   |' + '\r\n')
                file_last.write('    |   ' + str(import_method) + '()\r\n')

                from_file_list_next = from_file_list_export(str(from_file_list[int(num)][0]) + '.py')

                with open('./' + str(from_file_list[int(num)][0]) + '.py', encoding='utf-8', errors='ignore') as f:

                    for line_ch in f:
                        print(line_ch)
                        
                        for num_ffln, from_file_list_next_ch in enumerate(from_file_list_next):
                            
                            if from_file_list_next_ch[1].strip() in line_ch:
                                method_name = from_file_list_next_ch[1].strip()
                                print('from_file_list_next_ch[1].strip()■■■：', from_file_list_next_ch[1].strip())
                                print('line_ch■■■:', line_ch)


                                # TEXTO= "Var"
                                # subject= r"Var\boundary"
                                # if re.search(rf"\b(?=\w){TEXTO}(.*?)\\boundary(?!\w)", subject, re.IGNORECASE):
                                #     print("match")
                                # pdb.set_trace()
                                
                                # 読み込んだ該当1行にfrom内pyファイル名あり
                                #if from_file_list_next_ch[1].strip() + '(' in line_ch:
                                # 前に何か記載があり、指定のメソッド名のあとに半角スペースと（があり、後続に何か続くとき
                                if re.search(rf'\b(?=\w)(.*?){method_name}(.*?)\((.*?)(?!\w)', str(line_ch)):
                                    print('Bingo！！！！！！！！！！')

                                    # さらに.カンマから(カッコまでのものがあったので抽出
                                    method_text = re.search(rf'\b(?=\w)(.*?){method_name}(.*?)\((.*?)(?!\w)', str(line_ch))

                                    print('aa')

                                    if int(num_ffln) + 1 == len(from_file_list_next):
                                        # 次のfrom ファイルがないとき
                                        file_last.write('    |        ∟' + str(from_file_list_next_ch[0]) + '.py\r\n')
                                        file_last.write('            　         |' + '\r\n')
                                        file_last.write('                       ' + str(method_name) + '()\r\n')
                                    else:
                                        # 次のfrom ファイルがあるとき
                                        file_last.write('    |        ∟' + str(from_file_list_next_ch[0]) + '.py\r\n')
                                        file_last.write('    |      　|         |' + '\r\n')
                                        file_last.write('    |        |         ' + str(method_name) + '()\r\n')

            # import が１つのみのとき
            import_method = from_file_list[int(num)][1].strip() # 前後の空白をなくす
 
            if int(num) + 1 == len(from_file_list):
                # 次のfrom ファイルがないとき
                file_last.write('        |' + '\r\n')
                file_last.write('        ' + str(import_method) + '()\r\n')
            else:
                # 次のfrom ファイルがあるとき
                file_last.write('    |   |' + '\r\n')
                file_last.write('    |   ' + str(import_method) + '()\r\n')

file_last.close()
