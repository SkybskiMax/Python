import re
def extract_file_name(dirty_file_name):
    pattern = r'\d+_([a-zA-Z0-9_-]+[\.][a-zA-Z0-9_-]+)'
    return "".join(re.findall(pattern,dirty_file_name))

print(extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"))
print(extract_file_name("497112209578986190056_EMbLxtrccpdH_c_ss_uniZwU_p-.q80.H9sT33Cy36WymgS392d2Y1XP95"))
print(extract_file_name('034049698504534011734_Z-h_ZTPVqEHdsD.0hY.92K454R89u6_k7re1JN49Hv_82y'))