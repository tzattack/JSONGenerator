from json import dump
import Collector

'''
def generator(dir_name, site_type):
    json_file = dir_name + site_type + ".json"
    file = open(json_file, "w")

    content = "{\"" + dir_name + "\":\n"
    content += "\t{\n"
    content += "\t\t\"bin\":{\"device:/com/roles/front/app/yjhp/yj_hp\"},\n"
    content += "\t\t\"config\":[{\"device:/com/cfg/yj_hp_in.conf\"},{\"device:/com/cfg/yj_hp_output.conf\"},"
    content += "{\"snspro:/com/cfg/yj_snp_extract.conf}\",{\"snspro:/com/cfg/yj_snp_output.conf}\"],\n"
    content += "\t\"SupportVersion\":[{\"pc\":\"20160718\"}],"

    file.write(content)
    file.close()
    return 0

name = "21CN"
site = "BBS"
generator(name, site)
'''

Collector.collector()
