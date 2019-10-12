[h1]Load Order[/h1]
Not important.

[h1]Older Versions[/h1]
[url=https://steamcommunity.com/sharedfiles/filedetails/?id=1885042685]2.3[/url]

[h1]FAQ[/h1]

[i]What is this mod?[/i]
It's a mod which merges less populous species in an empire with the most populous species (in an empire).

[i]How does it work exactly?[/i]
You run the mod manually (by edict or using the [url=https://steamcommunity.com/sharedfiles/filedetails/?id=1840010432)]Dynamic Mod Menu[/url]). Select one of the following options:
1. Merge species in all countries
2. Merge species in all countries (include self-modified trait)
3. Merge robot and machine species in all countries
4. Merge species in a single country
5. Merge species in a single country (include self-modified trait)
6. Merge robot and machine species in a single country

Mod will then find all pops in a country which have a count less than 10 and merge them with the most populous species (of its kind).

[i]Are any pops excluded from this?[/i]
Only the ones that are being purged or self-modified. You can include the ones that are self-modified in this process by selecting the appropriate option though.

[i]What about half-breeds?[/i]
Half-breeds will be processed as well and merged. Provided that they fit within the parameters:
1. Have less than 10 pops
2. Have a valid species to merge to

[i]Can we have more control over merging process? [/i]
I thought about including this into phase 2. But decided against it, it's a royal pain to design a flexible enough UI in the game to do this. 

Maybe in a faraway future though.

[i]Are you handling newly grown pops?[/i]
No.

[i]Why aren't you handling newly grown pops?[/i]
The mod is designed to support AI Species Limit so I see no need to handle them.

[i]Does this impact performance?[/i]
The mod does not automatically run so it should not impact the gameplay. BUT when you do run it it might take a minute or two to merge all species and might freeze the game (can't do anything about that).

[i]Can I use in an existing game?[/i]
Sure it was designed to declutter existing games of species and then use AI Species Limit to keep them in check.

[i]Are there any requirements for this mod?[/i]
Mod doesn't have any requirements. It does work well with 2 of my other mods though.
1. Dynamic Mod Menu: without Dynamic Mod Menu launching this mod will be done via edicts menu. If DMM is installed edict will disappear and will be launchable through DMM.
2. AI Species Limit: Merge AI Species is designed to complement AI Species Limit but it doesn't have to be installed for this mod to work.

[i]How are robot species merged?[/i]
This option will find all machine and robot pops in a country that have less than than 10 pops. It will then locate the most populous machine or robot species and merge it with them making them a single species.

[i]Does the robot\machine merge differentiate between robot and synth ascension pops?[/i]
No.

[i]Why isn't there any differentiation between robots and synth ascension pops?[/i]
Short answer: They are all machines now.
Long answer: There's no way to differentiate these in the game via code.

[i]Is it really not possible do differentiate synth ascension pops between regular robots[/i]
Not without overwriting few stock events.

[i]Will you consider covering scenario to differentiate between synth and robots?[/i]
No.

[i]You messed up my game![/i]
Please backup your save games before running the mod.

[i]Why do I need to backup my game?[/i]
In theory the mod will not messup anything but you might not be satisfied with the results of the merge. Therefore before using it the first time I recommend that you backup your save run the mod and see the results.