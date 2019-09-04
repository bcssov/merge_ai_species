from templates.utils import settings, templater

template_flags = """
		save_event_target_as = mas_target_{0}"""

template_flag_assign = """
			{0} = {{
				limit = {{
					event_target:mas_target_{1} = {{
						is_same_value = event_target:mas_country
					}}
				}}
				save_event_target_as = mas_target_{1}
				set_country_flag = mas_processed
			}}"""

template_options = """
	option = {{
		name = merge_ai_species_main_menu.{1}.target_{0}

		trigger = {{
			NOT = {{
				event_target:mas_target_{0} = {{
					is_same_value = event_target:mas_country
				}}
			}}
		}}

		event_target:mas_target_{0} = {{
			save_event_target_as = mas_target
		}}

		country_event = {{
			id = merge_ai_species_main_menu.{2}
		}}
	}}"""

template_clear_flags = """
			{0} = {{
				limit = {{
					is_same_value = event_target:mas_target_{1}
				}}
				remove_country_flag = mas_processed
			}}"""


def process(publish_dir):
    lines_flags = []
    lines_flags_assign = []
    lines_options_10 = []
    lines_options_20 = []
    lines_clear_flags = []
    for i in range(1, settings.items_per_page + 1):
        lines_flags.append(template_flags.format(i))
        lines_options_10.append(template_options.format(i, 10, 11))
        lines_options_20.append(template_options.format(i, 20, 21))
        if i == 1:
            lines_flags_assign.append(template_flag_assign.format("if", i))
            lines_clear_flags.append(template_clear_flags.format("if", i))
        else:
            lines_flags_assign.append(
                template_flag_assign.format("else_if", i))
            lines_clear_flags.append(template_clear_flags.format("else_if", i))

    templater.process_file(
        publish_dir + "/events/merge_ai_species_main_menu.txt",
        lines_flags, lines_flags_assign, lines_options_10, lines_clear_flags,
        lines_flags, lines_flags_assign, lines_options_20, lines_clear_flags)
