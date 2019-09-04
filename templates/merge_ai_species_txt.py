from templates.utils import settings, templater

template_1 = """
				{1} = {{
					limit = {{
						root = {{
							count_owned_pops = {{
								count >= {0}
								limit = {{
									OR = {{
										is_same_species = prev
										is_subspecies = prev
									}}
									NOR = {{
										species = {{
											has_species_flag = mas_merge_species_currently_processing
										}}
										has_trait = trait_self_modified
									}}
								}}
							}}
						}}
					}}
					root = {{
						random_owned_pop_species = {{
							limit = {{
								count_pops = {{
									count >= {0}
									limit = {{
										OR = {{
											is_same_species = prevprev
											is_subspecies = prevprev
										}}
										NOR = {{
											species = {{
												has_species_flag = mas_merge_species_currently_processing
											}}
											has_trait = trait_self_modified
										}}
									}}
								}}
							}}
							set_species_flag = mas_merge_species_target_species
							save_event_target_as = mas_target_species
						}}
					}}
				}}"""

template_2 = """
				{1} = {{
					limit = {{
						root = {{
							count_owned_pops = {{
								count >= {0}
								limit = {{
									OR = {{
										is_same_species = prev
										is_subspecies = prev
									}}
									NOT = {{
										species = {{
											has_species_flag = mas_merge_species_currently_processing
										}}										
									}}
								}}
							}}
						}}
					}}
					root = {{
						random_owned_pop_species = {{
							limit = {{
								count_pops = {{
									count >= {0}
									limit = {{
										OR = {{
											is_same_species = prevprev
											is_subspecies = prevprev
										}}
										NOT = {{
											species = {{
												has_species_flag = mas_merge_species_currently_processing
											}}											
										}}
									}}
								}}
							}}
							set_species_flag = mas_merge_species_target_species
							save_event_target_as = mas_target_species
						}}
					}}
				}}"""


def process(publish_dir):
    lines_1 = []
    lines_2 = []

    for i in range(settings.max['range'], settings.middle['range'], settings.max['step']):
        if i == settings.max['range']:
            lines_1.append(template_1.format(i, "if"))
            lines_2.append(template_2.format(i, "if"))
        else:
            lines_1.append(template_1.format(i, "else_if"))
            lines_2.append(template_2.format(i, "else_if"))

    for i in range(settings.middle['range'], settings.low['range'], settings.middle['step']):
        lines_1.append(template_1.format(i, "else_if"))
        lines_2.append(template_2.format(i, "else_if"))
    for i in range(settings.low['range'], 0, settings.low['step']):
        lines_1.append(template_1.format(i, "else_if"))
        lines_2.append(template_2.format(i, "else_if"))

    templater.process_file(
        publish_dir + "/events/merge_ai_species.txt",
        lines_1, lines_2)
