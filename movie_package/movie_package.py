import numpy as np
import pandas as pd

# Extract the years and handle date ranges
def clean_year(year_text):
    """
    
    clean_year accepts a beautiful soup object of years and removes any ranges (anything with a "-"). It will leave you with one year.

    Parameters:
    -----------

    some_list: year_text
        A Beautiful soup object of a list of years
    
    Returns:
    --------

    list
        list of cleaned years
    
    """
    # Remove parentheses and strip whitespace
    clean_text = year_text.strip('()').strip()
    
    # If it's a range or contains 'Present', take the first year
    if '-' in clean_text or 'Present' in clean_text:
        return int(clean_text.split('-')[0])
    
    # For standard single years
    return int(clean_text)


# Clean Director Names
def extract_names(result_list):
    """
    
    extract_names accepts a list of directors and excecutive producers, takes the first name, and puts NA anywhere where a movie does not have a director listed

    Parameters:
    -----------

    result_list: list
        A list of director and executive producer names
    
    Returns:
    --------

    list
        A cleaned list of directors names
    
    """
    names = []
    for result in result_list:
        # Extract the raw text and remove labels like "Director:" or "Executive Producer:"
        text = result.get_text(strip=True)
        for label in ["Director:", "Executive Producer:"]:
            text = text.replace(label, "")
        # Remove trailing "and X more" if present
        clean_text = text.split("and")[0].strip()
        names.append(clean_text)
    
    names.insert(24, np.nan)

    return names


def clean_tomato(result_list):
    """
    
    clean_tomato accepts a list of critic ratings (tomato scores) and puts NA where a score does not exist yet (movie hasn't yet been released)

    Parameters:
    -----------

    result_list: list
        A list of ratings, from 0-100%
    
    Returns:
    --------

    list
        A list of cleaned ratings, with NA where a score did not exist and without the '%'
    
    """
    tomato_meter = []
    for result in result_list:
        score_tag = result.find('strong', {'data-qa': 'franchise-media-tomatometer'})
        if score_tag:
            score = int(score_tag.text.strip('%'))
        else:
            score = np.nan
        tomato_meter.append(score)
    return tomato_meter


# Get popcorn meter score
def clean_popcorn(result_list):
    """
    
    clean_popcorn accepts a list of user ratings (popcorn scores) and puts NA where a score does not exist yet (movie hasn't yet been released)

    Parameters:
    -----------

    result_list: list
        A list of ratings, from 0-100%
    
    Returns:
    --------

    list
        A list of cleaned ratings, with NA where a score did not exist and without the '%'
    
    """
    popcorn_meter = []
    for result in result_list:
        score_tag = result.find('rt-text', {'context': 'label'})
        if score_tag:
            score = int(score_tag.text.strip('%'))
        else:
            score = np.nan
        popcorn_meter.append(score)
    return popcorn_meter