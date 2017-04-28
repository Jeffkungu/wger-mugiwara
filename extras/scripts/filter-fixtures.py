# -*- coding: utf-8 -*-

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

'''
Simple script that filters the output of django's dumpdata command into more
manageable chunks.

Create the data.json e.g. with:
    python ../../manage.py dumpdata --indent 4 --natural-foreign > data.json
'''

import json


def filter_dump(data, model_list, filename):
    '''
    Helper function
    '''
    filter_data = [i for i in data if i['model'] in model_list]
    with open(filename, 'w') as outfile:
        json.dump(filter_data, outfile, indent=4)

# This is a full dump of the DB


FIXTURE = open('data.json')


DATA = json.load(FIXTURE)
FIXTURE.close()

#
# Ingredients
#
filter_dump(DATA, ('nutrition.ingredient',), 'ingredients.json')
filter_dump(DATA, ('nutrition.weightunit',), 'weight_units.json')
filter_dump(DATA, ('nutrition.ingredientweightunit',), 'ingredient_units.json')

#
# Exercises
#
filter_dump(DATA, ('exercises.muscle',), 'muscles.json')
filter_dump(DATA, ('exercises.exercisecategory',), 'categories.json')
filter_dump(DATA, ('exercises.exerciseimage',), 'exercise-images.json')
filter_dump(DATA, ('exercises.exercise', 'exercises.exercisecomment',), 'exercises.json')
filter_dump(DATA, ('exercises.equipment', 'exercises.equipment',), 'equipment.json')

#
# Gym
#
filter_dump(DATA, ('gym.gym',), 'gyms.json')
filter_dump(DATA, ('gym.gymconfig',), 'gym_config.json')
filter_dump(DATA, ('gym.gymadminconfig',), 'gym_adminconfig.json')
filter_dump(DATA, ('gym.gymuserconfig',), 'gym_userconfig.json')
filter_dump(DATA, ('gym.adminusernote',), 'gym_admin_user_notes.json')
filter_dump(DATA, ('gym.userdocument',), 'gym_user_documents.json')
filter_dump(DATA, ('gym.contract',), 'gym_contracts.json')

#
# Core
#
filter_dump(DATA, ('core.gym',), 'gyms.json')
filter_dump(DATA, ('core.language',), 'languages.json')
filter_dump(DATA, ('core.license',), 'licenses.json')
filter_dump(DATA, ('core.repetitionunit',), 'repetition_units.json')

#
# Configurations
#
filter_dump(DATA, ('config.languageconfig',), 'language_config.json')
filter_dump(DATA, ('config.gymconfig',), 'gym_config.json')

#
# Other
#
filter_dump(DATA, ('auth.group',), 'groups.json')
filter_dump(DATA, ('auth.user',), 'users.json')
