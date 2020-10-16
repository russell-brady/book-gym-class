from __future__ import print_function, unicode_literals
from PyInquirer import prompt
import bookClass

questions = [
    {
        'type': 'input',
        'name': 'email_address',
        'message': 'What\'s your email address'
    },
    {
        'type': 'password',
        'name': 'password',
        'message': 'What\'s your password'
    },
    {
        'type': 'list',
        'name': 'gym_id',
        'message': 'Which gym do you wish to attend?',
        'choices': [
            {
                'key': 'a',
                'name': 'Drumcondra',
                'value': '9'
            },
            {
                'key': 'b',
                'name': 'Blanchardstown',
                'value': '16'
            },
            {
                'key': 'c',
                'name': 'Baggot St.',
                'value': '2'
            },
            {
                'key': 'd',
                'name': 'CHQ',
                'value': '10'
            },
            {
                'key': 'e',
                'name': 'Georges St.',
                'value': '5'
            }
        ]
    },
    {
        'type': 'list',
        'name': 'gym_time',
        'message': 'Which time do you wish to attend?',
        'choices': [
            {
                'key': 'a',
                'name': '06:30 - 07:45',
                'value': '06:30 - 07:45'
            },
            {
                'key': 'b',
                'name': '11:30 - 12:45',
                'value': '11:30 - 12:45'
            },
            {
                'key': 'c',
                'name': '13:00 - 14:15',
                'value': '13:00 - 14:15'
            },
            {
                'key': 'd',
                'name': '14:30 - 15:45',
                'value': '14:30 - 15:45'
            },
            {
                'key': 'e',
                'name': '16:00 - 17:15',
                'value': '16:00 - 17:15'
            },
            {
                'key': 'f',
                'name': '17:00 - 18:15',
                'value': '17:00 - 18:15'
            },
            {
                'key': 'g',
                'name': '17:30 - 18:45',
                'value': '17:30 - 18:45'
            },
            {
                'key': 'h',
                'name': '19:00 - 20:15',
                'value': '19:00 - 20:15'
            },
            {
                'key': 'i',
                'name': '20:30 - 21:45',
                'value': '20:30 - 21:45'
            },
            {
                'key': 'k',
                'name': '22:00 - 23:15',
                'value': '22:00 - 23:15'
            }
        ]
    }
]

answers = prompt(questions)

requestSession = bookClass.create_request_session()
bookClass.login(requestSession, answers['email_address'], answers['password'])
bookClass.book_gym_slot(requestSession, answers['gym_id'], answers['gym_time'])
