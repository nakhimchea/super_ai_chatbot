import os


def main():
    files = os.listdir(os.path.join('CX-KM'))
    file_names = []
    for file in files:
        file_names.append(file.split('.json')[0])

    file_names = sorted(file_names)
    for name in file_names:
        if ('_1' not in name) and ('_usersays_km' not in name) and ('_usersays_en' not in name):
            try:
                os.remove(os.path.join('CX-KM/{}.json'.format(name)))
            except:
                print("Deleted")
        if '_1' not in name:
            try:
                os.rename(os.path.join('CX-KM/{}.json'.format(name)), os.path.join('CX-KM/{}'.format(name[:-12]+'_1{}.json'.format(name[-12:]))))
            except:
                print("Renamed")


if __name__ == '__main__':
    try:
        main()
    except EOFError or KeyboardInterrupt:
        print("Error Interrupted.")
