_vowels = 'aeiou'
_non_pulmonic_consonants = ''
_pulmonic_consonants = 'pbtdckgqGNnmrv'
_suprasegmentals = ''
_other_symbols = ''
_diacrilics = ''
_phonemes = sorted(list(
    _vowels + _non_pulmonic_consonants + _pulmonic_consonants + _suprasegmentals + _other_symbols + _diacrilics))
_punctuations = '!,-.:;? \'()'
_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

all_phonemes = sorted(list(_phonemes) + list(_punctuations))
