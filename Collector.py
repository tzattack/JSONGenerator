import os
import Generator


def type_check(site_type):
    if site_type.find("BBS") != 0:
        return "BBS"
    else:
        return "Unknown Type"


directories = [name for name in os.listdir('./') if os.path.isdir(os.path.join('./', name))]
directories.remove(".idea")
directories.remove("__pycache__")
directories.remove(".git")
print(directories)

client_ip = brand = platform = version = action = ''

# read directories in ./result/
counter = 0
for d in directories:
    subdirectory = './' + directories[counter] + '/result/'
    print(subdirectory)
    capture_names = [name for name in os.listdir(subdirectory) if os.path.isdir(os.path.join(subdirectory, name))]
    print(capture_names)

    # read capture sheet directories
    capture_counter = 0
    for c in capture_names:
        name = capture_names[capture_counter]
        print("\n###############################################################################################")
        print("\n\tCapture Name:\t" + name)

        sheet_directory = './' + directories[counter] + '/result/' + name + '/'

        sheet_names = [name for name in os.listdir(sheet_directory) if os.path.isfile(os.path.join(sheet_directory, name))]
        print("\tSheet Number:\t" + str(len(sheet_names)))
        sheet_counter = 0
        for s in sheet_names:
            sheet_file_dir = sheet_directory + sheet_names[sheet_counter]
            sheet_file = open(sheet_file_dir, "rt", encoding="latin-1")
            print("\tSheet:\t" + sheet_names[sheet_counter])
            sheet_content = sheet_file.readlines()
            line_counter = 0
            for line in sheet_content:
                if line_counter == 12:
                    print("\t\t" + str(line))
                elif line_counter == 37:
                    print("\t\t" + str(line))
                elif line_counter == 40:
                    print("\t\t" + str(line))
                line_counter += 1
            sheet_counter += 1

        # collect information from capture name
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

        print("\tIP:\t" + client_ip)
        print("\tBrand:\t" + brand)
        print("\tType:\t" + type_check(brand))
        print("\tPlatform:\t" + platform)
        print("\tVersion:\t" + version)
        print("\tAction:\t" + action)
        client_ip = brand = platform = version = action = ''

        capture_counter += 1

    counter += 1

