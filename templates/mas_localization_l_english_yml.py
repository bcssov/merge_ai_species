from templates.utils import settings, templater

template = " merge_ai_species_main_menu.{1}.target_{0}:0 \"[mas_target_{0}.GetName]\""


def process(publish_dir):
    lines_10 = []
    lines_20 = []
    for i in range(1, settings.items_per_page + 1):
        lines_10.append(template.format(i, 10))
        lines_10.append(template.format(i, 20))

    templater.process_file(
        publish_dir + "/localisation/english/mas_localization_l_english.yml",
        lines_10, lines_20)
