from templates.utils import settings, templater

template = " merge_ai_species_main_menu.{event_id}.target_{target_id}:0 \"[mas_target_{target_id}.GetName]\""


def process(publish_dir):
    lines = []
    for i in range(1, settings.items_per_page + 1):
        lines.append(template.format(target_id=i, event_id=10))
        lines.append(template.format(target_id=i, event_id=20))
        lines.append(template.format(target_id=i, event_id=30))

    templater.process_file(
        publish_dir + "/localisation/english/mas_localization_l_english.yml",
        targets=lines)
