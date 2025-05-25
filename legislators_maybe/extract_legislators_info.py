import ast
import pandas as pd

def extract_legislators_info(row):
    """
    Extract detailed information from a row in the legislators DataFrame.
    
    :param row: A row of the legislators DataFrame.
    :return: A dictionary of extracted values.
    """
    result = {}

    # Extract from 'name' column
    try:
        name_dict = ast.literal_eval(row['name']) if isinstance(row['name'], str) else row['name']
        result['first_name'] = name_dict.get('first', None)
        result['middle_name'] = name_dict.get('middle', None)
        result['last_name'] = name_dict.get('last', None)
        result['suffix'] = name_dict.get('suffix', None)
        result['nickname'] = name_dict.get('nickname', None)
        result['official_full_name'] = name_dict.get('official_full', None)
    except (ValueError, SyntaxError, AttributeError):
        result.update({'first_name': None, 'middle_name': None, 'last_name': None,
                       'suffix': None, 'nickname': None, 'official_full_name': None})

    # Extract from 'bio' column
    try:
        bio_dict = ast.literal_eval(row['bio']) if isinstance(row['bio'], str) else row['bio']
        birthdate = bio_dict.get('birthday', None)
        birthdate = pd.to_datetime(birthdate, errors='coerce').date() if birthdate else None
        birthday = birthdate.strftime('%m-%d') if birthdate else None
        result['birthdate'] = birthdate
        result['birthday'] = birthday
        result['gender'] = bio_dict.get('gender', None)
    except (ValueError, SyntaxError, AttributeError):
        result.update({'birthdate': None, 'birthday': None, 'gender': None})

    # Extract from 'terms' column
    try:
        terms_list = ast.literal_eval(row['terms']) if isinstance(row['terms'], str) else row['terms']
        first_term = terms_list[0] if isinstance(terms_list, list) and len(terms_list) > 0 else {}
        result['type'] = first_term.get('type', None)
        result['start_term'] = first_term.get('start', None)
        result['end_term'] = first_term.get('end', None)
        result['state'] = first_term.get('state', None)
        result['class'] = first_term.get('class', None)
        result['district'] = first_term.get('district', None)
        result['party'] = first_term.get('party', None)
        result['caucus'] = first_term.get('caucus', None)
        result['how'] = first_term.get('how', None)
    except (ValueError, SyntaxError, AttributeError):
        result.update({key: None for key in ['type', 'start_term', 'end_term', 'state', 'class', 'district',
                                             'party', 'caucus', 'how']})

    return result