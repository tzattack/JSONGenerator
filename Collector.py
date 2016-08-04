import os


def type_check(site_type):
    if site_type.find("BBS") != 0:
        return "BBS"
    else:
        return "Unknown Type"


def collector():
    name = ""
    support_version = {}
    input_output = {}
    input = ""
    file_content = []
    file_content_list = ""
    files = {}

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
        print("\n<<<<<<<< SUBDIRECTORY >>>>>>>>>")
        print(subdirectory)
        capture_names = [name for name in os.listdir(subdirectory) if os.path.isdir(os.path.join(subdirectory, name))]
        # print("<<<<<<<< CAPTURE NAME >>>>>>>>>")
        # print(capture_names)

        # read capture sheet directories
        capture_counter = 0
        for c in capture_names:
            name = capture_names[capture_counter]
            print("\n###############################################################################################")

            # name to be read in
            # print("\n\tCapture Name:\t" + name)
            input = name

            sheet_directory = './' + directories[counter] + '/result/' + name + '/'

            sheet_names = [name for name in os.listdir(sheet_directory) if
                           os.path.isfile(os.path.join(sheet_directory, name))]

            # sheet number to be read in
            sheet_number = str(len(sheet_names))
            # print("\n\tSheet Number:\t" + sheet_number)

            sheet_counter = 0
            for s in sheet_names:
                sheet_file_dir = sheet_directory + sheet_names[sheet_counter]
                sheet_file = open(sheet_file_dir, "rt", encoding="latin-1")

                # sheet name to be read in
                # print("\n\tSheet:\t" + sheet_names[sheet_counter])

                # sheet content to be read in
                sheet_content = sheet_file.readlines()
                line_counter = 0
                for line in sheet_content:
                    if line_counter == 12:
                        protocol = str(line)[0:len(str(line))-1]
                        # print("\t\t" + protocol)
                    elif line_counter == 37:
                        domain = str(line)[0:len(str(line))-1]
                        # print("\t\t" + domain)
                    elif line_counter == 40:
                        action_type = str(line)[0:len(str(line))-1]
                        # print("\t\t" + str(line))
                    line_counter += 1

                file_content_list = protocol + " " + domain + " " + action_type
                file_content.append(file_content_list)
                sheet_counter += 1

            for i in file_content:
                if file_content.count(i) > 0:
                    files[i] = file_content.count(i)
            input_output[input] = files
            file_content = []
            files = {}
            print("\tINPUT_OUTPUT:\t" + str(input_output))
            input_output = {}

            # collect information from capture name
            name_counter = 0
            name_divider = 0
            for b in name:
                if name[name_counter] == '_':
                    name_divider += 1

                if name[name_counter] != '_':
                    if name_divider == 0:
                        client_ip += name[name_counter]
                    elif name_divider == 1:
                        brand += name[name_counter]
                    elif name_divider == 2:
                        platform += name[name_counter]
                    elif name_divider == 3:
                        version += name[name_counter]
                    else:
                        action += name[name_counter]
                name_counter += 1

            # platform & version to be read in
            # print("\n\tIP:\t" + client_ip)
            print("\tBrand:\t" + brand)
            print("\tType:\t" + type_check(brand))
            print("\tPlatform:\t" + platform)
            print("\tVersion:\t" + version)
            # print("\tAction:\t" + action)
            client_ip = brand = platform = version = action = ''
            capture_counter += 1

        counter += 1


class Site:
    __name = ""
    __support_version = {}
    __input_output = {}
    __input = ""
    __file = []

    def __init__(self, name, support_version, input_output, input, file):
        self.__name = name
        self.__support_version = support_version
        self.__input_output = input_output
        self.__file = file

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_support_version(self, support_version):
        self.__support_version = support_version

    def get_support_version(self):
        return self.__support_version

    def set_input_output(self, input_output):
        self.__input_output = input_output

    def get_input_output(self):
        return self.__input_output

    def set_file(self, file):
        self.__file = file

    def get_file(self):
        return self.__file


collector()




