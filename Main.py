import os
import json


class Site:
    __web_dir = ""
    __name = ""
    __xx_type = ""
    __input_output = {}

    def __init__(self, web_dir, name, xx_type, input_output):
        self.__web_dir = web_dir
        self.__name = name
        self.__xx_type = xx_type
        self.__input_output = input_output

    def set_web_dir(self, web_dir):
        self.__web_dir = web_dir

    def get_web_dir(self):
        return self.__web_dir

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_xx_type(self, xx_type):
        self.__xx_type = xx_type

    def get_xx_type(self):
        return self.__xx_type

    def set_input_output(self, input_output):
        self.__input_output = input_output

    def get_input_output(self):
        return self.__input_output


def type_check(site_type):
    if site_type.find("BBS") != 0:
        return "BBS"
    else:
        return "Unknown Type"


def generator(website):
    json_file = website.get_web_dir() + website.get_name().lower() + ".json"
    file = open(json_file, "w")
    i_o_content = website.get_input_output()
    number = len(i_o_content)
    print(number)
    for i in i_o_content:
        print(i)
        print(i_o_content[i])

    content = "{\"" + website.get_name() + "\":\n"
    content += "{\n"
    content += "\"bin\":\n"
    content += "[\"device:/com/roles/front/app/yjhp/yj_hp\",\"snspro:/com/roles/snspro/httpextractor/yj_snp\"],\n"
    content += "\"config\":\n"
    content += "[\"device:/com/cfg/yj_hp_in.conf\",\n"
    content += "\"device:/com/cfg/yj_hp_output.conf\",\n"
    content += "\"snspro:/com/cfg/yj_snp_extract.conf\",\n"
    content += "\"snspro:/com/cfg/yj_snp_output.conf\"],\n"
    content += "\"input_outputs\":"
    if number > 1:
        content += "[\n"
    counter = 0
    for i in i_o_content:
        counter += 1
        if counter == number:
            content += "{\n\"input\":\n[\"" + i + \
                       ".cap\"],\n\"output\":{\n\"dir\":\"snspro:/ramdisk/front/output/yj_snp\",\n\"files\":[" \
                       + json.dumps(i_o_content[i]) + "]\n}\n}\n"
            break
        content += "{\n\"input\":\n[\"" + i + \
                   ".cap\"],\n\"output\":{\n\"dir\":\"snspro:/ramdisk/front/output/yj_snp\",\n\"files\":[" \
                   + json.dumps(i_o_content[i]) + "]\n}\n},\n"
    if number > 1:
        content += "]\n"
    content += "}\n}"

    file.write(content)
    file.close()

    return 0


def main():
    name = ""
    input_output = {}
    input = ""
    file_content = []
    file_content_list = ""
    files = {}
    site_type = ""

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
                    if line.find("Protocol") != -1:
                        protocol = str(line)[0:len(str(line))-1]
                        # print("\t\t" + protocol)
                    elif line.find("Domain") != -1:
                        domain = str(line)[0:len(str(line))-1]
                        # print("\t\t" + domain)
                    elif line.find("XX-Type") != -1:
                        action_type = str(line)[0:len(str(line))-1]
                        site_type = action_type[8:]
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
            # print("\tINPUT_OUTPUT:\t" + str(input_output))

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
                        xx_name = brand
                    elif name_divider == 2:
                        platform += name[name_counter]
                    elif name_divider == 3:
                        version += name[name_counter]
                    else:
                        action += name[name_counter]
                name_counter += 1

            # platform & version to be read in
            # print("\n\tIP:\t" + client_ip)
            # print("\tBrand:\t" + brand)
            # print("\tType:\t" + type_check(brand))
            # print("\tPlatform:\t" + platform)
            # print("\tVersion:\t" + version)
            # print("\tAction:\t" + action)
            client_ip = brand = platform = version = action = ''
            capture_counter += 1

        xx_type = ""
        site_type_counter = 0
        for s in site_type:
            if site_type[site_type_counter] != '_':
                xx_type += site_type[site_type_counter]
            else:
                break
            site_type_counter += 1
        # print(xx_type)
        # print(xx_name)

        web_dir = './' + directories[counter] + '/'
        website = Site(web_dir, xx_name, xx_type, input_output)
        generator(website)
        input_output.clear()

        counter += 1

main()





