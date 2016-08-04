from json import dump
import Main


def generator(Site):
    json_file = Site.get_name() + ".json"
    file = open(json_file, "w")

    content = "{\"" + website.get_name() + "\":\n"
    content += "\t{\n"
    content += "\t\t\"bin\":{\"device:/com/roles/front/app/yjhp/yj_hp\"},\n"
    content += "\t\t\"config\":[{\"device:/com/cfg/yj_hp_in.conf\"},{\"device:/com/cfg/yj_hp_output.conf\"},"
    content += "{\"snspro:/com/cfg/yj_snp_extract.conf}\",{\"snspro:/com/cfg/yj_snp_output.conf}\"],\n"
    content += "\t\"SupportVersion\":[{\"pc\":\"20160718\"}],"

    file.write(content)
    file.close()
    return 0



