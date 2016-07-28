import os
import Generator

directories = [name for name in os.listdir('./') if os.path.isdir(os.path.join('./', name))]
directories.remove(".idea")
directories.remove("__pycache__")
directories.remove(".git")
print(directories)

client_ip = ''
brand = ''
platform = ''
version = ''
action = ''

counter = 0
for dir in directories:
    subdirectory = './' + directories[counter] + '/result/'
    print(subdirectory)
    capture_names = [name for name in os.listdir(subdirectory) if os.path.isdir(os.path.join(subdirectory, name))]
    print(capture_names)

    capture_counter = 0
    for cap in capture_names:
        name = capture_names[capture_counter]
        print(name)

        sheet_directory = './' + directories[counter] + '/result/' + name + '/'
        print(sheet_directory)
        sheet_names = [name for name in os.listdir(sheet_directory) if os.path.isfile(os.path.join(sheet_directory, name))]
        print(len(sheet_names))
        name_counter = 0
        name_divider = 0
        for b in name:
            if name[name_counter] == '_':
                name_divider += 1

            if name[name_counter] != '_':
                if name_divider == 0:
                    client_ip += name[name_counter]
                elif name_divider ==1:
                    brand += name[name_counter]
                elif name_divider == 2:
                    platform += name[name_counter]
                elif name_divider == 3:
                    version += name[name_counter]
                else:
                    action += name[name_counter]

            name_counter += 1

        print(client_ip)
        print(brand)
        print(platform)
        print(version)
        print(action)
        client_ip = ''
        brand = ''
        platform = ''
        version = ''
        action = ''

        capture_counter += 1

    counter += 1
