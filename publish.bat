py -3 publish.py
cd publish
cd merge_ai_species
Bandizip c -r "merge_ai_species.zip" "*.*"
xcopy "merge_ai_species.zip" "%UserProfile%\Documents\Paradox Interactive\Stellaris\mod" /y
cd .. 
cd ..
cls